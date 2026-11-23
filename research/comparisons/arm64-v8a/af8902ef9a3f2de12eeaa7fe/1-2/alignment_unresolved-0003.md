# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (3)

[一覧の目次](README.md)

<a id="compare-a2022f65c2b30beaa85c9c9a7819af36"></a>

### [`0059c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c754.md) → [`005c0d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md) FUN_005c0d84

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 82.35% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0059c788"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005c0db8"
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
      "unmatched:0059c788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0ddc"
      ]
    ]
  ],
  "added": [
    [
      "005c0db8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c0ddc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059c788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c754.md#insn-0059c788) · [`0059c77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c754.md#insn-0059c77c)
- 新版 [`005c0db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md#insn-005c0db8) · [`005c0dac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0d84.md#insn-005c0dac)

~~~diff
- 0059c788 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0059c788 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0059c788 bytes 21010054
+ 005c0db8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 005c0db8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005c0db8 bytes 21010054
- 0059c77c ["INT_ADD", "register:40f0:8", ["const:59c77c:8", "const:4:8"]]
- 0059c77c ["CALL", null, ["callee:00480af8:8"]]
+ 005c0dac ["INT_ADD", "register:40f0:8", ["const:5c0dac:8", "const:4:8"]]
+ 005c0dac ["CALL", null, ["callee:00480af8:8"]]
- 0059c77c bytes 3905fb97
+ 005c0dac bytes 53fffa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4efb3abc7fe05b65a3ea130fef16d5ab"></a>

### [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) → [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) FUN_005c175c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 145件 [`00597088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597088.md) [`00597ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00597/00597ea8.md) [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`0059d170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d170.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 154件 [`005bb6b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bb/005bb6b8.md) [`005bc4d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc4d8.md) [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`005c17a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c17a0.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005c1778",
      "incomplete_value": true,
      "site": "005c177c",
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
    "old": {
      "definition_site": "0059d148",
      "incomplete_value": true,
      "site": "0059d14c",
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


#### 変更候補の命令位置

- 旧版 [`0059d14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md#insn-0059d14c) · [`0059d148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md#insn-0059d148) · [`0059d158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md#insn-0059d158)
- 新版 [`005c177c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md#insn-005c177c) · [`005c1788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md#insn-005c1788)

~~~diff
- 0059d14c ["INT_ADD", "register:40f0:8", ["const:59d14c:8", "const:4:8"]]
- 0059d14c ["CALL", null, ["local:b0:8"]]
+ 005c177c ["INT_ADD", "register:40f0:8", ["const:5c177c:8", "const:4:8"]]
+ 005c177c ["CALL", null, ["local:b0:8"]]
- 0059d14c bytes f8ffff97
+ 005c177c bytes f8ffff97
- 0059d148 ["COPY", "register:4008:8", ["register:4040:8"]]
- 0059d148 bytes e10308aa
- 0059d158 ["INT_ADD", "register:40f0:8", ["const:59d158:8", "const:4:8"]]
- 0059d158 ["CALL", null, ["local:b0:8"]]
+ 005c1788 ["INT_ADD", "register:40f0:8", ["const:5c1788:8", "const:4:8"]]
+ 005c1788 ["CALL", null, ["local:b0:8"]]
- 0059d158 bytes f5ffff97
+ 005c1788 bytes f5ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc95b1ec9bc82888d19169613c5af54"></a>

### [`0059d38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d38c.md) → [`005c19bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c19bc.md) FUN_005c19bc

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0059d1d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d1d4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`005c1804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1804.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 48.00% / 新版 48.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 8件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059d424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059d430"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059d50c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0059d3b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c1ac4"
      ]
    ],
    [
      "unmatched:0059d460",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c19fc"
      ]
    ],
    [
      "unmatched:0059d48c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c19fc"
      ]
    ]
  ],
  "added": [
    [
      "005c19e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c1ac4"
      ]
    ],
    [
      "005c1a90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c19fc"
      ]
    ],
    [
      "005c1abc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005c19fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0059d3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d38c.md#insn-0059d3b0) · [`0059d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d38c.md#insn-0059d424) · [`0059d430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d38c.md#insn-0059d430)

~~~diff
- 0059d3b0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0059d3b0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 0059d3b0 bytes 280700b4
- 0059d424 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0059d424 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 0059d424 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0059d424 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 0059d424 bytes c1692cf8
- 0059d430 ["INT_ADD", "tmp:0:8", ["register:4070:8", "const:1380:8"]]
- 0059d430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4088:8"]]
- 0059d430 bytes d1c109f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da7cbe8b329b1315cded3cb0a66603a0"></a>

### [`0059d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d658.md) → [`005c1c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c88.md) FUN_005c1c88

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059d658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059d658"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005c1c88"
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
      "unmatched:0059d658",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059d664",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0059d668",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005c1c88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005c1c94",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005c1c98",
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

- 旧版 [`0059d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d658.md#insn-0059d658) · [`0059d668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d658.md#insn-0059d668)
- 新版 [`005c1c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1c88.md#insn-005c1c88)

~~~diff
- 0059d658 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0059d658 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0059d658 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0059d658 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0059d658 bytes fd7bbfa9
- 0059d668 ["INT_ADD", "register:40f0:8", ["const:59d668:8", "const:4:8"]]
- 0059d668 ["CALL", null, ["ram:418c38:8"]]
- 0059d668 bytes 74edf997
+ 005c1c88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005c1c88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005c1c88 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005c1c88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005c1c88 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-decb3d1aa06b8930a6b12e52a8664d54"></a>

### [`0059df20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059df20.md) → [`005c2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2550.md) FUN_005c2550

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0059d680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d680.md) [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) [`0059e29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e29c.md) · 呼出先 0件 
- 新版 呼出元 3件 [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) [`005c2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md) [`005c28cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.04% / 新版 89.04%

CFGの説明率　旧版 53.33% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059df98"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059df9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059dfdc"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0059df98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059df20.md#insn-0059df98) · [`0059df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059df20.md#insn-0059df9c) · [`0059dfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059df20.md#insn-0059dfdc)

~~~diff
- 0059df98 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:4:8"]]
- 0059df98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
- 0059df98 bytes 6a0500b9
- 0059df9c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:8:8"]]
- 0059df9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:4"]]
- 0059df9c bytes 4c0800b9
- 0059dfdc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:4:8"]]
- 0059dfdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 0059dfdc bytes 0b0400b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f21e81444f4ab5002dee43430de14c29"></a>

### [`0059e29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e29c.md) → [`005c28cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md) FUN_005c28cc

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0059d680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d680.md) [`0059e044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e044.md) · 呼出先 1件 [`0059df20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059df20.md)
- 新版 呼出元 2件 [`005c1cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c1cb0.md) [`005c2674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2674.md) · 呼出先 1件 [`005c2550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2550.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0059e38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "005c29bc"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0059e38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e29c.md#insn-0059e38c) · [`0059e2bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e29c.md#insn-0059e2bc)
- 新版 [`005c29bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md#insn-005c29bc) · [`005c28ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c28cc.md#insn-005c28ec)

~~~diff
- 0059e38c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0059e38c ["RETURN", null, ["register:0:8"]]
- 0059e38c bytes c0035fd6
+ 005c29bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 005c29bc ["RETURN", null, ["register:0:8"]]
+ 005c29bc bytes c0035fd6
- 0059e2bc ["INT_ADD", "register:40f0:8", ["const:59e2bc:8", "const:4:8"]]
- 0059e2bc ["CALL", null, ["callee:005c2550:8"]]
+ 005c28ec ["INT_ADD", "register:40f0:8", ["const:5c28ec:8", "const:4:8"]]
+ 005c28ec ["CALL", null, ["callee:005c2550:8"]]
- 0059e2bc bytes 19ffff97
+ 005c28ec bytes 19ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad485bc89aa3515a9f8c091d2a693bfd"></a>

### [`0059e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e3e0.md) → [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) FUN_005c2a10

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0059e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e3e0.md) · 呼出先 2件 [`0059e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e3e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005bc78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005bc/005bc78c.md) [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) · 呼出先 2件 [`005c2a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059e3e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059e3e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059e3e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0059e3e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059e3e8",
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
      "005c2a14",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c2a18",
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

- 旧版 [`0059e3e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e3e0.md#insn-0059e3e4) · [`0059e3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e3e0.md#insn-0059e3e8)
- 新版 [`005c2a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a10.md#insn-005c2a14)

~~~diff
- 0059e3e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0059e3e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0059e3e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0059e3e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0059e3e4 bytes fd7bbea9
- 0059e3e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0059e3e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0059e3e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0059e3e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0059e3e8 bytes f44f01a9
+ 005c2a14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005c2a14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005c2a14 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005c2a14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005c2a14 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90a5ecb2fe5b6be6506302b3cc3909b0"></a>

### [`0059f288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f288.md) → [`005c38b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c38b8.md) FUN_005c38b8

採用 · 移動量 `+0x24630` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0059e424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e424.md) [`0059f454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f454.md) [`0059f6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f6ac.md) · 呼出先 2件 [`0063eaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063eaf8.md) [`00aa05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa05ac.md)
- 新版 呼出元 3件 [`005c2a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c2/005c2a54.md) [`005c3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3a84.md) [`005c3cdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3cdc.md) · 呼出先 2件 [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.52% / 新版 56.52%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 16件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f288"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f28c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0059f288",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059f28c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059f290",
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
      "005c38b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005c38bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005c38c0",
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

- 旧版 [`0059f288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f288.md#insn-0059f288) · [`0059f28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f288.md#insn-0059f28c) · [`0059f290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f288.md#insn-0059f290)

~~~diff
- 0059f288 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0059f288 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0059f288 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 0059f288 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0059f288 bytes fd7bbba9
- 0059f28c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0059f28c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0059f28c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0059f28c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0059f28c bytes fa6701a9
- 0059f290 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0059f290 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0059f290 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0059f290 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0059f290 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09deef75e9bc00ebe9585f6668c05e2f"></a>

### [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) → [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) FUN_005c3e3c

採用 · 移動量 `+0x24630` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 43件 [`0059c4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c4f4.md) [`0059c528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059c/0059c528.md) [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`005a1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a1/005a1c90.md) [`006181e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/006181e8.md) · 呼出先 2件 [`0059f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 54件 [`005c0b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b24.md) [`005c0b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c0b58.md) [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`005c62c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c6/005c62c0.md) [`0063dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dcd0.md) · 呼出先 2件 [`005c3e3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f810"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0059f814"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0059f810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0059f814",
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
      "005c3e40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005c3e44",
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

- 旧版 [`0059f810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md#insn-0059f810) · [`0059f814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f80c.md#insn-0059f814)
- 新版 [`005c3e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c3/005c3e3c.md#insn-005c3e40)

~~~diff
- 0059f810 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0059f810 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0059f810 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0059f810 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0059f810 bytes fd7bbea9
- 0059f814 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0059f814 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0059f814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0059f814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0059f814 bytes f44f01a9
+ 005c3e40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005c3e40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005c3e40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005c3e40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005c3e40 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a387d24a78ac891697482a15a413ef4c"></a>

### [`005a7844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md) → [`005cc4d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005cc4d4.md) FUN_005cc4d4

採用 · 移動量 `+0x24c90` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 74.29% / 新版 74.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a786c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a78ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005cc4fc"
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
      "unmatched:005a7858",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cc554"
      ]
    ],
    [
      "unmatched:005a786c",
      "DATA",
      [
        "storage",
        "00c0bd90",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005a78a4",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005cc4e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cc554"
      ]
    ],
    [
      "005cc4fc",
      "DATA",
      [
        "storage",
        "00c8b3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "005cc534",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005a7858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md#insn-005a7858) · [`005a786c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md#insn-005a786c) · [`005a78ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7844.md#insn-005a78ac)

~~~diff
- 005a7858 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005a7858 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 005a7858 bytes 730300b4
- 005a786c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 005a786c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005a786c bytes 680200f9
- 005a78ac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005a78ac ["COPY", "tmp:1:8", ["register:4000:8"]]
- 005a78ac ["INT_ADD", "register:4000:8", ["register:4000:8", "const:50:8"]]
- 005a78ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005a78ac bytes 080405f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e757a0031f3b2c1881e4ca6898f103d9"></a>

### [`005a8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a0c.md) → [`005cd6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md) FUN_005cd6d8

採用 · 移動量 `+0x24ccc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a98f4.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)
- 新版 呼出元 1件 [`005ce5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce5c0.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a8a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a8a0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005a8a10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005a8a0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005a8a10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005a8a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "005cd6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005cd6dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005cd724",
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

- 旧版 [`005a8a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a0c.md#insn-005a8a0c) · [`005a8a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a8a0c.md#insn-005a8a10)
- 新版 [`005cd6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cd/005cd6d8.md#insn-005cd6d8)

~~~diff
- 005a8a0c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005a8a0c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005a8a0c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005a8a0c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005a8a0c bytes fd7bbea9
- 005a8a10 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005a8a10 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005a8a10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005a8a10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005a8a10 bytes f44f01a9
+ 005cd6d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005cd6d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005cd6d8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005cd6d8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005cd6d8 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a055ae505012bc9d51af7e336b86caf8"></a>

### [`005a9f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md) → [`005cebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005cebdc.md) FUN_005cebdc

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005a97c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a97c0.md) [`005a9860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9860.md) [`005b0b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0b60.md) · 呼出先 3件 [`005afe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005afe3c.md) [`005aff7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005aff7c.md) [`005affc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005af/005affc8.md)
- 新版 呼出元 3件 [`005ce48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce48c.md) [`005ce52c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce52c.md) [`005d582c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d582c.md) · 呼出先 3件 [`005d4b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4b08.md) [`005d4c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c48.md) [`005d4c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d4/005d4c94.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 78.23% / 新版 80.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa000"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005aa00c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005ceccc"
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
      "005cec5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005aa268"
      ]
    ],
    [
      "005cec78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005aa268"
      ]
    ],
    [
      "005cecb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005aa008"
      ]
    ]
  ],
  "added": [
    [
      "005cec5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cef34"
      ]
    ],
    [
      "005cec78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cef34"
      ]
    ],
    [
      "005cecb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005cecd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005aa000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md#insn-005aa000) · [`005aa00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md#insn-005aa00c) · [`005aa268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9f10.md#insn-005aa268)

~~~diff
- 005aa000 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005aa000 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
- 005aa000 bytes 61feff54
- 005aa00c ["CBRANCH", null, ["local:b76:8", "register:101:1"]]
- 005aa00c bytes e0120054
- 005aa268 ["INT_ADD", "register:40f0:8", ["const:5aa268:8", "const:4:8"]]
- 005aa268 ["CALL", null, ["ram:5aff7c:8"]]
- 005aa268 bytes 45170094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c67e594858ddec6b09cd4254df83af68"></a>

### [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md) → [`005cfaf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfaf4.md) FUN_005cfaf4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005aa7fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa7fc.md) [`005b0f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b0/005b0f54.md) · 呼出先 3件 [`005aaff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aaff0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005cf4c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf4c8.md) [`005d5c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5c20.md) · 呼出先 3件 [`005cfcbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cfcbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 43.59% / 新版 48.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aae28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aae28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005aae2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005aae28",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aae2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005aae30",
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
      "005cfaf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005cfaf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005cfafc",
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

- 旧版 [`005aae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md#insn-005aae28) · [`005aae2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md#insn-005aae2c) · [`005aae30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aae28.md#insn-005aae30)

~~~diff
- 005aae28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005aae28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005aae28 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005aae28 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005aae28 bytes fd7bbda9
- 005aae2c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005aae2c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005aae2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005aae2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005aae2c bytes f65701a9
- 005aae30 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005aae30 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005aae30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005aae30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005aae30 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15dab584c9f2a5093afe389609784bf9"></a>

### [`005ab258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab258.md) → [`005cff24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md) FUN_005cff24

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005aa9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005aa/005aa9b4.md) [`005b1ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1ce4.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005cf680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cf680.md) [`005d69b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d6/005d69b0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 68.75% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "005cffa8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005ab2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab258.md#insn-005ab2dc) · [`005ab26c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab258.md#insn-005ab26c)
- 新版 [`005cffa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md#insn-005cffa8) · [`005cff38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cff24.md#insn-005cff38)

~~~diff
- 005ab2dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 005ab2dc ["RETURN", null, ["register:0:8"]]
- 005ab2dc bytes c0035fd6
+ 005cffa8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 005cffa8 ["RETURN", null, ["register:0:8"]]
+ 005cffa8 bytes c0035fd6
- 005ab26c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 005ab26c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 005cff38 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 005cff38 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 005ab26c bytes 340300b4
+ 005cff38 bytes 340300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6abf28fb6abc2b76a33dfd406f696a4f"></a>

### [`005ab4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab4c4.md) → [`005d0190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0190.md) FUN_005d0190

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.89% / 新版 95.89%

CFGの説明率　旧版 47.37% / 新版 64.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab50c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab50c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab554"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ab4f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0268"
      ]
    ]
  ],
  "added": [
    [
      "005d01c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0268"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ab4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab4c4.md#insn-005ab4f4) · [`005ab50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab4c4.md#insn-005ab50c) · [`005ab554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab4c4.md#insn-005ab554)

~~~diff
- 005ab4f4 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 005ab4f4 bytes 40050054
- 005ab50c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005ab50c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 005ab50c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 005ab50c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 005ab50c bytes 210100ad
- 005ab554 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 005ab554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:55:8"]]
- 005ab554 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005ab554 bytes 2a5105f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e819302a1f49872b4abc40271ad482b"></a>

### [`005ab664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md) → [`005d0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md) FUN_005d0330

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005ab2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab2e0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005cffac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cf/005cffac.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ab664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d0330"
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
      "unmatched:005ab664",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ab670",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005ab674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d0330",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d033c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d0340",
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

- 旧版 [`005ab664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md#insn-005ab664) · [`005ab674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005ab664.md#insn-005ab674)
- 新版 [`005d0330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0330.md#insn-005d0330)

~~~diff
- 005ab664 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ab664 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ab664 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005ab664 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ab664 bytes fd7bbfa9
- 005ab674 ["INT_ADD", "register:40f0:8", ["const:5ab674:8", "const:4:8"]]
- 005ab674 ["CALL", null, ["ram:418c38:8"]]
- 005ab674 bytes 71b5f997
+ 005d0330 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005d0330 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005d0330 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005d0330 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005d0330 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95391fb988739c6109ab33dc7478e917"></a>

### [`005abb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb4c.md) → [`005d0818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0818.md) FUN_005d0818

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 22.22% / 新版 22.22%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005abb5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005abb64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005abb64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005abb50",
      "READ",
      [
        "storage",
        "00c1b5b0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:005abb5c",
      "DATA",
      [
        "storage",
        "00bf3790",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "unmatched:005abb60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d085c"
      ]
    ]
  ],
  "added": [
    [
      "005d081c",
      "READ",
      [
        "storage",
        "00c9afa8",
        null,
        "pointer"
      ]
    ],
    [
      "005d0828",
      "DATA",
      [
        "storage",
        "00c707b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005d082c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d085c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005abb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb4c.md#insn-005abb5c) · [`005abb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb4c.md#insn-005abb60) · [`005abb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb4c.md#insn-005abb64)

~~~diff
- 005abb5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005abb5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005abb5c bytes 090000f9
- 005abb60 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005abb60 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 005abb60 bytes 880100b4
- 005abb64 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005abb64 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005abb64 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005abb64 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005abb64 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e0528d4494a614b41267b1d37a9171"></a>

### [`005abeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) → [`005d0b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0b78.md) FUN_005d0b78

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005a9c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a9/005a9c58.md) [`005ae770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ae/005ae770.md) · 呼出先 3件 [`005abb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abb94.md) [`005ac1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac1ac.md) [`00bdd990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd990.md)
- 新版 呼出元 2件 [`005ce924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ce/005ce924.md) [`005d343c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d3/005d343c.md) · 呼出先 3件 [`005d0860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0860.md) [`005d0e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d0/005d0e78.md) [`00c5a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 81.98% / 新版 79.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac068"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d0d34"
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
      "005d0be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005ac1a8"
      ]
    ],
    [
      "005d0bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005ac1a8"
      ]
    ],
    [
      "005d0ca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005ac1a8"
      ]
    ]
  ],
  "added": [
    [
      "005d0be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0e74"
      ]
    ],
    [
      "005d0bfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0e74"
      ]
    ],
    [
      "005d0ca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d0e74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md#insn-005ac068) · [`005ac0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md#insn-005ac0bc) · [`005ac1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md#insn-005ac1a8)

~~~diff
- 005ac068 ["CBRANCH", null, ["local:b69:8", "register:101:1"]]
- 005ac068 bytes 000a0054
- 005ac0bc ["CBRANCH", null, ["local:b49:8", "register:101:1"]]
- 005ac0bc bytes 20010054
- 005ac1a8 ["INT_ADD", "register:40f0:8", ["const:5ac1a8:8", "const:4:8"]]
- 005ac1a8 ["CALL", null, ["ram:5abb94:8"]]
- 005ac1a8 bytes 7bfeff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-127e32fb3014965e1e35d5302ddf081e"></a>

### [`005ac76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac76c.md) → [`005d1438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md) FUN_005d1438

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.28% / 新版 98.28%

CFGの説明率　旧版 50.00% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac7d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d149c"
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
      "unmatched:005ac7d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d14f4"
      ]
    ]
  ],
  "added": [
    [
      "005d149c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d14f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac76c.md#insn-005ac7d0) · [`005ac7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac76c.md#insn-005ac7b4)
- 新版 [`005d149c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md#insn-005d149c) · [`005d1480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1438.md#insn-005d1480)

~~~diff
- 005ac7d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005ac7d0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005ac7d0 bytes cb020054
+ 005d149c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005d149c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 005d149c bytes cb020054
- 005ac7b4 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005ac7b4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005d1480 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005d1480 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005ac7b4 bytes aa000054
+ 005d1480 bytes aa000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d818fd08e0a7e5dd1b7f312a2f815e33"></a>

### [`005ac908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac908.md) → [`005d15d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d15d4.md) FUN_005d15d4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ac938"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d1604"
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
      "unmatched:005ac938",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1618"
      ]
    ]
  ],
  "added": [
    [
      "005d1604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1618"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005ac938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac908.md#insn-005ac938) · [`005ac920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ac908.md#insn-005ac920)
- 新版 [`005d1604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d15d4.md#insn-005d1604) · [`005d15ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d15d4.md#insn-005d15ec)

~~~diff
- 005ac938 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005ac938 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005ac938 bytes aa000054
+ 005d1604 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 005d1604 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005d1604 bytes aa000054
- 005ac920 ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
- 005ac920 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005d15ec ["INT_EQUAL", "tmp:0:1", ["register:4048:4", "const:0:4"]]
+ 005d15ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005ac920 bytes e9000034
+ 005d15ec bytes e9000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f006712b69f5b9ce18abc856dcc99042"></a>

### [`005acdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acdb0.md) → [`005d1a7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1a7c.md) FUN_005d1a7c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.57% / 新版 68.57%

CFGの説明率　旧版 71.43% / 新版 58.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acdb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acdb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005acdb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005acdb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005acdb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005acdb8",
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
      "005d1a7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005d1a80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005d1a84",
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

- 旧版 [`005acdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acdb0.md#insn-005acdb0) · [`005acdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acdb0.md#insn-005acdb4) · [`005acdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acdb0.md#insn-005acdb8)

~~~diff
- 005acdb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005acdb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005acdb0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005acdb0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005acdb0 bytes fd7bbda9
- 005acdb4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005acdb4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005acdb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005acdb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005acdb4 bytes f65701a9
- 005acdb8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005acdb8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005acdb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005acdb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005acdb8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-388865651f7d8d7aef52a6f3da5bfd97"></a>

### [`005acf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acf80.md) → [`005d1c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c4c.md) FUN_005d1c4c

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005ace3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005ace3c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005d1b08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1b08.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005acf90"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005d1c5c"
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
      "unmatched:005acf90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005ace3c"
      ]
    ]
  ],
  "added": [
    [
      "005d1c5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005d1b08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005acf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acf80.md#insn-005acf90)
- 新版 [`005d1c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c4c.md#insn-005d1c5c)

~~~diff
- 005acf90 ["INT_ADD", "register:40f0:8", ["const:5acf90:8", "const:4:8"]]
- 005acf90 ["CALL", null, ["ram:5ace3c:8"]]
- 005acf90 bytes abffff97
+ 005d1c5c ["INT_ADD", "register:40f0:8", ["const:5d1c5c:8", "const:4:8"]]
+ 005d1c5c ["CALL", null, ["ram:5d1b08:8"]]
+ 005d1c5c bytes abffff97
~~~


<a id="compare-d3ce67d9fccc36310c3ca95193132129"></a>

### [`005acfa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md) → [`005d1c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d1/005d1c70.md) FUN_005d1c70

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`005ad904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ad904.md) [`005ada74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005ada74.md) [`005adcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ad/005adcd8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005d25d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d25d0.md) [`005d2740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d2740.md) [`005d29a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d2/005d29a4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 98.47% / 新版 98.47%

CFGの説明率　旧版 93.12% / 新版 90.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ad06c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ad110"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005ad118"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ad110",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1dfc"
      ]
    ],
    [
      "unmatched:005ad01c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005d1ddc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d1dfc"
      ]
    ],
    [
      "005d1ce8",
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

- 旧版 [`005ad01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md#insn-005ad01c) · [`005ad06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md#insn-005ad06c) · [`005ad110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ac/005acfa4.md#insn-005ad110)

~~~diff
- 005ad01c ["COPY", "register:0:8", ["register:4040:8"]]
- 005ad01c ["INT_ADD", "register:40f0:8", ["const:5ad01c:8", "const:4:8"]]
- 005ad01c ["CALLIND", null, ["register:0:8"]]
- 005ad01c bytes 00013fd6
- 005ad06c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 005ad06c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005ad06c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005ad06c ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 005ad06c bytes 5501899a
- 005ad110 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 005ad110 bytes 00010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc4140b7876a6871c290e3275610dde"></a>

### [`005b31f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b31f4.md) → [`005d7ec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7ec0.md) FUN_005d7ec0

採用 · 移動量 `+0x24ccc` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b2e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b2/005b2e10.md) · 呼出先 4件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`005d7adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d7/005d7adc.md) · 呼出先 4件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 25.93% / 新版 20.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3258"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3288"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b32b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b3258",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d7f38"
      ]
    ],
    [
      "unmatched:005b3288",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8048"
      ]
    ],
    [
      "unmatched:005b32b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8008"
      ]
    ]
  ],
  "added": [
    [
      "005d7f24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d7f38"
      ]
    ],
    [
      "005d7f54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8048"
      ]
    ],
    [
      "005d7f7c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8008"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b31f4.md#insn-005b3258) · [`005b3288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b31f4.md#insn-005b3288) · [`005b32b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b31f4.md#insn-005b32b0)

~~~diff
- 005b3258 ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
- 005b3258 bytes a0000054
- 005b3288 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 005b3288 ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 005b3288 bytes a90700b5
- 005b32b0 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 005b32b0 bytes 60040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38918ab6e8b406e84903269404fb187d"></a>

### [`005b3850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md) → [`005d851c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md) FUN_005d851c

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b1248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b1/005b1248.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005b39cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`005d5f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d5/005d5f14.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d8698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8698.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.63% / 新版 92.63%

CFGの説明率　旧版 65.22% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3884"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d8550"
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
      "unmatched:005b3884",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d85cc"
      ]
    ]
  ],
  "added": [
    [
      "005d8550",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d85cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md#insn-005b3884) · [`005b387c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3850.md#insn-005b387c)
- 新版 [`005d8550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d851c.md#insn-005d8550)

~~~diff
- 005b3884 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 005b3884 bytes e2030054
+ 005d8550 ["CBRANCH", null, ["local:b6:8", "register:102:1"]]
+ 005d8550 bytes e2030054
- 005b387c ["INT_MULT", "register:4050:8", ["register:4050:8", "register:4048:8"]]
- 005b387c bytes 4a7d099b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6032f2091e41757e147f4704e85a87d6"></a>

### [`005b39e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39e0.md) → [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) FUN_00695b6c

採用 · 移動量 `+0xe218c` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 10件 [`005a02e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a0/005a02e8.md) [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) [`0066181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/0066181c.md) [`008d5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d5/008d5008.md) [`00963004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00963/00963004.md) · 呼出先 4件 [`005b3d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3d60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9d0.md)
- 新版 呼出元 20件 [`006954cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md) [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) [`00698a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698a38.md) [`0090b76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090b/0090b76c.md) [`0091a9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0091a/0091a9dc.md) · 呼出先 4件 [`005d8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 89.89% / 新版 89.89%

CFGの説明率　旧版 63.29% / 新版 52.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3c48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00695dd4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3b08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00695c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005b3b10"
      ]
    ],
    [
      "unmatched:005b3b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695db4"
      ]
    ],
    [
      "unmatched:005b3b18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695cb8"
      ]
    ]
  ],
  "added": [
    [
      "00695c88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695c9c"
      ]
    ],
    [
      "00695c98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695db4"
      ]
    ],
    [
      "00695ca4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695cb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39e0.md#insn-005b3b08) · [`005b3b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39e0.md#insn-005b3b0c) · [`005b3b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39e0.md#insn-005b3b18)

~~~diff
- 005b3b08 ["COPY", "register:100:1", ["const:0:1"]]
- 005b3b08 ["COPY", "register:101:1", ["const:0:1"]]
- 005b3b08 ["COPY", "register:102:1", ["const:1:1"]]
- 005b3b08 ["COPY", "register:103:1", ["const:1:1"]]
- 005b3b08 bytes 4020201e
- 005b3b0c ["BOOL_NEGATE", "tmp:0:1", ["register:100:1"]]
- 005b3b0c ["CBRANCH", null, ["local:b40:8", "tmp:0:1"]]
- 005b3b0c bytes e5080054
- 005b3b18 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005b3b18 ["CBRANCH", null, ["local:b21:8", "tmp:0:1"]]
- 005b3b18 bytes a3000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97682586bf4f9bf3a13907b38700567b"></a>

### [`005b3d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3d60.md) → [`005d8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md) FUN_005d8a2c

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005b39e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b39e0.md) [`0066f668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f668.md) [`0066f824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f824.md) [`0066fbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fbc8.md) · 呼出先 3件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 4件 [`005d86ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d86ac.md) [`006959b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md) [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`00695f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695f10.md) · 呼出先 3件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 85.00% / 新版 80.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005b3e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005d8b34"
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
      "unmatched:005b3e68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8b78"
      ]
    ]
  ],
  "added": [
    [
      "005d8b34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8b78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b3e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3d60.md#insn-005b3e68) · [`005b3d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3d60.md#insn-005b3d70)
- 新版 [`005d8b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md#insn-005d8b34) · [`005d8a3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md#insn-005d8a3c)

~~~diff
- 005b3e68 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 005b3e68 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 005b3e68 bytes 2b0200b4
+ 005d8b34 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
+ 005d8b34 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
+ 005d8b34 bytes 2b0200b4
- 005b3d70 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 005b3d70 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 005d8a3c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 005d8a3c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 005b3d70 bytes e10300b4
+ 005d8a3c bytes e10300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f89cf5e71b7544545d63eea8e10e5da9"></a>

### [`005b4028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md) → [`005d8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md) FUN_005d8cf4

採用 · 移動量 `+0x24ccc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005a45f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a4/005a45f4.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`005b3f58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3f58.md) [`005b4210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`005c8ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8ebc.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`005d8c24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8c24.md) [`005d8edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8edc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.52% / 新版 88.52%

CFGの説明率　旧版 50.00% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b410c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4114"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b412c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b414c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8ea4"
      ]
    ],
    [
      "unmatched:005b41d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8e88"
      ]
    ]
  ],
  "added": [
    [
      "005d8e18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8ea4"
      ]
    ],
    [
      "005d8e9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005d8e88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b410c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md#insn-005b410c) · [`005b4114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md#insn-005b4114) · [`005b412c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md#insn-005b412c)

~~~diff
- 005b410c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005b410c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 005b410c bytes 2a0100f9
- 005b4114 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:28:8"]]
- 005b4114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b4114 bytes 2081823c
- 005b412c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:38:8"]]
- 005b412c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b412c bytes 2081833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823348e7344c590415ace6078be60bd7"></a>

### [`005b4210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md) → [`005d8edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8edc.md) FUN_005d8edc

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b4028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4028.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005d8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8cf4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d8edc"
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
      "unmatched:005b4210",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b421c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005b4220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005d8edc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d8ee8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005d8eec",
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

- 旧版 [`005b4210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md#insn-005b4210) · [`005b4220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4210.md#insn-005b4220)
- 新版 [`005d8edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8edc.md#insn-005d8edc)

~~~diff
- 005b4210 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b4210 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b4210 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005b4210 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b4210 bytes fd7bbfa9
- 005b4220 ["INT_ADD", "register:40f0:8", ["const:5b4220:8", "const:4:8"]]
- 005b4220 ["CALL", null, ["ram:418c38:8"]]
- 005b4220 bytes 8692f997
+ 005d8edc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005d8edc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005d8edc ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005d8edc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005d8edc bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d05e340a5bf53cc400c70afb7ac4e1b7"></a>

### [`005b4228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4228.md) → [`005d8ef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md) FUN_005d8ef4

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b424c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b424c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d8f18"
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
      "unmatched:005b424c",
      "DATA",
      [
        "storage",
        "00bf3dc0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b4250",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b4254",
      "DATA",
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
      "005d8f18",
      "DATA",
      [
        "storage",
        "00c70de8",
        null,
        "undefined *"
      ]
    ],
    [
      "005d8f1c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d8f20",
      "DATA",
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

- 旧版 [`005b424c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4228.md#insn-005b424c) · [`005b4258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4228.md#insn-005b4258)
- 新版 [`005d8f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8ef4.md#insn-005d8f18)

~~~diff
- 005b424c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b424c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b424c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b424c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b424c bytes 082400a9
- 005b4258 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b4258 ["RETURN", null, ["register:0:8"]]
- 005b4258 bytes c0035fd6
+ 005d8f18 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005d8f18 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005d8f18 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005d8f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005d8f18 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93eaaabb9717d7ff594f9eb42e3cdfa2"></a>

### [`005b4f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f88.md) → [`005d9c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md) FUN_005d9c54

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 75.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4fa0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d9c6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005b4fac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b4fa0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b4fac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "005d9c6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d9c78",
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

- 旧版 [`005b4fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f88.md#insn-005b4fa0) · [`005b4fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b4/005b4f88.md#insn-005b4fac)
- 新版 [`005d9c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9c54.md#insn-005d9c6c)

~~~diff
- 005b4fa0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005b4fa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005b4fa0 bytes f30b00f9
- 005b4fac ["INT_ADD", "register:40f0:8", ["const:5b4fac:8", "const:4:8"]]
- 005b4fac ["CALL", null, ["ram:457e1c:8"]]
- 005b4fac bytes 9c8bfa97
+ 005d9c6c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
+ 005d9c6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 005d9c6c bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32058a0642f44aa296a7f9d387fdcb01"></a>

### [`005b51e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51e8.md) → [`005d9eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d9/005d9eb4.md) FUN_005d9eb4

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b520c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b5210"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005d9ed8"
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
      "unmatched:005b520c",
      "DATA",
      [
        "storage",
        "00bf3ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b5214",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b5218",
      "DATA",
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
      "005d9ed8",
      "DATA",
      [
        "storage",
        "00c70ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "005d9ee0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005d9ee4",
      "DATA",
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

- 旧版 [`005b520c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51e8.md#insn-005b520c) · [`005b5210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51e8.md#insn-005b5210) · [`005b521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b5/005b51e8.md#insn-005b521c)

~~~diff
- 005b520c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b520c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b520c bytes 080000f9
- 005b5210 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 005b5210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b5210 bytes 0080803c
- 005b521c ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b521c ["RETURN", null, ["register:0:8"]]
- 005b521c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35bcd5dfe56e8c5fbe7e8ac53f8b48e6"></a>

### [`005b6284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6284.md) → [`005daf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf50.md) FUN_005daf50

採用 · 移動量 `+0x24ccc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b629c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005daf68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005b62a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b629c",
      "DATA",
      [
        "storage",
        "00bf3f40",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b62a0",
      "DATA",
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
      "005daf68",
      "DATA",
      [
        "storage",
        "00c70f68",
        null,
        "undefined *"
      ]
    ],
    [
      "005daf6c",
      "DATA",
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

- 旧版 [`005b629c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6284.md#insn-005b629c) · [`005b62a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6284.md#insn-005b62a4)
- 新版 [`005daf68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005da/005daf50.md#insn-005daf68)

~~~diff
- 005b629c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b629c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b629c bytes 080000f9
- 005b62a4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b62a4 ["RETURN", null, ["register:0:8"]]
- 005b62a4 bytes c0035fd6
+ 005daf68 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 005daf68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 005daf68 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3aaf870973d44181916ace1acca778e"></a>

### [`005b6a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a94.md) → [`005db764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db764.md) FUN_005db764

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b6ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005db788"
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
      "unmatched:005b6ab8",
      "DATA",
      [
        "storage",
        "00bf41d0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b6abc",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b6ac0",
      "DATA",
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
      "005db788",
      "DATA",
      [
        "storage",
        "00c711f8",
        null,
        "undefined *"
      ]
    ],
    [
      "005db78c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005db790",
      "DATA",
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

- 旧版 [`005b6ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a94.md#insn-005b6ab8) · [`005b6ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b6/005b6a94.md#insn-005b6ac4)
- 新版 [`005db788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005db764.md#insn-005db788)

~~~diff
- 005b6ab8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b6ab8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b6ab8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b6ab8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b6ab8 bytes 082400a9
- 005b6ac4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b6ac4 ["RETURN", null, ["register:0:8"]]
- 005b6ac4 bytes c0035fd6
+ 005db788 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005db788 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005db788 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005db788 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005db788 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c104884da65b1a4d4a954429216db050"></a>

### [`005b7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7204.md) → [`005dbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005db/005dbed4.md) FUN_005dbed4

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7204"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7208"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b7204",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7208",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b722c",
      "DATA",
      [
        "storage",
        "00bf4350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dbed4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005dbed8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dbefc",
      "DATA",
      [
        "storage",
        "00c71378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7204.md#insn-005b7204) · [`005b7208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7204.md#insn-005b7208) · [`005b722c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7204.md#insn-005b722c)

~~~diff
- 005b7204 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b7204 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b7204 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005b7204 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b7204 bytes fd7bbea9
- 005b7208 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005b7208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005b7208 bytes f30b00f9
- 005b722c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b722c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b722c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe9d79c1e881b2c94b1e066910d8f9f6"></a>

### [`005b7380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7380.md) → [`005dc050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc050.md) FUN_005dc050

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b73a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b73a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005dc074"
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
      "unmatched:005b73a4",
      "DATA",
      [
        "storage",
        "00bf43e0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b73a8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b73ac",
      "DATA",
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
      "005dc074",
      "DATA",
      [
        "storage",
        "00c71408",
        null,
        "undefined *"
      ]
    ],
    [
      "005dc078",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dc07c",
      "DATA",
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

- 旧版 [`005b73a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7380.md#insn-005b73a4) · [`005b73b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7380.md#insn-005b73b0)
- 新版 [`005dc074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc050.md#insn-005dc074)

~~~diff
- 005b73a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b73a4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b73a4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b73a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b73a4 bytes 082400a9
- 005b73b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b73b0 ["RETURN", null, ["register:0:8"]]
- 005b73b0 bytes c0035fd6
+ 005dc074 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005dc074 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005dc074 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005dc074 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005dc074 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe46845ab5fb4ac6e9c1741582dc59fc"></a>

### [`005b7480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7480.md) → [`005dc150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc150.md) FUN_005dc150

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b74a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b74a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005dc174"
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
      "unmatched:005b74a4",
      "DATA",
      [
        "storage",
        "00bf4460",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005b74a8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b74ac",
      "DATA",
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
      "005dc174",
      "DATA",
      [
        "storage",
        "00c71488",
        null,
        "undefined *"
      ]
    ],
    [
      "005dc178",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dc17c",
      "DATA",
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

- 旧版 [`005b74a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7480.md#insn-005b74a4) · [`005b74b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7480.md#insn-005b74b0)
- 新版 [`005dc174`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc150.md#insn-005dc174)

~~~diff
- 005b74a4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b74a4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005b74a4 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005b74a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b74a4 bytes 082400a9
- 005b74b0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b74b0 ["RETURN", null, ["register:0:8"]]
- 005b74b0 bytes c0035fd6
+ 005dc174 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 005dc174 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 005dc174 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 005dc174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 005dc174 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b9d22a2f84daf986892b1c1a7fd5823"></a>

### [`005b75f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b75f0.md) → [`005dc2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2c0.md) FUN_005dc2c0

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005a7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a7/005a7dfc.md) [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0087d888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087d/0087d888.md) [`008a0d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a0/008a0d28.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`005ccac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005cc/005ccac8.md) [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`008b0a28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b0/008b0a28.md) [`008d4bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d4/008d4bc0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b75f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b75f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005dc2c0"
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
      "unmatched:005b75f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b75fc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005b7600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005dc2c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dc2cc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005dc2d0",
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

- 旧版 [`005b75f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b75f0.md#insn-005b75f0) · [`005b7600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b75f0.md#insn-005b7600)
- 新版 [`005dc2c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2c0.md#insn-005dc2c0)

~~~diff
- 005b75f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b75f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b75f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005b75f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b75f0 bytes fd7bbfa9
- 005b7600 ["INT_ADD", "register:40f0:8", ["const:5b7600:8", "const:4:8"]]
- 005b7600 ["CALL", null, ["ram:418c38:8"]]
- 005b7600 bytes 8e85f997
+ 005dc2c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005dc2c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005dc2c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005dc2c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005dc2c0 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e4a037106ece02259b11df2cfa3673"></a>

### [`005b760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b760c.md) → [`005dc2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc2dc.md) FUN_005dc2dc

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b760c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b760c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7610"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b760c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7610",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b7630",
      "DATA",
      [
        "storage",
        "00bf44e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dc2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005dc2e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005dc300",
      "DATA",
      [
        "storage",
        "00c71508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b760c.md#insn-005b760c) · [`005b7610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b760c.md#insn-005b7610) · [`005b7630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b760c.md#insn-005b7630)

~~~diff
- 005b760c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005b760c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005b760c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005b760c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005b760c bytes fd7bbea9
- 005b7610 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005b7610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005b7610 bytes f30b00f9
- 005b7630 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005b7630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b7630 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff8aba55a98e4fc5116c7fba53b35d83"></a>

### [`005b7644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7644.md) → [`005dc314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dc314.md) FUN_005dc314

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b764c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b7654"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005dc31c"
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
      "unmatched:005b764c",
      "DATA",
      [
        "storage",
        "00bf44e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005dc31c",
      "DATA",
      [
        "storage",
        "00c71508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005b764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7644.md#insn-005b764c) · [`005b7654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7644.md#insn-005b7654) · [`005b7658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7644.md#insn-005b7658)

~~~diff
- 005b764c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005b764c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005b764c bytes 280000f9
- 005b7654 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 005b7654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005b7654 bytes 2080803c
- 005b7658 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005b7658 ["RETURN", null, ["register:0:8"]]
- 005b7658 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1cc1d352a3e7f4f3b534bd0095fa5ab"></a>

### [`005b97a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md) → [`005de470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005de/005de470.md) FUN_005de470

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005b9118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b9118.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005b7d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b7/005b7d98.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005ddde8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dd/005ddde8.md) · 呼出先 5件 [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`005dca68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005dc/005dca68.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 44.12% / 新版 40.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b97b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b97b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005b97c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005b97b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b97c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:005b98d8",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005de480",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005de498",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "005de5a8",
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

- 旧版 [`005b97b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md#insn-005b97b0) · [`005b97c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md#insn-005b97c8) · [`005b98d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b9/005b97a0.md#insn-005b98d8)

~~~diff
- 005b97b0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005b97b0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005b97b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 005b97b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005b97b0 bytes f44f07a9
- 005b97c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005b97c8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005b97c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005b97c8 bytes a8831ff8
- 005b98d8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005b98d8 ["INT_ADD", "register:40f0:8", ["const:5b98d8:8", "const:4:8"]]
- 005b98d8 ["CALLIND", null, ["register:0:8"]]
- 005b98d8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c5ddb6278e9fdae547c33383012e83"></a>

### [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md) → [`005df58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df58c.md) FUN_005df58c

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`005ba3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md) [`005baabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md) [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 7件 [`005df094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df094.md) [`005df78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df78c.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.38% / 新版 75.38%

CFGの説明率　旧版 76.92% / 新版 47.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba8bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba8bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba8c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba8bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba8c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba8c4",
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
      "005df58c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005df590",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "005df594",
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

- 旧版 [`005ba8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md#insn-005ba8bc) · [`005ba8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md#insn-005ba8c0) · [`005ba8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba8bc.md#insn-005ba8c4)

~~~diff
- 005ba8bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ba8bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ba8bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 005ba8bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ba8bc bytes fd7bbba9
- 005ba8c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005ba8c0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005ba8c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ba8c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba8c0 bytes fa6701a9
- 005ba8c4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 005ba8c4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 005ba8c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ba8c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba8c4 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6316f6fdbefd5a5ae9f6d1cef7c0686"></a>

### [`005ba9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba9c0.md) → [`005df690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df690.md) FUN_005df690

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005ba3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba3c4.md) [`005baabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005baabc.md) [`005c47c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c4/005c47c4.md) [`009eae0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ea/009eae0c.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 4件 [`005df094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df094.md) [`005df78c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005df/005df78c.md) [`005e94b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e9/005e94b4.md) [`00a47d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a47/00a47d08.md) · 呼出先 3件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba9c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba9c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ba9c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ba9c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba9c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ba9c8",
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
      "005df690",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005df694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005df698",
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

- 旧版 [`005ba9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba9c0.md#insn-005ba9c0) · [`005ba9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba9c0.md#insn-005ba9c4) · [`005ba9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ba/005ba9c0.md#insn-005ba9c8)

~~~diff
- 005ba9c0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ba9c0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ba9c0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005ba9c0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ba9c0 bytes fd7bbda9
- 005ba9c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 005ba9c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 005ba9c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ba9c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba9c4 bytes f65701a9
- 005ba9c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005ba9c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005ba9c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ba9c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ba9c8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c202079396e5ab915e14b13c5a4e4504"></a>

### [`005bb3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3a8.md) → [`005e0078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md) FUN_005e0078

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb3ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb3a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb3ac",
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
      "005e0078",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e007c",
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

- 旧版 [`005bb3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3a8.md#insn-005bb3a8) · [`005bb3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb3a8.md#insn-005bb3ac)
- 新版 [`005e0078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0078.md#insn-005e0078)

~~~diff
- 005bb3a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bb3a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bb3a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005bb3a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bb3a8 bytes fd7bbea9
- 005bb3ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bb3ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bb3ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005bb3ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb3ac bytes f44f01a9
+ 005e0078 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005e0078 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005e0078 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005e0078 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005e0078 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4be1a39cc458b25c8914bb3f7f51a12"></a>

### [`005bb454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb454.md) → [`005e0124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0124.md) FUN_005e0124

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bb458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bb454",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bb458",
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
      "005e0124",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e0128",
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

- 旧版 [`005bb454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb454.md#insn-005bb454) · [`005bb458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb454.md#insn-005bb458) · [`005bb494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb454.md#insn-005bb494)

~~~diff
- 005bb454 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bb454 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bb454 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005bb454 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bb454 bytes fd7bbea9
- 005bb458 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005bb458 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005bb458 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005bb458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005bb458 bytes f44f01a9
- 005bb494 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005bb494 ["RETURN", null, ["register:0:8"]]
- 005bb494 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6d1fd6208b5ffe593d11f68fd464dd9"></a>

### [`005bb4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb4ec.md) → [`005e01bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md) FUN_005e01bc

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009bd6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd6c4.md) · 呼出先 1件 [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md)
- 新版 呼出元 1件 [`00a1a5b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a5b4.md) · 呼出先 1件 [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005e01dc",
      "incomplete_value": true,
      "site": "005e01e8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "005bb520",
      "incomplete_value": true,
      "site": "005bb524",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005bb518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb4ec.md#insn-005bb518) · [`005bb524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb4ec.md#insn-005bb524) · [`005bb504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bb/005bb4ec.md#insn-005bb504)
- 新版 [`005e01e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01e8) · [`005e01f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01f4) · [`005e01d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e01bc.md#insn-005e01d4)

~~~diff
- 005bb518 ["INT_ADD", "register:40f0:8", ["const:5bb518:8", "const:4:8"]]
- 005bb518 ["CALL", null, ["callee:004803b0:8"]]
+ 005e01e8 ["INT_ADD", "register:40f0:8", ["const:5e01e8:8", "const:4:8"]]
+ 005e01e8 ["CALL", null, ["callee:004803b0:8"]]
- 005bb518 bytes 0088fa97
+ 005e01e8 bytes 7280fa97
- 005bb524 ["INT_ADD", "register:40f0:8", ["const:5bb524:8", "const:4:8"]]
- 005bb524 ["CALL", null, ["callee:004803b0:8"]]
+ 005e01f4 ["INT_ADD", "register:40f0:8", ["const:5e01f4:8", "const:4:8"]]
+ 005e01f4 ["CALL", null, ["callee:004803b0:8"]]
- 005bb524 bytes fd87fa97
+ 005e01f4 bytes 6f80fa97
- 005bb504 ["INT_ADD", "register:40f0:8", ["const:5bb504:8", "const:4:8"]]
- 005bb504 ["CALL", null, ["callee:004803b0:8"]]
+ 005e01d4 ["INT_ADD", "register:40f0:8", ["const:5e01d4:8", "const:4:8"]]
+ 005e01d4 ["CALL", null, ["callee:004803b0:8"]]
- 005bb504 bytes 0588fa97
+ 005e01d4 bytes 7780fa97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77b6f56eab6473023814fb5f714194c8"></a>

### [`005bdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md) → [`005e29ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e29ec.md) FUN_005e29ec

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 24件 [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 4件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 24件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 4件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bdd1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bdd1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bdd70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bdd1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bdd2c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:005bdd30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005bdd44"
      ]
    ]
  ],
  "added": [
    [
      "005e29ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005e29fc",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "005e2a00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005e2a14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md#insn-005bdd1c) · [`005bdd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md#insn-005bdd30) · [`005bdd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd1c.md#insn-005bdd40)

~~~diff
- 005bdd1c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005bdd1c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005bdd1c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005bdd1c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005bdd1c bytes fd7bbfa9
- 005bdd30 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 005bdd30 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 005bdd30 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 005bdd30 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 005bdd30 bytes a8000036
- 005bdd40 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005bdd40 ["RETURN", null, ["register:0:8"]]
- 005bdd40 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b0ababa6c1af75d10e0ed3346745c2a"></a>

### [`005bdd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd9c.md) → [`005e2a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md) FUN_005e2a6c

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 21件 [`005be404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005be/005be404.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 21件 [`005e30d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e3/005e30d4.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call, call_count, constant, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005bdddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005e2aac"
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
      "unmatched:005bdddc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005e2aac",
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

- 旧版 [`005bdddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd9c.md#insn-005bdddc) · [`005bddc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bdd9c.md#insn-005bddc8)
- 新版 [`005e2aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md#insn-005e2aac) · [`005e2a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2a6c.md#insn-005e2a98)

~~~diff
- 005bdddc ["COPY", "register:0:8", ["register:4040:8"]]
- 005bdddc ["INT_ADD", "register:40f0:8", ["const:5bdddc:8", "const:4:8"]]
- 005bdddc ["CALLIND", null, ["register:0:8"]]
- 005bdddc bytes 00013fd6
+ 005e2aac ["COPY", "register:0:8", ["register:4040:8"]]
+ 005e2aac ["INT_ADD", "register:40f0:8", ["const:5e2aac:8", "const:4:8"]]
+ 005e2aac ["CALLIND", null, ["register:0:8"]]
+ 005e2aac bytes 00013fd6
- 005bddc8 ["INT_ADD", "register:40f0:8", ["const:5bddc8:8", "const:4:8"]]
- 005bddc8 ["CALL", null, ["callee:00c538e0:8"]]
+ 005e2a98 ["INT_ADD", "register:40f0:8", ["const:5e2a98:8", "const:4:8"]]
+ 005e2a98 ["CALL", null, ["callee:00c538e0:8"]]
- 005bddc8 bytes 32641894
+ 005e2a98 bytes 92c31994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04e682aebbede982fbb690dd8eaa68cd"></a>

### [`005bde34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bde34.md) → [`005e2b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e2/005e2b04.md) FUN_005e2b04

採用 · 移動量 `+0x24cd0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`009f46cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f46cc.md) · 呼出先 2件 [`005c0264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c0264.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 4件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) [`007154c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007154c0.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`00a519e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a519e0.md) · 呼出先 2件 [`005e4f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e4/005e4f34.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.33% / 新版 73.33%

CFGの説明率　旧版 30.77% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bde50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bde54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005bdea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005bde50",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bde54",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:005bde78",
      "PARAM",
      [
        "storage",
        "002b6fa5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005e2b20",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "005e2b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "005e2b48",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005bde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bde34.md#insn-005bde50) · [`005bde54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bde34.md#insn-005bde54) · [`005bdea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bd/005bde34.md#insn-005bdea0)

~~~diff
- 005bde50 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005bde50 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 005bde50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 005bde50 bytes a8831ff8
- 005bde54 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 005bde54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4018:4"]]
- 005bde54 bytes e30b00b9
- 005bdea0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005bdea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 005bdea0 bytes e90b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c41521f2503487fccf268b38719304d"></a>

### [`005c03a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c03a8.md) → [`005e5078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md) FUN_005e5078

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044b9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b9cc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046e864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e864.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 14.29% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c03a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c03a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c03ac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c03a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c03ac",
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
      "005e5078",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e507c",
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

- 旧版 [`005c03a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c03a8.md#insn-005c03a8) · [`005c03ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c0/005c03a8.md#insn-005c03ac)
- 新版 [`005e5078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e5/005e5078.md#insn-005e5078)

~~~diff
- 005c03a8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c03a8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c03a8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005c03a8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c03a8 bytes fd7bbea9
- 005c03ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c03ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005c03ac bytes f30b00f9
+ 005e5078 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005e5078 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005e5078 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005e5078 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005e5078 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd0183e4d2be6c8fe434c634b273714f"></a>

### [`005c20b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20b0.md) → [`005e6d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6d80.md) FUN_005e6d80

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`005c20ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20ec.md)
- 新版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 1件 [`005e6dbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6dbc.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 77.78% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c20e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005c20ec"
      ]
    ]
  ],
  "added": [
    [
      "005e6db4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e6dbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c20b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20b0.md#insn-005c20b4) · [`005c20bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20b0.md#insn-005c20bc) · [`005c20c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c20b0.md#insn-005c20c4)
- 新版 [`005e6d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6d80.md#insn-005e6d84) · [`005e6d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6d80.md#insn-005e6d8c) · [`005e6d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e6/005e6d80.md#insn-005e6d94)

~~~diff
- 005c20b4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c20b4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005e6d84 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005e6d84 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005c20b4 bytes a80100b4
+ 005e6d84 bytes a80100b4
- 005c20bc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005c20bc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005e6d8c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 005e6d8c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005c20bc bytes 680100b4
+ 005e6d8c bytes 680100b4
- 005c20c4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 005c20c4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005e6d94 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 005e6d94 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005c20c4 bytes 28010034
+ 005e6d94 bytes 28010034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99803befbfa0cb017decb541a96e60ae"></a>

### [`005c2aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2aa0.md) → [`005e7770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7770.md) FUN_005e7770

採用 · 移動量 `+0x24cd0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005d2408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d2/005d2408.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006ee6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ee/006ee6c8.md) · 呼出先 1件 [`0058b674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058b/0058b674.md)
- 新版 呼出元 3件 [`005f70f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f7/005f70f0.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00718734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00718/00718734.md) · 呼出先 1件 [`005afc38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005af/005afc38.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 74.42% / 新版 74.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2b28"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "005e77f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ab8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c2ab8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058b674"
      ]
    ],
    [
      "unmatched:005c2ac4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058b674"
      ]
    ],
    [
      "unmatched:005c2ad0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0058b674"
      ]
    ]
  ],
  "added": [
    [
      "005e7788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005afc38"
      ]
    ],
    [
      "005e7794",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005afc38"
      ]
    ],
    [
      "005e77a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005afc38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c2ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2aa0.md#insn-005c2ab8) · [`005c2ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2aa0.md#insn-005c2ac4) · [`005c2ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2aa0.md#insn-005c2ad0)

~~~diff
- 005c2ab8 ["INT_ADD", "register:40f0:8", ["const:5c2ab8:8", "const:4:8"]]
- 005c2ab8 ["CALL", null, ["ram:58b674:8"]]
- 005c2ab8 bytes ef22ff97
- 005c2ac4 ["INT_ADD", "register:40f0:8", ["const:5c2ac4:8", "const:4:8"]]
- 005c2ac4 ["CALL", null, ["ram:58b674:8"]]
- 005c2ac4 bytes ec22ff97
- 005c2ad0 ["INT_ADD", "register:40f0:8", ["const:5c2ad0:8", "const:4:8"]]
- 005c2ad0 ["CALL", null, ["ram:58b674:8"]]
- 005c2ad0 bytes e922ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42d3af95e055991630f3ab723a73cd5e"></a>

### [`005c2ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md) → [`005e7b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7b90.md) FUN_005e7b90

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`005c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f88.md)
- 新版 呼出元 1件 [`00a4f1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a4f/00a4f1bc.md) · 呼出先 3件 [`005e0eac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0eac.md) [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md)

変更の種類 branch_condition_or_target, call, call_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005c2ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c2ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005c2ec8",
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
      "005e7b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "005e7b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005e7b98",
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

- 旧版 [`005c2ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md#insn-005c2ec0) · [`005c2ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md#insn-005c2ec4) · [`005c2ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2ec0.md#insn-005c2ec8)

~~~diff
- 005c2ec0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005c2ec0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005c2ec0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 005c2ec0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005c2ec0 bytes fd7bbda9
- 005c2ec4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005c2ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 005c2ec4 bytes f50b00f9
- 005c2ec8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 005c2ec8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 005c2ec8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005c2ec8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005c2ec8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b075f6074e24a4fc382b03b8865a1b29"></a>

### [`005c2f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f30.md) → [`005e7c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c00.md) FUN_005e7c00

採用 · 移動量 `+0x24cd0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009f4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f4/009f4ab8.md) [`00aa05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa05ac.md) · 呼出先 2件 [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`005c2f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f88.md)
- 新版 呼出元 2件 [`00a51dcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a51/00a51dcc.md) [`00affc2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aff/00affc2c.md) · 呼出先 2件 [`005e1af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1af0.md) [`005e7c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c58.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005c2f50"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005e7c20"
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
      "unmatched:005c2f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005bce20"
      ]
    ]
  ],
  "added": [
    [
      "005e7c20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "005e1af0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005c2f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f30.md#insn-005c2f50) · [`005c2f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f30.md#insn-005c2f3c)
- 新版 [`005e7c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c00.md#insn-005e7c20) · [`005e7c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e7/005e7c00.md#insn-005e7c0c)

~~~diff
- 005c2f50 ["INT_ADD", "register:40f0:8", ["const:5c2f50:8", "const:4:8"]]
- 005c2f50 ["CALL", null, ["ram:5bce20:8"]]
- 005c2f50 bytes b4e7ff97
+ 005e7c20 ["INT_ADD", "register:40f0:8", ["const:5e7c20:8", "const:4:8"]]
+ 005e7c20 ["CALL", null, ["ram:5e1af0:8"]]
+ 005e7c20 bytes b4e7ff97
- 005c2f3c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:4", "const:0:4"]]
- 005c2f3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 005e7c0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:4", "const:0:4"]]
+ 005e7c0c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 005c2f3c bytes 21010035
+ 005e7c0c bytes 21010035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fee5a9091353c5ae05dfb2cf1349ef78"></a>

### [`005cb46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb46c.md) → [`005f0158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0158.md) FUN_005f0158

採用 · 移動量 `+0x24cec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005cb23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb23c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`005eff28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005eff28.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cb46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cb46c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005f0158"
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
      "unmatched:005cb46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005cb478",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005cb47c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "005f0158",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005f0164",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005f0168",
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

- 旧版 [`005cb46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb46c.md#insn-005cb46c) · [`005cb47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cb46c.md#insn-005cb47c)
- 新版 [`005f0158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0158.md#insn-005f0158)

~~~diff
- 005cb46c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005cb46c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005cb46c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005cb46c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005cb46c bytes fd7bbfa9
- 005cb47c ["INT_ADD", "register:40f0:8", ["const:5cb47c:8", "const:4:8"]]
- 005cb47c ["CALL", null, ["ram:418c38:8"]]
- 005cb47c bytes ef35f997
+ 005f0158 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005f0158 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005f0158 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005f0158 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005f0158 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67c386a6ba33f9e2de268b714b47bd92"></a>

### [`005cbea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbea4.md) → [`005f0b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0b90.md) FUN_005f0b90

採用 · 移動量 `+0x24cec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005c8d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c8/005c8d50.md) [`005c98a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c9/005c98a4.md) [`005ca880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ca/005ca880.md) [`005cbd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbd78.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 4件 [`005eda3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ed/005eda3c.md) [`005ee590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ee/005ee590.md) [`005ef56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ef/005ef56c.md) [`005f0a64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0a64.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 83.08% / 新版 83.08%

CFGの説明率　旧版 22.22% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cbee0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cbef0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cbf20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cbee4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005f0be0"
      ]
    ],
    [
      "unmatched:005cbef0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f0c74"
      ]
    ],
    [
      "unmatched:005cbf44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005cbee8"
      ]
    ]
  ],
  "added": [
    [
      "005f0bd0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005f0be0"
      ]
    ],
    [
      "005f0bdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f0c74"
      ]
    ],
    [
      "005f0c30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f0bd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cbee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbea4.md#insn-005cbee0) · [`005cbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbea4.md#insn-005cbef0) · [`005cbf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbea4.md#insn-005cbf20)

~~~diff
- 005cbee0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 005cbee0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005cbee0 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 005cbee0 ["COPY", "register:40c8:8", ["tmp:0:8"]]
- 005cbee0 bytes 59018b9a
- 005cbef0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 005cbef0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 005cbef0 bytes c80400b4
- 005cbf20 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 005cbf20 ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 005cbf20 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005cbf20 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005cbf20 bytes 5733999a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74b75938372fb68cda075fd00564f6d5"></a>

### [`005cbfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbfa8.md) → [`005f0c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md) FUN_005f0c94

採用 · 移動量 `+0x24cec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 12.50% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005cbfec"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "005f0cd8"
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
      "unmatched:005cbfec",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "005f0cd8",
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

- 旧版 [`005cbfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbfa8.md#insn-005cbfec) · [`005cbfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cb/005cbfa8.md#insn-005cbfbc)
- 新版 [`005f0cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md#insn-005f0cd8) · [`005f0ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0c94.md#insn-005f0ca8)

~~~diff
- 005cbfec ["COPY", "register:0:8", ["register:4040:8"]]
- 005cbfec ["INT_ADD", "register:40f0:8", ["const:5cbfec:8", "const:4:8"]]
- 005cbfec ["CALLIND", null, ["register:0:8"]]
- 005cbfec bytes 00013fd6
+ 005f0cd8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 005f0cd8 ["INT_ADD", "register:40f0:8", ["const:5f0cd8:8", "const:4:8"]]
+ 005f0cd8 ["CALLIND", null, ["register:0:8"]]
+ 005f0cd8 bytes 00013fd6
- 005cbfbc ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005cbfbc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 005f0ca8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005f0ca8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 005cbfbc bytes f30200b4
+ 005f0ca8 bytes f30200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47fb94783099e2c6d65c989888b5ad1e"></a>

### [`005cc1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc1d0.md) → [`005f0ebc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md) FUN_005f0ebc

採用 · 移動量 `+0x24cec` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0046ef9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ef9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005cc220"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "005f0f0c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005cc220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc1d0.md#insn-005cc220) · [`005cc1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005cc1d0.md#insn-005cc1e4)
- 新版 [`005f0f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md#insn-005f0f0c) · [`005f0ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f0/005f0ebc.md#insn-005f0ed0)

~~~diff
- 005cc220 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005cc220 ["RETURN", null, ["register:0:8"]]
- 005cc220 bytes c0035fd6
+ 005f0f0c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 005f0f0c ["RETURN", null, ["register:0:8"]]
+ 005f0f0c bytes c0035fd6
- 005cc1e4 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 005cc1e4 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 005f0ed0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 005f0ed0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 005cc1e4 bytes b30100b4
+ 005f0ed0 bytes b30100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb5891a9319d17f46d65fc831c8384d8"></a>

### [`005ccfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005ccfb8.md) → [`005f1ca4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1ca4.md) FUN_005f1ca4

採用 · 移動量 `+0x24cec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccfb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccfb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005ccfbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005ccfb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ccfbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:005ccfc0",
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
      "005f1ca4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "005f1ca8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "005f1cac",
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

- 旧版 [`005ccfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005ccfb8.md#insn-005ccfb8) · [`005ccfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005ccfb8.md#insn-005ccfbc) · [`005ccfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cc/005ccfb8.md#insn-005ccfc0)

~~~diff
- 005ccfb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005ccfb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005ccfb8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 005ccfb8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005ccfb8 bytes fd7bbaa9
- 005ccfbc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 005ccfbc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 005ccfbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 005ccfbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ccfbc bytes fc6f01a9
- 005ccfc0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 005ccfc0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 005ccfc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 005ccfc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005ccfc0 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-888bf1e9b56450c5522fe2fe78889537"></a>

### [`005cd2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd2d4.md) → [`005f1fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f1/005f1fc0.md) FUN_005f1fc0

採用 · 移動量 `+0x24cec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 73.13% / 新版 73.13%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd32c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd358"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd39c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd320",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005f201c"
      ]
    ],
    [
      "unmatched:005cd32c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f20b0"
      ]
    ],
    [
      "005f2024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005cd324"
      ]
    ]
  ],
  "added": [
    [
      "005f200c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005f201c"
      ]
    ],
    [
      "005f2018",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f20b0"
      ]
    ],
    [
      "005f2024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f2010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd32c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd2d4.md#insn-005cd32c) · [`005cd358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd2d4.md#insn-005cd358) · [`005cd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd2d4.md#insn-005cd360)

~~~diff
- 005cd32c ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 005cd32c bytes c0040054
- 005cd358 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 005cd358 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 005cd358 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005cd358 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 005cd358 bytes 2801889a
- 005cd360 ["INT_ADD", "register:40f0:8", ["const:5cd360:8", "const:4:8"]]
- 005cd360 ["CALL", null, ["callee:00470074:8"]]
- 005cd360 bytes 9ffff997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78b338089324e169c2ef9b8aef223da6"></a>

### [`005cd500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd500.md) → [`005f21ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f21ec.md) FUN_005f21ec

採用 · 移動量 `+0x24cec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) · 呼出先 4件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00707ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707ea0.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 68.12% / 新版 68.12%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd538"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd5b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005cd5f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005cd52c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467820"
      ]
    ],
    [
      "unmatched:005cd538",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f22e4"
      ]
    ],
    [
      "unmatched:005cd5a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ]
  ],
  "added": [
    [
      "005f2218",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00467820"
      ]
    ],
    [
      "005f2224",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f22e4"
      ]
    ],
    [
      "005f228c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cd52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd500.md#insn-005cd52c) · [`005cd538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd500.md#insn-005cd538) · [`005cd5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cd500.md#insn-005cd5a0)

~~~diff
- 005cd52c ["INT_ADD", "register:40f0:8", ["const:5cd52c:8", "const:4:8"]]
- 005cd52c ["CALL", null, ["callee:00467820:8"]]
- 005cd52c bytes 17ddf997
- 005cd538 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 005cd538 bytes 00060054
- 005cd5a0 ["INT_ADD", "register:40f0:8", ["const:5cd5a0:8", "const:4:8"]]
- 005cd5a0 ["CALL", null, ["ram:449aec:8"]]
- 005cd5a0 bytes 53f1f997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221950a3a74f3ff69be7ff98626219c7"></a>

### [`005cda6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cda6c.md) → [`005f2758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f2/005f2758.md) FUN_005f2758

採用 · 移動量 `+0x24cec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 4件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459f04.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 4件 [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd9c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.84% / 新版 43.84%

CFGの説明率　旧版 12.50% / 新版 13.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdab4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005cdb68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005f27a0"
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
      "unmatched:005cda9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f2864"
      ]
    ],
    [
      "unmatched:005cdab0",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005cdac4"
      ]
    ],
    [
      "unmatched:005cdac0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f2864"
      ]
    ]
  ],
  "added": [
    [
      "005f2788",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f2864"
      ]
    ],
    [
      "005f279c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "005f27b0"
      ]
    ],
    [
      "005f27ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f2864"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005cda9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cda6c.md#insn-005cda9c) · [`005cdab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cda6c.md#insn-005cdab4) · [`005cdac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005cd/005cda6c.md#insn-005cdac0)

~~~diff
- 005cda9c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005cda9c ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 005cda9c bytes eb060054
- 005cdab4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e30:8"]]
- 005cdab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 005cdab4 bytes 991a07f9
- 005cdac0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005cdac0 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 005cdac0 ["CBRANCH", null, ["local:b22:8", "tmp:1:1"]]
- 005cdac0 bytes cd050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d75484bd8a70a50b097a4574f974302f"></a>

### [`005d1bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1bb4.md) → [`005f689c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f6/005f689c.md) FUN_005f689c

採用 · 移動量 `+0x24ce8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d0a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d0/005d0a68.md) [`007c80a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c8/007c80a0.md) [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 3件 [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00448040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 3件 [`005f5750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f5/005f5750.md) [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) · 呼出先 3件 [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aed8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aed8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 9.38% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1dec"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005d1e14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005f68e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:005d1e0c"
      ]
    ],
    [
      "unmatched:005d1dec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f6be0"
      ]
    ],
    [
      "unmatched:005d1e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f6ac8"
      ]
    ]
  ],
  "added": [
    [
      "005f68e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f6af4"
      ]
    ],
    [
      "005f6ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f6be0"
      ]
    ],
    [
      "005f6afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "005f6ac8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005d1c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1bb4.md#insn-005d1c84) · [`005d1dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1bb4.md#insn-005d1dec) · [`005d1e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d1/005d1bb4.md#insn-005d1e08)

~~~diff
- 005d1c84 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 005d1c84 ["COPY", "tmp:1:4", ["register:4050:4"]]
- 005d1c84 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 005d1c84 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 005d1c84 bytes 49b1891a
- 005d1dec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005d1dec ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 005d1dec bytes 61080054
- 005d1e08 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005d1e08 ["RETURN", null, ["register:0:8"]]
- 005d1e08 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b287a18f684030246fa8892c9a242329"></a>

### [`005d47e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d47e4.md) → [`005f94cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f94cc.md) FUN_005f94cc

採用 · 移動量 `+0x24ce8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) · 呼出先 2件 [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d47e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d47e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d47e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005d47e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d47e8",
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
      "005f94cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "005f94d0",
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

- 旧版 [`005d47e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d47e4.md#insn-005d47e4) · [`005d47e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d47e4.md#insn-005d47e8)
- 新版 [`005f94cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f94cc.md#insn-005f94cc)

~~~diff
- 005d47e4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d47e4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d47e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005d47e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d47e4 bytes fd7bbea9
- 005d47e8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005d47e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005d47e8 bytes f30b00f9
+ 005f94cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005f94cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005f94cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 005f94cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005f94cc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d38fa405efe2fd8ef7d12f4b63993878"></a>

### [`005d9548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9548.md) → [`005fe208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md) FUN_005fe208

採用 · 移動量 `+0x24cc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005d3af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d3/005d3af8.md) [`005d3f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d3/005d3f6c.md) [`005d4158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4158.md) [`006e92bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e92bc.md) [`006ea1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006ea1c0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 8件 [`005f87e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f87e0.md) [`005f8c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8c54.md) [`005f8e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f8/005f8e40.md) [`00713318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00713/00713318.md) [`0071421c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00714/0071421c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9548"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9548"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005fe208"
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
      "unmatched:005d9548",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d9554",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005d9558",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "005fe208",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005fe214",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005fe218",
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

- 旧版 [`005d9548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9548.md#insn-005d9548) · [`005d9558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9548.md#insn-005d9558)
- 新版 [`005fe208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe208.md#insn-005fe208)

~~~diff
- 005d9548 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d9548 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d9548 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005d9548 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d9548 bytes fd7bbfa9
- 005d9558 ["INT_ADD", "register:40f0:8", ["const:5d9558:8", "const:4:8"]]
- 005d9558 ["CALL", null, ["ram:41fdf0:8"]]
- 005d9558 bytes 261af997
+ 005fe208 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005fe208 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005fe208 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005fe208 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005fe208 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dd2296e500d980dcef6bbcb6cb958ad"></a>

### [`005d9570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9570.md) → [`005fe230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe230.md) FUN_005fe230

採用 · 移動量 `+0x24cc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`005d4824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4824.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`005f950c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f950c.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9570"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005fe230"
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
      "unmatched:005d9570",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d957c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005d9580",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "005fe230",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005fe23c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005fe240",
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

- 旧版 [`005d9570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9570.md#insn-005d9570) · [`005d9580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9570.md#insn-005d9580)
- 新版 [`005fe230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe230.md#insn-005fe230)

~~~diff
- 005d9570 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d9570 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d9570 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005d9570 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d9570 bytes fd7bbfa9
- 005d9580 ["INT_ADD", "register:40f0:8", ["const:5d9580:8", "const:4:8"]]
- 005d9580 ["CALL", null, ["ram:41fdf0:8"]]
- 005d9580 bytes 1c1af997
+ 005fe230 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005fe230 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005fe230 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005fe230 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005fe230 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b66913fbe344f2bf9ec299406225e424"></a>

### [`005d9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9584.md) → [`005fe244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md) FUN_005fe244

採用 · 移動量 `+0x24cc0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d4988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d4/005d4988.md) [`005d57d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d5/005d57d0.md) [`006eb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb364.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`005f9670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005f9/005f9670.md) [`005fa4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fa/005fa4b8.md) [`007153c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00715/007153c0.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005d9584"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "005fe244"
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
      "unmatched:005d9584",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005d9590",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:005d9594",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "005fe244",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "005fe250",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "005fe254",
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

- 旧版 [`005d9584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9584.md#insn-005d9584) · [`005d9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d9584.md#insn-005d9594)
- 新版 [`005fe244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe244.md#insn-005fe244)

~~~diff
- 005d9584 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005d9584 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005d9584 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 005d9584 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005d9584 bytes fd7bbfa9
- 005d9594 ["INT_ADD", "register:40f0:8", ["const:5d9594:8", "const:4:8"]]
- 005d9594 ["CALL", null, ["ram:41fdf0:8"]]
- 005d9594 bytes 171af997
+ 005fe244 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 005fe244 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 005fe244 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 005fe244 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 005fe244 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b9610dde7a15b900b06f3ee35b6abb"></a>

### [`005dfd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfd24.md) → [`00604c88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md) FUN_00604c88

採用 · 移動量 `+0x24f64` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 3件 [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005dfdc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00604d24"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`005dfdc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfd24.md#insn-005dfdc0) · [`005dfd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005df/005dfd24.md#insn-005dfd48)
- 新版 [`00604d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md#insn-00604d24) · [`00604cac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00604/00604c88.md#insn-00604cac)

~~~diff
- 005dfdc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:28:8"]]
- 005dfdc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005dfdc0 bytes 881600f9
+ 00604d24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:28:8"]]
+ 00604d24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00604d24 bytes 881600f9
- 005dfd48 ["INT_ADD", "register:40f0:8", ["const:5dfd48:8", "const:4:8"]]
- 005dfd48 ["CALL", null, ["callee:00c57be0:8"]]
+ 00604cac ["INT_ADD", "register:40f0:8", ["const:604cac:8", "const:4:8"]]
+ 00604cac ["CALL", null, ["callee:00c57be0:8"]]
- 005dfd48 bytes 12ed1794
+ 00604cac bytes cd4b1994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-984cbb0823ced413625bd41d79584cb1"></a>

### [`005f0304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0304.md) → [`00615b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615b44.md) FUN_00615b44

採用 · 移動量 `+0x25840` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 1件 [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 2件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 1件 [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)

変更の種類 call, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 16.67% / 新版 16.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "005f0310"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00615b50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005f0318"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005f0310",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a430"
      ]
    ],
    [
      "unmatched:005f0314",
      "DATA",
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
      "00615b50",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5a430"
      ]
    ],
    [
      "00615b54",
      "DATA",
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

- 旧版 [`005f0310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0304.md#insn-005f0310) · [`005f0318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0304.md#insn-005f0318)
- 新版 [`00615b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615b44.md#insn-00615b50)

~~~diff
- 005f0310 ["INT_ADD", "register:40f0:8", ["const:5f0310:8", "const:4:8"]]
- 005f0310 ["CALL", null, ["callee:00c5a430:8"]]
- 005f0310 bytes b4b51794
- 005f0318 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005f0318 ["RETURN", null, ["register:0:8"]]
- 005f0318 bytes c0035fd6
+ 00615b50 ["INT_ADD", "register:40f0:8", ["const:615b50:8", "const:4:8"]]
+ 00615b50 ["CALL", null, ["callee:00c5a430:8"]]
+ 00615b50 bytes 38121994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59a6253d251bfadddb0b5199851fd9bd"></a>

### [`005f05dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f05dc.md) → [`00615e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e1c.md) FUN_00615e1c

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 50.00% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "005f05f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00615e34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "005f0648"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005f05f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00615e50"
      ]
    ]
  ],
  "added": [
    [
      "00615e34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00615e50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f05f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f05dc.md#insn-005f05f4) · [`005f0648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f05dc.md#insn-005f0648)
- 新版 [`00615e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615e1c.md#insn-00615e34)

~~~diff
- 005f05f4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 005f05f4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 005f05f4 bytes e1000054
- 005f0648 ["COPY", "register:0:8", ["register:40f0:8"]]
- 005f0648 ["RETURN", null, ["register:0:8"]]
- 005f0648 bytes c0035fd6
+ 00615e34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00615e34 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00615e34 bytes e1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ebd3cb0c339dc6951e0dca8b9675c9e"></a>

### [`005f0e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e74.md) → [`006166b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166b4.md) FUN_006166b4

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f0e7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006166bc"
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
      "unmatched:005f0e7c",
      "DATA",
      [
        "storage",
        "00bf4600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006166bc",
      "DATA",
      [
        "storage",
        "00c71628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f0e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e74.md#insn-005f0e7c) · [`005f0e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0e74.md#insn-005f0e74)
- 新版 [`006166bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006166b4.md#insn-006166bc)

~~~diff
- 005f0e7c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005f0e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f0e7c bytes 280000f9
+ 006166bc ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 006166bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006166bc bytes 280000f9
- 005f0e74 ["COPY", "register:4040:8", ["const:bf4000:8"]]
- 005f0e74 bytes 28300090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9193d0b7da147dba4e486fe54d4e2779"></a>

### [`005f1068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1068.md) → [`006168a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md) FUN_006168a8

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006168d0"
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
      "unmatched:005f1090",
      "DATA",
      [
        "storage",
        "00bf4670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006168d0",
      "DATA",
      [
        "storage",
        "00c71698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1068.md#insn-005f1090) · [`005f107c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1068.md#insn-005f107c)
- 新版 [`006168d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md#insn-006168d0) · [`006168bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168a8.md#insn-006168bc)

~~~diff
- 005f1090 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005f1090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f1090 bytes 080000f9
+ 006168d0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006168d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006168d0 bytes 080000f9
- 005f107c ["INT_ADD", "register:40f0:8", ["const:5f107c:8", "const:4:8"]]
- 005f107c ["CALL", null, ["callee:00c57a90:8"]]
+ 006168bc ["INT_ADD", "register:40f0:8", ["const:6168bc:8", "const:4:8"]]
+ 006168bc ["CALL", null, ["callee:00c57a90:8"]]
- 005f107c bytes f1a71794
+ 006168bc bytes 75041994
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c86e90f85f6871ebc2bec59933bdeee"></a>

### [`005f10a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10a8.md) → [`006168e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/006168e8.md) FUN_006168e8

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f10b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f10bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f10c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005f10b0",
      "DATA",
      [
        "storage",
        "00bf4670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006168f0",
      "DATA",
      [
        "storage",
        "00c71698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f10b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10a8.md#insn-005f10b0) · [`005f10bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10a8.md#insn-005f10bc) · [`005f10c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f10a8.md#insn-005f10c0)

~~~diff
- 005f10b0 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 005f10b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f10b0 bytes 280000f9
- 005f10bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:18:8"]]
- 005f10bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f10bc bytes 280c00f9
- 005f10c0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 005f10c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 005f10c0 bytes 2080803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99bbe2c7d73102e4b14569a697589cf2"></a>

### [`005f1684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1684.md) → [`00616ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00616/00616ec4.md) FUN_00616ec4

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 35.71% / 新版 35.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1684"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1688"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:005f1684",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:005f1688",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005f16a8",
      "DATA",
      [
        "storage",
        "00bf4760",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00616ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00616ec8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00616ee8",
      "DATA",
      [
        "storage",
        "00c71788",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f1684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1684.md#insn-005f1684) · [`005f1688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1684.md#insn-005f1688) · [`005f16a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f1684.md#insn-005f16a8)

~~~diff
- 005f1684 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 005f1684 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 005f1684 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 005f1684 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 005f1684 bytes fd7bbea9
- 005f1688 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 005f1688 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 005f1688 bytes f30b00f9
- 005f16a8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005f16a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f16a8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69c93370b7d931ffd0f2acd658e08d3a"></a>

### [`005f17dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17dc.md) → [`0061701c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061701c.md) FUN_0061701c

採用 · 移動量 `+0x25840` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f1800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00617040"
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
      "unmatched:005f1800",
      "DATA",
      [
        "storage",
        "00bf48a0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:005f1804",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:005f1808",
      "DATA",
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
      "00617040",
      "DATA",
      [
        "storage",
        "00c718c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00617044",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00617048",
      "DATA",
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

- 旧版 [`005f1800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17dc.md#insn-005f1800) · [`005f180c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f1/005f17dc.md#insn-005f180c)
- 新版 [`00617040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00617/0061701c.md#insn-00617040)

~~~diff
- 005f1800 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 005f1800 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 005f1800 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 005f1800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 005f1800 bytes 082400a9
- 005f180c ["COPY", "register:0:8", ["register:40f0:8"]]
- 005f180c ["RETURN", null, ["register:0:8"]]
- 005f180c bytes c0035fd6
+ 00617040 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00617040 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00617040 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00617040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00617040 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0827c780dbce947a5e1dcc97139ff41"></a>

### [`005f47e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f47e4.md) → [`0061a034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md) FUN_0061a034

採用 · 移動量 `+0x25850` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "005f4808"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0061a058"
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
      "unmatched:005f4808",
      "DATA",
      [
        "storage",
        "00bf4a00",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0061a058",
      "DATA",
      [
        "storage",
        "00c71a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005f4808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f47e4.md#insn-005f4808) · [`005f47f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f4/005f47e4.md#insn-005f47f8)
- 新版 [`0061a058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md#insn-0061a058) · [`0061a048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0061a/0061a034.md#insn-0061a048)

~~~diff
- 005f4808 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 005f4808 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 005f4808 bytes 080000f9
+ 0061a058 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0061a058 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0061a058 bytes 080000f9
- 005f47f8 ["INT_ADD", "register:40f0:8", ["const:5f47f8:8", "const:4:8"]]
- 005f47f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 0061a048 ["INT_ADD", "register:40f0:8", ["const:61a048:8", "const:4:8"]]
+ 0061a048 ["CALL", null, ["callee:00c57a90:8"]]
- 005f47f8 bytes 129a1794
+ 0061a048 bytes 92f61894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09c1fcdf8cef4761448b795b1c7688a4"></a>

### [`00601234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601234.md) → [`00626d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626d2c.md) FUN_00626d2c

採用 · 移動量 `+0x25af8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00601240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00601240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00626d38"
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
      "unmatched:0060123c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00626d54"
      ]
    ],
    [
      "unmatched:00601240",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00601248",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00626d34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00626d54"
      ]
    ],
    [
      "00626d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00626d40",
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

- 旧版 [`0060123c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601234.md#insn-0060123c) · [`00601240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601234.md#insn-00601240) · [`00601248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601234.md#insn-00601248)

~~~diff
- 0060123c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0060123c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0060123c bytes 01010054
- 00601240 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00601240 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00601240 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00601240 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00601240 bytes fd7bbfa9
- 00601248 ["INT_ADD", "register:40f0:8", ["const:601248:8", "const:4:8"]]
- 00601248 ["CALL", null, ["ram:457e1c:8"]]
- 00601248 bytes f55af997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb27137b23720461355798d361f928d"></a>

### [`00601340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601340.md) → [`00626e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626e38.md) FUN_00626e38

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00626e5c",
      "DATA",
      [
        "storage",
        "00bf59c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00626e5c",
      "DATA",
      [
        "storage",
        "00c72ae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601340.md#insn-00601354) · [`0060135c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601340.md#insn-0060135c) · [`00601360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601340.md#insn-00601360)
- 新版 [`00626e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626e38.md#insn-00626e4c) · [`00626e54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626e38.md#insn-00626e54)

~~~diff
- 00601354 ["INT_ADD", "register:40f0:8", ["const:601354:8", "const:4:8"]]
- 00601354 ["CALL", null, ["callee:00c57a90:8"]]
+ 00626e4c ["INT_ADD", "register:40f0:8", ["const:626e4c:8", "const:4:8"]]
+ 00626e4c ["CALL", null, ["callee:00c57a90:8"]]
- 00601354 bytes 3b671794
+ 00626e4c bytes 11c31894
- 0060135c ["COPY", "register:4040:8", ["const:bf5000:8"]]
+ 00626e54 ["COPY", "register:4040:8", ["const:c72000:8"]]
- 0060135c bytes a82f0090
+ 00626e54 bytes 68320090
- 00601360 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 00601360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00601360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00601360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00601360 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-717444556c549dbe1b062402c748836f"></a>

### [`006013d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013d4.md) → [`00626ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ecc.md) FUN_00626ecc

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006013ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00626ee4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "006013f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006013ec",
      "DATA",
      [
        "storage",
        "00bf5a40",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006013f0",
      "DATA",
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
      "00626ee4",
      "DATA",
      [
        "storage",
        "00c72b68",
        null,
        "undefined *"
      ]
    ],
    [
      "00626ee8",
      "DATA",
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

- 旧版 [`006013ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013d4.md#insn-006013ec) · [`006013f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/006013d4.md#insn-006013f4)
- 新版 [`00626ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00626/00626ecc.md#insn-00626ee4)

~~~diff
- 006013ec ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006013ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006013ec bytes 080000f9
- 006013f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006013f4 ["RETURN", null, ["register:0:8"]]
- 006013f4 bytes c0035fd6
+ 00626ee4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00626ee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00626ee4 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b32e5a6e6267ad71cfbb263359a7c59f"></a>

### [`0060156c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060156c.md) → [`00627064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md) FUN_00627064

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00601594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0062708c"
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
      "unmatched:00601594",
      "DATA",
      [
        "storage",
        "00bf5ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0062708c",
      "DATA",
      [
        "storage",
        "00c72be8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060156c.md#insn-00601594) · [`00601580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/0060156c.md#insn-00601580)
- 新版 [`0062708c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md#insn-0062708c) · [`00627078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627064.md#insn-00627078)

~~~diff
- 00601594 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00601594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00601594 bytes 080000f9
+ 0062708c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0062708c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0062708c bytes 080000f9
- 00601580 ["INT_ADD", "register:40f0:8", ["const:601580:8", "const:4:8"]]
- 00601580 ["CALL", null, ["callee:00c57a90:8"]]
+ 00627078 ["INT_ADD", "register:40f0:8", ["const:627078:8", "const:4:8"]]
+ 00627078 ["CALL", null, ["callee:00c57a90:8"]]
- 00601580 bytes b0661794
+ 00627078 bytes 86c21894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed2cd5bf1d82d266decf7d281a2af1c"></a>

### [`00601ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601ca4.md) → [`0062779c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md) FUN_0062779c

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00601cc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006277c0"
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
      "unmatched:00601cc8",
      "DATA",
      [
        "storage",
        "00bf5b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006277c0",
      "DATA",
      [
        "storage",
        "00c72c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00601cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601ca4.md#insn-00601cc8) · [`00601cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00601/00601ca4.md#insn-00601cb8)
- 新版 [`006277c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md#insn-006277c0) · [`006277b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/0062779c.md#insn-006277b0)

~~~diff
- 00601cc8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00601cc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00601cc8 bytes 080000f9
+ 006277c0 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 006277c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 006277c0 bytes 080000f9
- 00601cb8 ["INT_ADD", "register:40f0:8", ["const:601cb8:8", "const:4:8"]]
- 00601cb8 ["CALL", null, ["callee:00c57a90:8"]]
+ 006277b0 ["INT_ADD", "register:40f0:8", ["const:6277b0:8", "const:4:8"]]
+ 006277b0 ["CALL", null, ["callee:00c57a90:8"]]
- 00601cb8 bytes e2641794
+ 006277b0 bytes b8c01894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-994287451edd754ede8e8ea2f9de61a6"></a>

### [`00602140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602140.md) → [`00627c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md) FUN_00627c38

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00602158"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00627c50"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00602160"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00602158",
      "DATA",
      [
        "storage",
        "00bf5bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0060215c",
      "DATA",
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
      "00627c50",
      "DATA",
      [
        "storage",
        "00c72ce8",
        null,
        "undefined *"
      ]
    ],
    [
      "00627c54",
      "DATA",
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

- 旧版 [`00602158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602140.md#insn-00602158) · [`00602160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00602/00602140.md#insn-00602160)
- 新版 [`00627c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00627/00627c38.md#insn-00627c50)

~~~diff
- 00602158 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00602158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00602158 bytes 080000f9
- 00602160 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00602160 ["RETURN", null, ["register:0:8"]]
- 00602160 bytes c0035fd6
+ 00627c50 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00627c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00627c50 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-140e224754ccac88de90f3b4aaac0c0b"></a>

### [`00604028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604028.md) → [`00629b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b20.md) FUN_00629b20

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) · 呼出先 2件 [`00607890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607890.md) [`0060b774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b774.md)
- 新版 呼出元 1件 [`006bbc58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006bb/006bbc58.md) · 呼出先 2件 [`0062d388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d388.md) [`0063126c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/0063126c.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0060404c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0060b774"
      ]
    ]
  ],
  "added": [
    [
      "00629b44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063126c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060403c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604028.md#insn-0060403c) · [`0060404c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/00604028.md#insn-0060404c)
- 新版 [`00629b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b20.md#insn-00629b34) · [`00629b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629b20.md#insn-00629b44)

~~~diff
- 0060403c ["INT_ADD", "register:40f0:8", ["const:60403c:8", "const:4:8"]]
- 0060403c ["CALL", null, ["callee:0062d388:8"]]
+ 00629b34 ["INT_ADD", "register:40f0:8", ["const:629b34:8", "const:4:8"]]
+ 00629b34 ["CALL", null, ["callee:0062d388:8"]]
- 0060403c bytes 150e0094
+ 00629b34 bytes 150e0094
- 0060404c ["BRANCH", null, ["ram:60b774:8"]]
- 0060404c bytes ca1d0014
+ 00629b44 ["BRANCH", null, ["ram:63126c:8"]]
+ 00629b44 bytes ca1d0014
~~~


<a id="compare-17ba4862d6201d19c3852585eb84d74c"></a>

### [`006041b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md) → [`00629ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00629/00629ca8.md) FUN_00629ca8

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006046b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006046b8.md) · 呼出先 9件 [`006075fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/006075fc.md) [`00607890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607890.md) [`00608668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608668.md) [`006091c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/006091c4.md) [`0060b6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b6e4.md)
- 新版 呼出元 1件 [`0062a1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062a1b0.md) · 呼出先 9件 [`0062d0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0f4.md) [`0062d388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d388.md) [`0062e160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e160.md) [`0062ecbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062ecbc.md) [`006311dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00631/006311dc.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 52.38% / 新版 55.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006041f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00604200"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00604250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006041f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0060b774"
      ]
    ],
    [
      "unmatched:00604200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00608668"
      ]
    ],
    [
      "00629d20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006091c4"
      ]
    ]
  ],
  "added": [
    [
      "00629cf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0063126c"
      ]
    ],
    [
      "00629cf8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0062e160"
      ]
    ],
    [
      "00629d20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0062ecbc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006041f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md#insn-006041f8) · [`00604200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md#insn-00604200) · [`00604250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00604/006041b0.md#insn-00604250)

~~~diff
- 006041f8 ["INT_ADD", "register:40f0:8", ["const:6041f8:8", "const:4:8"]]
- 006041f8 ["CALL", null, ["ram:60b774:8"]]
- 006041f8 bytes 5f1d0094
- 00604200 ["INT_ADD", "register:40f0:8", ["const:604200:8", "const:4:8"]]
- 00604200 ["CALL", null, ["ram:608668:8"]]
- 00604200 bytes 1a110094
- 00604250 ["INT_ADD", "register:40f0:8", ["const:604250:8", "const:4:8"]]
- 00604250 ["CALL", null, ["ram:60b72c:8"]]
- 00604250 bytes 371d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec9682685982bd5e3358c97f420fd42b"></a>

### [`0060646c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/0060646c.md) → [`0062bf64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062b/0062bf64.md) FUN_0062bf64

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00606cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/00606cb8.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0062c7b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062c/0062c7b0.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 74.19% / 新版 76.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00606538"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00606540"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0060654c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00606540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0062c010"
      ]
    ]
  ],
  "added": [
    [
      "0062c038",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0062c010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00606538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/0060646c.md#insn-00606538) · [`00606540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/0060646c.md#insn-00606540) · [`0060654c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00606/0060646c.md#insn-0060654c)

~~~diff
- 00606538 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00606538 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00606538 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00606538 ["COPY", "register:4058:8", ["tmp:0:8"]]
- 00606538 bytes 2b01889a
- 00606540 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00606540 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00606540 bytes c1feff54
- 0060654c ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 0060654c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0060654c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0060654c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 0060654c bytes e1028b9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde8c09b90310ddc6bfde564ed0cef87"></a>

### [`006075ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/006075ac.md) → [`0062d0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0a4.md) FUN_0062d0a4

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0062e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e08c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006075e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "0062d0d8"
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
      "unmatched:006075e0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0062d0d8",
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

- 旧版 [`006075e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/006075ac.md#insn-006075e0) · [`006075c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/006075ac.md#insn-006075c0)
- 新版 [`0062d0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0a4.md#insn-0062d0d8) · [`0062d0b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0a4.md#insn-0062d0b8)

~~~diff
- 006075e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 006075e0 ["INT_ADD", "register:40f0:8", ["const:6075e0:8", "const:4:8"]]
- 006075e0 ["CALLIND", null, ["register:0:8"]]
- 006075e0 bytes 00013fd6
+ 0062d0d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0062d0d8 ["INT_ADD", "register:40f0:8", ["const:62d0d8:8", "const:4:8"]]
+ 0062d0d8 ["CALLIND", null, ["register:0:8"]]
+ 0062d0d8 bytes 00013fd6
- 006075c0 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 006075c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0062d0b8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 0062d0b8 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006075c0 bytes 740100b4
+ 0062d0b8 bytes 740100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b14103fd3c42cc889f278b18350a26"></a>

### [`00608404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608404.md) → [`0062defc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062defc.md) FUN_0062defc

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0062e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e08c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 60.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608408"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00608404",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00608408",
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
      "0062defc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0062df00",
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

- 旧版 [`00608404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608404.md#insn-00608404) · [`00608408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608404.md#insn-00608408)
- 新版 [`0062defc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062defc.md#insn-0062defc)

~~~diff
- 00608404 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00608404 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00608404 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00608404 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00608404 bytes fd7bbea9
- 00608408 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00608408 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00608408 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00608408 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00608408 bytes f44f01a9
+ 0062defc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0062defc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0062defc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 0062defc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0062defc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77b584b9630f7439157d4222c6768e9c"></a>

### [`00608454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608454.md) → [`0062df4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062df4c.md) FUN_0062df4c

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00607ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607ac8.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0062d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 37.50% / 新版 28.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608458"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00608454",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00608458",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0060845c",
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
      "0062df4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0062df50",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0062df54",
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

- 旧版 [`00608454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608454.md#insn-00608454) · [`00608458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608454.md#insn-00608458) · [`0060845c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608454.md#insn-0060845c)

~~~diff
- 00608454 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00608454 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00608454 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00608454 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00608454 bytes fd7bbca9
- 00608458 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00608458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00608458 bytes f70b00f9
- 0060845c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0060845c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0060845c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0060845c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0060845c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-898885381453ce79c4ee166aa1993490"></a>

### [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md) → [`0062e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e08c.md) FUN_0062e08c

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006075ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/006075ac.md) [`00608404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608404.md) [`0060b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0062d0a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d0a4.md) [`0062defc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062defc.md) [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 81.48% / 新版 81.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00608598"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00608594",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00608598",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0060859c",
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
      "0062e08c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0062e090",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0062e094",
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

- 旧版 [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md#insn-00608594) · [`00608598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md#insn-00608598) · [`0060859c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md#insn-0060859c)

~~~diff
- 00608594 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00608594 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00608594 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00608594 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00608594 bytes fd7bbda9
- 00608598 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00608598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00608598 bytes f50b00f9
- 0060859c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0060859c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0060859c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0060859c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0060859c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa3a70e744f46f7895020f00d4c9254f"></a>

### [`0060af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af8c.md) → [`00630a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a84.md) FUN_00630a84

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0060af94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00630a8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0060af98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0060af94",
      "DATA",
      [
        "storage",
        "00bf5cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630a8c",
      "DATA",
      [
        "storage",
        "00c72df8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060af94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af8c.md#insn-0060af94) · [`0060af98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060a/0060af8c.md#insn-0060af98)
- 新版 [`00630a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630a84.md#insn-00630a8c)

~~~diff
- 0060af94 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 0060af94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0060af94 bytes 280000f9
- 0060af98 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0060af98 ["RETURN", null, ["register:0:8"]]
- 0060af98 bytes c0035fd6
+ 00630a8c ["COPY", "tmp:0:8", ["register:4008:8"]]
+ 00630a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00630a8c bytes 280000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-104c6442a9bbd5eb0bf053e5fe9a40b1"></a>

### [`0060b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md) → [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md) FUN_00630b64

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00607ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00607/00607ac8.md) [`0060b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md) [`00833cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00833/00833cf0.md) · 呼出先 5件 [`00608594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00608/00608594.md) [`0060b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0062d5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062d/0062d5c0.md) [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md) [`00865c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00865/00865c68.md) · 呼出先 5件 [`0062e08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062e/0062e08c.md) [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 25.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0060b0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00630bb4"
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
      "unmatched:0060b0bc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00630bb4",
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

- 旧版 [`0060b0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md#insn-0060b0bc) · [`0060b06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b06c.md#insn-0060b06c)
- 新版 [`00630bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md#insn-00630bb4) · [`00630b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630b64.md#insn-00630b64)

~~~diff
- 0060b0bc ["COPY", "register:0:8", ["register:4040:8"]]
- 0060b0bc ["INT_ADD", "register:40f0:8", ["const:60b0bc:8", "const:4:8"]]
- 0060b0bc ["CALLIND", null, ["register:0:8"]]
- 0060b0bc bytes 00013fd6
+ 00630bb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00630bb4 ["INT_ADD", "register:40f0:8", ["const:630bb4:8", "const:4:8"]]
+ 00630bb4 ["CALLIND", null, ["register:0:8"]]
+ 00630bb4 bytes 00013fd6
- 0060b06c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 0060b06c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00630b64 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00630b64 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0060b06c bytes a10300b4
+ 00630b64 bytes a10300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a0af0a50253a5fac43606659d6cd980"></a>

### [`0060b280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md) → [`00630d78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00630/00630d78.md) FUN_00630d78

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0060b280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0060b280"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0060b298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0060b280",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0060b28c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "unmatched:0060b298",
      "DATA",
      [
        "storage",
        "00bf5dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00630d78",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00630d84",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57a90"
      ]
    ],
    [
      "00630d90",
      "DATA",
      [
        "storage",
        "00c72ef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060b280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md#insn-0060b280) · [`0060b28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md#insn-0060b28c) · [`0060b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060b/0060b280.md#insn-0060b298)

~~~diff
- 0060b280 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0060b280 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0060b280 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 0060b280 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0060b280 bytes fd7bbfa9
- 0060b28c ["INT_ADD", "register:40f0:8", ["const:60b28c:8", "const:4:8"]]
- 0060b28c ["CALL", null, ["callee:00c57a90:8"]]
- 0060b28c bytes 6d3f1794
- 0060b298 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0060b298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0060b298 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1d975361c4564a06d0fe581043cae5"></a>

### [`0060fc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fc20.md) → [`00635718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md) FUN_00635718

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 46.67% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0060fc3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00635734"
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
      "unmatched:0060fc3c",
      "DATA",
      [
        "storage",
        "00bf5ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635734",
      "DATA",
      [
        "storage",
        "00c73008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0060fc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fc20.md#insn-0060fc3c) · [`0060fc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060f/0060fc20.md#insn-0060fc34)
- 新版 [`00635734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md#insn-00635734) · [`0063572c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635718.md#insn-0063572c)

~~~diff
- 0060fc3c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0060fc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0060fc3c bytes 090000f9
+ 00635734 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00635734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00635734 bytes 090000f9
- 0060fc34 ["COPY", "register:4048:8", ["const:bf5000:8"]]
+ 0063572c ["COPY", "register:4048:8", ["const:c73000:8"]]
- 0060fc34 bytes 292f00d0
+ 0063572c bytes e93100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b618381cf2dcba307f5e56ad847b02f2"></a>

### [`0061014c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/0061014c.md) → [`00635c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md) FUN_00635c44

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00635c60"
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
      "unmatched:00610168",
      "DATA",
      [
        "storage",
        "00bf5f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635c60",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00610168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/0061014c.md#insn-00610168) · [`00610160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/0061014c.md#insn-00610160)
- 新版 [`00635c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md#insn-00635c60) · [`00635c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635c44.md#insn-00635c58)

~~~diff
- 00610168 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00610168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00610168 bytes 090000f9
+ 00635c60 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00635c60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00635c60 bytes 090000f9
- 00610160 ["COPY", "register:4048:8", ["const:bf5000:8"]]
+ 00635c58 ["COPY", "register:4048:8", ["const:c73000:8"]]
- 00610160 bytes 292f00b0
+ 00635c58 bytes e93100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2dabbefd8daafeabe5d4afdba5d7b4"></a>

### [`006101b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006101b8.md) → [`00635cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md) FUN_00635cb0

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 38.46% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006101d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00635ccc"
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
      "unmatched:006101d4",
      "DATA",
      [
        "storage",
        "00bf5f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00635ccc",
      "DATA",
      [
        "storage",
        "00c73088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006101d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006101b8.md#insn-006101d4) · [`006101cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006101b8.md#insn-006101cc)
- 新版 [`00635ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md#insn-00635ccc) · [`00635cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635cb0.md#insn-00635cc4)

~~~diff
- 006101d4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006101d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006101d4 bytes 090000f9
+ 00635ccc ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00635ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00635ccc bytes 090000f9
- 006101cc ["COPY", "register:4048:8", ["const:bf5000:8"]]
+ 00635cc4 ["COPY", "register:4048:8", ["const:c73000:8"]]
- 006101cc bytes 292f00b0
+ 00635cc4 bytes e93100d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c9499b3c75a3aed41ddf9aed7908ec2"></a>

### [`00610380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610380.md) → [`00635e78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00635/00635e78.md) FUN_00635e78

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610380"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610384"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00610380",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00610384",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00610388",
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
      "00635e78",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00635e7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00635e80",
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

- 旧版 [`00610380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610380.md#insn-00610380) · [`00610384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610380.md#insn-00610384) · [`00610388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610380.md#insn-00610388)

~~~diff
- 00610380 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00610380 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00610380 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00610380 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00610380 bytes fd7bbda9
- 00610384 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00610384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00610384 bytes f50b00f9
- 00610388 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00610388 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00610388 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00610388 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00610388 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b498a8615ba9ac4b9ab41451914bff0a"></a>

### [`00610688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610688.md) → [`00636180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636180.md) FUN_00636180

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0060e154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060e154.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00633c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633c4c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 66.67% / 新版 73.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00610734"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "0063622c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00610734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610688.md#insn-00610734) · [`006106a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610688.md#insn-006106a4)
- 新版 [`0063622c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636180.md#insn-0063622c) · [`0063619c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636180.md#insn-0063619c)

~~~diff
- 00610734 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00610734 ["RETURN", null, ["register:0:8"]]
- 00610734 bytes c0035fd6
+ 0063622c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 0063622c ["RETURN", null, ["register:0:8"]]
+ 0063622c bytes c0035fd6
- 006106a4 ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
- 006106a4 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 0063619c ["INT_EQUAL", "tmp:0:1", ["register:40a8:8", "const:0:8"]]
+ 0063619c ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 006106a4 bytes 750300b4
+ 0063619c bytes 750300b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d278aaa9bbc05b13d9ee97b2ad2289d5"></a>

### [`006109a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006109a8.md) → [`006364a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006364a0.md) FUN_006364a0

採用 · 移動量 `+0x25af8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00610738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610738.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00636230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636230.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 57.14% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00610a48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00636540"
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
      "unmatched:00610a48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00636578"
      ]
    ]
  ],
  "added": [
    [
      "00636540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00636578"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00610a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006109a8.md#insn-00610a48) · [`006109ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/006109a8.md#insn-006109ac)
- 新版 [`00636540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006364a0.md#insn-00636540) · [`006364a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/006364a0.md#insn-006364a4)

~~~diff
- 00610a48 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00610a48 bytes c0010054
+ 00636540 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
+ 00636540 bytes c0010054
- 006109ac ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
+ 006364a4 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 006109ac bytes e0060054
+ 006364a4 bytes e0060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07165a0ede9dc8686c5a2e92c1e62378"></a>

### [`00610c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c14.md) → [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md) FUN_0063670c

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00610a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610a8c.md) [`0062d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d23c.md) [`00717134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00717/00717134.md) [`007689a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00768/007689a0.md) [`00769cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00769/00769cc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 6件 [`00636584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636584.md) [`00652d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652d20.md) [`00741238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00741/00741238.md) [`00792e74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00792/00792e74.md) [`00794194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00794/00794194.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610c14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610c14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0063670c"
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
      "unmatched:00610c14",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00610c20",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00610c24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "0063670c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00636718",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "0063671c",
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

- 旧版 [`00610c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c14.md#insn-00610c14) · [`00610c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c14.md#insn-00610c24)
- 新版 [`0063670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/0063670c.md#insn-0063670c)

~~~diff
- 00610c14 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00610c14 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00610c14 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00610c14 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00610c14 bytes fd7bbfa9
- 00610c24 ["INT_ADD", "register:40f0:8", ["const:610c24:8", "const:4:8"]]
- 00610c24 ["CALL", null, ["ram:418c38:8"]]
- 00610c24 bytes 0520f897
+ 0063670c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 0063670c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 0063670c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 0063670c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 0063670c bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a0e0be35d75ddab44aec460c8e3b504"></a>

### [`00610c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c2c.md) → [`00636724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636724.md) FUN_00636724

採用 · 移動量 `+0x25af8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 55.56% / 新版 55.56%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00610c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0063673c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00610c4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00610c44",
      "DATA",
      [
        "storage",
        "00bf5ff8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00610c48",
      "DATA",
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
      "0063673c",
      "DATA",
      [
        "storage",
        "00c73120",
        null,
        "undefined *"
      ]
    ],
    [
      "00636740",
      "DATA",
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

- 旧版 [`00610c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c2c.md#insn-00610c44) · [`00610c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00610/00610c2c.md#insn-00610c4c)
- 新版 [`0063673c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00636/00636724.md#insn-0063673c)

~~~diff
- 00610c44 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00610c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00610c44 bytes 080000f9
- 00610c4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00610c4c ["RETURN", null, ["register:0:8"]]
- 00610c4c bytes c0035fd6
+ 0063673c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0063673c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0063673c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

