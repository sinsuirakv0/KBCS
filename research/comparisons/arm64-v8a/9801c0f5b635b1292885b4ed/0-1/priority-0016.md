# v15.7.4 → v16.0.0 · 最優先の変更候補 (16)

[一覧の目次](README.md)

<a id="compare-9518bb4b8eb9ff618bc64778e8b2befc"></a>

### [`00529cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md) → [`0054cb5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md) FUN_0054cb5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004f8244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f8/004f8244.md) [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) [`005054cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00505/005054cc.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`0051b0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051b/0051b0dc.md) [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) [`00528364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00528/00528364.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0054cb6c",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00529cd4",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054cb68",
      "incomplete_value": true,
      "site": "0054cb6c",
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
            "const:f0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00529cd0",
      "incomplete_value": true,
      "site": "00529cd4",
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
      "0054cb68",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054cb6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0054cb68",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054cb6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md#insn-00529cd4) · [`00529ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md#insn-00529ccc) · [`00529cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529cc4.md#insn-00529cd0)
- 新版 [`0054cb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md#insn-0054cb6c) · [`0054cb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md#insn-0054cb64) · [`0054cb68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cb5c.md#insn-0054cb68)

~~~diff
- 00529cd4 ["INT_ADD", "register:40f0:8", ["const:529cd4:8", "const:4:8"]]
- 00529cd4 ["CALL", null, ["ram:41fdf0:8"]]
+ 0054cb6c ["INT_ADD", "register:40f0:8", ["const:54cb6c:8", "const:4:8"]]
+ 0054cb6c ["CALL", null, ["ram:4428f0:8"]]
- 00529cd4 bytes 47d8fb97
+ 0054cb6c bytes 61d7fb97
- 00529ccc ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054cb64 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00529ccc bytes e0ebffd0
+ 0054cb64 bytes 40ebfff0
- 00529cd0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00529cd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054cb68 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054cb68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cb68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054cb68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00529cd0 bytes 00740e91
+ 0054cb68 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df53158ad8062b0b2756daf6cb6eb626"></a>

### [`00529d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md) → [`0054cbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cbf4.md) FUN_0054cbf4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f9abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 71.00% / 新版 71.00%

CFGの説明率　旧版 34.18% / 新版 33.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00529d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00529d94"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00529db4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054cbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00529d88"
      ]
    ],
    [
      "unmatched:00529d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054cc48"
      ]
    ],
    [
      "unmatched:00529d94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054ccac"
      ]
    ]
  ],
  "added": [
    [
      "0054cbfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054cc20"
      ]
    ],
    [
      "0054cc1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054cc48"
      ]
    ],
    [
      "0054cc2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054ccac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00529d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md#insn-00529d84) · [`00529d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md#insn-00529d94) · [`00529db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00529/00529d5c.md#insn-00529db4)

~~~diff
- 00529d84 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
- 00529d84 bytes 62010054
- 00529d94 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 00529d94 bytes 00040054
- 00529db4 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00529db4 bytes c0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0516b9d0b8f98386ca4e90c46c25825"></a>

### [`0052a0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md) → [`0054cf90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054c/0054cf90.md) FUN_0054cf90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004f9abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f9/004f9abc.md) · 呼出先 6件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0052a1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a1c8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0051c954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051c/0051c954.md) · 呼出先 6件 [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0054d060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d060.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a140"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a148"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0054cfc0",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0052a140",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:0052a14c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054d014"
      ]
    ]
  ],
  "added": [
    [
      "0054cfc0",
      "READ",
      [
        "storage",
        "00c9a940",
        null,
        "pointer"
      ]
    ],
    [
      "0054cfd8",
      "DATA",
      [
        "storage",
        "00c65e88",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0054cfe4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054d014"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052a13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md#insn-0052a13c) · [`0052a140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md#insn-0052a140) · [`0052a148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a0f8.md#insn-0052a148)

~~~diff
- 0052a13c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0052a13c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0052a13c ["INT_ADD", "register:40a8:8", ["register:40a8:8", "const:28:8"]]
- 0052a13c ["STORE", null, ["const:1b1:8", "register:40a8:8", "tmp:1:8"]]
- 0052a13c bytes bf8e02f8
- 0052a140 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 0052a140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0052a140 bytes 081000f9
- 0052a148 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0052a148 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0052a148 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0052a148 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0052a148 bytes 1f7c03a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78f5e0472e385449cb6ccf3005a5dcb2"></a>

### [`0052a264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md) → [`0054d0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md) FUN_0054d0fc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004fb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fb/004fb4c0.md) · 呼出先 9件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00519a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00519/00519a68.md) [`0051cdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051c/0051cdc8.md)
- 新版 呼出元 1件 [`0051e358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051e/0051e358.md) · 呼出先 9件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053c900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053c/0053c900.md) [`0053fc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053f/0053fc60.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 42.86% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a2b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0054d1a8",
      "incomplete_value": true,
      "site": "0054d1a8",
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
      "definition_site": "0052a310",
      "incomplete_value": true,
      "site": "0052a310",
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
      "unmatched:0052a288",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a2a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0052a3ac"
      ]
    ],
    [
      "unmatched:0052a2b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054d120",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0054d138",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0054d244"
      ]
    ],
    [
      "0054d14c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052a288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md#insn-0052a288) · [`0052a2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md#insn-0052a2a0) · [`0052a2b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md#insn-0052a2b4)

~~~diff
- 0052a288 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0052a288 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0052a288 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0052a288 bytes a8831ff8
- 0052a2a0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 0052a2a0 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 0052a2a0 bytes 6a0800b5
- 0052a2b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 0052a2b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0052a2b4 bytes ea1300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66b940790758fbbd9c1a8e3b8a03ad52"></a>

### [`0052a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a400.md) → [`0054d298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d298.md) FUN_0054d298

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0052a264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a264.md) · 呼出先 2件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md)
- 新版 呼出元 1件 [`0054d0fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d0fc.md) · 呼出先 2件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.58% / 新版 75.58%

CFGの説明率　旧版 10.00% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 10件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052a400",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a404",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a408",
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
      "0054d298",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0054d29c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0054d2a0",
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

- 旧版 [`0052a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a400.md#insn-0052a400) · [`0052a404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a400.md#insn-0052a404) · [`0052a408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a400.md#insn-0052a408)

~~~diff
- 0052a400 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052a400 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052a400 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 0052a400 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052a400 bytes fd7bbca9
- 0052a404 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0052a404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0052a404 bytes f70b00f9
- 0052a408 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0052a408 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0052a408 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0052a408 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0052a408 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9681b50c611f92c59dce01544257a408"></a>

### [`0052a558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a558.md) → [`0054d3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d3f0.md) FUN_0054d3f0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a558"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a55c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052a558",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a55c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a560",
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
      "0054d3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0054d3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0054d3f8",
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

- 旧版 [`0052a558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a558.md#insn-0052a558) · [`0052a55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a558.md#insn-0052a55c) · [`0052a560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a558.md#insn-0052a560)

~~~diff
- 0052a558 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052a558 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052a558 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0052a558 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052a558 bytes fd7bbda9
- 0052a55c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0052a55c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0052a55c bytes f50b00f9
- 0052a560 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0052a560 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0052a560 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0052a560 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0052a560 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a793d5be9725f31f6155327badf237a"></a>

### [`0052a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md) → [`0054d464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d464.md) FUN_0054d464

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`004fdfd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004fd/004fdfd8.md) [`004ff950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ff/004ff950.md) [`0052a914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a914.md) · 呼出先 5件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`004f7dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f7/004f7dec.md) [`005180b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/005180b8.md) [`0051854c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00518/0051854c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00520e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00520/00520e70.md) [`005227e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00522/005227e8.md) [`0054d7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d7ac.md) · 呼出先 5件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0051ac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0051a/0051ac84.md) [`0053af50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053a/0053af50.md) [`0053b3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0053b/0053b3e4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 90.91% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a5cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a5cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0052a5d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0052a5cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a5d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0052a5d4",
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
      "0054d464",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0054d468",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0054d46c",
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

- 旧版 [`0052a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md#insn-0052a5cc) · [`0052a5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md#insn-0052a5d0) · [`0052a5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052a5cc.md#insn-0052a5d4)

~~~diff
- 0052a5cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0052a5cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0052a5cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0052a5cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0052a5cc bytes fd7bbda9
- 0052a5d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0052a5d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0052a5d0 bytes f50b00f9
- 0052a5d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0052a5d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0052a5d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0052a5d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0052a5d4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc7739af30b4cbb03919c21ba7e59ab0"></a>

### [`0052ab40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab40.md) → [`0054d9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md) FUN_0054d9d8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00504f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00504/00504f50.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00527de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00527/00527de8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "0054d9e8",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052ab50",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054d9e4",
      "incomplete_value": false,
      "site": "0054d9e8",
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
      "definition_site": "0052ab4c",
      "incomplete_value": false,
      "site": "0052ab50",
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
      "0054d9e4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054d9e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0054d9e4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054d9e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "004428f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ab50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab40.md#insn-0052ab50) · [`0052ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab40.md#insn-0052ab48) · [`0052ab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ab40.md#insn-0052ab4c)
- 新版 [`0054d9e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md#insn-0054d9e8) · [`0054d9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md#insn-0054d9e0) · [`0054d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054d9d8.md#insn-0054d9e4)

~~~diff
- 0052ab50 ["INT_ADD", "register:40f0:8", ["const:52ab50:8", "const:4:8"]]
- 0052ab50 ["CALL", null, ["ram:41fdf0:8"]]
+ 0054d9e8 ["INT_ADD", "register:40f0:8", ["const:54d9e8:8", "const:4:8"]]
+ 0054d9e8 ["CALL", null, ["ram:4428f0:8"]]
- 0052ab50 bytes a8d4fb97
+ 0054d9e8 bytes c2d3fb97
- 0052ab48 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054d9e0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0052ab48 bytes e0ebffb0
+ 0054d9e0 bytes 40ebffd0
- 0052ab4c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0052ab4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054d9e4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054d9e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054d9e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054d9e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052ab4c bytes 00740e91
+ 0054d9e4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b5d65101b02590b9981da22a7bd0120"></a>

### [`0052acbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md) → [`0054db54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md) FUN_0054db54

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052b868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b868.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e700.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054db64",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052accc",
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
      "definition_site": "0054db60",
      "incomplete_value": false,
      "site": "0054db64",
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
      "definition_site": "0052acc8",
      "incomplete_value": false,
      "site": "0052accc",
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
      "0054db60",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054db64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054db60",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054db64",
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

- 旧版 [`0052accc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md#insn-0052accc) · [`0052acc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md#insn-0052acc4) · [`0052acc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052acbc.md#insn-0052acc8)
- 新版 [`0054db64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md#insn-0054db64) · [`0054db5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md#insn-0054db5c) · [`0054db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054db54.md#insn-0054db60)

~~~diff
- 0052accc ["INT_ADD", "register:40f0:8", ["const:52accc:8", "const:4:8"]]
- 0052accc ["CALL", null, ["ram:418c38:8"]]
+ 0054db64 ["INT_ADD", "register:40f0:8", ["const:54db64:8", "const:4:8"]]
+ 0054db64 ["CALL", null, ["ram:43b738:8"]]
- 0052accc bytes dbb7fb97
+ 0054db64 bytes f5b6fb97
- 0052acc4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054db5c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0052acc4 bytes e0ebffb0
+ 0054db5c bytes 40ebffd0
- 0052acc8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0052acc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054db60 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054db60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054db60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054db60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052acc8 bytes 00740e91
+ 0054db60 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8135448604540b5167c2f091885c825"></a>

### [`0052ae7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae7c.md) → [`0054dd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md) FUN_0054dd14

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00506ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00506/00506ee0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00529d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00529/00529d78.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054dd24",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052ae8c",
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
      "definition_site": "0054dd20",
      "incomplete_value": false,
      "site": "0054dd24",
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
      "definition_site": "0052ae88",
      "incomplete_value": false,
      "site": "0052ae8c",
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
      "0054dd20",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054dd24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054dd20",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054dd24",
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

- 旧版 [`0052ae8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae7c.md#insn-0052ae8c) · [`0052ae84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae7c.md#insn-0052ae84) · [`0052ae88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae7c.md#insn-0052ae88)
- 新版 [`0054dd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md#insn-0054dd24) · [`0054dd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md#insn-0054dd1c) · [`0054dd20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd14.md#insn-0054dd20)

~~~diff
- 0052ae8c ["INT_ADD", "register:40f0:8", ["const:52ae8c:8", "const:4:8"]]
- 0052ae8c ["CALL", null, ["ram:418c38:8"]]
+ 0054dd24 ["INT_ADD", "register:40f0:8", ["const:54dd24:8", "const:4:8"]]
+ 0054dd24 ["CALL", null, ["ram:43b738:8"]]
- 0052ae8c bytes 6bb7fb97
+ 0054dd24 bytes 85b6fb97
- 0052ae84 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054dd1c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0052ae84 bytes e0ebffb0
+ 0054dd1c bytes 40ebffd0
- 0052ae88 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0052ae88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054dd20 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054dd20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dd20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054dd20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052ae88 bytes 00740e91
+ 0054dd20 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c68ff2ff2ba063e918729511c7184588"></a>

### [`0052b348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md) → [`0054e1e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md) FUN_0054e1e0

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052ae90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052a/0052ae90.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054dd28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054d/0054dd28.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054e1f0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052b358",
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
      "definition_site": "0054e1ec",
      "incomplete_value": false,
      "site": "0054e1f0",
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
      "definition_site": "0052b354",
      "incomplete_value": false,
      "site": "0052b358",
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
      "0054e1ec",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054e1f0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054e1ec",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054e1f0",
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

- 旧版 [`0052b358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md#insn-0052b358) · [`0052b350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md#insn-0052b350) · [`0052b354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052b348.md#insn-0052b354)
- 新版 [`0054e1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md#insn-0054e1f0) · [`0054e1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md#insn-0054e1e8) · [`0054e1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054e1e0.md#insn-0054e1ec)

~~~diff
- 0052b358 ["INT_ADD", "register:40f0:8", ["const:52b358:8", "const:4:8"]]
- 0052b358 ["CALL", null, ["ram:418c38:8"]]
+ 0054e1f0 ["INT_ADD", "register:40f0:8", ["const:54e1f0:8", "const:4:8"]]
+ 0054e1f0 ["CALL", null, ["ram:43b738:8"]]
- 0052b358 bytes 38b6fb97
+ 0054e1f0 bytes 52b5fb97
- 0052b350 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054e1e8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0052b350 bytes e0ebff90
+ 0054e1e8 bytes 40ebffb0
- 0052b354 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0052b354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052b354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052b354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054e1ec ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054e1ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e1ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054e1ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052b354 bytes 00740e91
+ 0054e1ec bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be47c8a678a2c95700d8b4b8d934c1b"></a>

### [`0052c024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md) → [`0054eebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md) FUN_0054eebc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052be2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052b/0052be2c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0054ecc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054ecc4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0054eecc",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052c034",
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
      "definition_site": "0054eec8",
      "incomplete_value": false,
      "site": "0054eecc",
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
      "definition_site": "0052c030",
      "incomplete_value": false,
      "site": "0052c034",
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
      "0054eec8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0054eecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0054eec8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0054eecc",
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

- 旧版 [`0052c034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md#insn-0052c034) · [`0052c02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md#insn-0052c02c) · [`0052c030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c024.md#insn-0052c030)
- 新版 [`0054eecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md#insn-0054eecc) · [`0054eec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md#insn-0054eec4) · [`0054eec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054e/0054eebc.md#insn-0054eec8)

~~~diff
- 0052c034 ["INT_ADD", "register:40f0:8", ["const:52c034:8", "const:4:8"]]
- 0052c034 ["CALL", null, ["ram:418c38:8"]]
+ 0054eecc ["INT_ADD", "register:40f0:8", ["const:54eecc:8", "const:4:8"]]
+ 0054eecc ["CALL", null, ["ram:43b738:8"]]
- 0052c034 bytes 01b3fb97
+ 0054eecc bytes 1bb2fb97
- 0052c02c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0054eec4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0052c02c bytes c0ebfff0
+ 0054eec4 bytes 40ebffb0
- 0052c030 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0052c030 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052c030 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052c030 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0054eec8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0054eec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0054eec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0054eec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052c030 bytes 00740e91
+ 0054eec8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-650819dcc2b97c7ed5c44082c643624d"></a>

### [`0052c558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md) → [`0054f3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md) _INIT_25

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004c45bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md) [`004c4764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4764.md) [`004f25dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) [`004f26f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f26f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`004e7454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e7454.md) [`004e75fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004e7/004e75fc.md) [`00515474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515474.md) [`00515590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00515/00515590.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054f714",
      "incomplete_value": false,
      "site": "0054f728",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa04",
      "incomplete_value": false,
      "site": "0054fa18",
      "value": [
        "leaf",
        "const:4e75fc:8"
      ]
    },
    "old": {
      "definition_site": "0052cb6c",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "leaf",
        "const:4c4764:8"
      ]
    },
    "ordinal": 35,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0054fa0c",
      "incomplete_value": false,
      "site": "0054fa18",
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
            "const:e68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
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
            "const:3a8:8"
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
      "0054f684",
      "DATA",
      [
        "storage",
        "0030312e",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "0054f6f8",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "byte[43]"
      ]
    ],
    [
      "0054f714",
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0054f684",
      "DATA",
      [
        "storage",
        "0030312e",
        null,
        "string"
      ]
    ],
    [
      "0054f6f8",
      "DATA",
      [
        "storage",
        "00415352",
        null,
        "qword"
      ]
    ],
    [
      "0054f714",
      "PARAM",
      [
        "storage",
        "00ca4e68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052c890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md#insn-0052c890) · [`0052cb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md#insn-0052cb80) · [`0052d020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md#insn-0052d020)
- 新版 [`0054f728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054f728) · [`0054fa18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054fa18) · [`0054feb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0054f/0054f3f0.md#insn-0054feb8)

~~~diff
- 0052c890 ["INT_ADD", "register:40f0:8", ["const:52c890:8", "const:4:8"]]
- 0052c890 ["CALL", null, ["callee:004e7454:8"]]
+ 0054f728 ["INT_ADD", "register:40f0:8", ["const:54f728:8", "const:4:8"]]
+ 0054f728 ["CALL", null, ["callee:004e7454:8"]]
- 0052c890 bytes 4b5ffe97
+ 0054f728 bytes 4b5ffe97
- 0052cb80 ["INT_ADD", "register:40f0:8", ["const:52cb80:8", "const:4:8"]]
- 0052cb80 ["CALL", null, ["callee:00c57a30:8"]]
+ 0054fa18 ["INT_ADD", "register:40f0:8", ["const:54fa18:8", "const:4:8"]]
+ 0054fa18 ["CALL", null, ["callee:00c57a30:8"]]
- 0052cb80 bytes 18b91a94
+ 0054fa18 bytes 06201c94
- 0052d020 ["INT_ADD", "register:40f0:8", ["const:52d020:8", "const:4:8"]]
- 0052d020 ["CALL", null, ["callee:00515474:8"]]
+ 0054feb8 ["INT_ADD", "register:40f0:8", ["const:54feb8:8", "const:4:8"]]
+ 0054feb8 ["CALL", null, ["callee:00515474:8"]]
- 0052d020 bytes 6f15ff97
+ 0054feb8 bytes 6f15ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9448a2065d011717b2bf6865d53b9b4c"></a>

### [`0052daf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf4.md) → [`0055098c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md) FUN_0055098c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006fd020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd020.md) [`006fd460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fd/006fd460.md) · 呼出先 1件 [`00553568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/00553568.md)
- 新版 呼出元 2件 [`00727120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727120.md) [`00727560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00727/00727560.md) · 呼出先 1件 [`00576400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00576/00576400.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509a8",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052db10",
      "incomplete_value": true,
      "site": "0052db10",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "FLOAT_NAN",
            "1",
            [
              [
                "live",
                "register:5020:8"
              ]
            ]
          ],
          [
            "FLOAT_NAN",
            "1",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005509a8",
      "incomplete_value": true,
      "site": "005509ac",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
      "definition_site": "0052db10",
      "incomplete_value": true,
      "site": "0052db14",
      "value": [
        "FLOAT_LESS",
        "1",
        [
          [
            "live",
            "register:5020:8"
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
      "005509a4",
      "READ",
      [
        "storage",
        "002b2578",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005509a4",
      "READ",
      [
        "storage",
        "002c3c48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052db00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf4.md#insn-0052db00) · [`0052db0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052daf4.md#insn-0052db0c)
- 新版 [`00550998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md#insn-00550998) · [`005509a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/0055098c.md#insn-005509a4)

~~~diff
- 0052db00 ["COPY", "register:4040:8", ["const:2b2000:8"]]
+ 00550998 ["COPY", "register:4040:8", ["const:2c3000:8"]]
- 0052db00 bytes 28ecffb0
+ 00550998 bytes 88ebfff0
- 0052db0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
- 0052db0c ["LOAD", "register:5060:8", ["const:1b1:8", "tmp:0:8"]]
- 0052db0c ["COPY", "register:5068:8", ["const:0:8"]]
- 0052db0c ["COPY", "register:5070:8", ["const:0:8"]]
+ 005509a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c48:8"]]
+ 005509a4 ["LOAD", "register:5060:8", ["const:1b1:8", "tmp:0:8"]]
+ 005509a4 ["COPY", "register:5068:8", ["const:0:8"]]
+ 005509a4 ["COPY", "register:5070:8", ["const:0:8"]]
- 0052db0c bytes 03bd42fd
+ 005509a4 bytes 032546fd
~~~


<a id="compare-38c042607b0c0383295488b43b501373"></a>

### [`0052db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md) → [`00550a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md) FUN_00550a2c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0052db88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00550a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a20.md) · 呼出先 12件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00550ad0",
      "incomplete_value": true,
      "site": "00550ad4",
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
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00550a6c",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0052dbd4",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00550aac",
      "incomplete_value": true,
      "site": "00550ab4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
              ]
            ]
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
      "00550a6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "00550aa8",
      "PARAM",
      [
        "storage",
        "004377f0",
        null,
        null
      ]
    ],
    [
      "00550aac",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00550a6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "00550aa8",
      "PARAM",
      [
        "storage",
        "0045a688",
        null,
        null
      ]
    ],
    [
      "00550aac",
      "READ",
      [
        "storage",
        "00c9a858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052dbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md#insn-0052dbd4) · [`0052dc1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md#insn-0052dc1c) · [`0052dc28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md#insn-0052dc28)
- 新版 [`00550a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550a6c) · [`00550ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550ab4) · [`00550ac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550a2c.md#insn-00550ac0)

~~~diff
- 0052dbd4 ["INT_ADD", "register:40f0:8", ["const:52dbd4:8", "const:4:8"]]
- 0052dbd4 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00550a6c ["INT_ADD", "register:40f0:8", ["const:550a6c:8", "const:4:8"]]
+ 00550a6c ["CALL", null, ["ram:c57ef0:8"]]
- 0052dbd4 bytes 33b61a94
+ 00550a6c bytes 211d1c94
- 0052dc1c ["INT_ADD", "register:40f0:8", ["const:52dc1c:8", "const:4:8"]]
- 0052dc1c ["CALL", null, ["callee:00c57f30:8"]]
+ 00550ab4 ["INT_ADD", "register:40f0:8", ["const:550ab4:8", "const:4:8"]]
+ 00550ab4 ["CALL", null, ["callee:00c57f30:8"]]
- 0052dc1c bytes 31b61a94
+ 00550ab4 bytes 1f1d1c94
- 0052dc28 ["INT_ADD", "register:40f0:8", ["const:52dc28:8", "const:4:8"]]
- 0052dc28 ["CALL", null, ["ram:bdb4f0:8"]]
+ 00550ac0 ["INT_ADD", "register:40f0:8", ["const:550ac0:8", "const:4:8"]]
+ 00550ac0 ["CALL", null, ["ram:c57f40:8"]]
- 0052dc28 bytes 32b61a94
+ 00550ac0 bytes 201d1c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4614be3fbc134a5ff71554ae87249219"></a>

### [`0052e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md) → [`00550ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md) FUN_00550ef4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005321d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b668.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) · 呼出先 5件 [`0055e500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e500.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00550f38",
      "incomplete_value": false,
      "site": "00550f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00550f3c",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f58",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f74",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00550f3c",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f58",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ],
    [
      "00550f74",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md#insn-0052e094) · [`0052e09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md#insn-0052e09c) · [`0052e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md#insn-0052e0a0)
- 新版 [`00550f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f2c) · [`00550f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f34) · [`00550f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md#insn-00550f38)

~~~diff
- 0052e094 ["INT_ADD", "register:40f0:8", ["const:52e094:8", "const:4:8"]]
- 0052e094 ["CALL", null, ["callee:0055e500:8"]]
+ 00550f2c ["INT_ADD", "register:40f0:8", ["const:550f2c:8", "const:4:8"]]
+ 00550f2c ["CALL", null, ["callee:0055e500:8"]]
- 0052e094 bytes 75350094
+ 00550f2c bytes 75350094
- 0052e09c ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 00550f34 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0052e09c bytes e83500f0
+ 00550f34 bytes c83800d0
- 0052e0a0 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0052e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00550f38 ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00550f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00550f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00550f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 bytes 08813091
+ 00550f38 bytes 08811f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d6c8d56674ed80c9c75bccb1c2616e4"></a>

### [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) → [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) FUN_00551234

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) · 呼出先 6件 [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) [`00597e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e8c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.95% / 新版 87.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055128c",
      "incomplete_value": true,
      "site": "00551294",
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
      "definition_site": "0052e3f4",
      "incomplete_value": true,
      "site": "0052e3fc",
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
                "const:500:8"
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
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
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
                "const:1a3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
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
                "const:293000:8"
              ],
              [
                "leaf",
                "const:9aa:8"
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
      "definition_site": "00551288",
      "incomplete_value": true,
      "site": "00551298",
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
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
      "00551288",
      "READ",
      [
        "storage",
        "002939aa",
        null,
        "string"
      ]
    ],
    [
      "00551288",
      "READ",
      [
        "storage",
        "002939ba",
        null,
        "string"
      ]
    ],
    [
      "0055128c",
      "READ",
      [
        "storage",
        "002b1500",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00551288",
      "READ",
      [
        "storage",
        "002a31a3",
        null,
        "string"
      ]
    ],
    [
      "00551288",
      "READ",
      [
        "storage",
        "002a31b3",
        null,
        "string"
      ]
    ],
    [
      "0055128c",
      "READ",
      [
        "storage",
        "002c2b50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md#insn-0052e3e0) · [`0052e3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md#insn-0052e3e4) · [`0052e3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md#insn-0052e3e8)
- 新版 [`00551278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-00551278) · [`0055127c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-0055127c) · [`00551280`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md#insn-00551280)

~~~diff
- 0052e3e0 ["INT_ADD", "register:40f0:8", ["const:52e3e0:8", "const:4:8"]]
- 0052e3e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00551278 ["INT_ADD", "register:40f0:8", ["const:551278:8", "const:4:8"]]
+ 00551278 ["CALL", null, ["callee:00c57a90:8"]]
- 0052e3e0 bytes 18b31a94
+ 00551278 bytes 061a1c94
- 0052e3e4 ["COPY", "register:4040:8", ["const:293000:8"]]
+ 0055127c ["COPY", "register:4040:8", ["const:2a3000:8"]]
- 0052e3e4 bytes 28ebffb0
+ 0055127c bytes 88eaffd0
- 0052e3e8 ["COPY", "tmp:0:8", ["const:9aa:8"]]
- 0052e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551280 ["COPY", "tmp:0:8", ["const:1a3:8"]]
+ 00551280 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551280 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551280 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 bytes 08a92691
+ 00551280 bytes 088d0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6af8fbc9d47ddad1a4f1ea88432d813f"></a>

### [`0052eee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md) → [`00551d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md) FUN_00551d80

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b74c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e5e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00551dd0",
      "incomplete_value": true,
      "site": "00551dd0",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00551dc0",
      "incomplete_value": true,
      "site": "00551dd0",
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
      "00551db8",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00551dc0",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00551db8",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00551dc0",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ef38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md#insn-0052ef38) · [`0052ef0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md#insn-0052ef0c) · [`0052ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md#insn-0052ef14)
- 新版 [`00551dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551dd0) · [`00551da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551da4) · [`00551dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551d80.md#insn-00551dac)

~~~diff
- 0052ef38 ["COPY", "register:0:8", ["register:4048:8"]]
- 0052ef38 ["INT_ADD", "register:40f0:8", ["const:52ef38:8", "const:4:8"]]
- 0052ef38 ["CALLIND", null, ["register:0:8"]]
+ 00551dd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00551dd0 ["INT_ADD", "register:40f0:8", ["const:551dd0:8", "const:4:8"]]
+ 00551dd0 ["CALLIND", null, ["register:0:8"]]
- 0052ef38 bytes 20013fd6
+ 00551dd0 bytes 20013fd6
- 0052ef0c ["INT_ADD", "register:40f0:8", ["const:52ef0c:8", "const:4:8"]]
- 0052ef0c ["CALL", null, ["callee:0055e5e4:8"]]
+ 00551da4 ["INT_ADD", "register:40f0:8", ["const:551da4:8", "const:4:8"]]
+ 00551da4 ["CALL", null, ["callee:0055e5e4:8"]]
- 0052ef0c bytes 10320094
+ 00551da4 bytes 10320094
- 0052ef14 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00551dac ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0052ef14 bytes 683700b0
+ 00551dac bytes 483a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0833b1e00542e28e3f541c7506b8708e"></a>

### [`0052f034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md) → [`00551ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md) FUN_00551ecc

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551edc",
      "incomplete_value": true,
      "site": "00551ee8",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00551eec",
      "incomplete_value": true,
      "site": "00551ef0",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:c20:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00551ee8",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00551ef0",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551ee8",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551ef0",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md#insn-0052f040) · [`0052f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md#insn-0052f044) · [`0052f068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md#insn-0052f068)
- 新版 [`00551ed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551ed8) · [`00551edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551edc) · [`00551f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md#insn-00551f00)

~~~diff
- 0052f040 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 00551ed8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0052f040 bytes e83500d0
+ 00551ed8 bytes c83800b0
- 0052f044 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0052f044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551edc ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00551edc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551edc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551edc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f044 bytes 08813091
+ 00551edc bytes 08811f91
- 0052f068 ["INT_ADD", "register:40f0:8", ["const:52f068:8", "const:4:8"]]
- 0052f068 ["CALL", null, ["callee:00c538e0:8"]]
+ 00551f00 ["INT_ADD", "register:40f0:8", ["const:551f00:8", "const:4:8"]]
+ 00551f00 ["CALL", null, ["callee:00c538e0:8"]]
- 0052f068 bytes 8a9f1a94
+ 00551f00 bytes 78061c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab92b698ee534c6aab2f4fef42e996d"></a>

### [`0052f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md) → [`00551f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md) FUN_00551f3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00551f4c",
      "incomplete_value": false,
      "site": "00551f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f0b4",
      "incomplete_value": false,
      "site": "0052f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "definition_site": "00551f5c",
      "incomplete_value": false,
      "site": "00551f60",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:7e0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f0c4",
      "incomplete_value": false,
      "site": "0052f0c8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c20:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00551f58",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "00551f60",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00551f58",
      "DATA",
      [
        "storage",
        "00c6a7e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00551f60",
      "DATA",
      [
        "storage",
        "00c6a848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md#insn-0052f0b0) · [`0052f0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md#insn-0052f0b4) · [`0052f0d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md#insn-0052f0d8)
- 新版 [`00551f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551f48) · [`00551f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551f4c) · [`00551f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md#insn-00551f70)

~~~diff
- 0052f0b0 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 00551f48 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0052f0b0 bytes e83500d0
+ 00551f48 bytes c83800b0
- 0052f0b4 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 0052f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00551f4c ["COPY", "tmp:0:8", ["const:7e0:8"]]
+ 00551f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00551f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 bytes 08813091
+ 00551f4c bytes 08811f91
- 0052f0d8 ["INT_ADD", "register:40f0:8", ["const:52f0d8:8", "const:4:8"]]
- 0052f0d8 ["CALL", null, ["callee:00c538e0:8"]]
+ 00551f70 ["INT_ADD", "register:40f0:8", ["const:551f70:8", "const:4:8"]]
+ 00551f70 ["CALL", null, ["callee:00c538e0:8"]]
- 0052f0d8 bytes 6e9f1a94
+ 00551f70 bytes 5c061c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9737394c19e985b7112092b13abcbebd"></a>

### [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) → [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) FUN_00551fb4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055211c",
      "incomplete_value": false,
      "site": "00552124",
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
    "old": {
      "definition_site": "0052f284",
      "incomplete_value": false,
      "site": "0052f28c",
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
            "const:3a4:8"
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
      "definition_site": "0055227c",
      "incomplete_value": false,
      "site": "00552284",
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
    "old": {
      "definition_site": "0052f3e4",
      "incomplete_value": false,
      "site": "0052f3ec",
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
            "const:379:8"
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
      "definition_site": "00552294",
      "incomplete_value": false,
      "site": "005522a0",
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
    "old": {
      "definition_site": "0052f3fc",
      "incomplete_value": false,
      "site": "0052f408",
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
            "const:885:8"
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
      "0055211c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00552140",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0055227c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0055211c",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00552140",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0055227c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md#insn-0052f28c) · [`0052f3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md#insn-0052f3ec) · [`0052f408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md#insn-0052f408)
- 新版 [`00552124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-00552124) · [`00552284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-00552284) · [`005522a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md#insn-005522a0)

~~~diff
- 0052f28c ["INT_ADD", "register:40f0:8", ["const:52f28c:8", "const:4:8"]]
- 0052f28c ["CALL", null, ["callee:00441e54:8"]]
+ 00552124 ["INT_ADD", "register:40f0:8", ["const:552124:8", "const:4:8"]]
+ 00552124 ["CALL", null, ["callee:00441e54:8"]]
- 0052f28c bytes 32c0fb97
+ 00552124 bytes 4cbffb97
- 0052f3ec ["INT_ADD", "register:40f0:8", ["const:52f3ec:8", "const:4:8"]]
- 0052f3ec ["CALL", null, ["callee:00441e54:8"]]
+ 00552284 ["INT_ADD", "register:40f0:8", ["const:552284:8", "const:4:8"]]
+ 00552284 ["CALL", null, ["callee:00441e54:8"]]
- 0052f3ec bytes dabffb97
+ 00552284 bytes f4befb97
- 0052f408 ["INT_ADD", "register:40f0:8", ["const:52f408:8", "const:4:8"]]
- 0052f408 ["CALL", null, ["callee:004427b4:8"]]
+ 005522a0 ["INT_ADD", "register:40f0:8", ["const:5522a0:8", "const:4:8"]]
+ 005522a0 ["CALL", null, ["callee:004427b4:8"]]
- 0052f408 bytes 2bc2fb97
+ 005522a0 bytes 45c1fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75f39636f9dd5363673836398d823e86"></a>

### [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) → [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) FUN_00552800

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00551fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551fb4.md) [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00552964",
      "incomplete_value": false,
      "site": "0055296c",
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
    "old": {
      "definition_site": "0052facc",
      "incomplete_value": false,
      "site": "0052fad4",
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
            "const:3a4:8"
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
      "definition_site": "00552988",
      "incomplete_value": false,
      "site": "00552994",
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
    "old": {
      "definition_site": "0052faf0",
      "incomplete_value": false,
      "site": "0052fafc",
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
            "const:885:8"
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
      "definition_site": "00552ac4",
      "incomplete_value": false,
      "site": "00552acc",
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
    "old": {
      "definition_site": "0052fc2c",
      "incomplete_value": false,
      "site": "0052fc34",
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
            "const:379:8"
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
      "00552964",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00552988",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00552ac4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00552964",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00552988",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00552ac4",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052fad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md#insn-0052fad4) · [`0052fafc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md#insn-0052fafc) · [`0052fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md#insn-0052fc34)
- 新版 [`0055296c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-0055296c) · [`00552994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-00552994) · [`00552acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md#insn-00552acc)

~~~diff
- 0052fad4 ["INT_ADD", "register:40f0:8", ["const:52fad4:8", "const:4:8"]]
- 0052fad4 ["CALL", null, ["callee:00441e54:8"]]
+ 0055296c ["INT_ADD", "register:40f0:8", ["const:55296c:8", "const:4:8"]]
+ 0055296c ["CALL", null, ["callee:00441e54:8"]]
- 0052fad4 bytes 20befb97
+ 0055296c bytes 3abdfb97
- 0052fafc ["INT_ADD", "register:40f0:8", ["const:52fafc:8", "const:4:8"]]
- 0052fafc ["CALL", null, ["callee:004427b4:8"]]
+ 00552994 ["INT_ADD", "register:40f0:8", ["const:552994:8", "const:4:8"]]
+ 00552994 ["CALL", null, ["callee:004427b4:8"]]
- 0052fafc bytes 6ec0fb97
+ 00552994 bytes 88bffb97
- 0052fc34 ["INT_ADD", "register:40f0:8", ["const:52fc34:8", "const:4:8"]]
- 0052fc34 ["CALL", null, ["callee:00441e54:8"]]
+ 00552acc ["INT_ADD", "register:40f0:8", ["const:552acc:8", "const:4:8"]]
+ 00552acc ["CALL", null, ["callee:00441e54:8"]]
- 0052fc34 bytes c8bdfb97
+ 00552acc bytes e2bcfb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98cf81feb16b36164721a182b0d8459"></a>

### [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) → [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) FUN_00553038

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00552800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00552/00552800.md) [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00553198",
      "incomplete_value": false,
      "site": "005531a0",
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
    "old": {
      "definition_site": "00530300",
      "incomplete_value": false,
      "site": "00530308",
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
            "const:3a4:8"
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
      "definition_site": "005531bc",
      "incomplete_value": false,
      "site": "005531c8",
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
    "old": {
      "definition_site": "00530324",
      "incomplete_value": false,
      "site": "00530330",
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
            "const:885:8"
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
      "definition_site": "005532f8",
      "incomplete_value": false,
      "site": "00553300",
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
    "old": {
      "definition_site": "00530460",
      "incomplete_value": false,
      "site": "00530468",
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
            "const:379:8"
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
      "00553198",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005531bc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "005532f8",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00553198",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005531bc",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "005532f8",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md#insn-00530308) · [`00530330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md#insn-00530330) · [`00530468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md#insn-00530468)
- 新版 [`005531a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-005531a0) · [`005531c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-005531c8) · [`00553300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md#insn-00553300)

~~~diff
- 00530308 ["INT_ADD", "register:40f0:8", ["const:530308:8", "const:4:8"]]
- 00530308 ["CALL", null, ["callee:00441e54:8"]]
+ 005531a0 ["INT_ADD", "register:40f0:8", ["const:5531a0:8", "const:4:8"]]
+ 005531a0 ["CALL", null, ["callee:00441e54:8"]]
- 00530308 bytes 13bcfb97
+ 005531a0 bytes 2dbbfb97
- 00530330 ["INT_ADD", "register:40f0:8", ["const:530330:8", "const:4:8"]]
- 00530330 ["CALL", null, ["callee:004427b4:8"]]
+ 005531c8 ["INT_ADD", "register:40f0:8", ["const:5531c8:8", "const:4:8"]]
+ 005531c8 ["CALL", null, ["callee:004427b4:8"]]
- 00530330 bytes 61befb97
+ 005531c8 bytes 7bbdfb97
- 00530468 ["INT_ADD", "register:40f0:8", ["const:530468:8", "const:4:8"]]
- 00530468 ["CALL", null, ["callee:00441e54:8"]]
+ 00553300 ["INT_ADD", "register:40f0:8", ["const:553300:8", "const:4:8"]]
+ 00553300 ["CALL", null, ["callee:00441e54:8"]]
- 00530468 bytes bbbbfb97
+ 00553300 bytes d5bafb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9721b511f3b096836f29aaa1e847e46d"></a>

### [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) → [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) FUN_0055386c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00553038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/00553038.md) [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005539c8",
      "incomplete_value": false,
      "site": "005539d0",
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
    "old": {
      "definition_site": "00530b30",
      "incomplete_value": false,
      "site": "00530b38",
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
            "const:3a4:8"
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
      "definition_site": "005539ec",
      "incomplete_value": false,
      "site": "005539f8",
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
    "old": {
      "definition_site": "00530b54",
      "incomplete_value": false,
      "site": "00530b60",
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
            "const:885:8"
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
      "definition_site": "00553b28",
      "incomplete_value": false,
      "site": "00553b30",
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
    "old": {
      "definition_site": "00530c90",
      "incomplete_value": false,
      "site": "00530c98",
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
            "const:379:8"
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
      "005539c8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005539ec",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00553b28",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005539c8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005539ec",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00553b28",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md#insn-00530b38) · [`00530b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md#insn-00530b60) · [`00530c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md#insn-00530c98)
- 新版 [`005539d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-005539d0) · [`005539f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-005539f8) · [`00553b30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md#insn-00553b30)

~~~diff
- 00530b38 ["INT_ADD", "register:40f0:8", ["const:530b38:8", "const:4:8"]]
- 00530b38 ["CALL", null, ["callee:00441e54:8"]]
+ 005539d0 ["INT_ADD", "register:40f0:8", ["const:5539d0:8", "const:4:8"]]
+ 005539d0 ["CALL", null, ["callee:00441e54:8"]]
- 00530b38 bytes 07bafb97
+ 005539d0 bytes 21b9fb97
- 00530b60 ["INT_ADD", "register:40f0:8", ["const:530b60:8", "const:4:8"]]
- 00530b60 ["CALL", null, ["callee:004427b4:8"]]
+ 005539f8 ["INT_ADD", "register:40f0:8", ["const:5539f8:8", "const:4:8"]]
+ 005539f8 ["CALL", null, ["callee:004427b4:8"]]
- 00530b60 bytes 55bcfb97
+ 005539f8 bytes 6fbbfb97
- 00530c98 ["INT_ADD", "register:40f0:8", ["const:530c98:8", "const:4:8"]]
- 00530c98 ["CALL", null, ["callee:00441e54:8"]]
+ 00553b30 ["INT_ADD", "register:40f0:8", ["const:553b30:8", "const:4:8"]]
+ 00553b30 ["CALL", null, ["callee:00441e54:8"]]
- 00530c98 bytes afb9fb97
+ 00553b30 bytes c9b8fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b8ebbb0c607bf1bbf816235bd735b7c"></a>

### [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) → [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) FUN_0055408c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0055386c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00553/0055386c.md) [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005541e0",
      "incomplete_value": false,
      "site": "005541e8",
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
    "old": {
      "definition_site": "00531348",
      "incomplete_value": false,
      "site": "00531350",
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
            "const:3a4:8"
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
      "definition_site": "00554204",
      "incomplete_value": false,
      "site": "00554210",
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
    "old": {
      "definition_site": "0053136c",
      "incomplete_value": false,
      "site": "00531378",
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
            "const:885:8"
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
      "definition_site": "0055433c",
      "incomplete_value": false,
      "site": "00554344",
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
    "old": {
      "definition_site": "005314a4",
      "incomplete_value": false,
      "site": "005314ac",
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
            "const:379:8"
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
      "005541e0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00554204",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0055433c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005541e0",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "00554204",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "0055433c",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md#insn-00531350) · [`00531378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md#insn-00531378) · [`005314ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md#insn-005314ac)
- 新版 [`005541e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-005541e8) · [`00554210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-00554210) · [`00554344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md#insn-00554344)

~~~diff
- 00531350 ["INT_ADD", "register:40f0:8", ["const:531350:8", "const:4:8"]]
- 00531350 ["CALL", null, ["callee:00441e54:8"]]
+ 005541e8 ["INT_ADD", "register:40f0:8", ["const:5541e8:8", "const:4:8"]]
+ 005541e8 ["CALL", null, ["callee:00441e54:8"]]
- 00531350 bytes 01b8fb97
+ 005541e8 bytes 1bb7fb97
- 00531378 ["INT_ADD", "register:40f0:8", ["const:531378:8", "const:4:8"]]
- 00531378 ["CALL", null, ["callee:004427b4:8"]]
+ 00554210 ["INT_ADD", "register:40f0:8", ["const:554210:8", "const:4:8"]]
+ 00554210 ["CALL", null, ["callee:004427b4:8"]]
- 00531378 bytes 4fbafb97
+ 00554210 bytes 69b9fb97
- 005314ac ["INT_ADD", "register:40f0:8", ["const:5314ac:8", "const:4:8"]]
- 005314ac ["CALL", null, ["callee:00441e54:8"]]
+ 00554344 ["INT_ADD", "register:40f0:8", ["const:554344:8", "const:4:8"]]
+ 00554344 ["CALL", null, ["callee:00441e54:8"]]
- 005314ac bytes aab7fb97
+ 00554344 bytes c4b6fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e6060111edc2d0b7f444a6d72125da"></a>

### [`005319f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md) → [`00554888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md) FUN_00554888

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) [`005319f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`0055408c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/0055408c.md) [`00554888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) · 呼出先 22件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`00441cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/00441cac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005549d8",
      "incomplete_value": false,
      "site": "005549e0",
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
    "old": {
      "definition_site": "00531b40",
      "incomplete_value": false,
      "site": "00531b48",
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
            "const:3a4:8"
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
      "definition_site": "00554b34",
      "incomplete_value": false,
      "site": "00554b3c",
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
    "old": {
      "definition_site": "00531c9c",
      "incomplete_value": false,
      "site": "00531ca4",
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
            "const:379:8"
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
      "definition_site": "00554b4c",
      "incomplete_value": false,
      "site": "00554b58",
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
    "old": {
      "definition_site": "00531cb4",
      "incomplete_value": false,
      "site": "00531cc0",
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
            "const:885:8"
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
      "005549d8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "005549fc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00554b34",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005549d8",
      "PARAM",
      [
        "storage",
        "002b7f13",
        null,
        null
      ]
    ],
    [
      "005549fc",
      "PARAM",
      [
        "storage",
        "002c0ea9",
        null,
        "string"
      ]
    ],
    [
      "00554b34",
      "PARAM",
      [
        "storage",
        "002b5da7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md#insn-00531b48) · [`00531ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md#insn-00531ca4) · [`00531cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md#insn-00531cc0)
- 新版 [`005549e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-005549e0) · [`00554b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-00554b3c) · [`00554b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00554/00554888.md#insn-00554b58)

~~~diff
- 00531b48 ["INT_ADD", "register:40f0:8", ["const:531b48:8", "const:4:8"]]
- 00531b48 ["CALL", null, ["callee:00441e54:8"]]
+ 005549e0 ["INT_ADD", "register:40f0:8", ["const:5549e0:8", "const:4:8"]]
+ 005549e0 ["CALL", null, ["callee:00441e54:8"]]
- 00531b48 bytes 03b6fb97
+ 005549e0 bytes 1db5fb97
- 00531ca4 ["INT_ADD", "register:40f0:8", ["const:531ca4:8", "const:4:8"]]
- 00531ca4 ["CALL", null, ["callee:00441e54:8"]]
+ 00554b3c ["INT_ADD", "register:40f0:8", ["const:554b3c:8", "const:4:8"]]
+ 00554b3c ["CALL", null, ["callee:00441e54:8"]]
- 00531ca4 bytes acb5fb97
+ 00554b3c bytes c6b4fb97
- 00531cc0 ["INT_ADD", "register:40f0:8", ["const:531cc0:8", "const:4:8"]]
- 00531cc0 ["CALL", null, ["callee:004427b4:8"]]
+ 00554b58 ["INT_ADD", "register:40f0:8", ["const:554b58:8", "const:4:8"]]
+ 00554b58 ["CALL", null, ["callee:004427b4:8"]]
- 00531cc0 bytes fdb7fb97
+ 00554b58 bytes 17b7fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-953739dc61e311d1de828de53e65425e"></a>

### [`005321d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) → [`00555070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md) FUN_00555070

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0052efd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052efd4.md) · 呼出先 6件 [`0052e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md) [`0053233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053233c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00551e6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551e6c.md) · 呼出先 6件 [`00550ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550ef4.md) [`005551d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/005551d4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005550a8",
      "incomplete_value": false,
      "site": "005550c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532210",
      "incomplete_value": false,
      "site": "0053222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "005550c4",
      "DATA",
      [
        "storage",
        "00bedd18",
        null,
        "pointer"
      ]
    ],
    [
      "00555158",
      "READ",
      [
        "storage",
        "00bedd28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005550c4",
      "DATA",
      [
        "storage",
        "00c6a8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00555158",
      "READ",
      [
        "storage",
        "00c6a8e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md#insn-00532200) · [`0053220c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md#insn-0053220c) · [`00532210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md#insn-00532210)
- 新版 [`00555098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-00555098) · [`005550a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-005550a4) · [`005550a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555070.md#insn-005550a8)

~~~diff
- 00532200 ["INT_ADD", "register:40f0:8", ["const:532200:8", "const:4:8"]]
- 00532200 ["CALL", null, ["callee:00c57a90:8"]]
+ 00555098 ["INT_ADD", "register:40f0:8", ["const:555098:8", "const:4:8"]]
+ 00555098 ["CALL", null, ["callee:00c57a90:8"]]
- 00532200 bytes 90a31a94
+ 00555098 bytes 7e0a1c94
- 0053220c ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 005550a4 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053220c bytes c83500f0
+ 005550a4 bytes a83800b0
- 00532210 ["COPY", "tmp:0:8", ["const:d18:8"]]
- 00532210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005550a8 ["COPY", "tmp:0:8", ["const:8d8:8"]]
+ 005550a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005550a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005550a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532210 bytes 08613491
+ 005550a8 bytes 08612391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-556245c298a356a0f782a26b29bdcbb5"></a>

### [`0053239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md) → [`00555234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md) FUN_00555234

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00590d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00590/00590d78.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00555240",
      "incomplete_value": false,
      "site": "00555240",
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
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005323a8",
      "incomplete_value": false,
      "site": "005323a8",
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
            "const:d48:8"
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
      "00555238",
      "READ",
      [
        "storage",
        "00c25d48",
        null,
        "undefined4"
      ]
    ],
    [
      "00555240",
      "WRITE",
      [
        "storage",
        "00c25d48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00555238",
      "READ",
      [
        "storage",
        "00ca5808",
        null,
        "undefined4"
      ]
    ],
    [
      "00555240",
      "WRITE",
      [
        "storage",
        "00ca5808",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005323a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md#insn-005323a8) · [`0053239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md#insn-0053239c) · [`005323a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md#insn-005323a0)
- 新版 [`00555240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md#insn-00555240) · [`00555234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md#insn-00555234) · [`00555238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555234.md#insn-00555238)

~~~diff
- 005323a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
- 005323a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00555240 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
+ 00555240 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005323a8 bytes 09490db9
+ 00555240 bytes 090908b9
- 0053239c ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 00555234 ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 0053239c bytes 883700f0
+ 00555234 bytes 883a0090
- 005323a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
- 005323a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 005323a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00555238 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:808:8"]]
+ 00555238 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00555238 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 005323a0 bytes 09494db9
+ 00555238 bytes 090948b9
~~~


<a id="compare-74bd26d28ecf19649c3e27b8248058c9"></a>

### [`005325a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md) → [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) FUN_00555438

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005323ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323ec.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md)
- 新版 呼出元 1件 [`00555284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555284.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, control_flow, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 5件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00555508",
      "incomplete_value": true,
      "site": "00555508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532670",
      "incomplete_value": true,
      "site": "00532670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005555dc",
      "incomplete_value": true,
      "site": "005555dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532744",
      "incomplete_value": true,
      "site": "00532744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "005556b4",
      "incomplete_value": true,
      "site": "005556b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053281c",
      "incomplete_value": true,
      "site": "0053281c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:d98:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00555490",
      "READ",
      [
        "storage",
        "00c25da8",
        null,
        "undefined1"
      ]
    ],
    [
      "00555498",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined8"
      ]
    ],
    [
      "0055549c",
      "WRITE",
      [
        "storage",
        "00c25d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00555490",
      "READ",
      [
        "storage",
        "00ca5868",
        null,
        "undefined1"
      ]
    ],
    [
      "00555498",
      "READ",
      [
        "storage",
        "00ca5850",
        null,
        "undefined8"
      ]
    ],
    [
      "0055549c",
      "WRITE",
      [
        "storage",
        "00ca5858",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md#insn-00532670) · [`00532744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md#insn-00532744) · [`0053281c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md#insn-0053281c)
- 新版 [`00555508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-00555508) · [`005555dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-005555dc) · [`005556b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md#insn-005556b4)

~~~diff
- 00532670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
- 00532670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
+ 00555508 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:858:8"]]
+ 00555508 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00532670 bytes 3bcd06f9
+ 00555508 bytes 3b2d04f9
- 00532744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
- 00532744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
+ 005555dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:858:8"]]
+ 005555dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 00532744 bytes 3acd06f9
+ 005555dc bytes 3a2d04f9
- 0053281c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
- 0053281c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 005556b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:858:8"]]
+ 005556b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0053281c bytes 3ccd06f9
+ 005556b4 bytes 3c2d04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c668b547e584c24466f739924e73fb9"></a>

### [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) → [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) FUN_00555c54

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00536a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md) [`00537560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md) · 呼出先 8件 [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`00538370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md) [`0056d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d0d0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) · 呼出先 8件 [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`0058ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.86% / 新版 98.86%

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
      "site": "00555d0c",
      "value": [
        "leaf",
        "ram:58ff68:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00532e74",
      "value": [
        "leaf",
        "ram:56d0d0:8"
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
      "00555d0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056d0d0"
      ]
    ]
  ],
  "added": [
    [
      "00555d0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058ff68"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md#insn-00532e74) · [`00532e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md#insn-00532e08) · [`00532e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md#insn-00532e24)
- 新版 [`00555d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555d0c) · [`00555ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555ca0) · [`00555cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md#insn-00555cbc)

~~~diff
- 00532e74 ["INT_ADD", "register:40f0:8", ["const:532e74:8", "const:4:8"]]
- 00532e74 ["CALL", null, ["ram:56d0d0:8"]]
+ 00555d0c ["INT_ADD", "register:40f0:8", ["const:555d0c:8", "const:4:8"]]
+ 00555d0c ["CALL", null, ["ram:58ff68:8"]]
- 00532e74 bytes 97e80094
+ 00555d0c bytes 97e80094
- 00532e08 ["INT_ADD", "register:40f0:8", ["const:532e08:8", "const:4:8"]]
- 00532e08 ["CALL", null, ["callee:00c57a90:8"]]
+ 00555ca0 ["INT_ADD", "register:40f0:8", ["const:555ca0:8", "const:4:8"]]
+ 00555ca0 ["CALL", null, ["callee:00c57a90:8"]]
- 00532e08 bytes 8ea01a94
+ 00555ca0 bytes 7c071c94
- 00532e24 ["INT_ADD", "register:40f0:8", ["const:532e24:8", "const:4:8"]]
- 00532e24 ["CALL", null, ["callee:00c57c90:8"]]
+ 00555cbc ["INT_ADD", "register:40f0:8", ["const:555cbc:8", "const:4:8"]]
+ 00555cbc ["CALL", null, ["callee:00c57c90:8"]]
- 00532e24 bytes 07a11a94
+ 00555cbc bytes f5071c94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d997e6002da55ae714ad5262f053b04"></a>

### [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) → [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) FUN_00555dcc

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005325a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`0053699c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md) [`00538370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00555438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555438.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00556f8c",
      "incomplete_value": true,
      "site": "00556f90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:110:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005340f4",
      "incomplete_value": true,
      "site": "005340f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 211,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00555e0c",
      "READ",
      [
        "storage",
        "00c1b460",
        null,
        "pointer"
      ]
    ],
    [
      "00555e18",
      "READ",
      [
        "storage",
        "00c26594",
        null,
        "undefined4"
      ]
    ],
    [
      "00555efc",
      "READ",
      [
        "storage",
        "00c26590",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00555e0c",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ],
    [
      "00555e18",
      "READ",
      [
        "storage",
        "00ca6054",
        null,
        "undefined4"
      ]
    ],
    [
      "00555efc",
      "READ",
      [
        "storage",
        "00ca6050",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md#insn-00532f68) · [`00532f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md#insn-00532f74) · [`0053305c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md#insn-0053305c)
- 新版 [`00555e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555e00) · [`00555e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555e0c) · [`00555ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md#insn-00555ef4)

~~~diff
- 00532f68 ["COPY", "register:4050:8", ["const:c1b000:8"]]
+ 00555e00 ["COPY", "register:4050:8", ["const:c9a000:8"]]
- 00532f68 bytes 4a3700b0
+ 00555e00 bytes 2a3a00b0
- 00532f74 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:460:8"]]
- 00532f74 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00555e0c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e50:8"]]
+ 00555e0c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00532f74 bytes 4a3142f9
+ 00555e0c bytes 4a2947f9
- 0053305c ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 00555ef4 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 0053305c bytes 883700f0
+ 00555ef4 bytes 883a00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c4348255942d035d2e8e55cdee34168"></a>

### [`00536a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md) → [`00559924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md) FUN_00559924

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537664.md) · 呼出先 14件 [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md)
- 新版 呼出元 1件 [`0055a4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a4fc.md) · 呼出先 14件 [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`0046c420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c420.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md)

変更の種類 call_argument_candidate, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.98% / 新版 93.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00559a48",
      "incomplete_value": false,
      "site": "00559a4c",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536bb0",
      "incomplete_value": false,
      "site": "00536bb4",
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
            "const:d50:8"
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
      "definition_site": "00559aac",
      "incomplete_value": false,
      "site": "00559ab0",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c14",
      "incomplete_value": false,
      "site": "00536c18",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00559af4",
      "incomplete_value": false,
      "site": "00559b04",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c5c",
      "incomplete_value": false,
      "site": "00536c6c",
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
            "const:d68:8"
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
      "0055995c",
      "READ",
      [
        "storage",
        "00c25d68",
        null,
        "undefined1"
      ]
    ],
    [
      "00559964",
      "READ",
      [
        "storage",
        "00c25d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00559968",
      "WRITE",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055995c",
      "READ",
      [
        "storage",
        "00ca5828",
        null,
        "undefined1"
      ]
    ],
    [
      "00559964",
      "READ",
      [
        "storage",
        "00ca5810",
        null,
        "undefined8"
      ]
    ],
    [
      "00559968",
      "WRITE",
      [
        "storage",
        "00ca5818",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md#insn-00536bb4) · [`00536c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md#insn-00536c18) · [`00536c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md#insn-00536c6c)
- 新版 [`00559a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559a4c) · [`00559ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559ab0) · [`00559b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559924.md#insn-00559b04)

~~~diff
- 00536bb4 ["INT_ADD", "register:40f0:8", ["const:536bb4:8", "const:4:8"]]
- 00536bb4 ["CALL", null, ["callee:00559bd0:8"]]
+ 00559a4c ["INT_ADD", "register:40f0:8", ["const:559a4c:8", "const:4:8"]]
+ 00559a4c ["CALL", null, ["callee:00559bd0:8"]]
- 00536bb4 bytes 61000094
+ 00559a4c bytes 61000094
- 00536c18 ["INT_ADD", "register:40f0:8", ["const:536c18:8", "const:4:8"]]
- 00536c18 ["CALL", null, ["callee:00559f00:8"]]
+ 00559ab0 ["INT_ADD", "register:40f0:8", ["const:559ab0:8", "const:4:8"]]
+ 00559ab0 ["CALL", null, ["callee:00559f00:8"]]
- 00536c18 bytes 14010094
+ 00559ab0 bytes 14010094
- 00536c6c ["INT_ADD", "register:40f0:8", ["const:536c6c:8", "const:4:8"]]
- 00536c6c ["CALL", null, ["callee:00c57a50:8"]]
+ 00559b04 ["INT_ADD", "register:40f0:8", ["const:559b04:8", "const:4:8"]]
+ 00559b04 ["CALL", null, ["callee:00c57a50:8"]]
- 00536c6c bytes e5901a94
+ 00559b04 bytes d3f71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ce6ad906cc1837c2c045eba0cb471b"></a>

### [`00537560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md) → [`0055a3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md) FUN_0055a3f8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) · 呼出先 8件 [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md) [`0056d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d0d0.md)
- 新版 呼出元 1件 [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) · 呼出先 8件 [`004684a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004684a8.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00559bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559bd0.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) [`0058ff68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058ff68.md)

変更の種類 call_argument_candidate, constant, control_flow, operands_and_dependencies, operation_sequence

命令の説明率　旧版 83.08% / 新版 83.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055a498",
      "incomplete_value": false,
      "site": "0055a4a4",
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
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537600",
      "incomplete_value": false,
      "site": "0053760c",
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
            "const:d88:8"
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
      "definition_site": "0055a4c0",
      "incomplete_value": false,
      "site": "0055a4d8",
      "value": [
        "leaf",
        "const:4684a8:8"
      ]
    },
    "old": {
      "definition_site": "00537628",
      "incomplete_value": false,
      "site": "00537640",
      "value": [
        "leaf",
        "const:445610:8"
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055a4c8",
      "incomplete_value": false,
      "site": "0055a4d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c62000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537630",
      "incomplete_value": false,
      "site": "00537640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "0055a410",
      "READ",
      [
        "storage",
        "00c25d88",
        null,
        "undefined1"
      ]
    ],
    [
      "0055a420",
      "READ",
      [
        "storage",
        "00c25d70",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a430",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0055a410",
      "READ",
      [
        "storage",
        "00ca5848",
        null,
        "undefined1"
      ]
    ],
    [
      "0055a420",
      "READ",
      [
        "storage",
        "00ca5830",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a430",
      "PARAM",
      [
        "storage",
        "00ca5830",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md#insn-0053760c) · [`00537640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md#insn-00537640) · [`0053764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md#insn-0053764c)
- 新版 [`0055a4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a4a4) · [`0055a4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a4d8) · [`0055a4e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a3f8.md#insn-0055a4e4)

~~~diff
- 0053760c ["INT_ADD", "register:40f0:8", ["const:53760c:8", "const:4:8"]]
- 0053760c ["CALL", null, ["callee:00c57a50:8"]]
+ 0055a4a4 ["INT_ADD", "register:40f0:8", ["const:55a4a4:8", "const:4:8"]]
+ 0055a4a4 ["CALL", null, ["callee:00c57a50:8"]]
- 0053760c bytes 7d8e1a94
+ 0055a4a4 bytes 6bf51b94
- 00537640 ["INT_ADD", "register:40f0:8", ["const:537640:8", "const:4:8"]]
- 00537640 ["CALL", null, ["callee:00c57a30:8"]]
+ 0055a4d8 ["INT_ADD", "register:40f0:8", ["const:55a4d8:8", "const:4:8"]]
+ 0055a4d8 ["CALL", null, ["callee:00c57a30:8"]]
- 00537640 bytes 688e1a94
+ 0055a4d8 bytes 56f51b94
- 0053764c ["INT_ADD", "register:40f0:8", ["const:53764c:8", "const:4:8"]]
- 0053764c ["CALL", null, ["callee:00c57a70:8"]]
+ 0055a4e4 ["INT_ADD", "register:40f0:8", ["const:55a4e4:8", "const:4:8"]]
+ 0055a4e4 ["CALL", null, ["callee:00c57a70:8"]]
- 0053764c bytes 758e1a94
+ 0055a4e4 bytes 63f51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeecf866eaad5c69276d79451d6f76b9"></a>

### [`005376d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005376d0.md) → [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md) FUN_0055a568

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a570",
      "incomplete_value": true,
      "site": "0055a574",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005376d8",
      "incomplete_value": true,
      "site": "005376dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a570",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a570",
      "READ",
      [
        "storage",
        "00ca6010",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005376d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005376d0.md#insn-005376d0) · [`005376d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005376d0.md#insn-005376d4)
- 新版 [`0055a568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md#insn-0055a568) · [`0055a56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a568.md#insn-0055a56c)

~~~diff
- 005376d0 ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0055a568 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 005376d0 bytes 683700f0
+ 0055a568 bytes 683a0090
- 005376d4 ["COPY", "tmp:0:8", ["const:550:8"]]
- 005376d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a56c ["COPY", "tmp:0:8", ["const:10:8"]]
+ 0055a56c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a56c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a56c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005376d4 bytes 08411591
+ 0055a56c bytes 08410091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e533d23f69845c8869206e0459eaee84"></a>

### [`00537724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537724.md) → [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md) FUN_0055a5bc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00467d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467d7c.md) [`00468cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468cc8.md) [`00468de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468de0.md) [`0046a9bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a9bc.md) [`0046ab08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046ab08.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a5dc",
      "incomplete_value": true,
      "site": "0055a5dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:e68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537744",
      "incomplete_value": true,
      "site": "00537744",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:478:8"
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
      "0055a5c8",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "0055a5cc",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a5d4",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0055a5c8",
      "READ",
      [
        "storage",
        "00c9ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0055a5cc",
      "READ",
      [
        "storage",
        "00ca6110",
        null,
        "undefined8"
      ]
    ],
    [
      "0055a5d4",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537724.md#insn-00537724) · [`0053772c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537724.md#insn-0053772c) · [`00537730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537724.md#insn-00537730)
- 新版 [`0055a5bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5bc) · [`0055a5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5c4) · [`0055a5c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5bc.md#insn-0055a5c8)

~~~diff
- 00537724 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0055a5bc ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00537724 bytes 28370090
+ 0055a5bc bytes 083a0090
- 0053772c ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 0055a5c4 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0053772c bytes 29370090
+ 0055a5c4 bytes 093a0090
- 00537730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
- 00537730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055a5c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e40:8"]]
+ 0055a5c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537730 bytes 082942f9
+ 0055a5c8 bytes 082147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e329408441a7be33f35f457d7be7ce43"></a>

### [`0053774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md) → [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md) FUN_0055a5e4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) · 呼出先 0件 
- 新版 呼出元 3件 [`0046792c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/0046792c.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a5f4",
      "incomplete_value": true,
      "site": "0055a5f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a5f4",
      "incomplete_value": true,
      "site": "0055a5f4",
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
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055a604",
      "incomplete_value": true,
      "site": "0055a604",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053776c",
      "incomplete_value": true,
      "site": "0053776c",
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
            "const:8:8"
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
      "0055a5f0",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ],
    [
      "0055a5f4",
      "WRITE",
      [
        "storage",
        "00c23f38",
        null,
        "undefined4"
      ]
    ],
    [
      "0055a5f4",
      "WRITE",
      [
        "storage",
        "00c23f3c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a5f0",
      "READ",
      [
        "storage",
        "00c9ae70",
        null,
        "pointer"
      ]
    ],
    [
      "0055a5f4",
      "WRITE",
      [
        "storage",
        "00ca3a20",
        null,
        "undefined4"
      ]
    ],
    [
      "0055a5f4",
      "WRITE",
      [
        "storage",
        "00ca3a24",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md#insn-0053774c) · [`00537754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md#insn-00537754) · [`00537758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md#insn-00537758)
- 新版 [`0055a5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5e4) · [`0055a5ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5ec) · [`0055a5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a5e4.md#insn-0055a5f0)

~~~diff
- 0053774c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 0055a5e4 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0053774c bytes 28370090
+ 0055a5e4 bytes 083a0090
- 00537754 ["COPY", "register:4048:8", ["const:c1b000:8"]]
+ 0055a5ec ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 00537754 bytes 29370090
+ 0055a5ec bytes 093a0090
- 00537758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:480:8"]]
- 00537758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055a5f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0055a5f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537758 bytes 084142f9
+ 0055a5f0 bytes 083947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8192e1dc42986d3c172a74867eafd075"></a>

### [`005377dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377dc.md) → [`0055a674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a674.md) FUN_0055a674

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 0件 
- 新版 呼出元 5件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a67c",
      "incomplete_value": true,
      "site": "0055a680",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005377e4",
      "incomplete_value": true,
      "site": "005377e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a67c",
      "READ",
      [
        "storage",
        "00c265a0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a67c",
      "READ",
      [
        "storage",
        "00ca6060",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377dc.md#insn-005377dc) · [`005377e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377dc.md#insn-005377e0)
- 新版 [`0055a674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a674.md#insn-0055a674) · [`0055a678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a674.md#insn-0055a678)

~~~diff
- 005377dc ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0055a674 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 005377dc bytes 683700f0
+ 0055a674 bytes 683a0090
- 005377e0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 005377e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a678 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0055a678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377e0 bytes 08811691
+ 0055a678 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5ee39cb6172d4a3a97c9f87afab56ea"></a>

### [`005377ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377ec.md) → [`0055a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a684.md) FUN_0055a684

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 0件 
- 新版 呼出元 5件 [`006181c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00618/006181c0.md) [`008aabe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008aa/008aabe4.md) [`008abcb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ab/008abcb4.md) [`008d8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8cd0.md) [`00b2ca20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2c/00b2ca20.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0055a68c",
      "incomplete_value": true,
      "site": "0055a690",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005377f4",
      "incomplete_value": true,
      "site": "005377f8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055a68c",
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0055a68c",
      "READ",
      [
        "storage",
        "00ca605c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377ec.md#insn-005377ec) · [`005377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377ec.md#insn-005377f0)
- 新版 [`0055a684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a684.md#insn-0055a684) · [`0055a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a684.md#insn-0055a688)

~~~diff
- 005377ec ["COPY", "register:4040:8", ["const:c26000:8"]]
+ 0055a684 ["COPY", "register:4040:8", ["const:ca6000:8"]]
- 005377ec bytes 683700f0
+ 0055a684 bytes 683a0090
- 005377f0 ["COPY", "tmp:0:8", ["const:59c:8"]]
- 005377f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055a688 ["COPY", "tmp:0:8", ["const:5c:8"]]
+ 0055a688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055a688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377f0 bytes 08711691
+ 0055a688 bytes 08710191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d81967f6d7f9a03388ea9dd6ad15a8"></a>

### [`00538260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md) → [`0055b0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md) FUN_0055b0f8

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0055b108",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00538270",
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
      "definition_site": "0055b104",
      "incomplete_value": false,
      "site": "0055b108",
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
      "definition_site": "0053826c",
      "incomplete_value": false,
      "site": "00538270",
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
      "0055b104",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0055b108",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0055b104",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0055b108",
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

- 旧版 [`00538270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md#insn-00538270) · [`00538268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md#insn-00538268) · [`0053826c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md#insn-0053826c)
- 新版 [`0055b108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md#insn-0055b108) · [`0055b100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md#insn-0055b100) · [`0055b104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b0f8.md#insn-0055b104)

~~~diff
- 00538270 ["INT_ADD", "register:40f0:8", ["const:538270:8", "const:4:8"]]
- 00538270 ["CALL", null, ["ram:418c38:8"]]
+ 0055b108 ["INT_ADD", "register:40f0:8", ["const:55b108:8", "const:4:8"]]
+ 0055b108 ["CALL", null, ["ram:43b738:8"]]
- 00538270 bytes 7282fb97
+ 0055b108 bytes 8c81fb97
- 00538268 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0055b100 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00538268 bytes 60ebfff0
+ 0055b100 bytes e0eaff90
- 0053826c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0053826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b104 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0055b104 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b104 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b104 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053826c bytes 00740e91
+ 0055b104 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-181c27f424f964e01c9649e84a06b1d3"></a>

### [`00538274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md) → [`0055b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md) FUN_0055b10c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0055a6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055a/0055a6b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0055b11c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00538284",
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
      "definition_site": "0055b118",
      "incomplete_value": false,
      "site": "0055b11c",
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
      "definition_site": "00538280",
      "incomplete_value": false,
      "site": "00538284",
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
      "0055b118",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0055b11c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0055b118",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0055b11c",
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

- 旧版 [`00538284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md#insn-00538284) · [`0053827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md#insn-0053827c) · [`00538280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md#insn-00538280)
- 新版 [`0055b11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md#insn-0055b11c) · [`0055b114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md#insn-0055b114) · [`0055b118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b10c.md#insn-0055b118)

~~~diff
- 00538284 ["INT_ADD", "register:40f0:8", ["const:538284:8", "const:4:8"]]
- 00538284 ["CALL", null, ["ram:418c38:8"]]
+ 0055b11c ["INT_ADD", "register:40f0:8", ["const:55b11c:8", "const:4:8"]]
+ 0055b11c ["CALL", null, ["ram:43b738:8"]]
- 00538284 bytes 6d82fb97
+ 0055b11c bytes 8781fb97
- 0053827c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0055b114 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0053827c bytes 60ebfff0
+ 0055b114 bytes e0eaff90
- 00538280 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00538280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b118 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0055b118 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b118 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b118 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00538280 bytes 00740e91
+ 0055b118 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edd504d02efb93204eb61dba40180cd7"></a>

### [`00538370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md) → [`0055b208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md) FUN_0055b208

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`005323ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323ec.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`0053699c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`00555284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555284.md) [`00555c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555c54.md) [`00555dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00555/00555dcc.md) [`00559834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559834.md) [`00559f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00559/00559f00.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "0055b218",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00538380",
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
      "definition_site": "0055b214",
      "incomplete_value": false,
      "site": "0055b218",
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
      "definition_site": "0053837c",
      "incomplete_value": false,
      "site": "00538380",
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
      "0055b214",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "0055b218",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0055b214",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0055b218",
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

- 旧版 [`00538380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md#insn-00538380) · [`00538378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md#insn-00538378) · [`0053837c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md#insn-0053837c)
- 新版 [`0055b218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md#insn-0055b218) · [`0055b210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md#insn-0055b210) · [`0055b214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b208.md#insn-0055b214)

~~~diff
- 00538380 ["INT_ADD", "register:40f0:8", ["const:538380:8", "const:4:8"]]
- 00538380 ["CALL", null, ["ram:418c38:8"]]
+ 0055b218 ["INT_ADD", "register:40f0:8", ["const:55b218:8", "const:4:8"]]
+ 0055b218 ["CALL", null, ["ram:43b738:8"]]
- 00538380 bytes 2e82fb97
+ 0055b218 bytes 4881fb97
- 00538378 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0055b210 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00538378 bytes 60ebfff0
+ 0055b210 bytes e0eaff90
- 0053837c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0053837c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0055b214 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 0055b214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0055b214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053837c bytes 00740e91
+ 0055b214 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ac3498b50ec0dad39b5edebddf2f821"></a>

### [`00539488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md) → [`0055c320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md) FUN_0055c320

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004665d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004665d0.md) [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 2件 [`00538384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538384.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00489468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489468.md) [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0055b21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b21c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c350",
      "incomplete_value": false,
      "site": "0055c35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:a60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005394b8",
      "incomplete_value": false,
      "site": "005394c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055c368",
      "value": [
        "leaf",
        "ram:55b21c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005394d0",
      "value": [
        "leaf",
        "ram:538384:8"
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
      "0055c35c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00538384"
      ]
    ]
  ],
  "added": [
    [
      "0055c35c",
      "DATA",
      [
        "storage",
        "00c6aa60",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0055b21c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005394d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md#insn-005394d0) · [`005394ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md#insn-005394ac) · [`005394b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md#insn-005394b4)
- 新版 [`0055c368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c368) · [`0055c344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c344) · [`0055c34c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c320.md#insn-0055c34c)

~~~diff
- 005394d0 ["INT_ADD", "register:40f0:8", ["const:5394d0:8", "const:4:8"]]
- 005394d0 ["CALL", null, ["ram:538384:8"]]
+ 0055c368 ["INT_ADD", "register:40f0:8", ["const:55c368:8", "const:4:8"]]
+ 0055c368 ["CALL", null, ["ram:55b21c:8"]]
- 005394d0 bytes adfbff97
+ 0055c368 bytes adfbff97
- 005394ac ["INT_ADD", "register:40f0:8", ["const:5394ac:8", "const:4:8"]]
- 005394ac ["CALL", null, ["callee:00c57a90:8"]]
+ 0055c344 ["INT_ADD", "register:40f0:8", ["const:55c344:8", "const:4:8"]]
+ 0055c344 ["CALL", null, ["callee:00c57a90:8"]]
- 005394ac bytes e5861a94
+ 0055c344 bytes d3ed1b94
- 005394b4 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c34c ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 005394b4 bytes a8350090
+ 0055c34c bytes 683800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-607b6adaabb79601f876773233ba200d"></a>

### [`0053950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md) → [`0055c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md) FUN_0055c3a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c3b8",
      "incomplete_value": false,
      "site": "0055c3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539520",
      "incomplete_value": false,
      "site": "0053952c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c3d0",
      "incomplete_value": false,
      "site": "0055c3d0",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539538",
      "incomplete_value": false,
      "site": "00539538",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c3c4",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c3d0",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c3c4",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c3d0",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053951c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md#insn-0053951c) · [`00539520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md#insn-00539520) · [`00539528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md#insn-00539528)
- 新版 [`0055c3b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md#insn-0055c3b4) · [`0055c3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md#insn-0055c3b8)

~~~diff
- 0053951c ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c3b4 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053951c bytes a8350090
+ 0055c3b4 bytes 683800d0
- 00539520 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00539520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c3b8 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0055c3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539520 bytes 08213691
+ 0055c3b8 bytes 08212591
- 00539528 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00539528 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73e7a5659a680a916300f9f2ba5da57d"></a>

### [`005395ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md) → [`0055c444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md) FUN_0055c444

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c458",
      "incomplete_value": false,
      "site": "0055c464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005395c0",
      "incomplete_value": false,
      "site": "005395cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c470",
      "incomplete_value": false,
      "site": "0055c470",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005395d8",
      "incomplete_value": false,
      "site": "005395d8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c464",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c470",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c464",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c470",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005395bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md#insn-005395bc) · [`005395c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md#insn-005395c0) · [`005395c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md#insn-005395c8)
- 新版 [`0055c454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md#insn-0055c454) · [`0055c458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md#insn-0055c458)

~~~diff
- 005395bc ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c454 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 005395bc bytes a8350090
+ 0055c454 bytes 683800d0
- 005395c0 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 005395c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c458 ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0055c458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005395c0 bytes 08213691
+ 0055c458 bytes 08212591
- 005395c8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005395c8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6a0b2bc7a0f5e98dc87645cb485dbb2"></a>

### [`00539654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md) → [`0055c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md) FUN_0055c4ec

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c50c",
      "incomplete_value": false,
      "site": "0055c50c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
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
      "definition_site": "0055c50c",
      "incomplete_value": false,
      "site": "0055c50c",
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
                "const:c6a000:8"
              ],
              [
                "leaf",
                "const:948:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0055c50c",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c50c",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c50c",
      "DATA",
      [
        "storage",
        "00c6a948",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c50c",
      "DATA",
      [
        "storage",
        "00c6a9b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md#insn-00539660) · [`00539664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md#insn-00539664) · [`00539684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md#insn-00539684)
- 新版 [`0055c4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c4f8) · [`0055c4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c4fc) · [`0055c51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md#insn-0055c51c)

~~~diff
- 00539660 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c4f8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00539660 bytes a8350090
+ 0055c4f8 bytes 683800d0
- 00539664 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00539664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c4fc ["COPY", "tmp:0:8", ["const:948:8"]]
+ 0055c4fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c4fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c4fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539664 bytes 08213691
+ 0055c4fc bytes 08212591
- 00539684 ["INT_ADD", "register:40f0:8", ["const:539684:8", "const:4:8"]]
- 00539684 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055c51c ["INT_ADD", "register:40f0:8", ["const:55c51c:8", "const:4:8"]]
+ 0055c51c ["CALL", null, ["callee:00c538e0:8"]]
- 00539684 bytes 03761a94
+ 0055c51c bytes f1dc1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-743bbaca5415b637c1bcb5b084c0eb2e"></a>

### [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) → [`0055c6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md) FUN_0055c6a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) [`005385e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005385e0.md) [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 2件 [`005399b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`00551234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551234.md) [`0055b478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055b/0055b478.md) [`00a992ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a99/00a992ac.md) · 呼出先 2件 [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c6d0",
      "incomplete_value": false,
      "site": "0055c6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539838",
      "incomplete_value": false,
      "site": "00539840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c6e4",
      "incomplete_value": false,
      "site": "0055c6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053984c",
      "incomplete_value": false,
      "site": "0053984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "0055c6d8",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c6e4",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c6d8",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055c6e4",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md#insn-00539830) · [`00539834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md#insn-00539834) · [`00539838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md#insn-00539838)
- 新版 [`0055c6c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6c8) · [`0055c6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6cc) · [`0055c6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c6a4.md#insn-0055c6d0)

~~~diff
- 00539830 ["INT_ADD", "register:40f0:8", ["const:539830:8", "const:4:8"]]
- 00539830 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055c6c8 ["INT_ADD", "register:40f0:8", ["const:55c6c8:8", "const:4:8"]]
+ 0055c6c8 ["CALL", null, ["callee:00c57a90:8"]]
- 00539830 bytes 04861a94
+ 0055c6c8 bytes f2ec1b94
- 00539834 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c6cc ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00539834 bytes a8350090
+ 0055c6cc bytes 683800d0
- 00539838 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00539838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c6d0 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 0055c6d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c6d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c6d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539838 bytes 08013d91
+ 0055c6d0 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2003d0868c8c072f72fa2b77e9de7d8f"></a>

### [`0053994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053994c.md) → [`0055c7e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e4.md) FUN_0055c7e4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0055c7f0",
      "incomplete_value": false,
      "site": "0055c7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539958",
      "incomplete_value": false,
      "site": "0053995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "0055c7f4",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c7f4",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053994c.md#insn-00539954) · [`00539958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053994c.md#insn-00539958)
- 新版 [`0055c7ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e4.md#insn-0055c7ec) · [`0055c7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c7e4.md#insn-0055c7f0)

~~~diff
- 00539954 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 0055c7ec ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 00539954 bytes a9350090
+ 0055c7ec bytes 693800d0
- 00539958 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00539958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c7f0 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0055c7f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c7f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c7f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539958 bytes 29c13b91
+ 0055c7f0 bytes 29c12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1acb4d3c0f77c06ccc0cb1748cdd7a5a"></a>

### [`00539970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539970.md) → [`0055c808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md) FUN_0055c808

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0055c810",
      "incomplete_value": false,
      "site": "0055c814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539978",
      "incomplete_value": false,
      "site": "0053997c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "0055c814",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055c814",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539970.md#insn-00539974) · [`00539978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539970.md#insn-00539978) · [`0053999c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539970.md#insn-0053999c)
- 新版 [`0055c80c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md#insn-0055c80c) · [`0055c810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md#insn-0055c810) · [`0055c834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c808.md#insn-0055c834)

~~~diff
- 00539974 ["COPY", "register:4048:8", ["const:bed000:8"]]
+ 0055c80c ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 00539974 bytes a9350090
+ 0055c80c bytes 693800d0
- 00539978 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00539978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0055c810 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0055c810 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c810 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0055c810 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539978 bytes 29c13b91
+ 0055c810 bytes 29c12a91
- 0053999c ["INT_ADD", "register:40f0:8", ["const:53999c:8", "const:4:8"]]
- 0053999c ["CALL", null, ["callee:00c57ab0:8"]]
+ 0055c834 ["INT_ADD", "register:40f0:8", ["const:55c834:8", "const:4:8"]]
+ 0055c834 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053999c bytes b1851a94
+ 0055c834 bytes 9fec1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2441033670e45180f02f89c4dd072fc1"></a>

### [`00539b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md) → [`0055c9c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md) FUN_0055c9c4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) · 呼出先 3件 [`005399b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`0055c784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c784.md) · 呼出先 3件 [`0055c848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c848.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055c9f4",
      "incomplete_value": false,
      "site": "0055ca00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b5c",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055ca14",
      "incomplete_value": false,
      "site": "0055ca14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b7c",
      "incomplete_value": false,
      "site": "00539b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "0055ca00",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ca14",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055ca00",
      "DATA",
      [
        "storage",
        "00c6ab00",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ca14",
      "DATA",
      [
        "storage",
        "00c6aab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md#insn-00539b54) · [`00539b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md#insn-00539b58) · [`00539b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md#insn-00539b5c)
- 新版 [`0055c9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055c9ec) · [`0055c9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055c9f0) · [`0055c9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c9c4.md#insn-0055c9f4)

~~~diff
- 00539b54 ["INT_ADD", "register:40f0:8", ["const:539b54:8", "const:4:8"]]
- 00539b54 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055c9ec ["INT_ADD", "register:40f0:8", ["const:55c9ec:8", "const:4:8"]]
+ 0055c9ec ["CALL", null, ["callee:00c57a90:8"]]
- 00539b54 bytes 3b851a94
+ 0055c9ec bytes 29ec1b94
- 00539b58 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055c9f0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00539b58 bytes a8350090
+ 0055c9f0 bytes 683800d0
- 00539b5c ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00539b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055c9f4 ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 0055c9f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055c9f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539b5c bytes 08013d91
+ 0055c9f4 bytes 08012c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a06d07c662fc654d16ab7c1902fd33cb"></a>

### [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) → [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) FUN_0055caa0

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053a518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md) · 呼出先 11件 [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0053a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`0055d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md) · 呼出先 11件 [`0046c40c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c40c.md) [`00535b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00535/00535b2c.md) [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.80% / 新版 95.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055cad0",
      "incomplete_value": false,
      "site": "0055cadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c38",
      "incomplete_value": false,
      "site": "00539c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "definition_site": "0055cb24",
      "incomplete_value": false,
      "site": "0055cb30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c8c",
      "incomplete_value": false,
      "site": "00539c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055cc94",
      "value": [
        "leaf",
        "ram:c57aa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00539dfc",
      "value": [
        "leaf",
        "ram:bdb050:8"
      ]
    },
    "ordinal": 13,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055cadc",
      "DATA",
      [
        "storage",
        "00bedf90",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cb30",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb050"
      ]
    ]
  ],
  "added": [
    [
      "0055cadc",
      "DATA",
      [
        "storage",
        "00c6ab50",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cb30",
      "DATA",
      [
        "storage",
        "00c6ab90",
        null,
        "undefined *"
      ]
    ],
    [
      "0055cc94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57aa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md#insn-00539dfc) · [`00539c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md#insn-00539c34) · [`00539c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md#insn-00539c38)
- 新版 [`0055cc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cc94) · [`0055cacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cacc) · [`0055cad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md#insn-0055cad0)

~~~diff
- 00539dfc ["INT_ADD", "register:40f0:8", ["const:539dfc:8", "const:4:8"]]
- 00539dfc ["CALL", null, ["ram:bdb050:8"]]
+ 0055cc94 ["INT_ADD", "register:40f0:8", ["const:55cc94:8", "const:4:8"]]
+ 0055cc94 ["CALL", null, ["ram:c57aa0:8"]]
- 00539dfc bytes 95841a94
+ 0055cc94 bytes 83eb1b94
- 00539c34 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055cacc ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 00539c34 bytes a8350090
+ 0055cacc bytes 683800d0
- 00539c38 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00539c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055cad0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 0055cad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055cad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055cad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539c38 bytes 08413e91
+ 0055cad0 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c362b01b21501eee138c910463c65673"></a>

### [`0053a518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md) → [`0055d3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md) FUN_0055d3b0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00444d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444d18.md) · 呼出先 2件 [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00467bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467bb0.md) · 呼出先 2件 [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d3e4",
      "incomplete_value": false,
      "site": "0055d3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a54c",
      "incomplete_value": false,
      "site": "0053a558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "0055d3f0",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d3f0",
      "DATA",
      [
        "storage",
        "00c6ac20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md#insn-0053a540) · [`0053a548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md#insn-0053a548) · [`0053a54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md#insn-0053a54c)
- 新版 [`0055d3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3d8) · [`0055d3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3e0) · [`0055d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d3b0.md#insn-0055d3e4)

~~~diff
- 0053a540 ["INT_ADD", "register:40f0:8", ["const:53a540:8", "const:4:8"]]
- 0053a540 ["CALL", null, ["callee:00c57a90:8"]]
+ 0055d3d8 ["INT_ADD", "register:40f0:8", ["const:55d3d8:8", "const:4:8"]]
+ 0055d3d8 ["CALL", null, ["callee:00c57a90:8"]]
- 0053a540 bytes c0821a94
+ 0055d3d8 bytes aee91b94
- 0053a548 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0055d3e0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053a548 bytes a8350090
+ 0055d3e0 bytes 683800b0
- 0053a54c ["COPY", "tmp:0:8", ["const:60:8"]]
- 0053a54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d3e4 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 0055d3e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d3e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d3e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a54c bytes 08810191
+ 0055d3e4 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52d247a85077e15d61f756bb197e8b20"></a>

### [`0053a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md) → [`0055d488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md) FUN_0055d488

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) · 呼出先 1件 [`0053b028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md)
- 新版 呼出元 1件 [`0055caa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055caa0.md) · 呼出先 1件 [`0055dec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055dec0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0055d4a4",
      "incomplete_value": true,
      "site": "0055d4a8",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a60c",
      "incomplete_value": true,
      "site": "0053a610",
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
            "const:20:8"
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
      "0055d4a8",
      "DATA",
      [
        "storage",
        "00bee020",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055d4a8",
      "DATA",
      [
        "storage",
        "00c6abe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md#insn-0053a608) · [`0053a60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md#insn-0053a60c) · [`0053a660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md#insn-0053a660)
- 新版 [`0055d4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md#insn-0055d4a0) · [`0055d4a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md#insn-0055d4a4) · [`0055d4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d488.md#insn-0055d4f8)

~~~diff
- 0053a608 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0055d4a0 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053a608 bytes a8350090
+ 0055d4a0 bytes 683800b0
- 0053a60c ["COPY", "tmp:0:8", ["const:20:8"]]
- 0053a60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055d4a4 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0055d4a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d4a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055d4a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a60c bytes 08810091
+ 0055d4a4 bytes 08812f91
- 0053a660 ["INT_ADD", "register:40f0:8", ["const:53a660:8", "const:4:8"]]
- 0053a660 ["CALL", null, ["callee:0055dec0:8"]]
+ 0055d4f8 ["INT_ADD", "register:40f0:8", ["const:55d4f8:8", "const:4:8"]]
+ 0055d4f8 ["CALL", null, ["callee:0055dec0:8"]]
- 0053a660 bytes 72020094
+ 0055d4f8 bytes 72020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa5b935c1446e5595fd2a9e484bfe48"></a>

### [`0053a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md) → [`0055d5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md) FUN_0055d5a8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0053ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md) [`0053b81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md) [`0056cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md) [`0056cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cec4.md) [`0056d050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d050.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) [`0058fee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fee8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055d684",
      "value": [
        "leaf",
        "ram:58fd5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a7ec",
      "value": [
        "leaf",
        "ram:56cec4:8"
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
      "site": "0055d690",
      "value": [
        "leaf",
        "ram:58fee8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a7f8",
      "value": [
        "leaf",
        "ram:56d050:8"
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
      "site": "0055d6cc",
      "value": [
        "leaf",
        "ram:5901b0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a834",
      "value": [
        "leaf",
        "ram:56d318:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055d684",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056cec4"
      ]
    ],
    [
      "0055d690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056d050"
      ]
    ],
    [
      "0055d6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056d318"
      ]
    ]
  ],
  "added": [
    [
      "0055d684",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fd5c"
      ]
    ],
    [
      "0055d690",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fee8"
      ]
    ],
    [
      "0055d6cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005901b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md#insn-0053a7ec) · [`0053a7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md#insn-0053a7f8) · [`0053a834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a710.md#insn-0053a834)
- 新版 [`0055d684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d684) · [`0055d690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d690) · [`0055d6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d5a8.md#insn-0055d6cc)

~~~diff
- 0053a7ec ["INT_ADD", "register:40f0:8", ["const:53a7ec:8", "const:4:8"]]
- 0053a7ec ["CALL", null, ["ram:56cec4:8"]]
+ 0055d684 ["INT_ADD", "register:40f0:8", ["const:55d684:8", "const:4:8"]]
+ 0055d684 ["CALL", null, ["ram:58fd5c:8"]]
- 0053a7ec bytes b6c90094
+ 0055d684 bytes b6c90094
- 0053a7f8 ["INT_ADD", "register:40f0:8", ["const:53a7f8:8", "const:4:8"]]
- 0053a7f8 ["CALL", null, ["ram:56d050:8"]]
+ 0055d690 ["INT_ADD", "register:40f0:8", ["const:55d690:8", "const:4:8"]]
+ 0055d690 ["CALL", null, ["ram:58fee8:8"]]
- 0053a7f8 bytes 16ca0094
+ 0055d690 bytes 16ca0094
- 0053a834 ["INT_ADD", "register:40f0:8", ["const:53a834:8", "const:4:8"]]
- 0053a834 ["CALL", null, ["ram:56d318:8"]]
+ 0055d6cc ["INT_ADD", "register:40f0:8", ["const:55d6cc:8", "const:4:8"]]
+ 0055d6cc ["CALL", null, ["ram:5901b0:8"]]
- 0053a834 bytes b9ca0094
+ 0055d6cc bytes b9ca0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908885115acc5b1c4413dfe391a91374"></a>

### [`0053a8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md) → [`0055d780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md) FUN_0055d780

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0053ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md) [`0053b81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md) [`0056cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md) [`0056cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cec4.md) [`0056cf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cf88.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md) [`0058fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fe20.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055d834",
      "value": [
        "leaf",
        "ram:58fd5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a99c",
      "value": [
        "leaf",
        "ram:56cec4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055d840",
      "value": [
        "leaf",
        "ram:58fee8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a9a8",
      "value": [
        "leaf",
        "ram:56d050:8"
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
      "site": "0055d848",
      "value": [
        "leaf",
        "ram:58fe20:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053a9b0",
      "value": [
        "leaf",
        "ram:56cf88:8"
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
      "0055d834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056cec4"
      ]
    ],
    [
      "0055d840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056d050"
      ]
    ],
    [
      "0055d848",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056cf88"
      ]
    ]
  ],
  "added": [
    [
      "0055d834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fd5c"
      ]
    ],
    [
      "0055d840",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fee8"
      ]
    ],
    [
      "0055d848",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fe20"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md#insn-0053a99c) · [`0053a9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md#insn-0053a9a8) · [`0053a9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a8e8.md#insn-0053a9b0)
- 新版 [`0055d834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d834) · [`0055d840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d840) · [`0055d848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d780.md#insn-0055d848)

~~~diff
- 0053a99c ["INT_ADD", "register:40f0:8", ["const:53a99c:8", "const:4:8"]]
- 0053a99c ["CALL", null, ["ram:56cec4:8"]]
+ 0055d834 ["INT_ADD", "register:40f0:8", ["const:55d834:8", "const:4:8"]]
+ 0055d834 ["CALL", null, ["ram:58fd5c:8"]]
- 0053a99c bytes 4ac90094
+ 0055d834 bytes 4ac90094
- 0053a9a8 ["INT_ADD", "register:40f0:8", ["const:53a9a8:8", "const:4:8"]]
- 0053a9a8 ["CALL", null, ["ram:56d050:8"]]
+ 0055d840 ["INT_ADD", "register:40f0:8", ["const:55d840:8", "const:4:8"]]
+ 0055d840 ["CALL", null, ["ram:58fee8:8"]]
- 0053a9a8 bytes aac90094
+ 0055d840 bytes aac90094
- 0053a9b0 ["INT_ADD", "register:40f0:8", ["const:53a9b0:8", "const:4:8"]]
- 0053a9b0 ["CALL", null, ["ram:56cf88:8"]]
+ 0055d848 ["INT_ADD", "register:40f0:8", ["const:55d848:8", "const:4:8"]]
+ 0055d848 ["CALL", null, ["ram:58fe20:8"]]
- 0053a9b0 bytes 76c90094
+ 0055d848 bytes 76c90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c446d667738f70475bf8b09f33beaf60"></a>

### [`0053aac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md) → [`0055d95c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md) FUN_0055d95c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0053ac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053ac84.md) [`0053b81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b81c.md) [`0056cd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cd68.md) [`0056cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cdfc.md) [`0056cec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056cec4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0055db1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055db1c.md) [`0055e6b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e6b4.md) [`0058fc00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc00.md) [`0058fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fc94.md) [`0058fd5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058fd5c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055d9dc",
      "value": [
        "leaf",
        "ram:58fd5c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053ab44",
      "value": [
        "leaf",
        "ram:56cec4:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055d9e4",
      "value": [
        "leaf",
        "ram:58fc00:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053ab4c",
      "value": [
        "leaf",
        "ram:56cd68:8"
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
      "site": "0055da1c",
      "value": [
        "leaf",
        "ram:5901b0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053ab84",
      "value": [
        "leaf",
        "ram:56d318:8"
      ]
    },
    "ordinal": 4,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0055d9dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056cec4"
      ]
    ],
    [
      "0055d9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056cd68"
      ]
    ],
    [
      "0055da1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0056d318"
      ]
    ]
  ],
  "added": [
    [
      "0055d9dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fd5c"
      ]
    ],
    [
      "0055d9e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058fc00"
      ]
    ],
    [
      "0055da1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005901b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ab44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md#insn-0053ab44) · [`0053ab4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md#insn-0053ab4c) · [`0053ab84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053aac4.md#insn-0053ab84)
- 新版 [`0055d9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055d9dc) · [`0055d9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055d9e4) · [`0055da1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055d/0055d95c.md#insn-0055da1c)

~~~diff
- 0053ab44 ["INT_ADD", "register:40f0:8", ["const:53ab44:8", "const:4:8"]]
- 0053ab44 ["CALL", null, ["ram:56cec4:8"]]
+ 0055d9dc ["INT_ADD", "register:40f0:8", ["const:55d9dc:8", "const:4:8"]]
+ 0055d9dc ["CALL", null, ["ram:58fd5c:8"]]
- 0053ab44 bytes e0c80094
+ 0055d9dc bytes e0c80094
- 0053ab4c ["INT_ADD", "register:40f0:8", ["const:53ab4c:8", "const:4:8"]]
- 0053ab4c ["CALL", null, ["ram:56cd68:8"]]
+ 0055d9e4 ["INT_ADD", "register:40f0:8", ["const:55d9e4:8", "const:4:8"]]
+ 0055d9e4 ["CALL", null, ["ram:58fc00:8"]]
- 0053ab4c bytes 87c80094
+ 0055d9e4 bytes 87c80094
- 0053ab84 ["INT_ADD", "register:40f0:8", ["const:53ab84:8", "const:4:8"]]
- 0053ab84 ["CALL", null, ["ram:56d318:8"]]
+ 0055da1c ["INT_ADD", "register:40f0:8", ["const:55da1c:8", "const:4:8"]]
+ 0055da1c ["CALL", null, ["ram:5901b0:8"]]
- 0053ab84 bytes e5c90094
+ 0055da1c bytes e5c90094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04dc17a1285b4f76e8df4f20f288ae22"></a>

### [`0053b5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5e4.md) → [`0055e47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md) FUN_0055e47c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "0055e494",
      "incomplete_value": false,
      "site": "0055e498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5fc",
      "incomplete_value": false,
      "site": "0053b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "0055e498",
      "DATA",
      [
        "storage",
        "00bedf90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e498",
      "DATA",
      [
        "storage",
        "00c6ab50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5e4.md#insn-0053b5f8) · [`0053b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5e4.md#insn-0053b5fc) · [`0053b610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5e4.md#insn-0053b610)
- 新版 [`0055e490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e490) · [`0055e494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e494) · [`0055e4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e47c.md#insn-0055e4a8)

~~~diff
- 0053b5f8 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0055e490 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053b5f8 bytes 883500d0
+ 0055e490 bytes 68380090
- 0053b5fc ["COPY", "tmp:0:8", ["const:f90:8"]]
- 0053b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e494 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 0055e494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc bytes 08413e91
+ 0055e494 bytes 08412d91
- 0053b610 ["INT_ADD", "register:40f0:8", ["const:53b610:8", "const:4:8"]]
- 0053b610 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055e4a8 ["INT_ADD", "register:40f0:8", ["const:55e4a8:8", "const:4:8"]]
+ 0055e4a8 ["CALL", null, ["callee:00c538e0:8"]]
- 0053b610 bytes 206e1a94
+ 0055e4a8 bytes 0ed51b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6347346d9f5abff91acf74e970a1561b"></a>

### [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) → [`0055e56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md) FUN_0055e56c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0052f034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md) [`0052f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md) [`0053950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md) [`005395ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md) [`00539654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 6件 [`00551ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551ecc.md) [`00551f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00551/00551f3c.md) [`0055c3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c3a4.md) [`0055c444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c444.md) [`0055c4ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055c/0055c4ec.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

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
      "definition_site": "0055e580",
      "incomplete_value": false,
      "site": "0055e584",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b6e8",
      "incomplete_value": false,
      "site": "0053b6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b0:8"
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
      "0055e584",
      "DATA",
      [
        "storage",
        "00bee0b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055e584",
      "DATA",
      [
        "storage",
        "00c6ac70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md#insn-0053b6e4) · [`0053b6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md#insn-0053b6e8) · [`0053b6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md#insn-0053b6fc)
- 新版 [`0055e57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e57c) · [`0055e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e580) · [`0055e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055e56c.md#insn-0055e594)

~~~diff
- 0053b6e4 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0055e57c ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053b6e4 bytes 883500f0
+ 0055e57c bytes 68380090
- 0053b6e8 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 0053b6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055e580 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 0055e580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055e580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 bytes 08c10291
+ 0055e580 bytes 08c13191
- 0053b6fc ["INT_ADD", "register:40f0:8", ["const:53b6fc:8", "const:4:8"]]
- 0053b6fc ["CALL", null, ["callee:00c538e0:8"]]
+ 0055e594 ["INT_ADD", "register:40f0:8", ["const:55e594:8", "const:4:8"]]
+ 0055e594 ["CALL", null, ["callee:00c538e0:8"]]
- 0053b6fc bytes e56d1a94
+ 0055e594 bytes d3d41b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c126e6283bc3570aa572d8126a52c7e5"></a>

### [`0053be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md) → [`0055ecc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md) FUN_0055ecc8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046a54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a54c.md) · 呼出先 7件 [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) [`00574740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574740.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0048d3e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048d3e4.md) · 呼出先 7件 [`00581454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00581/00581454.md) [`005975d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d8.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055eebc",
      "incomplete_value": false,
      "site": "0055eec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c024",
      "incomplete_value": false,
      "site": "0053c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "definition_site": "0055eee8",
      "incomplete_value": false,
      "site": "0055eee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c050",
      "incomplete_value": false,
      "site": "0053c050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "definition_site": "0055ef04",
      "incomplete_value": false,
      "site": "0055ef04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c06c",
      "incomplete_value": false,
      "site": "0053c06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "0055eec4",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ],
    [
      "0055eee8",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef04",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055eec4",
      "DATA",
      [
        "storage",
        "00c6ad48",
        null,
        "undefined *"
      ]
    ],
    [
      "0055eee8",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0055ef04",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053be7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md#insn-0053be7c) · [`0053be94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md#insn-0053be94) · [`0053beb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md#insn-0053beb0)
- 新版 [`0055ed14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed14) · [`0055ed2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed2c) · [`0055ed48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055e/0055ecc8.md#insn-0055ed48)

~~~diff
- 0053be7c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053be7c ["INT_ADD", "register:40f0:8", ["const:53be7c:8", "const:4:8"]]
- 0053be7c ["CALLIND", null, ["register:0:8"]]
+ 0055ed14 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0055ed14 ["INT_ADD", "register:40f0:8", ["const:55ed14:8", "const:4:8"]]
+ 0055ed14 ["CALLIND", null, ["register:0:8"]]
- 0053be7c bytes 00013fd6
+ 0055ed14 bytes 00013fd6
- 0053be94 ["INT_ADD", "register:40f0:8", ["const:53be94:8", "const:4:8"]]
- 0053be94 ["CALL", null, ["callee:00581454:8"]]
+ 0055ed2c ["INT_ADD", "register:40f0:8", ["const:55ed2c:8", "const:4:8"]]
+ 0055ed2c ["CALL", null, ["callee:00581454:8"]]
- 0053be94 bytes ca890094
+ 0055ed2c bytes ca890094
- 0053beb0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053beb0 ["INT_ADD", "register:40f0:8", ["const:53beb0:8", "const:4:8"]]
- 0053beb0 ["CALLIND", null, ["register:0:8"]]
+ 0055ed48 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0055ed48 ["INT_ADD", "register:40f0:8", ["const:55ed48:8", "const:4:8"]]
+ 0055ed48 ["CALLIND", null, ["register:0:8"]]
- 0053beb0 bytes 20013fd6
+ 0055ed48 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b93b83f9031019361f8dfb0b03116ad4"></a>

### [`0053c470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c470.md) → [`0055f308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md) FUN_0055f308

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f320",
      "incomplete_value": false,
      "site": "0055f324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c488",
      "incomplete_value": false,
      "site": "0053c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "0055f324",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f324",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c470.md#insn-0053c484) · [`0053c488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c470.md#insn-0053c488) · [`0053c49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c470.md#insn-0053c49c)
- 新版 [`0055f31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f31c) · [`0055f320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f320) · [`0055f334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f308.md#insn-0055f334)

~~~diff
- 0053c484 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0055f31c ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053c484 bytes 883500d0
+ 0055f31c bytes 483800f0
- 0053c488 ["COPY", "tmp:0:8", ["const:110:8"]]
- 0053c488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f320 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0055f320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c488 bytes 08410491
+ 0055f320 bytes 08413391
- 0053c49c ["INT_ADD", "register:40f0:8", ["const:53c49c:8", "const:4:8"]]
- 0053c49c ["CALL", null, ["callee:00c538e0:8"]]
+ 0055f334 ["INT_ADD", "register:40f0:8", ["const:55f334:8", "const:4:8"]]
+ 0055f334 ["CALL", null, ["callee:00c538e0:8"]]
- 0053c49c bytes 7d6a1a94
+ 0055f334 bytes 6bd11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d15864b7d4b08f567621d892c35bd992"></a>

### [`0053c50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c50c.md) → [`0055f3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md) FUN_0055f3a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0055f3bc",
      "incomplete_value": false,
      "site": "0055f3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c524",
      "incomplete_value": false,
      "site": "0053c528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
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
      "0055f3c0",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0055f3c0",
      "DATA",
      [
        "storage",
        "00c6acd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c50c.md#insn-0053c520) · [`0053c524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c50c.md#insn-0053c524) · [`0053c538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c50c.md#insn-0053c538)
- 新版 [`0055f3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f3b8) · [`0055f3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f3bc) · [`0055f3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f3a4.md#insn-0055f3d0)

~~~diff
- 0053c520 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0055f3b8 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053c520 bytes 883500d0
+ 0055f3b8 bytes 483800f0
- 0053c524 ["COPY", "tmp:0:8", ["const:110:8"]]
- 0053c524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0055f3bc ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 0055f3bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0055f3bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c524 bytes 08410491
+ 0055f3bc bytes 08413391
- 0053c538 ["INT_ADD", "register:40f0:8", ["const:53c538:8", "const:4:8"]]
- 0053c538 ["CALL", null, ["callee:00c538e0:8"]]
+ 0055f3d0 ["INT_ADD", "register:40f0:8", ["const:55f3d0:8", "const:4:8"]]
+ 0055f3d0 ["CALL", null, ["callee:00c538e0:8"]]
- 0053c538 bytes 566a1a94
+ 0055f3d0 bytes 44d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dad474e83fe289796ff9cd80c0f9d5b1"></a>

### [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) → [`0055f484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md) FUN_0055f484

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 18件 [`0045d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`0045d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md) [`0045d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md) [`0045d7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 18件 [`0048031c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048031c.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00480444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480444.md) [`004805e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004805e8.md) [`0048067c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/0048067c.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0055f4cc",
      "incomplete_value": true,
      "site": "0055f4cc",
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
            "const:874:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c634",
      "incomplete_value": true,
      "site": "0053c634",
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
            "const:db4:8"
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
      "definition_site": "0055f4b0",
      "incomplete_value": false,
      "site": "0055f4b4",
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
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c618",
      "incomplete_value": false,
      "site": "0053c61c",
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
            "const:db8:8"
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
      "definition_site": "0055f4c8",
      "incomplete_value": false,
      "site": "0055f4d0",
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
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c630",
      "incomplete_value": false,
      "site": "0053c638",
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
            "const:db8:8"
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
      "0055f494",
      "READ",
      [
        "storage",
        "00c25db8",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4a0",
      "READ",
      [
        "storage",
        "00c25db4",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4b0",
      "PARAM",
      [
        "storage",
        "00c25db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f494",
      "READ",
      [
        "storage",
        "00ca5878",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4a0",
      "READ",
      [
        "storage",
        "00ca5874",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f4b0",
      "PARAM",
      [
        "storage",
        "00ca5878",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md#insn-0053c61c) · [`0053c634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md#insn-0053c634) · [`0053c638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md#insn-0053c638)
- 新版 [`0055f4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f4b4) · [`0055f4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f4cc) · [`0055f4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f484.md#insn-0055f4d0)

~~~diff
- 0053c61c ["INT_ADD", "register:40f0:8", ["const:53c61c:8", "const:4:8"]]
- 0053c61c ["CALL", null, ["callee:00c57a50:8"]]
+ 0055f4b4 ["INT_ADD", "register:40f0:8", ["const:55f4b4:8", "const:4:8"]]
+ 0055f4b4 ["CALL", null, ["callee:00c57a50:8"]]
- 0053c61c bytes 797a1a94
+ 0055f4b4 bytes 67e11b94
- 0053c634 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0053c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:db4:8"]]
- 0053c634 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0055f4cc ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0055f4cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:874:8"]]
+ 0055f4cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0053c634 bytes 09d13639
+ 0055f4cc bytes 09d12139
- 0053c638 ["INT_ADD", "register:40f0:8", ["const:53c638:8", "const:4:8"]]
- 0053c638 ["CALL", null, ["callee:00c57a70:8"]]
+ 0055f4d0 ["INT_ADD", "register:40f0:8", ["const:55f4d0:8", "const:4:8"]]
+ 0055f4d0 ["CALL", null, ["callee:00c57a70:8"]]
- 0053c638 bytes 7a7a1a94
+ 0055f4d0 bytes 68e11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32980016226d6802fbdb56602b3b2295"></a>

### [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) → [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) FUN_0055f538

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md) [`00a4131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4131c.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 2件 [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) [`00a9f220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9f/00a9f220.md) · 呼出先 5件 [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f57c",
      "incomplete_value": true,
      "site": "0055f580",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c6e4",
      "incomplete_value": true,
      "site": "0053c6e8",
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
            "const:dd0:8"
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
      "definition_site": "0055f598",
      "incomplete_value": false,
      "site": "0055f5ac",
      "value": [
        "leaf",
        "const:560428:8"
      ]
    },
    "old": {
      "definition_site": "0053c700",
      "incomplete_value": false,
      "site": "0053c714",
      "value": [
        "leaf",
        "const:53d590:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f5a0",
      "incomplete_value": false,
      "site": "0055f5ac",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c708",
      "incomplete_value": false,
      "site": "0053c714",
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
            "const:dc0:8"
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
      "0055f550",
      "READ",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f55c",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f57c",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f550",
      "READ",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f55c",
      "READ",
      [
        "storage",
        "00ca5880",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f57c",
      "PARAM",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md#insn-0053c6e8) · [`0053c714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md#insn-0053c714) · [`0053c720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md#insn-0053c720)
- 新版 [`0055f580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f580) · [`0055f5ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f5ac) · [`0055f5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md#insn-0055f5b8)

~~~diff
- 0053c6e8 ["INT_ADD", "register:40f0:8", ["const:53c6e8:8", "const:4:8"]]
- 0053c6e8 ["CALL", null, ["callee:00c57a50:8"]]
+ 0055f580 ["INT_ADD", "register:40f0:8", ["const:55f580:8", "const:4:8"]]
+ 0055f580 ["CALL", null, ["callee:00c57a50:8"]]
- 0053c6e8 bytes 467a1a94
+ 0055f580 bytes 34e11b94
- 0053c714 ["INT_ADD", "register:40f0:8", ["const:53c714:8", "const:4:8"]]
- 0053c714 ["CALL", null, ["callee:00c57a30:8"]]
+ 0055f5ac ["INT_ADD", "register:40f0:8", ["const:55f5ac:8", "const:4:8"]]
+ 0055f5ac ["CALL", null, ["callee:00c57a30:8"]]
- 0053c714 bytes 337a1a94
+ 0055f5ac bytes 21e11b94
- 0053c720 ["INT_ADD", "register:40f0:8", ["const:53c720:8", "const:4:8"]]
- 0053c720 ["CALL", null, ["callee:00c57a70:8"]]
+ 0055f5b8 ["INT_ADD", "register:40f0:8", ["const:55f5b8:8", "const:4:8"]]
+ 0055f5b8 ["CALL", null, ["callee:00c57a70:8"]]
- 0053c720 bytes 407a1a94
+ 0055f5b8 bytes 2ee11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98258dc61bd3a3c51c71d22aae56cac5"></a>

### [`0053c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md) → [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) FUN_0055f5d8

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00a75bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a75/00a75bb4.md) · 呼出先 5件 [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) [`00560428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560428.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f624",
      "incomplete_value": false,
      "site": "0055f628",
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
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c78c",
      "incomplete_value": false,
      "site": "0053c790",
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
            "const:dd0:8"
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
      "definition_site": "0055f640",
      "incomplete_value": false,
      "site": "0055f654",
      "value": [
        "leaf",
        "const:560428:8"
      ]
    },
    "old": {
      "definition_site": "0053c7a8",
      "incomplete_value": false,
      "site": "0053c7bc",
      "value": [
        "leaf",
        "const:53d590:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f648",
      "incomplete_value": false,
      "site": "0055f654",
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
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c7b0",
      "incomplete_value": false,
      "site": "0053c7bc",
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
            "const:dc0:8"
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
      "0055f5f0",
      "READ",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f604",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f624",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0055f5f0",
      "READ",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ],
    [
      "0055f604",
      "READ",
      [
        "storage",
        "00ca5880",
        null,
        "undefined8"
      ]
    ],
    [
      "0055f624",
      "PARAM",
      [
        "storage",
        "00ca5890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md#insn-0053c790) · [`0053c7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md#insn-0053c7bc) · [`0053c7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md#insn-0053c7c8)
- 新版 [`0055f628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f628) · [`0055f654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f654) · [`0055f660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md#insn-0055f660)

~~~diff
- 0053c790 ["INT_ADD", "register:40f0:8", ["const:53c790:8", "const:4:8"]]
- 0053c790 ["CALL", null, ["callee:00c57a50:8"]]
+ 0055f628 ["INT_ADD", "register:40f0:8", ["const:55f628:8", "const:4:8"]]
+ 0055f628 ["CALL", null, ["callee:00c57a50:8"]]
- 0053c790 bytes 1c7a1a94
+ 0055f628 bytes 0ae11b94
- 0053c7bc ["INT_ADD", "register:40f0:8", ["const:53c7bc:8", "const:4:8"]]
- 0053c7bc ["CALL", null, ["callee:00c57a30:8"]]
+ 0055f654 ["INT_ADD", "register:40f0:8", ["const:55f654:8", "const:4:8"]]
+ 0055f654 ["CALL", null, ["callee:00c57a30:8"]]
- 0053c7bc bytes 097a1a94
+ 0055f654 bytes f7e01b94
- 0053c7c8 ["INT_ADD", "register:40f0:8", ["const:53c7c8:8", "const:4:8"]]
- 0053c7c8 ["CALL", null, ["callee:00c57a70:8"]]
+ 0055f660 ["INT_ADD", "register:40f0:8", ["const:55f660:8", "const:4:8"]]
+ 0055f660 ["CALL", null, ["callee:00c57a70:8"]]
- 0053c7c8 bytes 167a1a94
+ 0055f660 bytes 04e11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94441fb9ded4d8b7d76f01b1907df134"></a>

### [`0053c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md) → [`0055f688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md) FUN_0055f688

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0055f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

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
      "definition_site": "0055f730",
      "incomplete_value": true,
      "site": "0055f734",
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
      "definition_site": "0053c898",
      "incomplete_value": true,
      "site": "0053c89c",
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
      "0055f6b8",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0055f6c0",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0055f6d4",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0055f6b8",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "0055f6c0",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "0055f6d4",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md#insn-0053c814) · [`0053c818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md#insn-0053c818) · [`0053c820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md#insn-0053c820)
- 新版 [`0055f6ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f6ac) · [`0055f6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f6b0) · [`0055f6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md#insn-0055f6b8)

~~~diff
- 0053c814 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 0055f6ac ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 0053c814 bytes f93600d0
+ 0055f6ac bytes d93900f0
- 0053c818 ["COPY", "register:40c0:8", ["const:c1a000:8"]]
+ 0055f6b0 ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 0053c818 bytes f83600d0
+ 0055f6b0 bytes d83900f0
- 0053c820 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e98:8"]]
- 0053c820 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0055f6b8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:888:8"]]
+ 0055f6b8 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c820 bytes 394f47f9
+ 0055f6b8 bytes 394744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c343b121c141243802524cb8214849c"></a>

### [`0053c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md) → [`0055f828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md) FUN_0055f828

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md) · 呼出先 6件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)
- 新版 呼出元 1件 [`0055f688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f688.md) · 呼出先 6件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e00.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.56% / 新版 94.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f894",
      "incomplete_value": true,
      "site": "0055f898",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0053c9fc",
      "incomplete_value": true,
      "site": "0053ca00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0055f8b4",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053ca1c",
      "value": [
        "leaf",
        "ram:bdb440:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0055f8f0",
      "incomplete_value": true,
      "site": "0055f8f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0053ca58",
      "incomplete_value": true,
      "site": "0053ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0055f894",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0055f894",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0055f8b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "0055f894",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "0055f894",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0055f8b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md#insn-0053ca00) · [`0053ca1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md#insn-0053ca1c) · [`0053ca5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md#insn-0053ca5c)
- 新版 [`0055f898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f898) · [`0055f8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f8b4) · [`0055f8f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f828.md#insn-0055f8f4)

~~~diff
- 0053ca00 ["INT_ADD", "register:40f0:8", ["const:53ca00:8", "const:4:8"]]
- 0053ca00 ["CALL", null, ["callee:00c57e80:8"]]
+ 0055f898 ["INT_ADD", "register:40f0:8", ["const:55f898:8", "const:4:8"]]
+ 0055f898 ["CALL", null, ["callee:00c57e80:8"]]
- 0053ca00 bytes 8c7a1a94
+ 0055f898 bytes 7ae11b94
- 0053ca1c ["INT_ADD", "register:40f0:8", ["const:53ca1c:8", "const:4:8"]]
- 0053ca1c ["CALL", null, ["ram:bdb440:8"]]
+ 0055f8b4 ["INT_ADD", "register:40f0:8", ["const:55f8b4:8", "const:4:8"]]
+ 0055f8b4 ["CALL", null, ["ram:c57e90:8"]]
- 0053ca1c bytes 897a1a94
+ 0055f8b4 bytes 77e11b94
- 0053ca5c ["INT_ADD", "register:40f0:8", ["const:53ca5c:8", "const:4:8"]]
- 0053ca5c ["CALL", null, ["callee:00c57e80:8"]]
+ 0055f8f4 ["INT_ADD", "register:40f0:8", ["const:55f8f4:8", "const:4:8"]]
+ 0055f8f4 ["CALL", null, ["callee:00c57e80:8"]]
- 0053ca5c bytes 757a1a94
+ 0055f8f4 bytes 63e11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9243ec6de4debe90e7553353e802a180"></a>

### [`0053cda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cda4.md) → [`0055fc3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md) FUN_0055fc3c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "0055fc6c",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053cdd4",
      "value": [
        "leaf",
        "ram:44ac28:8"
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
      "0055fc6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044ac28"
      ]
    ]
  ],
  "added": [
    [
      "0055fc6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053cdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cda4.md#insn-0053cdd4) · [`0053cdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cda4.md#insn-0053cdf8)
- 新版 [`0055fc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md#insn-0055fc6c) · [`0055fc90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc3c.md#insn-0055fc90)

~~~diff
- 0053cdd4 ["INT_ADD", "register:40f0:8", ["const:53cdd4:8", "const:4:8"]]
- 0053cdd4 ["CALL", null, ["ram:44ac28:8"]]
+ 0055fc6c ["INT_ADD", "register:40f0:8", ["const:55fc6c:8", "const:4:8"]]
+ 0055fc6c ["CALL", null, ["ram:46dac0:8"]]
- 0053cdd4 bytes 9537fc97
+ 0055fc6c bytes 9537fc97
- 0053cdf8 ["INT_ADD", "register:40f0:8", ["const:53cdf8:8", "const:4:8"]]
- 0053cdf8 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055fc90 ["INT_ADD", "register:40f0:8", ["const:55fc90:8", "const:4:8"]]
+ 0055fc90 ["CALL", null, ["callee:00c57ae0:8"]]
- 0053cdf8 bytes a6781a94
+ 0055fc90 bytes 94df1b94
~~~


<a id="compare-763f9a9d56927389ab17b5b11c3b3091"></a>

### [`0053cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cdfc.md) → [`0055fc94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md) FUN_0055fc94

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac28.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046dac0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dac0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "0055fcc4",
      "value": [
        "leaf",
        "ram:46dac0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053ce2c",
      "value": [
        "leaf",
        "ram:44ac28:8"
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
      "0055fcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0044ac28"
      ]
    ]
  ],
  "added": [
    [
      "0055fcc4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046dac0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ce2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cdfc.md#insn-0053ce2c) · [`0053ce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053cdfc.md#insn-0053ce50)
- 新版 [`0055fcc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md#insn-0055fcc4) · [`0055fce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055fc94.md#insn-0055fce8)

~~~diff
- 0053ce2c ["INT_ADD", "register:40f0:8", ["const:53ce2c:8", "const:4:8"]]
- 0053ce2c ["CALL", null, ["ram:44ac28:8"]]
+ 0055fcc4 ["INT_ADD", "register:40f0:8", ["const:55fcc4:8", "const:4:8"]]
+ 0055fcc4 ["CALL", null, ["ram:46dac0:8"]]
- 0053ce2c bytes 7f37fc97
+ 0055fcc4 bytes 7f37fc97
- 0053ce50 ["INT_ADD", "register:40f0:8", ["const:53ce50:8", "const:4:8"]]
- 0053ce50 ["CALL", null, ["callee:00c57ae0:8"]]
+ 0055fce8 ["INT_ADD", "register:40f0:8", ["const:55fce8:8", "const:4:8"]]
+ 0055fce8 ["CALL", null, ["callee:00c57ae0:8"]]
- 0053ce50 bytes 90781a94
+ 0055fce8 bytes 7edf1b94
~~~


<a id="compare-0906ad70bb8aa40b620407db17a1d0c3"></a>

### [`0053d168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md) → [`00560000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md) FUN_00560000

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d080.md) [`005748e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748e4.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) [`00bdb5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)
- 新版 呼出元 2件 [`0055ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055ff18.md) [`0059777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059777c.md) · 呼出先 4件 [`00548218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00548/00548218.md) [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) [`00c58030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58030.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560044",
      "incomplete_value": true,
      "site": "00560044",
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
      "definition_site": "0053d1ac",
      "incomplete_value": true,
      "site": "0053d1ac",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056003c",
      "incomplete_value": true,
      "site": "00560048",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0053d1a4",
      "incomplete_value": true,
      "site": "0053d1b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00560054",
      "incomplete_value": true,
      "site": "00560054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0053d1bc",
      "incomplete_value": true,
      "site": "0053d1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00560024",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "00560028",
      "READ",
      [
        "storage",
        "00c1b498",
        null,
        "pointer"
      ]
    ],
    [
      "0056003c",
      "READ",
      [
        "storage",
        "00c134d0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00560024",
      "READ",
      [
        "storage",
        "00c9ae90",
        null,
        "pointer"
      ]
    ],
    [
      "00560028",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "0056003c",
      "READ",
      [
        "storage",
        "00c92e78",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md#insn-0053d180) · [`0053d184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md#insn-0053d184) · [`0053d18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md#insn-0053d18c)
- 新版 [`00560018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-00560018) · [`0056001c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-0056001c) · [`00560024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560000.md#insn-00560024)

~~~diff
- 0053d180 ["COPY", "register:40c8:8", ["const:c1b000:8"]]
+ 00560018 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 0053d180 bytes f93600d0
+ 00560018 bytes d93900d0
- 0053d184 ["COPY", "register:40c0:8", ["const:c1b000:8"]]
+ 0056001c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
- 0053d184 bytes f83600d0
+ 0056001c bytes d83900d0
- 0053d18c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:4a0:8"]]
- 0053d18c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00560024 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e90:8"]]
+ 00560024 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d18c bytes 395342f9
+ 00560024 bytes 394b47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5d6b7a7d41eb3597ef95efdca5ef23"></a>

### [`0053d294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d294.md) → [`0056012c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md) FUN_0056012c

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d080.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`0055ff18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055ff18.md) · 呼出先 6件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.96% / 新版 95.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0056019c",
      "incomplete_value": true,
      "site": "005601a0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d304",
      "incomplete_value": true,
      "site": "0053d308",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e40:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "005601bc",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053d324",
      "value": [
        "leaf",
        "ram:bdb440:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00560254",
      "incomplete_value": true,
      "site": "00560258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0053d3bc",
      "incomplete_value": true,
      "site": "0053d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0056019c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0056019c",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005601bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "0056019c",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "0056019c",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005601bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d294.md#insn-0053d308) · [`0053d324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d294.md#insn-0053d324) · [`0053d3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d294.md#insn-0053d3c0)
- 新版 [`005601a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-005601a0) · [`005601bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-005601bc) · [`00560258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056012c.md#insn-00560258)

~~~diff
- 0053d308 ["INT_ADD", "register:40f0:8", ["const:53d308:8", "const:4:8"]]
- 0053d308 ["CALL", null, ["callee:00c57e80:8"]]
+ 005601a0 ["INT_ADD", "register:40f0:8", ["const:5601a0:8", "const:4:8"]]
+ 005601a0 ["CALL", null, ["callee:00c57e80:8"]]
- 0053d308 bytes 4a781a94
+ 005601a0 bytes 38df1b94
- 0053d324 ["INT_ADD", "register:40f0:8", ["const:53d324:8", "const:4:8"]]
- 0053d324 ["CALL", null, ["ram:bdb440:8"]]
+ 005601bc ["INT_ADD", "register:40f0:8", ["const:5601bc:8", "const:4:8"]]
+ 005601bc ["CALL", null, ["ram:c57e90:8"]]
- 0053d324 bytes 47781a94
+ 005601bc bytes 35df1b94
- 0053d3c0 ["INT_ADD", "register:40f0:8", ["const:53d3c0:8", "const:4:8"]]
- 0053d3c0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00560258 ["INT_ADD", "register:40f0:8", ["const:560258:8", "const:4:8"]]
+ 00560258 ["CALL", null, ["callee:00c57e80:8"]]
- 0053d3c0 bytes 1c781a94
+ 00560258 bytes 0adf1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-666873736e0eef92355853f5b0194893"></a>

### [`0053d46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d46c.md) → [`00560304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md) FUN_00560304

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md) [`00bdc9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bc0.md) [`00c59410`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59410.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560328",
      "incomplete_value": true,
      "site": "00560330",
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
      "definition_site": "0053d490",
      "incomplete_value": true,
      "site": "0053d498",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0056033c",
      "incomplete_value": true,
      "site": "0056033c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0056033c",
      "incomplete_value": true,
      "site": "0056033c",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
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
      "00560320",
      "READ",
      [
        "storage",
        "00c1b498",
        null,
        "pointer"
      ]
    ],
    [
      "00560328",
      "READ",
      [
        "storage",
        "00c134c8",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0056032c",
      "READ",
      [
        "storage",
        "00c134e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "00560320",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "00560328",
      "READ",
      [
        "storage",
        "00c92e70",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0056032c",
      "READ",
      [
        "storage",
        "00c92e88",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d46c.md#insn-0053d47c) · [`0053d480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d46c.md#insn-0053d480) · [`0053d488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d46c.md#insn-0053d488)
- 新版 [`00560314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560314) · [`00560318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560318) · [`00560320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560304.md#insn-00560320)

~~~diff
- 0053d47c ["COPY", "register:40a8:8", ["const:c1b000:8"]]
+ 00560314 ["COPY", "register:40a8:8", ["const:c9a000:8"]]
- 0053d47c bytes f53600d0
+ 00560314 bytes d53900d0
- 0053d480 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00560318 ["COPY", "register:4048:8", ["const:c9a000:8"]]
- 0053d480 bytes e93600b0
+ 00560318 bytes c93900d0
- 0053d488 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:498:8"]]
- 0053d488 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00560320 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e88:8"]]
+ 00560320 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d488 bytes b54e42f9
+ 00560320 bytes b54647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e9753d7ee95506e82e09c0018a85bc7"></a>

### [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) → [`00560380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md) FUN_00560380

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)
- 新版 呼出元 2件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`0055f5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f5d8.md) · 呼出先 2件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00560390",
      "incomplete_value": false,
      "site": "00560398",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4f8",
      "incomplete_value": false,
      "site": "0053d500",
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
            "const:db0:8"
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
      "00560390",
      "PARAM",
      [
        "storage",
        "00c25db0",
        null,
        null
      ]
    ],
    [
      "005603b8",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ],
    [
      "005603c4",
      "DATA",
      [
        "storage",
        "00bee1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560390",
      "PARAM",
      [
        "storage",
        "00ca5870",
        null,
        null
      ]
    ],
    [
      "005603b8",
      "DATA",
      [
        "storage",
        "00c6ae20",
        null,
        "undefined *"
      ]
    ],
    [
      "005603c4",
      "DATA",
      [
        "storage",
        "00c6ad98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md#insn-0053d500) · [`0053d4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md#insn-0053d4f4) · [`0053d4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md#insn-0053d4f8)
- 新版 [`00560398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-00560398) · [`0056038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-0056038c) · [`00560390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560380.md#insn-00560390)

~~~diff
- 0053d500 ["INT_ADD", "register:40f0:8", ["const:53d500:8", "const:4:8"]]
- 0053d500 ["CALL", null, ["callee:00c57fb0:8"]]
+ 00560398 ["INT_ADD", "register:40f0:8", ["const:560398:8", "const:4:8"]]
+ 00560398 ["CALL", null, ["callee:00c57fb0:8"]]
- 0053d500 bytes 18781a94
+ 00560398 bytes 06df1b94
- 0053d4f4 ["COPY", "register:4000:8", ["const:c25000:8"]]
+ 0056038c ["COPY", "register:4000:8", ["const:ca5000:8"]]
- 0053d4f4 bytes 40370090
+ 0056038c bytes 203a00b0
- 0053d4f8 ["COPY", "tmp:0:8", ["const:db0:8"]]
- 0053d4f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00560390 ["COPY", "tmp:0:8", ["const:870:8"]]
+ 00560390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00560390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00560390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 bytes 00c03691
+ 00560390 bytes 00c02191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-41a4c15830adc11d49ed53b3725965d0"></a>

### [`0053d5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d5e0.md) → [`00560478`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560478.md) FUN_00560478

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.87% / 新版 94.87%

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
      "site": "005604e4",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053d64c",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "005604c8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "005604c8",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005604e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "005604c8",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "005604c8",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "005604e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57e90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d5e0.md#insn-0053d64c) · [`0053d624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d5e0.md#insn-0053d624) · [`0053d628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d5e0.md#insn-0053d628)
- 新版 [`005604e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560478.md#insn-005604e4) · [`005604bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560478.md#insn-005604bc) · [`005604c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560478.md#insn-005604c0)

~~~diff
- 0053d64c ["INT_ADD", "register:40f0:8", ["const:53d64c:8", "const:4:8"]]
- 0053d64c ["CALL", null, ["ram:bdb440:8"]]
+ 005604e4 ["INT_ADD", "register:40f0:8", ["const:5604e4:8", "const:4:8"]]
+ 005604e4 ["CALL", null, ["ram:c57e90:8"]]
- 0053d64c bytes 7d771a94
+ 005604e4 bytes 6bde1b94
- 0053d624 ["INT_ADD", "register:40f0:8", ["const:53d624:8", "const:4:8"]]
- 0053d624 ["CALL", null, ["callee:00c57e70:8"]]
+ 005604bc ["INT_ADD", "register:40f0:8", ["const:5604bc:8", "const:4:8"]]
+ 005604bc ["CALL", null, ["callee:00c57e70:8"]]
- 0053d624 bytes 7f771a94
+ 005604bc bytes 6dde1b94
- 0053d628 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 005604c0 ["COPY", "register:4008:8", ["const:c9a000:8"]]
- 0053d628 bytes e13600b0
+ 005604c0 bytes c13900d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-369589a32914b6f75dd84bff460a409d"></a>

### [`0053d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md) → [`0056074c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md) _INIT_26

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b7dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bfa930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa930.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.49% / 新版 80.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560788",
      "incomplete_value": true,
      "site": "00560788",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ddd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d8f0",
      "incomplete_value": true,
      "site": "0053d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0056079c",
      "value": [
        "leaf",
        "ram:c57fa0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053d904",
      "value": [
        "leaf",
        "ram:bdb550:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00560794",
      "incomplete_value": false,
      "site": "0056079c",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d8fc",
      "incomplete_value": false,
      "site": "0053d904",
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
            "const:db0:8"
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
      "0056076c",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "00560794",
      "PARAM",
      [
        "storage",
        "00c25db0",
        null,
        null
      ]
    ],
    [
      "0056079c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb550"
      ]
    ]
  ],
  "added": [
    [
      "0056076c",
      "READ",
      [
        "storage",
        "002b8ddd",
        null,
        "string"
      ]
    ],
    [
      "00560794",
      "PARAM",
      [
        "storage",
        "00ca5870",
        null,
        null
      ]
    ],
    [
      "0056079c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57fa0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md#insn-0053d904) · [`0053d930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md#insn-0053d930) · [`0053d8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md#insn-0053d8c8)
- 新版 [`0056079c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-0056079c) · [`005607c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-005607c8) · [`00560760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056074c.md#insn-00560760)

~~~diff
- 0053d904 ["INT_ADD", "register:40f0:8", ["const:53d904:8", "const:4:8"]]
- 0053d904 ["CALL", null, ["ram:bdb550:8"]]
+ 0056079c ["INT_ADD", "register:40f0:8", ["const:56079c:8", "const:4:8"]]
+ 0056079c ["CALL", null, ["ram:c57fa0:8"]]
- 0053d904 bytes 13771a94
+ 0056079c bytes 01de1b94
- 0053d930 ["INT_ADD", "register:40f0:8", ["const:53d930:8", "const:4:8"]]
- 0053d930 ["CALL", null, ["callee:00c57a30:8"]]
+ 005607c8 ["INT_ADD", "register:40f0:8", ["const:5607c8:8", "const:4:8"]]
+ 005607c8 ["CALL", null, ["callee:00c57a30:8"]]
- 0053d930 bytes ac751a94
+ 005607c8 bytes 9adc1b94
- 0053d8c8 ["COPY", "register:4050:8", ["const:2a8000:8"]]
+ 00560760 ["COPY", "register:4050:8", ["const:2b8000:8"]]
- 0053d8c8 bytes 4aebfff0
+ 00560760 bytes caeaff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10435e6ecb2b57b365e418c06683372d"></a>

### [`0053d984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md) → [`0056081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md) FUN_0056081c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) [`008fc35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fc35c.md) [`008fcaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fcaf4.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 12件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) [`009308a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00930/009308a4.md) [`009313c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00931/009313c0.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560838",
      "incomplete_value": false,
      "site": "00560840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9a0",
      "incomplete_value": false,
      "site": "0053d9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560850",
      "incomplete_value": false,
      "site": "00560850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9b8",
      "incomplete_value": false,
      "site": "0053d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "00560840",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ],
    [
      "00560850",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560840",
      "DATA",
      [
        "storage",
        "00c6aed0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560850",
      "DATA",
      [
        "storage",
        "00c6af20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md#insn-0053d998) · [`0053d99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md#insn-0053d99c) · [`0053d9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md#insn-0053d9a0)
- 新版 [`00560830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560830) · [`00560834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560834) · [`00560838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md#insn-00560838)

~~~diff
- 0053d998 ["INT_ADD", "register:40f0:8", ["const:53d998:8", "const:4:8"]]
- 0053d998 ["CALL", null, ["callee:00c57a90:8"]]
+ 00560830 ["INT_ADD", "register:40f0:8", ["const:560830:8", "const:4:8"]]
+ 00560830 ["CALL", null, ["callee:00c57a90:8"]]
- 0053d998 bytes aa751a94
+ 00560830 bytes 98dc1b94
- 0053d99c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00560834 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053d99c bytes 883500b0
+ 00560834 bytes 483800d0
- 0053d9a0 ["COPY", "tmp:0:8", ["const:310:8"]]
- 0053d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560838 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00560838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 bytes 08410c91
+ 00560838 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed8fe3b91ad3297ca7536a367a551184"></a>

### [`0053d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md) → [`00560864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md) FUN_00560864

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0052db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0053df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053df70.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005509d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/005509d4.md) [`00560e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560e08.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005608fc",
      "incomplete_value": false,
      "site": "005608fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053da64",
      "incomplete_value": false,
      "site": "0053da64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "005608fc",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0056097c",
      "READ",
      [
        "storage",
        "00bee3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005608fc",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ],
    [
      "0056097c",
      "READ",
      [
        "storage",
        "00c6af98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d9fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md#insn-0053d9fc) · [`0053da1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md#insn-0053da1c) · [`0053da40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md#insn-0053da40)
- 新版 [`00560894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-00560894) · [`005608b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-005608b4) · [`005608d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560864.md#insn-005608d8)

~~~diff
- 0053d9fc ["INT_ADD", "register:40f0:8", ["const:53d9fc:8", "const:4:8"]]
- 0053d9fc ["CALL", null, ["callee:005509d4:8"]]
+ 00560894 ["INT_ADD", "register:40f0:8", ["const:560894:8", "const:4:8"]]
+ 00560894 ["CALL", null, ["callee:005509d4:8"]]
- 0053d9fc bytes 50c0ff97
+ 00560894 bytes 50c0ff97
- 0053da1c ["COPY", "register:0:8", ["register:4040:8"]]
- 0053da1c ["INT_ADD", "register:40f0:8", ["const:53da1c:8", "const:4:8"]]
- 0053da1c ["CALLIND", null, ["register:0:8"]]
+ 005608b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005608b4 ["INT_ADD", "register:40f0:8", ["const:5608b4:8", "const:4:8"]]
+ 005608b4 ["CALLIND", null, ["register:0:8"]]
- 0053da1c bytes 00013fd6
+ 005608b4 bytes 00013fd6
- 0053da40 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053da40 ["INT_ADD", "register:40f0:8", ["const:53da40:8", "const:4:8"]]
- 0053da40 ["CALLIND", null, ["register:0:8"]]
+ 005608d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005608d8 ["INT_ADD", "register:40f0:8", ["const:5608d8:8", "const:4:8"]]
+ 005608d8 ["CALLIND", null, ["register:0:8"]]
- 0053da40 bytes 00013fd6
+ 005608d8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cccd96d8a1375a5a60c3d23313aee976"></a>

### [`0053dc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc90.md) → [`00560b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md) FUN_00560b28

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00560b40",
      "incomplete_value": false,
      "site": "00560b44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dca8",
      "incomplete_value": false,
      "site": "0053dcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00560b44",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560b44",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc90.md#insn-0053dca4) · [`0053dca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc90.md#insn-0053dca8) · [`0053dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc90.md#insn-0053dcb8)
- 新版 [`00560b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b3c) · [`00560b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b40) · [`00560b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b28.md#insn-00560b50)

~~~diff
- 0053dca4 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 00560b3c ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 0053dca4 bytes 893500b0
+ 00560b3c bytes 493800d0
- 0053dca8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053dca8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560b40 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00560b40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 bytes 29c10a91
+ 00560b40 bytes 29c13991
- 0053dcb8 ["INT_ADD", "register:40f0:8", ["const:53dcb8:8", "const:4:8"]]
- 0053dcb8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00560b50 ["INT_ADD", "register:40f0:8", ["const:560b50:8", "const:4:8"]]
+ 00560b50 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053dcb8 bytes ea741a94
+ 00560b50 bytes d8db1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92b848fe182fa8a8193596fc4deff8b2"></a>

### [`0053dce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dce0.md) → [`00560b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md) FUN_00560b78

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560b90",
      "incomplete_value": false,
      "site": "00560b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dcf8",
      "incomplete_value": false,
      "site": "0053dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00560b94",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560b94",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dce0.md#insn-0053dcf4) · [`0053dcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dce0.md#insn-0053dcf8) · [`0053dd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dce0.md#insn-0053dd08)
- 新版 [`00560b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560b8c) · [`00560b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560b90) · [`00560ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560b78.md#insn-00560ba0)

~~~diff
- 0053dcf4 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 00560b8c ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 0053dcf4 bytes 893500b0
+ 00560b8c bytes 493800d0
- 0053dcf8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 0053dcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560b90 ["COPY", "tmp:0:8", ["const:e70:8"]]
+ 00560b90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560b90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 bytes 29c10a91
+ 00560b90 bytes 29c13991
- 0053dd08 ["INT_ADD", "register:40f0:8", ["const:53dd08:8", "const:4:8"]]
- 0053dd08 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00560ba0 ["INT_ADD", "register:40f0:8", ["const:560ba0:8", "const:4:8"]]
+ 00560ba0 ["CALL", null, ["callee:00c57ab0:8"]]
- 0053dd08 bytes d6741a94
+ 00560ba0 bytes c4db1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c775bf8975ba053a64c0167d53d8dc8"></a>

### [`0053dde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dde0.md) → [`00560c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md) FUN_00560c78

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00560c90",
      "incomplete_value": false,
      "site": "00560c9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ddf8",
      "incomplete_value": false,
      "site": "0053de04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00560c9c",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560c9c",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ddf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dde0.md#insn-0053ddf4) · [`0053ddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dde0.md#insn-0053ddf8) · [`0053de28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dde0.md#insn-0053de28)
- 新版 [`00560c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560c8c) · [`00560c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560c90) · [`00560cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560c78.md#insn-00560cc0)

~~~diff
- 0053ddf4 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00560c8c ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053ddf4 bytes 883500b0
+ 00560c8c bytes 483800d0
- 0053ddf8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 0053ddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560c90 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 00560c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 bytes 08c10e91
+ 00560c90 bytes 08c13d91
- 0053de28 ["COPY", "register:0:8", ["register:4040:8"]]
- 0053de28 ["INT_ADD", "register:40f0:8", ["const:53de28:8", "const:4:8"]]
- 0053de28 ["CALLIND", null, ["register:0:8"]]
+ 00560cc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00560cc0 ["INT_ADD", "register:40f0:8", ["const:560cc0:8", "const:4:8"]]
+ 00560cc0 ["CALLIND", null, ["register:0:8"]]
- 0053de28 bytes 00013fd6
+ 00560cc0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3839d0c14a134f635cc320a536b16158"></a>

### [`0053de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053de3c.md) → [`00560cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md) FUN_00560cd4

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560d00",
      "incomplete_value": false,
      "site": "00560d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053de68",
      "incomplete_value": false,
      "site": "0053de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00560d00",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560d00",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053de3c.md#insn-0053de50) · [`0053de5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053de3c.md#insn-0053de5c) · [`0053de60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053de3c.md#insn-0053de60)
- 新版 [`00560ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560ce8) · [`00560cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560cf4) · [`00560cf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560cd4.md#insn-00560cf8)

~~~diff
- 0053de50 ["INT_ADD", "register:40f0:8", ["const:53de50:8", "const:4:8"]]
- 0053de50 ["CALL", null, ["callee:00c57a90:8"]]
+ 00560ce8 ["INT_ADD", "register:40f0:8", ["const:560ce8:8", "const:4:8"]]
+ 00560ce8 ["CALL", null, ["callee:00c57a90:8"]]
- 0053de50 bytes 7c741a94
+ 00560ce8 bytes 6adb1b94
- 0053de5c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00560cf4 ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053de5c bytes 883500b0
+ 00560cf4 bytes 483800d0
- 0053de60 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 0053de60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560cf8 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 00560cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053de60 bytes 08c10e91
+ 00560cf8 bytes 08c13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24ce9b0e84fa4d71ef60a8eeb6ed8c67"></a>

### [`0053dec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dec4.md) → [`00560d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md) FUN_00560d5c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00560d78",
      "incomplete_value": true,
      "site": "00560d78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dee0",
      "incomplete_value": true,
      "site": "0053dee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4048:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "00560d78",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560d78",
      "DATA",
      [
        "storage",
        "00c6af70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dec4.md#insn-0053ded8) · [`0053dedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dec4.md#insn-0053dedc) · [`0053df00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dec4.md#insn-0053df00)
- 新版 [`00560d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d70) · [`00560d74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d74) · [`00560d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560d5c.md#insn-00560d98)

~~~diff
- 0053ded8 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 00560d70 ["COPY", "register:4048:8", ["const:c6a000:8"]]
- 0053ded8 bytes 893500b0
+ 00560d70 bytes 493800d0
- 0053dedc ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 0053dedc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00560d74 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 00560d74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00560d74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00560d74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dedc bytes 29c10e91
+ 00560d74 bytes 29c13d91
- 0053df00 ["COPY", "register:0:8", ["register:4048:8"]]
- 0053df00 ["INT_ADD", "register:40f0:8", ["const:53df00:8", "const:4:8"]]
- 0053df00 ["CALLIND", null, ["register:0:8"]]
+ 00560d98 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00560d98 ["INT_ADD", "register:40f0:8", ["const:560d98:8", "const:4:8"]]
+ 00560d98 ["CALLIND", null, ["register:0:8"]]
- 0053df00 bytes 20013fd6
+ 00560d98 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1848503c687512488451bb8025496b5d"></a>

### [`0053e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md) → [`00560ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md) FUN_00560ea0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00560ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ac8.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00560eb8",
      "incomplete_value": false,
      "site": "00560eb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e020",
      "incomplete_value": false,
      "site": "0053e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "definition_site": "00560ec4",
      "incomplete_value": false,
      "site": "00560ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e02c",
      "incomplete_value": false,
      "site": "0053e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
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
      "00560eb8",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ],
    [
      "00560ec4",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00560eb8",
      "DATA",
      [
        "storage",
        "00c6aff0",
        null,
        "undefined *"
      ]
    ],
    [
      "00560ec4",
      "DATA",
      [
        "storage",
        "00c6ae70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md#insn-0053e014) · [`0053e018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md#insn-0053e018) · [`0053e024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md#insn-0053e024)
- 新版 [`00560eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md#insn-00560eac) · [`00560eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560ea0.md#insn-00560eb0)

~~~diff
- 0053e014 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00560eac ["COPY", "register:4040:8", ["const:c6a000:8"]]
- 0053e014 bytes 88350090
+ 00560eac bytes 483800d0
- 0053e018 ["COPY", "tmp:0:8", ["const:430:8"]]
- 0053e018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00560eb0 ["COPY", "tmp:0:8", ["const:ff0:8"]]
+ 00560eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00560eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00560eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e018 bytes 08c11091
+ 00560eb0 bytes 08c13f91
- 0053e024 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053e024 bytes 88350090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d81421d40978d6e35383657d5fb08e42"></a>

### [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md) → [`00561074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md) FUN_00561074

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 14件 [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) [`00574738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574738.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 14件 [`0055f538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0055f/0055f538.md) [`005975d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975d0.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.39% / 新版 96.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005610cc",
      "incomplete_value": false,
      "site": "005610d8",
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
            "const:3ec:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e234",
      "incomplete_value": false,
      "site": "0053e240",
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
            "const:8fb:8"
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
      "definition_site": "0056135c",
      "incomplete_value": false,
      "site": "00561364",
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
            "const:d05:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e4c4",
      "incomplete_value": false,
      "site": "0053e4cc",
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
            "const:74b:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005613fc",
      "incomplete_value": false,
      "site": "00561400",
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
            "const:189:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e564",
      "incomplete_value": false,
      "site": "0053e568",
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
            "const:75b:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005610cc",
      "PARAM",
      [
        "storage",
        "002a68fb",
        null,
        "string"
      ]
    ],
    [
      "00561194",
      "PARAM",
      [
        "storage",
        "002aa706",
        null,
        "string"
      ]
    ],
    [
      "005611b0",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005610cc",
      "PARAM",
      [
        "storage",
        "002b73ec",
        null,
        "string"
      ]
    ],
    [
      "00561194",
      "PARAM",
      [
        "storage",
        "002bb482",
        null,
        "string"
      ]
    ],
    [
      "005611b0",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md#insn-0053e240) · [`0053e4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md#insn-0053e4cc) · [`0053e568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md#insn-0053e568)
- 新版 [`005610d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-005610d8) · [`00561364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-00561364) · [`00561400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561074.md#insn-00561400)

~~~diff
- 0053e240 ["INT_ADD", "register:40f0:8", ["const:53e240:8", "const:4:8"]]
- 0053e240 ["CALL", null, ["callee:00c57b60:8"]]
+ 005610d8 ["INT_ADD", "register:40f0:8", ["const:5610d8:8", "const:4:8"]]
+ 005610d8 ["CALL", null, ["callee:00c57b60:8"]]
- 0053e240 bytes b4731a94
+ 005610d8 bytes a2da1b94
- 0053e4cc ["INT_ADD", "register:40f0:8", ["const:53e4cc:8", "const:4:8"]]
- 0053e4cc ["CALL", null, ["callee:00c57cb0:8"]]
+ 00561364 ["INT_ADD", "register:40f0:8", ["const:561364:8", "const:4:8"]]
+ 00561364 ["CALL", null, ["callee:00c57cb0:8"]]
- 0053e4cc bytes 65731a94
+ 00561364 bytes 53da1b94
- 0053e568 ["INT_ADD", "register:40f0:8", ["const:53e568:8", "const:4:8"]]
- 0053e568 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00561400 ["INT_ADD", "register:40f0:8", ["const:561400:8", "const:4:8"]]
+ 00561400 ["CALL", null, ["callee:00c57cb0:8"]]
- 0053e568 bytes 3e731a94
+ 00561400 bytes 2cda1b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43efd319fe50789fc0a88e9b1d90dd1e"></a>

### [`0053e9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md) → [`00561868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md) FUN_00561868

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004567c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004567c8.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00561884",
      "incomplete_value": false,
      "site": "0056188c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e9ec",
      "incomplete_value": false,
      "site": "0053e9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0056188c",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056188c",
      "DATA",
      [
        "storage",
        "00c6b040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md#insn-0053e9e4) · [`0053e9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md#insn-0053e9e8) · [`0053e9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md#insn-0053e9ec)
- 新版 [`0056187c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md#insn-0056187c) · [`00561880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md#insn-00561880) · [`00561884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561868.md#insn-00561884)

~~~diff
- 0053e9e4 ["INT_ADD", "register:40f0:8", ["const:53e9e4:8", "const:4:8"]]
- 0053e9e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0056187c ["INT_ADD", "register:40f0:8", ["const:56187c:8", "const:4:8"]]
+ 0056187c ["CALL", null, ["callee:00c57a90:8"]]
- 0053e9e4 bytes 97711a94
+ 0056187c bytes 85d81b94
- 0053e9e8 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00561880 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0053e9e8 bytes 88350090
+ 00561880 bytes 483800d0
- 0053e9ec ["COPY", "tmp:0:8", ["const:480:8"]]
- 0053e9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561884 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00561884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec bytes 08011291
+ 00561884 bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de1bed388da6f8b0e23a01f177a34997"></a>

### [`0053ea14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ea14.md) → [`005618ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md) FUN_005618ac

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 5件 [`0053d588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d588.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 5件 [`00560420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560420.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00561928",
      "incomplete_value": false,
      "site": "00561930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b4000:8"
          ],
          [
            "leaf",
            "const:ec9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ea90",
      "incomplete_value": false,
      "site": "0053ea98",
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
            "const:65c:8"
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
      "0056190c",
      "PARAM",
      [
        "storage",
        "00298c4e",
        null,
        null
      ]
    ],
    [
      "00561928",
      "PARAM",
      [
        "storage",
        "002a465c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0056190c",
      "PARAM",
      [
        "storage",
        "002a8a0c",
        null,
        null
      ]
    ],
    [
      "00561928",
      "PARAM",
      [
        "storage",
        "002b4ec9",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ea98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ea14.md#insn-0053ea98) · [`0053ea70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ea14.md#insn-0053ea70) · [`0053ea74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ea14.md#insn-0053ea74)
- 新版 [`00561930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-00561930) · [`00561908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-00561908) · [`0056190c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/005618ac.md#insn-0056190c)

~~~diff
- 0053ea98 ["INT_ADD", "register:40f0:8", ["const:53ea98:8", "const:4:8"]]
- 0053ea98 ["CALL", null, ["callee:00c57b70:8"]]
+ 00561930 ["INT_ADD", "register:40f0:8", ["const:561930:8", "const:4:8"]]
+ 00561930 ["CALL", null, ["callee:00c57b70:8"]]
- 0053ea98 bytes a2711a94
+ 00561930 bytes 90d81b94
- 0053ea70 ["COPY", "register:4008:8", ["const:298000:8"]]
+ 00561908 ["COPY", "register:4008:8", ["const:2a8000:8"]]
- 0053ea70 bytes c1eaffd0
+ 00561908 bytes 21eafff0
- 0053ea74 ["COPY", "tmp:0:8", ["const:c4e:8"]]
- 0053ea74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0056190c ["COPY", "tmp:0:8", ["const:a0c:8"]]
+ 0056190c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0056190c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0056190c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 bytes 21383191
+ 0056190c bytes 21302891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f893d965dbfba943b292e50fc91ae740"></a>

### [`0053ec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ec4c.md) → [`00561ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md) FUN_00561ae4

採用 · 移動量 `+0x22e98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md)
- 新版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 4件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d60.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561b30",
      "incomplete_value": true,
      "site": "00561b30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8ce:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ec98",
      "incomplete_value": true,
      "site": "0053ec98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f4:8"
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
      "definition_site": "00561b50",
      "incomplete_value": true,
      "site": "00561b60",
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
      "definition_site": "0053ecb8",
      "incomplete_value": true,
      "site": "0053ecc8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00561b4c",
      "incomplete_value": true,
      "site": "00561b64",
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
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e25:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ecb4",
      "incomplete_value": true,
      "site": "0053eccc",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:aff:8"
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
      "00561b08",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "00561b4c",
      "READ",
      [
        "storage",
        "002adaff",
        null,
        "string"
      ]
    ],
    [
      "00561b4c",
      "READ",
      [
        "storage",
        "002adb0f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00561b08",
      "READ",
      [
        "storage",
        "002b38ce",
        null,
        "string"
      ]
    ],
    [
      "00561b4c",
      "READ",
      [
        "storage",
        "002bee25",
        null,
        "string"
      ]
    ],
    [
      "00561b4c",
      "READ",
      [
        "storage",
        "002bee35",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ec64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ec4c.md#insn-0053ec64) · [`0053ec68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ec4c.md#insn-0053ec68) · [`0053eca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ec4c.md#insn-0053eca4)
- 新版 [`00561afc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561afc) · [`00561b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561b00) · [`00561b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561ae4.md#insn-00561b3c)

~~~diff
- 0053ec64 ["COPY", "register:4050:8", ["const:2a3000:8"]]
+ 00561afc ["COPY", "register:4050:8", ["const:2b3000:8"]]
- 0053ec64 bytes 2aebffb0
+ 00561afc bytes 8aeaffd0
- 0053ec68 ["COPY", "tmp:0:8", ["const:1f4:8"]]
- 0053ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00561b00 ["COPY", "tmp:0:8", ["const:8ce:8"]]
+ 00561b00 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b00 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00561b00 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 bytes 4ad10791
+ 00561b00 bytes 4a392391
- 0053eca4 ["INT_ADD", "register:40f0:8", ["const:53eca4:8", "const:4:8"]]
- 0053eca4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00561b3c ["INT_ADD", "register:40f0:8", ["const:561b3c:8", "const:4:8"]]
+ 00561b3c ["CALL", null, ["callee:00c57a90:8"]]
- 0053eca4 bytes e7701a94
+ 00561b3c bytes d5d71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e036e017f1a1408e9ba623c2509ab39"></a>

### [`0053ee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee14.md) → [`00561cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md) FUN_00561cac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`008d52f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d5/008d52f0.md) [`008d6b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d6/008d6b44.md) · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00561cc8",
      "incomplete_value": false,
      "site": "00561cd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ee30",
      "incomplete_value": false,
      "site": "0053ee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "00561cd0",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561cd0",
      "DATA",
      [
        "storage",
        "00c6b090",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee14.md#insn-0053ee28) · [`0053ee2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee14.md#insn-0053ee2c) · [`0053ee30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee14.md#insn-0053ee30)
- 新版 [`00561cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md#insn-00561cc0) · [`00561cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md#insn-00561cc4) · [`00561cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cac.md#insn-00561cc8)

~~~diff
- 0053ee28 ["INT_ADD", "register:40f0:8", ["const:53ee28:8", "const:4:8"]]
- 0053ee28 ["CALL", null, ["callee:00c57a90:8"]]
+ 00561cc0 ["INT_ADD", "register:40f0:8", ["const:561cc0:8", "const:4:8"]]
+ 00561cc0 ["CALL", null, ["callee:00c57a90:8"]]
- 0053ee28 bytes 86701a94
+ 00561cc0 bytes 74d71b94
- 0053ee2c ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 00561cc4 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0053ee2c bytes 88350090
+ 00561cc4 bytes 483800d0
- 0053ee30 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0053ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00561cc8 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00561cc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00561cc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00561cc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 bytes 08411391
+ 00561cc8 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec4551f21b2de2376a045277e414f226"></a>

### [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) → [`00561cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md) FUN_00561cf4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00540878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540878.md) [`0056244c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md) [`0057476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057476c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 21件 [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`0043e538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e538.md) [`00444de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00444/00444de0.md) [`0044f908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f908.md) [`0044fccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044fccc.md) · 呼出先 7件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00563710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563710.md) [`005852e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00585/005852e4.md) [`00597604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597604.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00561db4",
      "incomplete_value": false,
      "site": "00561db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ef1c",
      "incomplete_value": false,
      "site": "0053ef1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00561d38",
      "incomplete_value": true,
      "site": "00561d38",
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
      "definition_site": "0053eea0",
      "incomplete_value": true,
      "site": "0053eea0",
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
      "00561d34",
      "READ",
      [
        "storage",
        "00c25e00",
        null,
        "undefined8"
      ]
    ],
    [
      "00561db4",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ],
    [
      "00561e40",
      "READ",
      [
        "storage",
        "00bee548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00561d34",
      "READ",
      [
        "storage",
        "00ca58c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00561db4",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00561e40",
      "READ",
      [
        "storage",
        "00c6b108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md#insn-0053ee98) · [`0053ee9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md#insn-0053ee9c) · [`0053eec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md#insn-0053eec8)
- 新版 [`00561d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d30) · [`00561d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d34) · [`00561d60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561cf4.md#insn-00561d60)

~~~diff
- 0053ee98 ["COPY", "register:4048:8", ["const:c25000:8"]]
+ 00561d30 ["COPY", "register:4048:8", ["const:ca5000:8"]]
- 0053ee98 bytes 293700f0
+ 00561d30 bytes 293a0090
- 0053ee9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
- 0053ee9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00561d34 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8c0:8"]]
+ 00561d34 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ee9c bytes 290147f9
+ 00561d34 bytes 296144f9
- 0053eec8 ["INT_ADD", "register:40f0:8", ["const:53eec8:8", "const:4:8"]]
- 0053eec8 ["CALL", null, ["callee:0043bae0:8"]]
+ 00561d60 ["INT_ADD", "register:40f0:8", ["const:561d60:8", "const:4:8"]]
+ 00561d60 ["CALL", null, ["callee:0043bae0:8"]]
- 0053eec8 bytes 4668fb97
+ 00561d60 bytes 6067fb97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddecd022021e21afb00f6d312145149c"></a>

### [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) → [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) FUN_00561f90

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949c4c.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00541908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 3件 [`0043df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043df70.md) [`00458ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00458/00458ab0.md) [`0097f6f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0097f/0097f6f8.md) · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428dc.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`005647a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005623a8",
      "incomplete_value": false,
      "site": "005623b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053f510",
      "incomplete_value": false,
      "site": "0053f51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005623b4",
      "DATA",
      [
        "storage",
        "00bee660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005623b4",
      "DATA",
      [
        "storage",
        "00c6b220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053f164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md#insn-0053f164) · [`0053f174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md#insn-0053f174) · [`0053f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md#insn-0053f1a0)
- 新版 [`00561ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-00561ffc) · [`0056200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-0056200c) · [`00562038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md#insn-00562038)

~~~diff
- 0053f164 ["INT_ADD", "register:40f0:8", ["const:53f164:8", "const:4:8"]]
- 0053f164 ["CALL", null, ["callee:005626b4:8"]]
+ 00561ffc ["INT_ADD", "register:40f0:8", ["const:561ffc:8", "const:4:8"]]
+ 00561ffc ["CALL", null, ["callee:005626b4:8"]]
- 0053f164 bytes ae010094
+ 00561ffc bytes ae010094
- 0053f174 ["INT_ADD", "register:40f0:8", ["const:53f174:8", "const:4:8"]]
- 0053f174 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0056200c ["INT_ADD", "register:40f0:8", ["const:56200c:8", "const:4:8"]]
+ 0056200c ["CALL", null, ["callee:00c57ab0:8"]]
- 0053f174 bytes bb6f1a94
+ 0056200c bytes a9d61b94
- 0053f1a0 ["INT_ADD", "register:40f0:8", ["const:53f1a0:8", "const:4:8"]]
- 0053f1a0 ["CALL", null, ["callee:00c58030:8"]]
+ 00562038 ["INT_ADD", "register:40f0:8", ["const:562038:8", "const:4:8"]]
+ 00562038 ["CALL", null, ["callee:00c58030:8"]]
- 0053f1a0 bytes 10711a94
+ 00562038 bytes fed71b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a5c602e7187adf100bee37b9722a56"></a>

### [`0053fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md) → [`00562c9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md) FUN_00562c9c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00562d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562d50.md) [`00563058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563058.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00562cac",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0053fe14",
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
      "definition_site": "00562ca8",
      "incomplete_value": false,
      "site": "00562cac",
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
      "definition_site": "0053fe10",
      "incomplete_value": false,
      "site": "0053fe14",
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
      "00562ca8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00562cac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00562ca8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00562cac",
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

- 旧版 [`0053fe14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md#insn-0053fe14) · [`0053fe0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md#insn-0053fe0c) · [`0053fe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md#insn-0053fe10)
- 新版 [`00562cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md#insn-00562cac) · [`00562ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md#insn-00562ca4) · [`00562ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/00562c9c.md#insn-00562ca8)

~~~diff
- 0053fe14 ["INT_ADD", "register:40f0:8", ["const:53fe14:8", "const:4:8"]]
- 0053fe14 ["CALL", null, ["ram:418c38:8"]]
+ 00562cac ["INT_ADD", "register:40f0:8", ["const:562cac:8", "const:4:8"]]
+ 00562cac ["CALL", null, ["ram:43b738:8"]]
- 0053fe14 bytes 8963fb97
+ 00562cac bytes a362fb97
- 0053fe0c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00562ca4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0053fe0c bytes 40ebff90
+ 00562ca4 bytes a0eaffb0
- 0053fe10 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0053fe10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00562ca8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00562ca8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00562ca8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00562ca8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 bytes 00740e91
+ 00562ca8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b79387b434c73f85f558d759c5e1af5"></a>

### [`00540614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540614.md) → [`005634ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md) FUN_005634ac

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "005634c4",
      "incomplete_value": false,
      "site": "005634c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054062c",
      "incomplete_value": false,
      "site": "00540630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "005634c8",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005634c8",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540614.md#insn-00540628) · [`0054062c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540614.md#insn-0054062c) · [`0054063c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540614.md#insn-0054063c)
- 新版 [`005634c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md#insn-005634c0) · [`005634c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md#insn-005634c4) · [`005634d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634ac.md#insn-005634d4)

~~~diff
- 00540628 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 005634c0 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00540628 bytes 693500d0
+ 005634c0 bytes 49380090
- 0054062c ["COPY", "tmp:0:8", ["const:520:8"]]
- 0054062c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005634c4 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 005634c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005634c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005634c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054062c bytes 29811491
+ 005634c4 bytes 29810391
- 0054063c ["INT_ADD", "register:40f0:8", ["const:54063c:8", "const:4:8"]]
- 0054063c ["CALL", null, ["callee:00c57ab0:8"]]
+ 005634d4 ["INT_ADD", "register:40f0:8", ["const:5634d4:8", "const:4:8"]]
+ 005634d4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0054063c bytes 896a1a94
+ 005634d4 bytes 77d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c39b53845c68c7c3836505940ab47539"></a>

### [`00540664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540664.md) → [`005634fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md) FUN_005634fc

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563514",
      "incomplete_value": false,
      "site": "00563518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054067c",
      "incomplete_value": false,
      "site": "00540680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "00563518",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563518",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540664.md#insn-00540678) · [`0054067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540664.md#insn-0054067c) · [`0054068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540664.md#insn-0054068c)
- 新版 [`00563510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563510) · [`00563514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563514) · [`00563524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/005634fc.md#insn-00563524)

~~~diff
- 00540678 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 00563510 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00540678 bytes 693500d0
+ 00563510 bytes 49380090
- 0054067c ["COPY", "tmp:0:8", ["const:520:8"]]
- 0054067c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00563514 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00563514 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00563514 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00563514 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054067c bytes 29811491
+ 00563514 bytes 29810391
- 0054068c ["INT_ADD", "register:40f0:8", ["const:54068c:8", "const:4:8"]]
- 0054068c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00563524 ["INT_ADD", "register:40f0:8", ["const:563524:8", "const:4:8"]]
+ 00563524 ["CALL", null, ["callee:00c57ab0:8"]]
- 0054068c bytes 756a1a94
+ 00563524 bytes 63d11b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a555fec45552690e852dcde493275c2"></a>

### [`005406b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005406b0.md) → [`00563548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md) FUN_00563548

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056357c",
      "incomplete_value": false,
      "site": "0056357c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005406e4",
      "incomplete_value": false,
      "site": "005406e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
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
      "0056357c",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0056357c",
      "DATA",
      [
        "storage",
        "00c6b0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005406c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005406b0.md#insn-005406c8) · [`005406d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005406b0.md#insn-005406d4) · [`005406d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005406b0.md#insn-005406d8)
- 新版 [`00563560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-00563560) · [`0056356c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-0056356c) · [`00563570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563548.md#insn-00563570)

~~~diff
- 005406c8 ["INT_ADD", "register:40f0:8", ["const:5406c8:8", "const:4:8"]]
- 005406c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00563560 ["INT_ADD", "register:40f0:8", ["const:563560:8", "const:4:8"]]
+ 00563560 ["CALL", null, ["callee:00c57a90:8"]]
- 005406c8 bytes 5e6a1a94
+ 00563560 bytes 4cd11b94
- 005406d4 ["COPY", "register:4050:8", ["const:bee000:8"]]
+ 0056356c ["COPY", "register:4050:8", ["const:c6b000:8"]]
- 005406d4 bytes 6a3500d0
+ 0056356c bytes 4a380090
- 005406d8 ["COPY", "tmp:0:8", ["const:520:8"]]
- 005406d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00563570 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00563570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00563570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00563570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005406d8 bytes 4a811491
+ 00563570 bytes 4a810391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e26c270861ead2caf708543a569d91"></a>

### [`005408b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005408b8.md) → [`00563750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md) FUN_00563750

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0056377c",
      "incomplete_value": true,
      "site": "0056377c",
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
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e4",
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
      "00563774",
      "READ",
      [
        "storage",
        "00c25e00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00563774",
      "READ",
      [
        "storage",
        "00ca58c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005408d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005408b8.md#insn-005408d4) · [`005408dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005408b8.md#insn-005408dc) · [`00540900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005408b8.md#insn-00540900)
- 新版 [`0056376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-0056376c) · [`00563774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-00563774) · [`00563798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563750.md#insn-00563798)

~~~diff
- 005408d4 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0056376c ["COPY", "register:4040:8", ["const:ca5000:8"]]
- 005408d4 bytes 283700b0
+ 0056376c bytes 083a00d0
- 005408dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
- 005408dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00563774 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8c0:8"]]
+ 00563774 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005408dc bytes 080147f9
+ 00563774 bytes 086144f9
- 00540900 ["COPY", "register:0:8", ["register:4048:8"]]
- 00540900 ["INT_ADD", "register:40f0:8", ["const:540900:8", "const:4:8"]]
- 00540900 ["CALLIND", null, ["register:0:8"]]
+ 00563798 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00563798 ["INT_ADD", "register:40f0:8", ["const:563798:8", "const:4:8"]]
+ 00563798 ["CALLIND", null, ["register:0:8"]]
- 00540900 bytes 20013fd6
+ 00563798 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d612fdf4fd25e85b000d925d0e14aa75"></a>

### [`005409a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409a4.md) → [`0056383c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056383c.md) FUN_0056383c

採用 · 移動量 `+0x22e98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0056384c",
      "incomplete_value": false,
      "site": "00563850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409b4",
      "incomplete_value": false,
      "site": "005409b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "00563850",
      "DATA",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00563850",
      "DATA",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409a4.md#insn-005409b0) · [`005409b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409a4.md#insn-005409b4)
- 新版 [`00563848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056383c.md#insn-00563848) · [`0056384c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056383c.md#insn-0056384c)

~~~diff
- 005409b0 ["COPY", "register:4048:8", ["const:bee000:8"]]
+ 00563848 ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005409b0 bytes 693500d0
+ 00563848 bytes 49380090
- 005409b4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005409b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0056384c ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 0056384c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0056384c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0056384c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005409b4 bytes 29c11791
+ 0056384c bytes 29c10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c053b81da00ad41c4609680510bcc69"></a>

### [`005409c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md) → [`0056385c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md) FUN_0056385c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0054243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054243c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00540c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005652d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005652d4.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`00563ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563ac4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00563888",
      "incomplete_value": false,
      "site": "005638a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:1b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409f0",
      "incomplete_value": false,
      "site": "00540a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
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
      "005638a4",
      "DATA",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00563954",
      "READ",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005638a4",
      "DATA",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00563954",
      "READ",
      [
        "storage",
        "00c6b1b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md#insn-005409ec) · [`005409f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md#insn-005409f0) · [`00540a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md#insn-00540a30)
- 新版 [`00563884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-00563884) · [`00563888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-00563888) · [`005638c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/0056385c.md#insn-005638c8)

~~~diff
- 005409ec ["COPY", "register:4050:8", ["const:bee000:8"]]
+ 00563884 ["COPY", "register:4050:8", ["const:c6b000:8"]]
- 005409ec bytes 6a3500d0
+ 00563884 bytes 4a380090
- 005409f0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
- 005409f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00563888 ["COPY", "tmp:0:8", ["const:1b0:8"]]
+ 00563888 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00563888 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00563888 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005409f0 bytes 4ac11791
+ 00563888 bytes 4ac10691
- 00540a30 ["INT_ADD", "register:40f0:8", ["const:540a30:8", "const:4:8"]]
- 00540a30 ["CALL", null, ["callee:005626b4:8"]]
+ 005638c8 ["INT_ADD", "register:40f0:8", ["const:5638c8:8", "const:4:8"]]
+ 005638c8 ["CALL", null, ["callee:005626b4:8"]]
- 00540a30 bytes 7bfbff97
+ 005638c8 bytes 7bfbff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dce6eb15e4aecc48bf5a18aa1c77267"></a>

### [`005416b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md) → [`00564548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md) FUN_00564548

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00540f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540f58.md) [`00832d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832d28.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`008e6014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e6/008e6014.md) [`009e6044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e6/009e6044.md) · 呼出先 9件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)
- 新版 呼出元 5件 [`00563df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00563/00563df0.md) [`00864ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/00864ca0.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`0091a0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a0f8.md) [`00a42f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a42/00a42f40.md) · 呼出先 9件 [`00459490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459490.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ba0.md) [`00c57bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57bb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.07% / 新版 91.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564590",
      "incomplete_value": true,
      "site": "005645a0",
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
      "definition_site": "005416f8",
      "incomplete_value": true,
      "site": "00541708",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00564598",
      "incomplete_value": true,
      "site": "005645a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00541700",
      "incomplete_value": true,
      "site": "0054170c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005645f8",
      "incomplete_value": true,
      "site": "005645fc",
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
      "definition_site": "00541760",
      "incomplete_value": true,
      "site": "00541764",
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
      "0056457c",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00564580",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00564598",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0056457c",
      "READ",
      [
        "storage",
        "00c9a888",
        null,
        "pointer"
      ]
    ],
    [
      "00564580",
      "READ",
      [
        "storage",
        "00c9a7b8",
        null,
        "pointer"
      ]
    ],
    [
      "00564598",
      "READ",
      [
        "storage",
        "00c92e08",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005416d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md#insn-005416d4) · [`005416d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md#insn-005416d8) · [`005416e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005416b0.md#insn-005416e4)
- 新版 [`0056456c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-0056456c) · [`00564570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-00564570) · [`0056457c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564548.md#insn-0056457c)

~~~diff
- 005416d4 ["COPY", "register:40d0:8", ["const:c1a000:8"]]
+ 0056456c ["COPY", "register:40d0:8", ["const:c9a000:8"]]
- 005416d4 bytes da3600b0
+ 0056456c bytes ba3900d0
- 005416d8 ["COPY", "register:40c8:8", ["const:c1a000:8"]]
+ 00564570 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
- 005416d8 bytes d93600b0
+ 00564570 bytes b93900d0
- 005416e4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e98:8"]]
- 005416e4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0056457c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:888:8"]]
+ 0056457c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 005416e4 bytes 5a4f47f9
+ 0056457c bytes 5a4744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b9669dab0e661e624605155b3f593a2"></a>

### [`00541908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md) → [`005647a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md) FUN_005647a0

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00561f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00561/00561f90.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

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
      "definition_site": "005647c4",
      "incomplete_value": false,
      "site": "005647c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054192c",
      "incomplete_value": false,
      "site": "0054192c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "005647c4",
      "DATA",
      [
        "storage",
        "00bee6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005647c4",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md#insn-00541920) · [`00541924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md#insn-00541924) · [`00541928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md#insn-00541928)
- 新版 [`005647b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md#insn-005647b8) · [`005647bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/005647a0.md#insn-005647bc)

~~~diff
- 00541920 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 005647b8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00541920 bytes 683500b0
+ 005647b8 bytes 283800f0
- 00541924 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00541924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00541924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00541924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005647bc ["COPY", "tmp:0:8", ["const:270:8"]]
+ 005647bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005647bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005647bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00541924 bytes 08c11a91
+ 005647bc bytes 08c10991
- 00541928 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00541928 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66670a6fc54c2182e4a76fae5eeeb740"></a>

### [`00541e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541e74.md) → [`00564d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md) FUN_00564d0c

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00564d8c",
      "incomplete_value": false,
      "site": "00564d94",
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
            "const:c8d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00541ef4",
      "incomplete_value": false,
      "site": "00541efc",
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
            "const:5cc:8"
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
      "definition_site": "00564f64",
      "incomplete_value": false,
      "site": "00564f70",
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
            "const:86e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005420cc",
      "incomplete_value": false,
      "site": "005420d8",
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
            "const:c15:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00564d8c",
      "PARAM",
      [
        "storage",
        "002a25cc",
        null,
        null
      ]
    ],
    [
      "00564ec8",
      "PARAM",
      [
        "storage",
        "002928f0",
        null,
        null
      ]
    ],
    [
      "00564f64",
      "PARAM",
      [
        "storage",
        "00297c15",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00564d8c",
      "PARAM",
      [
        "storage",
        "002b2c8d",
        null,
        null
      ]
    ],
    [
      "00564ec8",
      "PARAM",
      [
        "storage",
        "002a2000",
        null,
        null
      ]
    ],
    [
      "00564f64",
      "PARAM",
      [
        "storage",
        "002a786e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00541efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541e74.md#insn-00541efc) · [`005420d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541e74.md#insn-005420d8) · [`00541eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541e74.md#insn-00541eb4)
- 新版 [`00564d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564d94) · [`00564f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564f70) · [`00564d4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564d0c.md#insn-00564d4c)

~~~diff
- 00541efc ["INT_ADD", "register:40f0:8", ["const:541efc:8", "const:4:8"]]
- 00541efc ["CALL", null, ["callee:00c57b70:8"]]
+ 00564d94 ["INT_ADD", "register:40f0:8", ["const:564d94:8", "const:4:8"]]
+ 00564d94 ["CALL", null, ["callee:00c57b70:8"]]
- 00541efc bytes 89641a94
+ 00564d94 bytes 77cb1b94
- 005420d8 ["INT_ADD", "register:40f0:8", ["const:5420d8:8", "const:4:8"]]
- 005420d8 ["CALL", null, ["callee:00c57b60:8"]]
+ 00564f70 ["INT_ADD", "register:40f0:8", ["const:564f70:8", "const:4:8"]]
+ 00564f70 ["CALL", null, ["callee:00c57b60:8"]]
- 005420d8 bytes 0e641a94
+ 00564f70 bytes fcca1b94
- 00541eb4 ["COPY", "register:0:8", ["register:4048:8"]]
- 00541eb4 ["INT_ADD", "register:40f0:8", ["const:541eb4:8", "const:4:8"]]
- 00541eb4 ["CALLIND", null, ["register:0:8"]]
+ 00564d4c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00564d4c ["INT_ADD", "register:40f0:8", ["const:564d4c:8", "const:4:8"]]
+ 00564d4c ["CALLIND", null, ["register:0:8"]]
- 00541eb4 bytes 20013fd6
+ 00564d4c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db74020386d9f44ddd45aac852b2ef71"></a>

### [`0054250c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054250c.md) → [`005653a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md) FUN_005653a4

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005418fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/005418fc.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00564794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00564/00564794.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005653bc",
      "incomplete_value": false,
      "site": "005653c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542524",
      "incomplete_value": false,
      "site": "00542528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:6b0:8"
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
      "005653c0",
      "DATA",
      [
        "storage",
        "00bee6b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005653c0",
      "DATA",
      [
        "storage",
        "00c6b270",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054250c.md#insn-00542520) · [`00542524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054250c.md#insn-00542524) · [`00542538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054250c.md#insn-00542538)
- 新版 [`005653b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-005653b8) · [`005653bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-005653bc) · [`005653d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/005653a4.md#insn-005653d0)

~~~diff
- 00542520 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 005653b8 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 00542520 bytes 68350090
+ 005653b8 bytes 283800d0
- 00542524 ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00542524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00542524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00542524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005653bc ["COPY", "tmp:0:8", ["const:270:8"]]
+ 005653bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005653bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005653bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00542524 bytes 08c11a91
+ 005653bc bytes 08c10991
- 00542538 ["INT_ADD", "register:40f0:8", ["const:542538:8", "const:4:8"]]
- 00542538 ["CALL", null, ["callee:00c538e0:8"]]
+ 005653d0 ["INT_ADD", "register:40f0:8", ["const:5653d0:8", "const:4:8"]]
+ 005653d0 ["CALL", null, ["callee:00c538e0:8"]]
- 00542538 bytes 56521a94
+ 005653d0 bytes 44b91b94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03c1db2e02299614fdceef34bdf7dce0"></a>

### [`005425e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005425e4.md) → [`0056547c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md) _INIT_27

採用 · 移動量 `+0x22e98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e10c.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00560fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/00560fa4.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 52.00% / 新版 52.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 10件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005654a4",
      "incomplete_value": false,
      "site": "005654a4",
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
                "const:8a0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054260c",
      "incomplete_value": false,
      "site": "0054260c",
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
                "const:de0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:20:8"
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
      "definition_site": "005654c4",
      "incomplete_value": false,
      "site": "005654c4",
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
            "const:8d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054262c",
      "incomplete_value": false,
      "site": "0054262c",
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
            "const:e10:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005654cc",
      "incomplete_value": false,
      "site": "005654cc",
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
                "const:8d0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00542634",
      "incomplete_value": false,
      "site": "00542634",
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
                "const:e10:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:1:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00565494",
      "PARAM",
      [
        "storage",
        "00c25de0",
        null,
        null
      ]
    ],
    [
      "0056549c",
      "PARAM",
      [
        "storage",
        "0053e10c",
        null,
        null
      ]
    ],
    [
      "005654a0",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00565494",
      "PARAM",
      [
        "storage",
        "00ca58a0",
        null,
        null
      ]
    ],
    [
      "0056549c",
      "PARAM",
      [
        "storage",
        "00560fa4",
        null,
        null
      ]
    ],
    [
      "005654a0",
      "PARAM",
      [
        "storage",
        "00c62b90",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00542610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005425e4.md#insn-00542610) · [`00542640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005425e4.md#insn-00542640) · [`0054266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/005425e4.md#insn-0054266c)
- 新版 [`005654a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md#insn-005654a8) · [`005654d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00565/0056547c.md#insn-005654d8)

~~~diff
- 00542610 ["INT_ADD", "register:40f0:8", ["const:542610:8", "const:4:8"]]
- 00542610 ["CALL", null, ["callee:00c57a30:8"]]
+ 005654a8 ["INT_ADD", "register:40f0:8", ["const:5654a8:8", "const:4:8"]]
+ 005654a8 ["CALL", null, ["callee:00c57a30:8"]]
- 00542610 bytes 74621a94
+ 005654a8 bytes 62c91b94
- 00542640 ["INT_ADD", "register:40f0:8", ["const:542640:8", "const:4:8"]]
- 00542640 ["CALL", null, ["callee:00c57a30:8"]]
+ 005654d8 ["INT_ADD", "register:40f0:8", ["const:5654d8:8", "const:4:8"]]
+ 005654d8 ["CALL", null, ["callee:00c57a30:8"]]
- 00542640 bytes 68621a94
+ 005654d8 bytes 56c91b94
- 0054266c ["INT_ADD", "register:40f0:8", ["const:54266c:8", "const:4:8"]]
- 0054266c ["CALL", null, ["callee:00c57a30:8"]]
- 0054266c bytes 5d621a94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

