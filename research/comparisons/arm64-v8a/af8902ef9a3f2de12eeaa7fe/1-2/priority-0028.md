# v15.7.4 → v16.0.0 · 最優先の変更候補 (28)

[一覧の目次](README.md)

<a id="compare-d8bd4b45f0fc0ac605dd15ef8799f0d1"></a>

### [`0066bc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md) → [`00691fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/00691fdc.md) FUN_00691fdc

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00660748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660748.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0066bebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bebc.md) [`0066c094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00686a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00686/00686a38.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00692204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692204.md) [`006923dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923dc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 40.48% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066bdb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066bdb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00692100"
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
      "unmatched:0066bcf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692184"
      ]
    ],
    [
      "unmatched:0066bdb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0069217c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006921b0"
      ]
    ]
  ],
  "added": [
    [
      "0069203c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006921b0"
      ]
    ],
    [
      "00692100",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0069217c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00692184"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066bcf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md#insn-0066bcf4) · [`0066bdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md#insn-0066bdb8) · [`0066bdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md#insn-0066bdc4)
- 新版 [`0069210c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/00691fdc.md#insn-0069210c)

~~~diff
- 0066bcf4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0066bcf4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0066bcf4 ["CBRANCH", null, ["local:b27:8", "tmp:1:1"]]
- 0066bcf4 bytes a80b0054
- 0066bdb8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0066bdb8 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 0066bdb8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0066bdb8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0066bdb8 bytes e92301a9
- 0066bdc4 ["INT_ADD", "register:40f0:8", ["const:66bdc4:8", "const:4:8"]]
- 0066bdc4 ["CALL", null, ["callee:00692204:8"]]
+ 0069210c ["INT_ADD", "register:40f0:8", ["const:69210c:8", "const:4:8"]]
+ 0069210c ["CALL", null, ["callee:00692204:8"]]
- 0066bdc4 bytes 3e000094
+ 0069210c bytes 3e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-291acb627935530ed063fdba0f00c054"></a>

### [`0066bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bff4.md) → [`0069233c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/0069233c.md) FUN_0069233c

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 35.00% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0066c060",
      "incomplete_value": true,
      "site": "0066c064",
      "value": [
        "LOAD",
        "8",
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
                "register:40a8:8"
              ],
              [
                "leaf",
                "const:ffffffffffffffc8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0066c064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bff4.md#insn-0066c064) · [`0066c018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bff4.md#insn-0066c018) · [`0066c028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bff4.md#insn-0066c028)
- 新版 [`006923ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/0069233c.md#insn-006923ac) · [`00692360`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/0069233c.md#insn-00692360) · [`00692370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/0069233c.md#insn-00692370)

~~~diff
- 0066c064 ["INT_ADD", "register:40f0:8", ["const:66c064:8", "const:4:8"]]
- 0066c064 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006923ac ["INT_ADD", "register:40f0:8", ["const:6923ac:8", "const:4:8"]]
+ 006923ac ["CALL", null, ["callee:00c57ab0:8"]]
- 0066c064 bytes ffbb1594
+ 006923ac bytes c1151794
- 0066c018 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 00692360 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 0066c018 bytes a0020054
+ 00692360 bytes a0020054
- 0066c028 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0066c028 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0066c028 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0066c028 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00692370 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00692370 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00692370 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00692370 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 0066c028 bytes c8000037
+ 00692370 bytes c8000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ccc873931ae62edbe04e78f53fc386f"></a>

### [`0066c094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md) → [`006923dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923dc.md) FUN_006923dc

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0066bc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00691fdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00691/00691fdc.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006923ec",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066c0a4",
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
      "definition_site": "006923e8",
      "incomplete_value": false,
      "site": "006923ec",
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
      "definition_site": "0066c0a0",
      "incomplete_value": false,
      "site": "0066c0a4",
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
      "006923e8",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006923ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006923e8",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006923ec",
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

- 旧版 [`0066c0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md#insn-0066c0a4) · [`0066c09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md#insn-0066c09c) · [`0066c0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md#insn-0066c0a0)
- 新版 [`006923ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923dc.md#insn-006923ec) · [`006923e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923dc.md#insn-006923e4) · [`006923e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006923dc.md#insn-006923e8)

~~~diff
- 0066c0a4 ["INT_ADD", "register:40f0:8", ["const:66c0a4:8", "const:4:8"]]
- 0066c0a4 ["CALL", null, ["ram:418c38:8"]]
+ 006923ec ["INT_ADD", "register:40f0:8", ["const:6923ec:8", "const:4:8"]]
+ 006923ec ["CALL", null, ["ram:43b738:8"]]
- 0066c0a4 bytes e5b2f697
+ 006923ec bytes d3a4f697
- 0066c09c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006923e4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0066c09c bytes c0e1fff0
+ 006923e4 bytes 20e1ffb0
- 0066c0a0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0066c0a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006923e8 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006923e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006923e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006923e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 bytes 00740e91
+ 006923e8 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f970740a87b9f53cc4bdca1077d6abe"></a>

### [`0066c0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md) → [`00692440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md) FUN_00692440

採用 · 移動量 `+0x26348` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00660f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660f48.md) [`0066c0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md) [`0081715c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00817/0081715c.md) · 呼出先 2件 [`0066c0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00687238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/00687238.md) [`00692440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md) [`00848f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/00848f54.md) · 呼出先 2件 [`00692440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0066c0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md#insn-0066c0f8) · [`0066c118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md#insn-0066c118) · [`0066c124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c0f8.md#insn-0066c124)
- 新版 [`00692440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md#insn-00692440) · [`00692460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md#insn-00692460) · [`0069246c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692440.md#insn-0069246c)

~~~diff
- 0066c0f8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 0066c0f8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00692440 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00692440 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0066c0f8 bytes 010200b4
+ 00692440 bytes 010200b4
- 0066c118 ["INT_ADD", "register:40f0:8", ["const:66c118:8", "const:4:8"]]
- 0066c118 ["CALL", null, ["local:b0:8"]]
+ 00692460 ["INT_ADD", "register:40f0:8", ["const:692460:8", "const:4:8"]]
+ 00692460 ["CALL", null, ["local:b0:8"]]
- 0066c118 bytes f8ffff97
+ 00692460 bytes f8ffff97
- 0066c124 ["INT_ADD", "register:40f0:8", ["const:66c124:8", "const:4:8"]]
- 0066c124 ["CALL", null, ["local:b0:8"]]
+ 0069246c ["INT_ADD", "register:40f0:8", ["const:69246c:8", "const:4:8"]]
+ 0069246c ["CALL", null, ["local:b0:8"]]
- 0066c124 bytes f5ffff97
+ 0069246c bytes f5ffff97
~~~


<a id="compare-28b5cda66f3aad4c4da9f122c29b3416"></a>

### [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) → [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) FUN_00692484

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`006615d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006615d4.md) [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) [`0066e9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md) [`0066ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 11件 [`006878c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/006878c4.md) [`0068e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068e714.md) [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) [`00694ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ce8.md) [`00694da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694da0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00692494",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066c14c",
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
      "definition_site": "00692490",
      "incomplete_value": false,
      "site": "00692494",
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
      "definition_site": "0066c148",
      "incomplete_value": false,
      "site": "0066c14c",
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
      "00692490",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00692494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00692490",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00692494",
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

- 旧版 [`0066c14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md#insn-0066c14c) · [`0066c144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md#insn-0066c144) · [`0066c148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md#insn-0066c148)
- 新版 [`00692494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md#insn-00692494) · [`0069248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md#insn-0069248c) · [`00692490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md#insn-00692490)

~~~diff
- 0066c14c ["INT_ADD", "register:40f0:8", ["const:66c14c:8", "const:4:8"]]
- 0066c14c ["CALL", null, ["ram:418c38:8"]]
+ 00692494 ["INT_ADD", "register:40f0:8", ["const:692494:8", "const:4:8"]]
+ 00692494 ["CALL", null, ["ram:43b738:8"]]
- 0066c14c bytes bbb2f697
+ 00692494 bytes a9a4f697
- 0066c144 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 0069248c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0066c144 bytes c0e1fff0
+ 0069248c bytes 20e1ffb0
- 0066c148 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0066c148 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c148 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00692490 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00692490 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00692490 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00692490 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c148 bytes 00740e91
+ 00692490 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245c22ba5c7696adbbd94f95fc470559"></a>

### [`0066c150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md) → [`00692498`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692498.md) FUN_00692498

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065ef18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ef18.md) [`0065f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f044.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`00684f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00684/00684f70.md) [`00685208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685208.md) [`00685334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00685/00685334.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "006924a8",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066c160",
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
      "definition_site": "006924a4",
      "incomplete_value": false,
      "site": "006924a8",
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
      "definition_site": "0066c15c",
      "incomplete_value": false,
      "site": "0066c160",
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
      "006924a4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006924a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "006924a4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006924a8",
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

- 旧版 [`0066c160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md#insn-0066c160) · [`0066c158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md#insn-0066c158) · [`0066c15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md#insn-0066c15c)
- 新版 [`006924a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692498.md#insn-006924a8) · [`006924a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692498.md#insn-006924a0) · [`006924a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692498.md#insn-006924a4)

~~~diff
- 0066c160 ["INT_ADD", "register:40f0:8", ["const:66c160:8", "const:4:8"]]
- 0066c160 ["CALL", null, ["ram:41fdf0:8"]]
+ 006924a8 ["INT_ADD", "register:40f0:8", ["const:6924a8:8", "const:4:8"]]
+ 006924a8 ["CALL", null, ["ram:4428f0:8"]]
- 0066c160 bytes 24cff697
+ 006924a8 bytes 12c1f697
- 0066c158 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006924a0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0066c158 bytes c0e1fff0
+ 006924a0 bytes 20e1ffb0
- 0066c15c ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0066c15c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c15c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c15c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006924a4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006924a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006924a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006924a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c15c bytes 00740e91
+ 006924a4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb996bf67b3b86a6d19ccf9b5dcba228"></a>

### [`0066c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md) → [`006924c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006924c0.md) FUN_006924c0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00663f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663f40.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0068a278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068a278.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006924d0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066c188",
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
      "definition_site": "006924cc",
      "incomplete_value": false,
      "site": "006924d0",
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
      "definition_site": "0066c184",
      "incomplete_value": false,
      "site": "0066c188",
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
      "006924cc",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006924d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006924cc",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006924d0",
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

- 旧版 [`0066c188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md#insn-0066c188) · [`0066c180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md#insn-0066c180) · [`0066c184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md#insn-0066c184)
- 新版 [`006924d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006924c0.md#insn-006924d0) · [`006924c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006924c0.md#insn-006924c8) · [`006924cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006924c0.md#insn-006924cc)

~~~diff
- 0066c188 ["INT_ADD", "register:40f0:8", ["const:66c188:8", "const:4:8"]]
- 0066c188 ["CALL", null, ["ram:418c38:8"]]
+ 006924d0 ["INT_ADD", "register:40f0:8", ["const:6924d0:8", "const:4:8"]]
+ 006924d0 ["CALL", null, ["ram:43b738:8"]]
- 0066c188 bytes acb2f697
+ 006924d0 bytes 9aa4f697
- 0066c180 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006924c8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0066c180 bytes c0e1fff0
+ 006924c8 bytes 20e1ffb0
- 0066c184 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0066c184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006924cc ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006924cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006924cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006924cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c184 bytes 00740e91
+ 006924cc bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cd839f387c3667665f91b03cd2670c4"></a>

### [`0066c850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md) → [`00692b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692b98.md) FUN_00692b98

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0066c18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c18c.md) [`0066c850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md) · 呼出先 4件 [`0066c850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md) [`0066cd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cd6c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`006924d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/006924d4.md) [`00692b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692b98.md) · 呼出先 4件 [`00692b98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692b98.md) [`006930b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006930b4.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.26% / 新版 82.26%

CFGの説明率　旧版 54.43% / 新版 53.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 17件, `unresolved_store_alignment` 22件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066c854"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066c854"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066c858"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0066c854",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0066c858",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0066c85c",
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
      "00692b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00692ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00692ba4",
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

- 旧版 [`0066c854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md#insn-0066c854) · [`0066c858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md#insn-0066c858) · [`0066c85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c850.md#insn-0066c85c)

~~~diff
- 0066c854 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0066c854 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0066c854 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0066c854 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0066c854 bytes fd7b07a9
- 0066c858 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0066c858 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0066c858 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0066c858 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0066c858 bytes fc6f08a9
- 0066c85c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0066c85c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0066c85c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0066c85c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0066c85c bytes fa6709a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb2297c19a3ab058d00072f947800a1"></a>

### [`0066cfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md) → [`006932f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006932f8.md) FUN_006932f8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069331c",
      "incomplete_value": false,
      "site": "0069331c",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066cfd4",
      "incomplete_value": false,
      "site": "0066cfd4",
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
            "const:328:8"
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
      "0069331c",
      "DATA",
      [
        "storage",
        "00bf7328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069331c",
      "DATA",
      [
        "storage",
        "00c74450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066cfc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md#insn-0066cfc4) · [`0066cfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md#insn-0066cfcc) · [`0066cfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md#insn-0066cfd0)
- 新版 [`0069330c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006932f8.md#insn-0069330c) · [`00693314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006932f8.md#insn-00693314) · [`00693318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006932f8.md#insn-00693318)

~~~diff
- 0066cfc4 ["INT_ADD", "register:40f0:8", ["const:66cfc4:8", "const:4:8"]]
- 0066cfc4 ["CALL", null, ["callee:00c57a90:8"]]
+ 0069330c ["INT_ADD", "register:40f0:8", ["const:69330c:8", "const:4:8"]]
+ 0069330c ["CALL", null, ["callee:00c57a90:8"]]
- 0066cfc4 bytes 1fb81594
+ 0069330c bytes e1111794
- 0066cfcc ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00693314 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066cfcc bytes 482c00f0
+ 00693314 bytes 082f00b0
- 0066cfd0 ["COPY", "tmp:0:8", ["const:328:8"]]
- 0066cfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693318 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00693318 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693318 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693318 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 bytes 08a10c91
+ 00693318 bytes 08411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-301b6833098a67c92fafc6a2db520216"></a>

### [`0066cfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfe4.md) → [`0069332c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069332c.md) FUN_0069332c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693338",
      "incomplete_value": false,
      "site": "00693338",
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
            "const:450:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066cff0",
      "incomplete_value": false,
      "site": "0066cff0",
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
            "const:328:8"
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
      "00693338",
      "DATA",
      [
        "storage",
        "00bf7328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693338",
      "DATA",
      [
        "storage",
        "00c74450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066cfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfe4.md#insn-0066cfe8) · [`0066cfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfe4.md#insn-0066cfec)
- 新版 [`00693330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069332c.md#insn-00693330) · [`00693334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069332c.md#insn-00693334)

~~~diff
- 0066cfe8 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00693330 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066cfe8 bytes 492c00f0
+ 00693330 bytes 092f00b0
- 0066cfec ["COPY", "tmp:0:8", ["const:328:8"]]
- 0066cfec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066cfec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066cfec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00693334 ["COPY", "tmp:0:8", ["const:450:8"]]
+ 00693334 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00693334 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00693334 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066cfec bytes 29a10c91
+ 00693334 bytes 29411191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9337d81abca79243033b0bc3e55ab601"></a>

### [`0066d000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d000.md) → [`00693348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693348.md) FUN_00693348

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00665758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665758.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068ba90.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "00693368",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066d020",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "site": "00693374",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066d02c",
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
      "00693368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00693374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00693390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00665758"
      ]
    ]
  ],
  "added": [
    [
      "00693368",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00693374",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00693390",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0068ba90"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d000.md#insn-0066d020) · [`0066d02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d000.md#insn-0066d02c) · [`0066d048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d000.md#insn-0066d048)
- 新版 [`00693368`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693348.md#insn-00693368) · [`00693374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693348.md#insn-00693374) · [`00693390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693348.md#insn-00693390)

~~~diff
- 0066d020 ["INT_ADD", "register:40f0:8", ["const:66d020:8", "const:4:8"]]
- 0066d020 ["CALL", null, ["ram:457e1c:8"]]
+ 00693368 ["INT_ADD", "register:40f0:8", ["const:693368:8", "const:4:8"]]
+ 00693368 ["CALL", null, ["ram:47acb4:8"]]
- 0066d020 bytes 7fabf797
+ 00693368 bytes 539ef797
- 0066d02c ["INT_ADD", "register:40f0:8", ["const:66d02c:8", "const:4:8"]]
- 0066d02c ["CALL", null, ["ram:457e1c:8"]]
+ 00693374 ["INT_ADD", "register:40f0:8", ["const:693374:8", "const:4:8"]]
+ 00693374 ["CALL", null, ["ram:47acb4:8"]]
- 0066d02c bytes 7cabf797
+ 00693374 bytes 509ef797
- 0066d048 ["BRANCH", null, ["ram:665758:8"]]
+ 00693390 ["BRANCH", null, ["ram:68ba90:8"]]
- 0066d048 bytes c4e1ff17
+ 00693390 bytes c0e1ff17
~~~


<a id="compare-492b26b79f7349ff2ff2aba580376e7d"></a>

### [`0066d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0b4.md) → [`006933fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006933fc.md) FUN_006933fc

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693408",
      "incomplete_value": false,
      "site": "00693408",
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
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d0c0",
      "incomplete_value": false,
      "site": "0066d0c0",
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
            "const:3a8:8"
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
      "00693408",
      "DATA",
      [
        "storage",
        "00bf73a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693408",
      "DATA",
      [
        "storage",
        "00c744d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0b4.md#insn-0066d0b8) · [`0066d0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0b4.md#insn-0066d0bc)
- 新版 [`00693400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006933fc.md#insn-00693400) · [`00693404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006933fc.md#insn-00693404)

~~~diff
- 0066d0b8 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00693400 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066d0b8 bytes 492c00d0
+ 00693400 bytes 092f00b0
- 0066d0bc ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 0066d0bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00693404 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 00693404 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00693404 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00693404 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc bytes 29a10e91
+ 00693404 bytes 29411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ef4d7ae94f5f06495a16fd0d63a4437"></a>

### [`0066d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md) → [`00693418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693418.md) FUN_00693418

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00665758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665758.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0068ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068ba90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.60% / 新版 72.60%

CFGの説明率　旧版 74.19% / 新版 63.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066d23c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066d240"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066d244"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00693448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0066d124"
      ]
    ],
    [
      "00693450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:0066d124",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00693448",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069346c"
      ]
    ],
    [
      "00693450",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0069346c",
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

- 旧版 [`0066d108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md#insn-0066d108) · [`0066d124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md#insn-0066d124) · [`0066d134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md#insn-0066d134)
- 新版 [`00693450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693418.md#insn-00693450)

~~~diff
- 0066d108 ["INT_ADD", "register:40f0:8", ["const:66d108:8", "const:4:8"]]
- 0066d108 ["CALL", null, ["ram:457e1c:8"]]
+ 00693450 ["INT_ADD", "register:40f0:8", ["const:693450:8", "const:4:8"]]
+ 00693450 ["CALL", null, ["ram:47acb4:8"]]
- 0066d108 bytes 45abf797
+ 00693450 bytes 199ef797
- 0066d124 ["INT_ADD", "register:40f0:8", ["const:66d124:8", "const:4:8"]]
- 0066d124 ["CALL", null, ["ram:457e1c:8"]]
- 0066d124 bytes 3eabf797
- 0066d134 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0066d134 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 0066d134 bytes 01120054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-488bc3c8bfe2dfc1734bf83c59bcc28d"></a>

### [`0066d3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md) → [`0069371c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069371c.md) FUN_0069371c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693740",
      "incomplete_value": false,
      "site": "00693740",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d3f8",
      "incomplete_value": false,
      "site": "0066d3f8",
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
            "const:418:8"
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
      "00693740",
      "DATA",
      [
        "storage",
        "00bf7418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693740",
      "DATA",
      [
        "storage",
        "00c74540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md#insn-0066d3e8) · [`0066d3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md#insn-0066d3f0) · [`0066d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md#insn-0066d3f4)
- 新版 [`00693730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069371c.md#insn-00693730) · [`00693738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069371c.md#insn-00693738) · [`0069373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069371c.md#insn-0069373c)

~~~diff
- 0066d3e8 ["INT_ADD", "register:40f0:8", ["const:66d3e8:8", "const:4:8"]]
- 0066d3e8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00693730 ["INT_ADD", "register:40f0:8", ["const:693730:8", "const:4:8"]]
+ 00693730 ["CALL", null, ["callee:00c57a90:8"]]
- 0066d3e8 bytes 16b71594
+ 00693730 bytes d8101794
- 0066d3f0 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00693738 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066d3f0 bytes 482c00d0
+ 00693738 bytes 082f00b0
- 0066d3f4 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0066d3f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069373c ["COPY", "tmp:0:8", ["const:540:8"]]
+ 0069373c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069373c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069373c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 bytes 08611091
+ 0069373c bytes 08011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31306256f1e2e85ccb15894c89acc85c"></a>

### [`0066d408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d408.md) → [`00693750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693750.md) FUN_00693750

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069375c",
      "incomplete_value": false,
      "site": "0069375c",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d414",
      "incomplete_value": false,
      "site": "0066d414",
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
            "const:418:8"
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
      "0069375c",
      "DATA",
      [
        "storage",
        "00bf7418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069375c",
      "DATA",
      [
        "storage",
        "00c74540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d408.md#insn-0066d40c) · [`0066d410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d408.md#insn-0066d410)
- 新版 [`00693754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693750.md#insn-00693754) · [`00693758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693750.md#insn-00693758)

~~~diff
- 0066d40c ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00693754 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066d40c bytes 492c00d0
+ 00693754 bytes 092f00b0
- 0066d410 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0066d410 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d410 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d410 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00693758 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00693758 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00693758 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00693758 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d410 bytes 29611091
+ 00693758 bytes 29011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f71e19eb4b097f6d02224208becffda"></a>

### [`0066d424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d424.md) → [`0069376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069376c.md) FUN_0069376c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00693788",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066d440",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00693788",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00693788",
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

- 旧版 [`0066d440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d424.md#insn-0066d440) · [`0066d44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d424.md#insn-0066d44c)
- 新版 [`00693788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069376c.md#insn-00693788) · [`00693794`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069376c.md#insn-00693794)

~~~diff
- 0066d440 ["INT_ADD", "register:40f0:8", ["const:66d440:8", "const:4:8"]]
- 0066d440 ["CALL", null, ["ram:457e1c:8"]]
+ 00693788 ["INT_ADD", "register:40f0:8", ["const:693788:8", "const:4:8"]]
+ 00693788 ["CALL", null, ["ram:47acb4:8"]]
- 0066d440 bytes 77aaf797
+ 00693788 bytes 4b9df797
- 0066d44c ["INT_ADD", "register:40f0:8", ["const:66d44c:8", "const:4:8"]]
- 0066d44c ["CALL", null, ["callee:0047cd94:8"]]
+ 00693794 ["INT_ADD", "register:40f0:8", ["const:693794:8", "const:4:8"]]
+ 00693794 ["CALL", null, ["callee:0047cd94:8"]]
- 0066d44c bytes acb2f797
+ 00693794 bytes 80a5f797
~~~


<a id="compare-705a9955bfd905c05859e73937a79063"></a>

### [`0066d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md) → [`006937d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006937d8.md) FUN_006937d8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006937fc",
      "incomplete_value": false,
      "site": "006937fc",
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
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d4b4",
      "incomplete_value": false,
      "site": "0066d4b4",
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
            "const:4a8:8"
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
      "006937fc",
      "DATA",
      [
        "storage",
        "00bf74a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006937fc",
      "DATA",
      [
        "storage",
        "00c745d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md#insn-0066d4a4) · [`0066d4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md#insn-0066d4ac) · [`0066d4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md#insn-0066d4b0)
- 新版 [`006937ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006937d8.md#insn-006937ec) · [`006937f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006937d8.md#insn-006937f4) · [`006937f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/006937d8.md#insn-006937f8)

~~~diff
- 0066d4a4 ["INT_ADD", "register:40f0:8", ["const:66d4a4:8", "const:4:8"]]
- 0066d4a4 ["CALL", null, ["callee:00c57a90:8"]]
+ 006937ec ["INT_ADD", "register:40f0:8", ["const:6937ec:8", "const:4:8"]]
+ 006937ec ["CALL", null, ["callee:00c57a90:8"]]
- 0066d4a4 bytes e7b61594
+ 006937ec bytes a9101794
- 0066d4ac ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006937f4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066d4ac bytes 482c00d0
+ 006937f4 bytes 082f00b0
- 0066d4b0 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0066d4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006937f8 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 006937f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006937f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006937f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 bytes 08a11291
+ 006937f8 bytes 08411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07f7f622fcad3f2133d46f1540ac621a"></a>

### [`0066d4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4c4.md) → [`0069380c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069380c.md) FUN_0069380c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693818",
      "incomplete_value": false,
      "site": "00693818",
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
            "const:5d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d4d0",
      "incomplete_value": false,
      "site": "0066d4d0",
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
            "const:4a8:8"
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
      "00693818",
      "DATA",
      [
        "storage",
        "00bf74a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693818",
      "DATA",
      [
        "storage",
        "00c745d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4c4.md#insn-0066d4c8) · [`0066d4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4c4.md#insn-0066d4cc)
- 新版 [`00693810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069380c.md#insn-00693810) · [`00693814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069380c.md#insn-00693814)

~~~diff
- 0066d4c8 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00693810 ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066d4c8 bytes 492c00d0
+ 00693810 bytes 092f00b0
- 0066d4cc ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 0066d4cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00693814 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00693814 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00693814 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00693814 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc bytes 29a11291
+ 00693814 bytes 29411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee13aebaca985502cdb4aa6577c41875"></a>

### [`0066d4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4e0.md) → [`00693828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693828.md) FUN_00693828

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00664634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664634.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068a96c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00693850",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066d508",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "site": "00693860",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066d518",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00693890",
      "incomplete_value": true,
      "site": "00693894",
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
            "const:2f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d548",
      "incomplete_value": true,
      "site": "0066d54c",
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
            "const:2e48:8"
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
      "00693850",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00693860",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00693850",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00693860",
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

- 旧版 [`0066d508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4e0.md#insn-0066d508) · [`0066d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4e0.md#insn-0066d518) · [`0066d54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4e0.md#insn-0066d54c)
- 新版 [`00693850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693828.md#insn-00693850) · [`00693860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693828.md#insn-00693860) · [`00693894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693828.md#insn-00693894)

~~~diff
- 0066d508 ["INT_ADD", "register:40f0:8", ["const:66d508:8", "const:4:8"]]
- 0066d508 ["CALL", null, ["ram:457e1c:8"]]
+ 00693850 ["INT_ADD", "register:40f0:8", ["const:693850:8", "const:4:8"]]
+ 00693850 ["CALL", null, ["ram:47acb4:8"]]
- 0066d508 bytes 45aaf797
+ 00693850 bytes 199df797
- 0066d518 ["INT_ADD", "register:40f0:8", ["const:66d518:8", "const:4:8"]]
- 0066d518 ["CALL", null, ["ram:457e1c:8"]]
+ 00693860 ["INT_ADD", "register:40f0:8", ["const:693860:8", "const:4:8"]]
+ 00693860 ["CALL", null, ["ram:47acb4:8"]]
- 0066d518 bytes 41aaf797
+ 00693860 bytes 159df797
- 0066d54c ["INT_ADD", "register:40f0:8", ["const:66d54c:8", "const:4:8"]]
- 0066d54c ["CALL", null, ["callee:008b7984:8"]]
+ 00693894 ["INT_ADD", "register:40f0:8", ["const:693894:8", "const:4:8"]]
+ 00693894 ["CALL", null, ["callee:008b7984:8"]]
- 0066d54c bytes a65c0894
+ 00693894 bytes 3c900894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-871e580f708814920e91aa23fe232b65"></a>

### [`0066d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md) → [`0069390c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069390c.md) FUN_0069390c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00693930",
      "incomplete_value": false,
      "site": "00693938",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d5e8",
      "incomplete_value": false,
      "site": "0066d5f0",
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
            "const:528:8"
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
      "00693938",
      "DATA",
      [
        "storage",
        "00bf7528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693938",
      "DATA",
      [
        "storage",
        "00c74650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md#insn-0066d5d8) · [`0066d5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md#insn-0066d5e4) · [`0066d5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md#insn-0066d5e8)
- 新版 [`00693920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069390c.md#insn-00693920) · [`0069392c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069390c.md#insn-0069392c) · [`00693930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/0069390c.md#insn-00693930)

~~~diff
- 0066d5d8 ["INT_ADD", "register:40f0:8", ["const:66d5d8:8", "const:4:8"]]
- 0066d5d8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00693920 ["INT_ADD", "register:40f0:8", ["const:693920:8", "const:4:8"]]
+ 00693920 ["CALL", null, ["callee:00c57a90:8"]]
- 0066d5d8 bytes 9ab61594
+ 00693920 bytes 5c101794
- 0066d5e4 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 0069392c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066d5e4 bytes 482c00d0
+ 0069392c bytes 082f00b0
- 0066d5e8 ["COPY", "tmp:0:8", ["const:528:8"]]
- 0066d5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693930 ["COPY", "tmp:0:8", ["const:650:8"]]
+ 00693930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 bytes 08a11491
+ 00693930 bytes 08411991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-684fd3c030b58aea379a93494174f5d7"></a>

### [`0066d63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d63c.md) → [`00693984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693984.md) FUN_00693984

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 95.57% / 新版 95.57%

CFGの説明率　旧版 80.95% / 新版 85.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066d740"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066d788"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00693a88"
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
      "00693a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00693a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:0066d740",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693a98"
      ]
    ]
  ],
  "added": [
    [
      "00693a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00693a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00693a88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00693a98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d63c.md#insn-0066d6e8) · [`0066d710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d63c.md#insn-0066d710) · [`0066d740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d63c.md#insn-0066d740)
- 新版 [`00693a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693984.md#insn-00693a30) · [`00693a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693984.md#insn-00693a58)

~~~diff
- 0066d6e8 ["INT_ADD", "register:40f0:8", ["const:66d6e8:8", "const:4:8"]]
- 0066d6e8 ["CALL", null, ["ram:457e1c:8"]]
+ 00693a30 ["INT_ADD", "register:40f0:8", ["const:693a30:8", "const:4:8"]]
+ 00693a30 ["CALL", null, ["ram:47acb4:8"]]
- 0066d6e8 bytes cda9f797
+ 00693a30 bytes a19cf797
- 0066d710 ["INT_ADD", "register:40f0:8", ["const:66d710:8", "const:4:8"]]
- 0066d710 ["CALL", null, ["ram:457e1c:8"]]
+ 00693a58 ["INT_ADD", "register:40f0:8", ["const:693a58:8", "const:4:8"]]
+ 00693a58 ["CALL", null, ["ram:47acb4:8"]]
- 0066d710 bytes c3a9f797
+ 00693a58 bytes 979cf797
- 0066d740 ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
- 0066d740 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdfa64c8b2558a0b545cdd1a8b689b9d"></a>

### [`0066d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md) → [`00693c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693c28.md) FUN_00693c28

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00693c4c",
      "incomplete_value": false,
      "site": "00693c4c",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d904",
      "incomplete_value": false,
      "site": "0066d904",
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
            "const:5a8:8"
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
      "00693c4c",
      "DATA",
      [
        "storage",
        "00bf75a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00693c4c",
      "DATA",
      [
        "storage",
        "00c746d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md#insn-0066d8f4) · [`0066d8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md#insn-0066d8fc) · [`0066d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md#insn-0066d900)
- 新版 [`00693c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693c28.md#insn-00693c3c) · [`00693c44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693c28.md#insn-00693c44) · [`00693c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693c28.md#insn-00693c48)

~~~diff
- 0066d8f4 ["INT_ADD", "register:40f0:8", ["const:66d8f4:8", "const:4:8"]]
- 0066d8f4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00693c3c ["INT_ADD", "register:40f0:8", ["const:693c3c:8", "const:4:8"]]
+ 00693c3c ["CALL", null, ["callee:00c57a90:8"]]
- 0066d8f4 bytes d3b51594
+ 00693c3c bytes 950f1794
- 0066d8fc ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00693c44 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066d8fc bytes 482c00d0
+ 00693c44 bytes 082f00b0
- 0066d900 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 0066d900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00693c48 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00693c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00693c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00693c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d900 bytes 08a11691
+ 00693c48 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22545d29967d6e0d8f7b8f486c023211"></a>

### [`0066e014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e014.md) → [`0069435c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069435c.md) FUN_0069435c

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00664634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664634.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068a96c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068a96c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 71.43% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e09c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006943e4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00694384",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0066e03c",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00694384",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00694394",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00694384",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00694394",
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

- 旧版 [`0066e03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e014.md#insn-0066e03c) · [`0066e04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e014.md#insn-0066e04c) · [`0066e080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e014.md#insn-0066e080)
- 新版 [`00694384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069435c.md#insn-00694384) · [`00694394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069435c.md#insn-00694394) · [`006943c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069435c.md#insn-006943c8)

~~~diff
- 0066e03c ["INT_ADD", "register:40f0:8", ["const:66e03c:8", "const:4:8"]]
- 0066e03c ["CALL", null, ["ram:457e1c:8"]]
+ 00694384 ["INT_ADD", "register:40f0:8", ["const:694384:8", "const:4:8"]]
+ 00694384 ["CALL", null, ["ram:47acb4:8"]]
- 0066e03c bytes 78a7f797
+ 00694384 bytes 4c9af797
- 0066e04c ["INT_ADD", "register:40f0:8", ["const:66e04c:8", "const:4:8"]]
- 0066e04c ["CALL", null, ["ram:457e1c:8"]]
+ 00694394 ["INT_ADD", "register:40f0:8", ["const:694394:8", "const:4:8"]]
+ 00694394 ["CALL", null, ["ram:47acb4:8"]]
- 0066e04c bytes 74a7f797
+ 00694394 bytes 489af797
- 0066e080 ["INT_ADD", "register:40f0:8", ["const:66e080:8", "const:4:8"]]
- 0066e080 ["CALL", null, ["callee:008b7984:8"]]
+ 006943c8 ["INT_ADD", "register:40f0:8", ["const:6943c8:8", "const:4:8"]]
+ 006943c8 ["CALL", null, ["callee:008b7984:8"]]
- 0066e080 bytes d9590894
+ 006943c8 bytes 6f8d0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97cc6481e412b69be0089efa0abb3289"></a>

### [`0066e1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md) → [`0069452c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069452c.md) FUN_0069452c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694550",
      "incomplete_value": false,
      "site": "00694550",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e208",
      "incomplete_value": false,
      "site": "0066e208",
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
            "const:828:8"
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
      "00694550",
      "DATA",
      [
        "storage",
        "00bf7828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694550",
      "DATA",
      [
        "storage",
        "00c74950",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md#insn-0066e1f8) · [`0066e200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md#insn-0066e200) · [`0066e204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md#insn-0066e204)
- 新版 [`00694540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069452c.md#insn-00694540) · [`00694548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069452c.md#insn-00694548) · [`0069454c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069452c.md#insn-0069454c)

~~~diff
- 0066e1f8 ["INT_ADD", "register:40f0:8", ["const:66e1f8:8", "const:4:8"]]
- 0066e1f8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00694540 ["INT_ADD", "register:40f0:8", ["const:694540:8", "const:4:8"]]
+ 00694540 ["CALL", null, ["callee:00c57a90:8"]]
- 0066e1f8 bytes 92b31594
+ 00694540 bytes 540d1794
- 0066e200 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00694548 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e200 bytes 482c00b0
+ 00694548 bytes 082f0090
- 0066e204 ["COPY", "tmp:0:8", ["const:828:8"]]
- 0066e204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069454c ["COPY", "tmp:0:8", ["const:950:8"]]
+ 0069454c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069454c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069454c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e204 bytes 08a12091
+ 0069454c bytes 08412591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc94d63a126b9ce4c406375bd239cccf"></a>

### [`0066e34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md) → [`00694694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694694.md) FUN_00694694

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006946b8",
      "incomplete_value": false,
      "site": "006946c0",
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
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e370",
      "incomplete_value": false,
      "site": "0066e378",
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
            "const:8a8:8"
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
      "006946c0",
      "DATA",
      [
        "storage",
        "00bf78a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006946c0",
      "DATA",
      [
        "storage",
        "00c749d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md#insn-0066e360) · [`0066e36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md#insn-0066e36c) · [`0066e370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md#insn-0066e370)
- 新版 [`006946a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694694.md#insn-006946a8) · [`006946b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694694.md#insn-006946b4) · [`006946b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694694.md#insn-006946b8)

~~~diff
- 0066e360 ["INT_ADD", "register:40f0:8", ["const:66e360:8", "const:4:8"]]
- 0066e360 ["CALL", null, ["callee:00c57a90:8"]]
+ 006946a8 ["INT_ADD", "register:40f0:8", ["const:6946a8:8", "const:4:8"]]
+ 006946a8 ["CALL", null, ["callee:00c57a90:8"]]
- 0066e360 bytes 38b31594
+ 006946a8 bytes fa0c1794
- 0066e36c ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006946b4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e36c bytes 482c00b0
+ 006946b4 bytes 082f0090
- 0066e370 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 0066e370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006946b8 ["COPY", "tmp:0:8", ["const:9d0:8"]]
+ 006946b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006946b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006946b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e370 bytes 08a12291
+ 006946b8 bytes 08412791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5f4a15583609fce5475696e0ebcabe0"></a>

### [`0066e3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e3c4.md) → [`0069470c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069470c.md) FUN_0069470c

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.04% / 新版 93.04%

CFGの説明率　旧版 41.30% / 新版 44.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e500"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e50c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694848"
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
      "0069475c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0066e498"
      ]
    ],
    [
      "006947b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:0066e498",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "0069475c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006947e0"
      ]
    ],
    [
      "006947b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006947e0",
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

- 旧版 [`0066e470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e3c4.md#insn-0066e470) · [`0066e498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e3c4.md#insn-0066e498) · [`0066e500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e3c4.md#insn-0066e500)
- 新版 [`006947b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/0069470c.md#insn-006947b8)

~~~diff
- 0066e470 ["INT_ADD", "register:40f0:8", ["const:66e470:8", "const:4:8"]]
- 0066e470 ["CALL", null, ["ram:457e1c:8"]]
+ 006947b8 ["INT_ADD", "register:40f0:8", ["const:6947b8:8", "const:4:8"]]
+ 006947b8 ["CALL", null, ["ram:47acb4:8"]]
- 0066e470 bytes 6ba6f797
+ 006947b8 bytes 3f99f797
- 0066e498 ["INT_ADD", "register:40f0:8", ["const:66e498:8", "const:4:8"]]
- 0066e498 ["CALL", null, ["ram:457e1c:8"]]
- 0066e498 bytes 61a6f797
- 0066e500 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0066e500 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0066e500 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 0066e500 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0066e500 bytes 4881889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39cd559ccd20c54475f592a176e190b1"></a>

### [`0066e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md) → [`006949b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/006949b0.md) FUN_006949b0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006949d4",
      "incomplete_value": false,
      "site": "006949d4",
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
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e68c",
      "incomplete_value": false,
      "site": "0066e68c",
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
            "const:928:8"
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
      "006949d4",
      "DATA",
      [
        "storage",
        "00bf7928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006949d4",
      "DATA",
      [
        "storage",
        "00c74a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md#insn-0066e67c) · [`0066e684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md#insn-0066e684) · [`0066e688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md#insn-0066e688)
- 新版 [`006949c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/006949b0.md#insn-006949c4) · [`006949cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/006949b0.md#insn-006949cc) · [`006949d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/006949b0.md#insn-006949d0)

~~~diff
- 0066e67c ["INT_ADD", "register:40f0:8", ["const:66e67c:8", "const:4:8"]]
- 0066e67c ["CALL", null, ["callee:00c57a90:8"]]
+ 006949c4 ["INT_ADD", "register:40f0:8", ["const:6949c4:8", "const:4:8"]]
+ 006949c4 ["CALL", null, ["callee:00c57a90:8"]]
- 0066e67c bytes 71b21594
+ 006949c4 bytes 330c1794
- 0066e684 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006949cc ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e684 bytes 482c00b0
+ 006949cc bytes 082f0090
- 0066e688 ["COPY", "tmp:0:8", ["const:928:8"]]
- 0066e688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006949d0 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 006949d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006949d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006949d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e688 bytes 08a12491
+ 006949d0 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a828b9e429a8cf5b8f19d8c7b8f99de3"></a>

### [`0066e6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e6b8.md) → [`00694a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a00.md) FUN_00694a00

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00694a08"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e6d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0066e6c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694a3c"
      ]
    ],
    [
      "unmatched:0066e6d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00694a08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00694a3c"
      ]
    ],
    [
      "00694a1c",
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

- 旧版 [`0066e6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e6b8.md#insn-0066e6c0) · [`0066e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e6b8.md#insn-0066e6d4)
- 新版 [`00694a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a00.md#insn-00694a08)

~~~diff
- 0066e6c0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0066e6c0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0066e6c0 bytes a1010054
- 0066e6d4 ["INT_ADD", "register:40f0:8", ["const:66e6d4:8", "const:4:8"]]
- 0066e6d4 ["CALL", null, ["ram:457e1c:8"]]
- 0066e6d4 bytes d2a5f797
+ 00694a08 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00694a08 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00694a08 bytes a1010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb42cf059479a053167f0bd418129f70"></a>

### [`0066e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md) → [`00694a6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a6c.md) FUN_00694a6c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

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
      "definition_site": "00694a90",
      "incomplete_value": false,
      "site": "00694a94",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e748",
      "incomplete_value": false,
      "site": "0066e74c",
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
            "const:9a8:8"
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
      "00694a94",
      "DATA",
      [
        "storage",
        "00bf79a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694a94",
      "DATA",
      [
        "storage",
        "00c74ad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md#insn-0066e738) · [`0066e744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md#insn-0066e744) · [`0066e748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md#insn-0066e748)
- 新版 [`00694a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a6c.md#insn-00694a80) · [`00694a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a6c.md#insn-00694a8c) · [`00694a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694a6c.md#insn-00694a90)

~~~diff
- 0066e738 ["INT_ADD", "register:40f0:8", ["const:66e738:8", "const:4:8"]]
- 0066e738 ["CALL", null, ["callee:00c57a90:8"]]
+ 00694a80 ["INT_ADD", "register:40f0:8", ["const:694a80:8", "const:4:8"]]
+ 00694a80 ["CALL", null, ["callee:00c57a90:8"]]
- 0066e738 bytes 42b21594
+ 00694a80 bytes 040c1794
- 0066e744 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00694a8c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e744 bytes 482c00b0
+ 00694a8c bytes 082f0090
- 0066e748 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0066e748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694a90 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00694a90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694a90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694a90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e748 bytes 08a12691
+ 00694a90 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab0e523917dffa11933be632ce86b61d"></a>

### [`0066e764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e764.md) → [`00694aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694aac.md) FUN_00694aac

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694ab0",
      "incomplete_value": false,
      "site": "00694ab4",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e768",
      "incomplete_value": false,
      "site": "0066e76c",
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
            "const:9a8:8"
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
      "00694ab4",
      "DATA",
      [
        "storage",
        "00bf79a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694ab4",
      "DATA",
      [
        "storage",
        "00c74ad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e764.md#insn-0066e764) · [`0066e768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e764.md#insn-0066e768)
- 新版 [`00694aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694aac.md#insn-00694aac) · [`00694ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694aac.md#insn-00694ab0)

~~~diff
- 0066e764 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00694aac ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e764 bytes 482c00b0
+ 00694aac bytes 082f0090
- 0066e768 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 0066e768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694ab0 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00694ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e768 bytes 08a12691
+ 00694ab0 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05e036d330d5105b39f0d057bd9cd5d3"></a>

### [`0066e93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e93c.md) → [`00694c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694c84.md) FUN_00694c84

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00694c90",
      "incomplete_value": false,
      "site": "00694c94",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e948",
      "incomplete_value": false,
      "site": "0066e94c",
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
            "const:a28:8"
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
      "00694c94",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694c94",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e93c.md#insn-0066e944) · [`0066e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e93c.md#insn-0066e948)
- 新版 [`00694c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694c84.md#insn-00694c8c) · [`00694c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694c84.md#insn-00694c90)

~~~diff
- 0066e944 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00694c8c ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066e944 bytes 492c00b0
+ 00694c8c bytes 092f0090
- 0066e948 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0066e948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00694c90 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00694c90 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00694c90 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00694c90 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e948 bytes 29a12891
+ 00694c90 bytes 29412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc1593f84d5f9ea65b21624737c15bf"></a>

### [`0066e960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e960.md) → [`00694ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ca8.md) FUN_00694ca8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0066e96c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00694cb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0066e988",
      "incomplete_value": true,
      "site": "0066e98c",
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
      "unmatched:0066e96c",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694cb4",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e960.md#insn-0066e96c) · [`0066e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e960.md#insn-0066e98c)
- 新版 [`00694cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ca8.md#insn-00694cd4) · [`00694cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ca8.md#insn-00694cb4)

~~~diff
- 0066e96c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0066e96c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0066e96c bytes 090000f9
- 0066e98c ["INT_ADD", "register:40f0:8", ["const:66e98c:8", "const:4:8"]]
- 0066e98c ["CALL", null, ["callee:00c57ab0:8"]]
+ 00694cd4 ["INT_ADD", "register:40f0:8", ["const:694cd4:8", "const:4:8"]]
+ 00694cd4 ["CALL", null, ["callee:00c57ab0:8"]]
- 0066e98c bytes b5b11594
+ 00694cd4 bytes 770b1794
+ 00694cb4 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00694cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00694cb4 bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d02ecf9fa69abc9923f07834bb0b5c"></a>

### [`0066e9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md) → [`00694ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ce8.md) FUN_00694ce8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00694d08",
      "incomplete_value": false,
      "site": "00694d10",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e9c0",
      "incomplete_value": false,
      "site": "0066e9c8",
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
            "const:a28:8"
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
      "00694d10",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694d10",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md#insn-0066e9b8) · [`0066e9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md#insn-0066e9bc) · [`0066e9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md#insn-0066e9c0)
- 新版 [`00694d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ce8.md#insn-00694d00) · [`00694d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ce8.md#insn-00694d04) · [`00694d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694ce8.md#insn-00694d08)

~~~diff
- 0066e9b8 ["INT_ADD", "register:40f0:8", ["const:66e9b8:8", "const:4:8"]]
- 0066e9b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00694d00 ["INT_ADD", "register:40f0:8", ["const:694d00:8", "const:4:8"]]
+ 00694d00 ["CALL", null, ["callee:00c57a90:8"]]
- 0066e9b8 bytes a2b11594
+ 00694d00 bytes 640b1794
- 0066e9bc ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00694d04 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066e9bc bytes 482c00b0
+ 00694d04 bytes 082f0090
- 0066e9c0 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0066e9c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694d08 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00694d08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694d08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694d08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 bytes 08a12891
+ 00694d08 bytes 08412d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55a14c398b331ba6498174713a0de640"></a>

### [`0066ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md) → [`00694da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694da0.md) FUN_00694da0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "00694db4",
      "incomplete_value": false,
      "site": "00694dbc",
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
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ea6c",
      "incomplete_value": false,
      "site": "0066ea74",
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
            "const:a28:8"
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
      "00694dbc",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00694dbc",
      "DATA",
      [
        "storage",
        "00c74b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ea68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md#insn-0066ea68) · [`0066ea6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md#insn-0066ea6c) · [`0066eaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md#insn-0066eaa0)
- 新版 [`00694db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694da0.md#insn-00694db0) · [`00694db4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694da0.md#insn-00694db4) · [`00694de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00694/00694da0.md#insn-00694de8)

~~~diff
- 0066ea68 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00694db0 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066ea68 bytes 482c00b0
+ 00694db0 bytes 082f0090
- 0066ea6c ["COPY", "tmp:0:8", ["const:a28:8"]]
- 0066ea6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00694db4 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00694db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00694db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00694db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c bytes 08a12891
+ 00694db4 bytes 08412d91
- 0066eaa0 ["INT_ADD", "register:40f0:8", ["const:66eaa0:8", "const:4:8"]]
- 0066eaa0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00694de8 ["INT_ADD", "register:40f0:8", ["const:694de8:8", "const:4:8"]]
+ 00694de8 ["CALL", null, ["callee:00c57a90:8"]]
- 0066eaa0 bytes 68b11594
+ 00694de8 bytes 2a0b1794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e28091fe4e1a84a7cdb2c3c1b70989b4"></a>

### [`0066ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef6c.md) → [`006952b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952b4.md) FUN_006952b4

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006952c0",
      "incomplete_value": false,
      "site": "006952c4",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ef78",
      "incomplete_value": false,
      "site": "0066ef7c",
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
            "const:ad8:8"
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
      "006952c4",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006952c4",
      "DATA",
      [
        "storage",
        "00c74c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ef74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef6c.md#insn-0066ef74) · [`0066ef78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef6c.md#insn-0066ef78)
- 新版 [`006952bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952b4.md#insn-006952bc) · [`006952c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952b4.md#insn-006952c0)

~~~diff
- 0066ef74 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 006952bc ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066ef74 bytes 492c00b0
+ 006952bc bytes e92e00f0
- 0066ef78 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0066ef78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006952c0 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 006952c0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006952c0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006952c0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 bytes 29612b91
+ 006952c0 bytes 29013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d9b22b230c75ea40f23784d1f4d721d"></a>

### [`0066ef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md) → [`006952d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952d8.md) FUN_006952d8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006952e0",
      "incomplete_value": false,
      "site": "006952e4",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ef98",
      "incomplete_value": false,
      "site": "0066ef9c",
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
            "const:ad8:8"
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
      "006952e4",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006952e4",
      "DATA",
      [
        "storage",
        "00c74c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ef94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md#insn-0066ef94) · [`0066ef98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md#insn-0066ef98) · [`0066efbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md#insn-0066efbc)
- 新版 [`006952dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952d8.md#insn-006952dc) · [`006952e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952d8.md#insn-006952e0) · [`00695304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006952d8.md#insn-00695304)

~~~diff
- 0066ef94 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 006952dc ["COPY", "register:4048:8", ["const:c74000:8"]]
- 0066ef94 bytes 492c00b0
+ 006952dc bytes e92e00f0
- 0066ef98 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0066ef98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006952e0 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 006952e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006952e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006952e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 bytes 29612b91
+ 006952e0 bytes 29013091
- 0066efbc ["INT_ADD", "register:40f0:8", ["const:66efbc:8", "const:4:8"]]
- 0066efbc ["CALL", null, ["callee:00c57ab0:8"]]
+ 00695304 ["INT_ADD", "register:40f0:8", ["const:695304:8", "const:4:8"]]
+ 00695304 ["CALL", null, ["callee:00c57ab0:8"]]
- 0066efbc bytes 29b01594
+ 00695304 bytes eb091794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a6382e255d3acaae476a8ef4417f105"></a>

### [`0066efd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md) → [`00695318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695318.md) FUN_00695318

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00695338",
      "incomplete_value": false,
      "site": "00695340",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066eff0",
      "incomplete_value": false,
      "site": "0066eff8",
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
            "const:ad8:8"
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
      "00695340",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00695340",
      "DATA",
      [
        "storage",
        "00c74c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066efe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md#insn-0066efe8) · [`0066efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md#insn-0066efec) · [`0066eff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md#insn-0066eff0)
- 新版 [`00695330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695318.md#insn-00695330) · [`00695334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695318.md#insn-00695334) · [`00695338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695318.md#insn-00695338)

~~~diff
- 0066efe8 ["INT_ADD", "register:40f0:8", ["const:66efe8:8", "const:4:8"]]
- 0066efe8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00695330 ["INT_ADD", "register:40f0:8", ["const:695330:8", "const:4:8"]]
+ 00695330 ["CALL", null, ["callee:00c57a90:8"]]
- 0066efe8 bytes 16b01594
+ 00695330 bytes d8091794
- 0066efec ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00695334 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066efec bytes 482c00b0
+ 00695334 bytes e82e00f0
- 0066eff0 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0066eff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00695338 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 00695338 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00695338 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00695338 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 bytes 08612b91
+ 00695338 bytes 08013091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2916006fb04c3ba1ac954535270f662f"></a>

### [`0066f090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md) → [`006953d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006953d8.md) FUN_006953d8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

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
      "definition_site": "006953ec",
      "incomplete_value": false,
      "site": "006953f4",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066f0a4",
      "incomplete_value": false,
      "site": "0066f0ac",
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
            "const:ad8:8"
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
      "006953f4",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006953f4",
      "DATA",
      [
        "storage",
        "00c74c00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066f0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md#insn-0066f0a0) · [`0066f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md#insn-0066f0a4) · [`0066f0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md#insn-0066f0e0)
- 新版 [`006953e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006953d8.md#insn-006953e8) · [`006953ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006953d8.md#insn-006953ec) · [`00695428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006953d8.md#insn-00695428)

~~~diff
- 0066f0a0 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006953e8 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066f0a0 bytes 482c0090
+ 006953e8 bytes e82e00f0
- 0066f0a4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
- 0066f0a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006953ec ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 006953ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006953ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006953ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 bytes 08612b91
+ 006953ec bytes 08013091
- 0066f0e0 ["INT_ADD", "register:40f0:8", ["const:66f0e0:8", "const:4:8"]]
- 0066f0e0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00695428 ["INT_ADD", "register:40f0:8", ["const:695428:8", "const:4:8"]]
+ 00695428 ["CALL", null, ["callee:00c57a90:8"]]
- 0066f0e0 bytes d8af1594
+ 00695428 bytes 9a091794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65691514fda7668c5e190b2ee892e62a"></a>

### [`0066f184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md) → [`006954cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md) FUN_006954cc

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 24件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 86.01% / 新版 86.01%

CFGの説明率　旧版 28.57% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066f514"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0069585c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0066f20c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0066f1f4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:0066f1f8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:0066f200",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0069553c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00695540",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00695548",
      "PARAM",
      [
        "storage",
        "00c74bd8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066f20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md#insn-0066f20c) · [`0066f22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md#insn-0066f22c) · [`0066f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md#insn-0066f258)
- 新版 [`006955a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md#insn-006955a0)

~~~diff
- 0066f20c ["INT_ADD", "register:40f0:8", ["const:66f20c:8", "const:4:8"]]
- 0066f20c ["CALL", null, ["callee:00c58210:8"]]
- 0066f20c bytes 6db11594
- 0066f22c ["INT_ADD", "register:40f0:8", ["const:66f22c:8", "const:4:8"]]
- 0066f22c ["CALL", null, ["ram:66f824:8"]]
- 0066f22c bytes 7e010094
- 0066f258 ["INT_ADD", "register:40f0:8", ["const:66f258:8", "const:4:8"]]
- 0066f258 ["CALL", null, ["callee:0046a8a8:8"]]
+ 006955a0 ["INT_ADD", "register:40f0:8", ["const:6955a0:8", "const:4:8"]]
+ 006955a0 ["CALL", null, ["callee:0046a8a8:8"]]
- 0066f258 bytes ee61f797
+ 006955a0 bytes c254f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fa0e3c4827a354bc2139d52eb129c76"></a>

### [`0066f668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f668.md) → [`006959b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md) FUN_006959b0

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`0066f184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md) [`00670388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md) [`00671c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md) [`00672ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md) · 呼出先 3件 [`005b3d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3d60.md) [`0066fbc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fbc8.md) [`00bdd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9d0.md)
- 新版 呼出元 4件 [`006954cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006954cc.md) [`006966d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006966d0.md) [`00697f94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f94.md) [`0069923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/0069923c.md) · 呼出先 3件 [`005d8a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8a2c.md) [`00695f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695f10.md) [`00c5a420`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a420.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 73.08% / 新版 70.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00695aa0",
      "incomplete_value": true,
      "site": "00695aa8",
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
            "const:10:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0066f760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f668.md#insn-0066f760) · [`0066f6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f668.md#insn-0066f6a0) · [`0066f6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f668.md#insn-0066f6b8)
- 新版 [`00695aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md#insn-00695aa8) · [`006959e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md#insn-006959e8) · [`00695a00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/006959b0.md#insn-00695a00)

~~~diff
- 0066f760 ["INT_ADD", "register:40f0:8", ["const:66f760:8", "const:4:8"]]
- 0066f760 ["CALL", null, ["callee:00695f10:8"]]
+ 00695aa8 ["INT_ADD", "register:40f0:8", ["const:695aa8:8", "const:4:8"]]
+ 00695aa8 ["CALL", null, ["callee:00695f10:8"]]
- 0066f760 bytes 1a010094
+ 00695aa8 bytes 1a010094
- 0066f6a0 ["BRANCH", null, ["local:b12:8"]]
+ 006959e8 ["BRANCH", null, ["local:b13:8"]]
- 0066f6a0 bytes 28000014
+ 006959e8 bytes 28000014
- 0066f6b8 ["BRANCH", null, ["local:b12:8"]]
+ 00695a00 ["BRANCH", null, ["local:b13:8"]]
- 0066f6b8 bytes 22000014
+ 00695a00 bytes 22000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30a10dc0ad854bf8e28fd52c021a10db"></a>

### [`0066f794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f794.md) → [`00695adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695adc.md) FUN_00695adc

採用 · 移動量 `+0x26348` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 46.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0066f7ec",
      "incomplete_value": false,
      "site": "0066f7f0",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "0066f7e8",
      "incomplete_value": true,
      "site": "0066f7f0",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0066f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f794.md#insn-0066f7f0) · [`0066f7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f794.md#insn-0066f7ac) · [`0066f7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f794.md#insn-0066f7b8)
- 新版 [`00695b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695adc.md#insn-00695b38) · [`00695af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695adc.md#insn-00695af4) · [`00695b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695adc.md#insn-00695b00)

~~~diff
- 0066f7f0 ["INT_ADD", "register:40f0:8", ["const:66f7f0:8", "const:4:8"]]
- 0066f7f0 ["CALL", null, ["callee:00c538e0:8"]]
+ 00695b38 ["INT_ADD", "register:40f0:8", ["const:695b38:8", "const:4:8"]]
+ 00695b38 ["CALL", null, ["callee:00c538e0:8"]]
- 0066f7f0 bytes a89d1594
+ 00695b38 bytes 6af71694
- 0066f7ac ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 0066f7ac ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00695af4 ["INT_NOTEQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00695af4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0066f7ac bytes 760100b5
+ 00695af4 bytes 760100b5
- 0066f7b8 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0066f7b8 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00695b00 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00695b00 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0066f7b8 bytes e00200b4
+ 00695b00 bytes e00200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aff600755df6bba1ae7c834f709a29d"></a>

### [`0066fb38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fb38.md) → [`00695e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695e80.md) FUN_00695e80

採用 · 移動量 `+0x26348` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change` · `reordered`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 38.46% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0066fb5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00695ea4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0066fb8c",
      "incomplete_value": true,
      "site": "0066fb94",
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
            "const:8:8"
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
      "unmatched:0066fb5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f00"
      ]
    ]
  ],
  "added": [
    [
      "00695ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00695f00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066fb5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fb38.md#insn-0066fb5c) · [`0066fb94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fb38.md#insn-0066fb94)
- 新版 [`00695edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695e80.md#insn-00695edc) · [`00695ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695e80.md#insn-00695ea4)

~~~diff
- 0066fb5c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0066fb5c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 0066fb5c bytes e00200b4
- 0066fb94 ["INT_ADD", "register:40f0:8", ["const:66fb94:8", "const:4:8"]]
- 0066fb94 ["CALL", null, ["callee:00c538e0:8"]]
+ 00695edc ["INT_ADD", "register:40f0:8", ["const:695edc:8", "const:4:8"]]
+ 00695edc ["CALL", null, ["callee:00c538e0:8"]]
- 0066fb94 bytes bf9c1594
+ 00695edc bytes 81f61694
+ 00695ea4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00695ea4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00695ea4 bytes e00200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0ffd721468b5022b696060007bcda9"></a>

### [`0066fef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md) → [`00696238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696238.md) FUN_00696238

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00696258",
      "incomplete_value": false,
      "site": "0069625c",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ff10",
      "incomplete_value": false,
      "site": "0066ff14",
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
            "const:b58:8"
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
      "0069625c",
      "DATA",
      [
        "storage",
        "00bf7b58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069625c",
      "DATA",
      [
        "storage",
        "00c74c80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ff04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md#insn-0066ff04) · [`0066ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md#insn-0066ff0c) · [`0066ff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md#insn-0066ff10)
- 新版 [`0069624c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696238.md#insn-0069624c) · [`00696254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696238.md#insn-00696254) · [`00696258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696238.md#insn-00696258)

~~~diff
- 0066ff04 ["INT_ADD", "register:40f0:8", ["const:66ff04:8", "const:4:8"]]
- 0066ff04 ["CALL", null, ["callee:00c57a90:8"]]
+ 0069624c ["INT_ADD", "register:40f0:8", ["const:69624c:8", "const:4:8"]]
+ 0069624c ["CALL", null, ["callee:00c57a90:8"]]
- 0066ff04 bytes 4fac1594
+ 0069624c bytes 11061794
- 0066ff0c ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00696254 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 0066ff0c bytes 482c0090
+ 00696254 bytes e82e00d0
- 0066ff10 ["COPY", "tmp:0:8", ["const:b58:8"]]
- 0066ff10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696258 ["COPY", "tmp:0:8", ["const:c80:8"]]
+ 00696258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 bytes 08612d91
+ 00696258 bytes 08013291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c60e435e42d1ef2cbc50811de54dba"></a>

### [`0067006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md) → [`006963b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006963b4.md) FUN_006963b4

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006963d8",
      "incomplete_value": false,
      "site": "006963d8",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670090",
      "incomplete_value": false,
      "site": "00670090",
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
            "const:bd8:8"
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
      "006963d8",
      "DATA",
      [
        "storage",
        "00bf7bd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006963d8",
      "DATA",
      [
        "storage",
        "00c74d00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md#insn-00670080) · [`00670088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md#insn-00670088) · [`0067008c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md#insn-0067008c)
- 新版 [`006963c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006963b4.md#insn-006963c8) · [`006963d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006963b4.md#insn-006963d0) · [`006963d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006963b4.md#insn-006963d4)

~~~diff
- 00670080 ["INT_ADD", "register:40f0:8", ["const:670080:8", "const:4:8"]]
- 00670080 ["CALL", null, ["callee:00c57a90:8"]]
+ 006963c8 ["INT_ADD", "register:40f0:8", ["const:6963c8:8", "const:4:8"]]
+ 006963c8 ["CALL", null, ["callee:00c57a90:8"]]
- 00670080 bytes f0ab1594
+ 006963c8 bytes b2051794
- 00670088 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006963d0 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00670088 bytes 282c00f0
+ 006963d0 bytes e82e00d0
- 0067008c ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 0067008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006963d4 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 006963d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006963d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006963d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067008c bytes 08612f91
+ 006963d4 bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6955aa835146443bebce207921be5104"></a>

### [`006700bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md) → [`00696404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696404.md) FUN_00696404

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) [`0066ab18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066ab18.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) [`00690e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00690/00690e60.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 70.00% / 新版 63.64%

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
      "site": "00696438",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006700f0",
      "value": [
        "leaf",
        "ram:457e1c:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00696468",
      "incomplete_value": true,
      "site": "0069646c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670120",
      "incomplete_value": true,
      "site": "00670124",
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
            "const:2f88:8"
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
      "00696438",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00696438",
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

- 旧版 [`006700f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md#insn-006700f0) · [`00670124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md#insn-00670124) · [`006700ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md#insn-006700ec)
- 新版 [`00696438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696404.md#insn-00696438) · [`0069646c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696404.md#insn-0069646c) · [`00696434`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696404.md#insn-00696434)

~~~diff
- 006700f0 ["INT_ADD", "register:40f0:8", ["const:6700f0:8", "const:4:8"]]
- 006700f0 ["CALL", null, ["ram:457e1c:8"]]
+ 00696438 ["INT_ADD", "register:40f0:8", ["const:696438:8", "const:4:8"]]
+ 00696438 ["CALL", null, ["ram:47acb4:8"]]
- 006700f0 bytes 4b9ff797
+ 00696438 bytes 1f92f797
- 00670124 ["INT_ADD", "register:40f0:8", ["const:670124:8", "const:4:8"]]
- 00670124 ["CALL", null, ["callee:00a83068:8"]]
+ 0069646c ["INT_ADD", "register:40f0:8", ["const:69646c:8", "const:4:8"]]
+ 0069646c ["CALL", null, ["callee:00a83068:8"]]
- 00670124 bytes 2dd40e94
+ 0069646c bytes ffb20f94
- 006700ec ["INT_ADD", "register:40f0:8", ["const:6700ec:8", "const:4:8"]]
- 006700ec ["CALL", null, ["callee:008b9134:8"]]
+ 00696434 ["INT_ADD", "register:40f0:8", ["const:696434:8", "const:4:8"]]
+ 00696434 ["CALL", null, ["callee:008b9134:8"]]
- 006700ec bytes a5570894
+ 00696434 bytes 408b0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe93288b31652b613caa1bcc93cbea4f"></a>

### [`006701a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md) → [`006964f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006964f0.md) FUN_006964f0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00696514",
      "incomplete_value": false,
      "site": "00696514",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006701cc",
      "incomplete_value": false,
      "site": "006701cc",
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
            "const:c58:8"
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
      "00696514",
      "DATA",
      [
        "storage",
        "00bf7c58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696514",
      "DATA",
      [
        "storage",
        "00c74d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006701bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md#insn-006701bc) · [`006701c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md#insn-006701c4) · [`006701c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md#insn-006701c8)
- 新版 [`00696504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006964f0.md#insn-00696504) · [`0069650c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006964f0.md#insn-0069650c) · [`00696510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/006964f0.md#insn-00696510)

~~~diff
- 006701bc ["INT_ADD", "register:40f0:8", ["const:6701bc:8", "const:4:8"]]
- 006701bc ["CALL", null, ["callee:00c57a90:8"]]
+ 00696504 ["INT_ADD", "register:40f0:8", ["const:696504:8", "const:4:8"]]
+ 00696504 ["CALL", null, ["callee:00c57a90:8"]]
- 006701bc bytes a1ab1594
+ 00696504 bytes 63051794
- 006701c4 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 0069650c ["COPY", "register:4040:8", ["const:c74000:8"]]
- 006701c4 bytes 282c00f0
+ 0069650c bytes e82e00d0
- 006701c8 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 006701c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006701c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006701c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696510 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00696510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006701c8 bytes 08613191
+ 00696510 bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4554593244804efcf3514fad67dce05"></a>

### [`00670a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a7c.md) → [`00696dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696dc4.md) FUN_00696dc4

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00696dc8",
      "incomplete_value": false,
      "site": "00696dcc",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670a80",
      "incomplete_value": false,
      "site": "00670a84",
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
            "const:d58:8"
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
      "00696dcc",
      "DATA",
      [
        "storage",
        "00bf7d58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00696dcc",
      "DATA",
      [
        "storage",
        "00c74e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a7c.md#insn-00670a7c) · [`00670a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a7c.md#insn-00670a80)
- 新版 [`00696dc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696dc4.md#insn-00696dc4) · [`00696dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696dc4.md#insn-00696dc8)

~~~diff
- 00670a7c ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00696dc4 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00670a7c bytes 282c00f0
+ 00696dc4 bytes e82e00d0
- 00670a80 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00670a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00670a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00670a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00696dc8 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00696dc8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00696dc8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00696dc8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00670a80 bytes 08613591
+ 00696dc8 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30f78af118cfb6f62b843504911d8383"></a>

### [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) → [`00696de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696de4.md) FUN_00696de4

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md) [`0066a360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md) [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md) [`006906a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00690/006906a8.md) [`00697128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 53.33% / 新版 45.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 3件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00696f68",
      "incomplete_value": true,
      "site": "00696f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670c20",
      "incomplete_value": true,
      "site": "00670c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00696f74",
      "incomplete_value": false,
      "site": "00696f7c",
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
            "const:d2a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670c2c",
      "incomplete_value": false,
      "site": "00670c34",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00696f9c",
      "incomplete_value": false,
      "site": "00696fa8",
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
            "const:ed1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670c54",
      "incomplete_value": false,
      "site": "00670c60",
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
            "const:917:8"
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
      "unmatched:00670ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696e60"
      ]
    ],
    [
      "unmatched:00670ad8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696e60"
      ]
    ],
    [
      "unmatched:00670ae0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b9134"
      ]
    ]
  ],
  "added": [
    [
      "00696e18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696e60"
      ]
    ],
    [
      "00696e20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00696e60"
      ]
    ],
    [
      "00696e28",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b9134"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md#insn-00670ad0) · [`00670ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md#insn-00670ad8) · [`00670ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md#insn-00670ae0)

~~~diff
- 00670ad0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00670ad0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00670ad0 bytes 41020054
- 00670ad8 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00670ad8 bytes 00020054
- 00670ae0 ["INT_ADD", "register:40f0:8", ["const:670ae0:8", "const:4:8"]]
- 00670ae0 ["CALL", null, ["callee:008b9134:8"]]
- 00670ae0 bytes 28550894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e4d64a4af52886ca0a6f3cdeee15833"></a>

### [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md) → [`00697128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md) FUN_00697128

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) [`006f3154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f3/006f3154.md) [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) [`008d9aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d9/008d9aa4.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) · 呼出先 5件 [`00670f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md) [`00adc094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc094.md) [`00adc120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc120.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 5件 [`00696de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696de4.md) [`0071d1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071d/0071d1bc.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 5件 [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md) [`00b3baf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3baf8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 27.78% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00670eb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006971f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00697158",
      "incomplete_value": true,
      "site": "0069715c",
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
            "const:c400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670e10",
      "incomplete_value": true,
      "site": "00670e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
          ],
          [
            "live",
            "register:40b0:8"
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
      "unmatched:00670eb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069724c"
      ]
    ]
  ],
  "added": [
    [
      "006971f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069724c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md#insn-00670e14) · [`00670e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md#insn-00670e7c) · [`00670eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md#insn-00670eb0)
- 新版 [`0069715c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md#insn-0069715c) · [`006971c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md#insn-006971c4)

~~~diff
- 00670e14 ["INT_ADD", "register:40f0:8", ["const:670e14:8", "const:4:8"]]
- 00670e14 ["CALL", null, ["callee:00b3ba6c:8"]]
+ 0069715c ["INT_ADD", "register:40f0:8", ["const:69715c:8", "const:4:8"]]
+ 0069715c ["CALL", null, ["callee:00b3ba6c:8"]]
- 00670e14 bytes a0ac1194
+ 0069715c bytes 44921294
- 00670e7c ["INT_ADD", "register:40f0:8", ["const:670e7c:8", "const:4:8"]]
- 00670e7c ["CALL", null, ["callee:00697250:8"]]
+ 006971c4 ["INT_ADD", "register:40f0:8", ["const:6971c4:8", "const:4:8"]]
+ 006971c4 ["CALL", null, ["callee:00697250:8"]]
- 00670e7c bytes 23000094
+ 006971c4 bytes 23000094
- 00670eb0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00670eb0 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00670eb0 bytes a1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b3b9e844c7f5433aeb4e67d591af6f4"></a>

### [`00670f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md) → [`00697250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697250.md) FUN_00697250

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md) [`006f42ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f42ec.md) [`006f4518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f4518.md) [`006f478c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f4/006f478c.md) · 呼出先 6件 [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) [`0073f368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f368.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 4件 [`00697128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697128.md) [`0071e354`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e354.md) [`0071e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e580.md) [`0071e7f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071e/0071e7f4.md) · 呼出先 6件 [`00767108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767108.md) [`00767c74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00767/00767c74.md) [`00769674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769674.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 62.90% / 新版 62.90%

CFGの説明率　旧版 17.65% / 新版 23.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00670f38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00697280"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00670f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00670f38",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00670f3c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073f368"
      ]
    ],
    [
      "unmatched:00670f40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006972c8"
      ]
    ]
  ],
  "added": [
    [
      "00697280",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00697284",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00769674"
      ]
    ],
    [
      "00697288",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006972c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md#insn-00670f38) · [`00670f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md#insn-00670f3c) · [`00670f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md#insn-00670f40)

~~~diff
- 00670f38 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00670f38 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00670f38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00670f38 bytes a8831ff8
- 00670f3c ["INT_ADD", "register:40f0:8", ["const:670f3c:8", "const:4:8"]]
- 00670f3c ["CALL", null, ["ram:73f368:8"]]
- 00670f3c bytes 0b390394
- 00670f40 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00670f40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00670f40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00670f40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00670f40 bytes 00020036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebfa48d6f6d05a44a38ff6fd1b15c33f"></a>

### [`0067102c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md) → [`00697374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697374.md) FUN_00697374

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00697394",
      "incomplete_value": false,
      "site": "00697398",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067104c",
      "incomplete_value": false,
      "site": "00671050",
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
            "const:dd8:8"
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
      "00697398",
      "DATA",
      [
        "storage",
        "00bf7dd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697398",
      "DATA",
      [
        "storage",
        "00c74f00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md#insn-00671040) · [`00671048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md#insn-00671048) · [`0067104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md#insn-0067104c)
- 新版 [`00697388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697374.md#insn-00697388) · [`00697390`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697374.md#insn-00697390) · [`00697394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697374.md#insn-00697394)

~~~diff
- 00671040 ["INT_ADD", "register:40f0:8", ["const:671040:8", "const:4:8"]]
- 00671040 ["CALL", null, ["callee:00c57a90:8"]]
+ 00697388 ["INT_ADD", "register:40f0:8", ["const:697388:8", "const:4:8"]]
+ 00697388 ["CALL", null, ["callee:00c57a90:8"]]
- 00671040 bytes 00a81594
+ 00697388 bytes c2011794
- 00671048 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00697390 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00671048 bytes 282c00d0
+ 00697390 bytes e82e00b0
- 0067104c ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 0067104c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067104c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067104c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00697394 ["COPY", "tmp:0:8", ["const:f00:8"]]
+ 00697394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00697394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00697394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067104c bytes 08613791
+ 00697394 bytes 08013c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-865cc8197fadaddb4e0cd106ef5ba2b9"></a>

### [`00671084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671084.md) → [`006973cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006973cc.md) FUN_006973cc

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d64.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 63.64% / 新版 63.64%

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
      "site": "00697404",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006710bc",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "site": "0069741c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006710d4",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00697404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "0069741c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00697404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "0069741c",
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

- 旧版 [`006710bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671084.md#insn-006710bc) · [`006710d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671084.md#insn-006710d4) · [`006710a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671084.md#insn-006710a0)
- 新版 [`00697404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006973cc.md#insn-00697404) · [`0069741c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006973cc.md#insn-0069741c) · [`006973e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006973cc.md#insn-006973e8)

~~~diff
- 006710bc ["INT_ADD", "register:40f0:8", ["const:6710bc:8", "const:4:8"]]
- 006710bc ["CALL", null, ["ram:457e1c:8"]]
+ 00697404 ["INT_ADD", "register:40f0:8", ["const:697404:8", "const:4:8"]]
+ 00697404 ["CALL", null, ["ram:47acb4:8"]]
- 006710bc bytes 589bf797
+ 00697404 bytes 2c8ef797
- 006710d4 ["INT_ADD", "register:40f0:8", ["const:6710d4:8", "const:4:8"]]
- 006710d4 ["CALL", null, ["ram:457e1c:8"]]
+ 0069741c ["INT_ADD", "register:40f0:8", ["const:69741c:8", "const:4:8"]]
+ 0069741c ["CALL", null, ["ram:47acb4:8"]]
- 006710d4 bytes 529bf797
+ 0069741c bytes 268ef797
- 006710a0 ["INT_ADD", "register:40f0:8", ["const:6710a0:8", "const:4:8"]]
- 006710a0 ["CALL", null, ["callee:008b6f04:8"]]
+ 006973e8 ["INT_ADD", "register:40f0:8", ["const:6973e8:8", "const:4:8"]]
+ 006973e8 ["CALL", null, ["callee:008b6f04:8"]]
- 006710a0 bytes 314b0894
+ 006973e8 bytes c77e0894
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-315a4f506bd346bb11f2a2ef01549782"></a>

### [`00671160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671160.md) → [`006974a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006974a8.md) FUN_006974a8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006974ac",
      "incomplete_value": false,
      "site": "006974b0",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671164",
      "incomplete_value": false,
      "site": "00671168",
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
            "const:e58:8"
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
      "006974b0",
      "DATA",
      [
        "storage",
        "00bf7e58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006974b0",
      "DATA",
      [
        "storage",
        "00c74f80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671160.md#insn-00671160) · [`00671164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671160.md#insn-00671164)
- 新版 [`006974a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006974a8.md#insn-006974a8) · [`006974ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006974a8.md#insn-006974ac)

~~~diff
- 00671160 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 006974a8 ["COPY", "register:4040:8", ["const:c74000:8"]]
- 00671160 bytes 282c00d0
+ 006974a8 bytes e82e00b0
- 00671164 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00671164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006974ac ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 006974ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006974ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006974ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671164 bytes 08613991
+ 006974ac bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81b6379be54b4dedf35793bfb1497d79"></a>

### [`00671220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671220.md) → [`00697568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697568.md) FUN_00697568

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00697574",
      "incomplete_value": false,
      "site": "00697578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067122c",
      "incomplete_value": false,
      "site": "00671230",
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
            "const:ed8:8"
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
      "00697578",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697578",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671220.md#insn-00671228) · [`0067122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671220.md#insn-0067122c)
- 新版 [`00697570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697568.md#insn-00697570) · [`00697574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697568.md#insn-00697574)

~~~diff
- 00671228 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00697570 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 00671228 bytes 292c00d0
+ 00697570 bytes e92e00d0
- 0067122c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0067122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0067122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0067122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00697574 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00697574 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00697574 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00697574 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0067122c bytes 29613b91
+ 00697574 bytes 29010091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13d5707ff93ab58e1973c41f530d2913"></a>

### [`00671244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md) → [`0069758c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/0069758c.md) FUN_0069758c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00697594",
      "incomplete_value": false,
      "site": "00697598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067124c",
      "incomplete_value": false,
      "site": "00671250",
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
            "const:ed8:8"
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
      "00697598",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697598",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md#insn-00671248) · [`0067124c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md#insn-0067124c) · [`00671270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md#insn-00671270)
- 新版 [`00697590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/0069758c.md#insn-00697590) · [`00697594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/0069758c.md#insn-00697594) · [`006975b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/0069758c.md#insn-006975b8)

~~~diff
- 00671248 ["COPY", "register:4048:8", ["const:bf7000:8"]]
+ 00697590 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 00671248 bytes 292c00d0
+ 00697590 bytes e92e00d0
- 0067124c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 0067124c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0067124c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0067124c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00697594 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00697594 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00697594 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00697594 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0067124c bytes 29613b91
+ 00697594 bytes 29010091
- 00671270 ["INT_ADD", "register:40f0:8", ["const:671270:8", "const:4:8"]]
- 00671270 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006975b8 ["INT_ADD", "register:40f0:8", ["const:6975b8:8", "const:4:8"]]
+ 006975b8 ["CALL", null, ["callee:00c57ab0:8"]]
- 00671270 bytes 7ca71594
+ 006975b8 bytes 3e011794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b27aca5ccfd1fabeb36ecc0781bf870"></a>

### [`00671284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671284.md) → [`006975cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006975cc.md) FUN_006975cc

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 36.36% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006712ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006975f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006712cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006712ac",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006712cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697640"
      ]
    ]
  ],
  "added": [
    [
      "006975f4",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ],
    [
      "00697614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697640"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006712ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671284.md#insn-006712ac) · [`006712cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671284.md#insn-006712cc) · [`006712d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671284.md#insn-006712d8)
- 新版 [`00697620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/006975cc.md#insn-00697620)

~~~diff
- 006712ac ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006712ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006712ac bytes 080000f9
- 006712cc ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 006712cc bytes 60010054
- 006712d8 ["INT_ADD", "register:40f0:8", ["const:6712d8:8", "const:4:8"]]
- 006712d8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00697620 ["INT_ADD", "register:40f0:8", ["const:697620:8", "const:4:8"]]
+ 00697620 ["CALL", null, ["callee:00c57a90:8"]]
- 006712d8 bytes 5aa71594
+ 00697620 bytes 1c011794
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db4550d5b0514f66e2d627aa8443737e"></a>

### [`0067133c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md) → [`00697684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697684.md) FUN_00697684

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 5.56% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671358"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671360"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671364"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00671358",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006976a0",
      "DATA",
      [
        "storage",
        "00c75000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md#insn-00671358) · [`00671360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md#insn-00671360) · [`00671364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md#insn-00671364)

~~~diff
- 00671358 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00671358 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00671358 bytes 280000f9
- 00671360 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00671360 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00671360 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:18:8"]]
- 00671360 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 00671360 bytes 9f8e01f8
- 00671364 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00671364 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00671364 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00671364 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00671364 bytes 9ffe00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235d317d2e754f8f7ea8b8f838b990fc"></a>

### [`006713f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/006713f4.md) → [`0069773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/0069773c.md) FUN_0069773c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006713fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006713fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671400"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006713f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069776c"
      ]
    ],
    [
      "unmatched:006713fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00671400",
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
      "00697740",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069776c"
      ]
    ],
    [
      "00697744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00697748",
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

- 旧版 [`006713f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/006713f4.md#insn-006713f8) · [`006713fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/006713f4.md#insn-006713fc) · [`00671400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/006713f4.md#insn-00671400)

~~~diff
- 006713f8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006713f8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 006713f8 bytes 680100b4
- 006713fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006713fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006713fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006713fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006713fc bytes fd7bbea9
- 00671400 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00671400 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00671400 bytes f30b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f60666ef6f4d36c8c06a1a1a268fa5cf"></a>

### [`00671a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md) → [`00697de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697de0.md) FUN_00697de0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671ac0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671ad4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671adc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00671ac0",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00671ae8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697e5c"
      ]
    ]
  ],
  "added": [
    [
      "00697e08",
      "DATA",
      [
        "storage",
        "00c75080",
        null,
        "undefined *"
      ]
    ],
    [
      "00697e30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00697e5c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md#insn-00671ac0) · [`00671ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md#insn-00671ad4) · [`00671adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md#insn-00671adc)

~~~diff
- 00671ac0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00671ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00671ac0 bytes 080000f9
- 00671ad4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00671ad4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00671ad4 bytes 0080803c
- 00671adc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 00671adc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00671adc bytes 091800b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17809d74b80bdc4662501ec4fd70f3ba"></a>

### [`00671b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md) → [`00697ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697ea0.md) FUN_00697ea0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00692484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00692/00692484.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 30.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671b74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00671b84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00671b74",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00697ebc",
      "DATA",
      [
        "storage",
        "00c75080",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md#insn-00671b74) · [`00671b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md#insn-00671b80) · [`00671b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md#insn-00671b84)

~~~diff
- 00671b74 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00671b74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00671b74 bytes 280000f9
- 00671b80 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00671b80 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00671b80 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:20:8"]]
- 00671b80 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 00671b80 bytes 9f0e02f8
- 00671b84 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00671b84 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:fffffffffffffff8:8"]]
- 00671b84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00671b84 bytes 88821fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e48fccf93d1777e0a21f99c55e1d142"></a>

### [`00671c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c00.md) → [`00697f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f48.md) FUN_00697f48

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00671c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c00.md#insn-00671c08)
- 新版 [`00697f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f48.md#insn-00697f50)

~~~diff
- 00671c08 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00671c08 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00697f50 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00697f50 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00671c08 bytes 600000b4
+ 00697f50 bytes 600000b4
~~~


<a id="compare-3535d6c3670466c3f590e06d19b5c16f"></a>

### [`00671c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c18.md) → [`00697f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f60.md) FUN_00697f60

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0068f598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068f/0068f598.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 16.67% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00697f7c",
      "incomplete_value": true,
      "site": "00697f80",
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


#### 変更候補の命令位置

- 旧版 [`00671c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c18.md#insn-00671c38) · [`00671c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c18.md#insn-00671c1c)
- 新版 [`00697f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f60.md#insn-00697f80) · [`00697f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00697/00697f60.md#insn-00697f64)

~~~diff
- 00671c38 ["INT_ADD", "register:40f0:8", ["const:671c38:8", "const:4:8"]]
- 00671c38 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00697f80 ["INT_ADD", "register:40f0:8", ["const:697f80:8", "const:4:8"]]
+ 00697f80 ["CALL", null, ["callee:00c57ab0:8"]]
- 00671c38 bytes 0aa51594
+ 00697f80 bytes ccfe1694
- 00671c1c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00671c1c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00697f64 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00697f64 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00671c1c bytes 680100b4
+ 00697f64 bytes 680100b4
~~~


<a id="compare-4de54d41ac19dad006548745f1fa6f7a"></a>

### [`006723a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md) → [`006986f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006986f0.md) FUN_006986f0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698710",
      "incomplete_value": false,
      "site": "00698714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006723c8",
      "incomplete_value": false,
      "site": "006723cc",
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
            "const:fd8:8"
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
      "00698714",
      "DATA",
      [
        "storage",
        "00bf7fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698714",
      "DATA",
      [
        "storage",
        "00c75100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006723bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md#insn-006723bc) · [`006723c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md#insn-006723c4) · [`006723c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md#insn-006723c8)
- 新版 [`00698704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006986f0.md#insn-00698704) · [`0069870c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006986f0.md#insn-0069870c) · [`00698710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006986f0.md#insn-00698710)

~~~diff
- 006723bc ["INT_ADD", "register:40f0:8", ["const:6723bc:8", "const:4:8"]]
- 006723bc ["CALL", null, ["callee:00c57a90:8"]]
+ 00698704 ["INT_ADD", "register:40f0:8", ["const:698704:8", "const:4:8"]]
+ 00698704 ["CALL", null, ["callee:00c57a90:8"]]
- 006723bc bytes 21a31594
+ 00698704 bytes e3fc1694
- 006723c4 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 0069870c ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006723c4 bytes 282c00b0
+ 0069870c bytes e82e00b0
- 006723c8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 006723c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006723c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006723c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698710 ["COPY", "tmp:0:8", ["const:100:8"]]
+ 00698710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006723c8 bytes 08613f91
+ 00698710 bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1163d92fd860bcd2eaa132f468e41c8f"></a>

### [`006723e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723e0.md) → [`00698728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698728.md) FUN_00698728

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069872c",
      "incomplete_value": false,
      "site": "00698730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006723e4",
      "incomplete_value": false,
      "site": "006723e8",
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
            "const:fd8:8"
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
      "00698730",
      "DATA",
      [
        "storage",
        "00bf7fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698730",
      "DATA",
      [
        "storage",
        "00c75100",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006723e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723e0.md#insn-006723e0) · [`006723e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723e0.md#insn-006723e4)
- 新版 [`00698728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698728.md#insn-00698728) · [`0069872c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698728.md#insn-0069872c)

~~~diff
- 006723e0 ["COPY", "register:4040:8", ["const:bf7000:8"]]
+ 00698728 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006723e0 bytes 282c00b0
+ 00698728 bytes e82e00b0
- 006723e4 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 006723e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006723e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006723e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0069872c ["COPY", "tmp:0:8", ["const:100:8"]]
+ 0069872c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0069872c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0069872c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006723e4 bytes 08613f91
+ 0069872c bytes 08010491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf9bc3687db79f84ae79c346b4f2fca"></a>

### [`0067251c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/0067251c.md) → [`00698864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698864.md) FUN_00698864

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d64.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 30.00% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00672534",
      "incomplete_value": true,
      "site": "00672538",
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00672554"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0067256c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00698894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0067256c"
      ]
    ],
    [
      "unmatched:00672554",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:0067256c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00698894",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006988b4"
      ]
    ],
    [
      "0069889c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006988b4",
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

- 旧版 [`00672538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/0067251c.md#insn-00672538) · [`00672554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/0067251c.md#insn-00672554) · [`0067256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/0067251c.md#insn-0067256c)
- 新版 [`00698880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698864.md#insn-00698880)

~~~diff
- 00672538 ["INT_ADD", "register:40f0:8", ["const:672538:8", "const:4:8"]]
- 00672538 ["CALL", null, ["callee:008b6f04:8"]]
+ 00698880 ["INT_ADD", "register:40f0:8", ["const:698880:8", "const:4:8"]]
+ 00698880 ["CALL", null, ["callee:008b6f04:8"]]
- 00672538 bytes 0b460894
+ 00698880 bytes a1790894
- 00672554 ["INT_ADD", "register:40f0:8", ["const:672554:8", "const:4:8"]]
- 00672554 ["CALL", null, ["ram:457e1c:8"]]
- 00672554 bytes 3296f797
- 0067256c ["INT_ADD", "register:40f0:8", ["const:67256c:8", "const:4:8"]]
- 0067256c ["CALL", null, ["ram:457e1c:8"]]
- 0067256c bytes 2c96f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d34978b0684f4203082bdc0efa23177"></a>

### [`00672688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md) → [`006989d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006989d0.md) FUN_006989d0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 37.50% / 新版 37.50%

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
      "site": "00672688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00672688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067268c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00672688",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067268c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006726b0",
      "DATA",
      [
        "storage",
        "00bf8158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006989d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006989d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006989f8",
      "DATA",
      [
        "storage",
        "00c75280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md#insn-00672688) · [`0067268c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md#insn-0067268c) · [`0067269c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md#insn-0067269c)
- 新版 [`006989e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/006989d0.md#insn-006989e4)

~~~diff
- 00672688 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00672688 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00672688 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00672688 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00672688 bytes fd7bbea9
- 0067268c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0067268c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0067268c bytes f30b00f9
- 0067269c ["INT_ADD", "register:40f0:8", ["const:67269c:8", "const:4:8"]]
- 0067269c ["CALL", null, ["callee:00c57a90:8"]]
+ 006989e4 ["INT_ADD", "register:40f0:8", ["const:6989e4:8", "const:4:8"]]
+ 006989e4 ["CALL", null, ["callee:00c57a90:8"]]
- 0067269c bytes 69a21594
+ 006989e4 bytes 2bfc1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce478157911c1d132ca58f5b4b43dd31"></a>

### [`006726c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726c8.md) → [`00698a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698a10.md) FUN_00698a10

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698a14",
      "incomplete_value": false,
      "site": "00698a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006726cc",
      "incomplete_value": false,
      "site": "006726d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00698a18",
      "DATA",
      [
        "storage",
        "00bf8158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698a18",
      "DATA",
      [
        "storage",
        "00c75280",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006726c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726c8.md#insn-006726c8) · [`006726cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726c8.md#insn-006726cc)
- 新版 [`00698a10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698a10.md#insn-00698a10) · [`00698a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698a10.md#insn-00698a14)

~~~diff
- 006726c8 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 00698a10 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006726c8 bytes 282c00d0
+ 00698a10 bytes e82e00b0
- 006726cc ["COPY", "tmp:0:8", ["const:158:8"]]
- 006726cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006726cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006726cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698a14 ["COPY", "tmp:0:8", ["const:280:8"]]
+ 00698a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006726cc bytes 08610591
+ 00698a14 bytes 08010a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed1c7f1ace81ceeeab59099a32d0b514"></a>

### [`006726f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md) → [`00698a38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698a38.md) FUN_00698a38

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046a8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046a8a8.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.47% / 新版 77.47%

CFGの説明率　旧版 36.36% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 15件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006726f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006726f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006726f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006726f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:006726f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006726fc",
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
      "00698a3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00698a40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00698a44",
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

- 旧版 [`006726f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-006726f4) · [`006726f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-006726f8) · [`006726fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-006726fc)

~~~diff
- 006726f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 006726f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 006726f4 bytes e81300fd
- 006726f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006726f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006726f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 006726f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006726f8 bytes fd7b03a9
- 006726fc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 006726fc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 006726fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006726fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006726fc bytes fc6f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-529da0821532233e14ea67f241dfddf5"></a>

### [`006729f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md) → [`00698d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d3c.md) FUN_00698d3c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698d5c",
      "incomplete_value": false,
      "site": "00698d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672a14",
      "incomplete_value": false,
      "site": "00672a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "00698d60",
      "DATA",
      [
        "storage",
        "00bf81d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698d60",
      "DATA",
      [
        "storage",
        "00c75300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md#insn-00672a08) · [`00672a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md#insn-00672a10) · [`00672a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md#insn-00672a14)
- 新版 [`00698d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d3c.md#insn-00698d50) · [`00698d58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d3c.md#insn-00698d58) · [`00698d5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d3c.md#insn-00698d5c)

~~~diff
- 00672a08 ["INT_ADD", "register:40f0:8", ["const:672a08:8", "const:4:8"]]
- 00672a08 ["CALL", null, ["callee:00c57a90:8"]]
+ 00698d50 ["INT_ADD", "register:40f0:8", ["const:698d50:8", "const:4:8"]]
+ 00698d50 ["CALL", null, ["callee:00c57a90:8"]]
- 00672a08 bytes 8ea11594
+ 00698d50 bytes 50fb1694
- 00672a10 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 00698d58 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 00672a10 bytes 282c00d0
+ 00698d58 bytes e82e00b0
- 00672a14 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00672a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698d5c ["COPY", "tmp:0:8", ["const:300:8"]]
+ 00698d5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698d5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698d5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672a14 bytes 08610791
+ 00698d5c bytes 08010c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615026bb9b624630b66764a5e3eb5ba5"></a>

### [`00672a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md) → [`00698d94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d94.md) FUN_00698d94

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00661f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/00661f64.md) [`0066341c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066341c.md) [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00688254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00688/00688254.md) [`0068970c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00689/0068970c.md) [`0068ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068e/0068ed40.md)

変更の種類 call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 66.67% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00672b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00672b30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00698e74"
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
      "00698dc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:00672ad4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00668a08"
      ]
    ],
    [
      "unmatched:00672b0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f1e2c"
      ]
    ]
  ],
  "added": [
    [
      "00698dc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00698e1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0068ed40"
      ]
    ],
    [
      "00698e54",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071be98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md#insn-00672a80) · [`00672ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md#insn-00672ab8) · [`00672b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md#insn-00672b0c)
- 新版 [`00698dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d94.md#insn-00698dc8) · [`00698e00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698d94.md#insn-00698e00)

~~~diff
- 00672a80 ["INT_ADD", "register:40f0:8", ["const:672a80:8", "const:4:8"]]
- 00672a80 ["CALL", null, ["ram:457e1c:8"]]
+ 00698dc8 ["INT_ADD", "register:40f0:8", ["const:698dc8:8", "const:4:8"]]
+ 00698dc8 ["CALL", null, ["ram:47acb4:8"]]
- 00672a80 bytes e794f797
+ 00698dc8 bytes bb87f797
- 00672ab8 ["INT_ADD", "register:40f0:8", ["const:672ab8:8", "const:4:8"]]
- 00672ab8 ["CALL", null, ["callee:008b7904:8"]]
+ 00698e00 ["INT_ADD", "register:40f0:8", ["const:698e00:8", "const:4:8"]]
+ 00698e00 ["CALL", null, ["callee:008b7904:8"]]
- 00672ab8 bytes 2b470894
+ 00698e00 bytes c17a0894
- 00672b0c ["INT_ADD", "register:40f0:8", ["const:672b0c:8", "const:4:8"]]
- 00672b0c ["CALL", null, ["ram:6f1e2c:8"]]
- 00672b0c bytes c8fc0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4bb1756d2eb4bdee633c8eb1841c32"></a>

### [`00672bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bb0.md) → [`00698ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ef8.md) FUN_00698ef8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698efc",
      "incomplete_value": false,
      "site": "00698f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672bb4",
      "incomplete_value": false,
      "site": "00672bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:258:8"
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
      "00698f00",
      "DATA",
      [
        "storage",
        "00bf8258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698f00",
      "DATA",
      [
        "storage",
        "00c75380",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bb0.md#insn-00672bb0) · [`00672bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bb0.md#insn-00672bb4)
- 新版 [`00698ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ef8.md#insn-00698ef8) · [`00698efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ef8.md#insn-00698efc)

~~~diff
- 00672bb0 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 00698ef8 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 00672bb0 bytes 282c00d0
+ 00698ef8 bytes e82e00b0
- 00672bb4 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00672bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00698efc ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00698efc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00698efc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00698efc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 bytes 08610991
+ 00698efc bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0408082861ce4e33e1362b2733f8397"></a>

### [`00672bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bd0.md) → [`00698f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698f18.md) FUN_00698f18

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d64.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6f04.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 45.45% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00698f30",
      "incomplete_value": true,
      "site": "00698f34",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00672be8",
      "incomplete_value": true,
      "site": "00672bec",
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00698f50",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00672c08",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "site": "00698f68",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00672c20",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "00698f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00698f68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00698f50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00698f68",
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

- 旧版 [`00672bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bd0.md#insn-00672bec) · [`00672c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bd0.md#insn-00672c08) · [`00672c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bd0.md#insn-00672c20)
- 新版 [`00698f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698f18.md#insn-00698f34) · [`00698f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698f18.md#insn-00698f50) · [`00698f68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698f18.md#insn-00698f68)

~~~diff
- 00672bec ["INT_ADD", "register:40f0:8", ["const:672bec:8", "const:4:8"]]
- 00672bec ["CALL", null, ["callee:008b6f04:8"]]
+ 00698f34 ["INT_ADD", "register:40f0:8", ["const:698f34:8", "const:4:8"]]
+ 00698f34 ["CALL", null, ["callee:008b6f04:8"]]
- 00672bec bytes 5e440894
+ 00698f34 bytes f4770894
- 00672c08 ["INT_ADD", "register:40f0:8", ["const:672c08:8", "const:4:8"]]
- 00672c08 ["CALL", null, ["ram:457e1c:8"]]
+ 00698f50 ["INT_ADD", "register:40f0:8", ["const:698f50:8", "const:4:8"]]
+ 00698f50 ["CALL", null, ["ram:47acb4:8"]]
- 00672c08 bytes 8594f797
+ 00698f50 bytes 5987f797
- 00672c20 ["INT_ADD", "register:40f0:8", ["const:672c20:8", "const:4:8"]]
- 00672c20 ["CALL", null, ["ram:457e1c:8"]]
+ 00698f68 ["INT_ADD", "register:40f0:8", ["const:698f68:8", "const:4:8"]]
+ 00698f68 ["CALL", null, ["ram:47acb4:8"]]
- 00672c20 bytes 7f94f797
+ 00698f68 bytes 5387f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eaa19f02bfbfa18d8aeb3172f006598c"></a>

### [`00672ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ca8.md) → [`00698ff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ff0.md) FUN_00698ff0

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00698ffc",
      "incomplete_value": false,
      "site": "00698ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:400:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672cb4",
      "incomplete_value": false,
      "site": "00672cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "00698ffc",
      "DATA",
      [
        "storage",
        "00bf82d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00698ffc",
      "DATA",
      [
        "storage",
        "00c75400",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ca8.md#insn-00672cac) · [`00672cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ca8.md#insn-00672cb0)
- 新版 [`00698ff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ff0.md#insn-00698ff4) · [`00698ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00698/00698ff0.md#insn-00698ff8)

~~~diff
- 00672cac ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 00698ff4 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 00672cac bytes 292c00d0
+ 00698ff4 bytes e92e00b0
- 00672cb0 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00672cb0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00698ff8 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00698ff8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00698ff8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00698ff8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00672cb0 bytes 29610b91
+ 00698ff8 bytes 29011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363a240f84f929662ed634ea3fe4969a"></a>

### [`00672ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ed8.md) → [`00699220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/00699220.md) FUN_00699220

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0069922c",
      "incomplete_value": false,
      "site": "0069922c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c75000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672ee4",
      "incomplete_value": false,
      "site": "00672ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "0069922c",
      "DATA",
      [
        "storage",
        "00bf8358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0069922c",
      "DATA",
      [
        "storage",
        "00c75480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ed8.md#insn-00672edc) · [`00672ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ed8.md#insn-00672ee0)
- 新版 [`00699224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/00699220.md#insn-00699224) · [`00699228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/00699220.md#insn-00699228)

~~~diff
- 00672edc ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 00699224 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 00672edc bytes 292c00d0
+ 00699224 bytes e92e0090
- 00672ee0 ["COPY", "tmp:0:8", ["const:358:8"]]
- 00672ee0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00699228 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00699228 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00699228 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00699228 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00672ee0 bytes 29610d91
+ 00699228 bytes 29011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcea642674f5135d3be0dc7544fd910d"></a>

### [`00672ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md) → [`0069923c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/0069923c.md) FUN_0069923c

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0066181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/0066181c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`00687b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00687/00687b0c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.98% / 新版 81.98%

CFGの説明率　旧版 13.79% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00672f1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00699264"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00672f98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00672f1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00672f40",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00672f44",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00699264",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00699288",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0069928c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md#insn-00672f1c) · [`00672f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md#insn-00672f54) · [`00672f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672ef4.md#insn-00672f7c)
- 新版 [`0069929c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/0069923c.md#insn-0069929c)

~~~diff
- 00672f1c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00672f1c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00672f1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00672f1c bytes a8831ff8
- 00672f54 ["INT_ADD", "register:40f0:8", ["const:672f54:8", "const:4:8"]]
- 00672f54 ["CALL", null, ["callee:00c58210:8"]]
+ 0069929c ["INT_ADD", "register:40f0:8", ["const:69929c:8", "const:4:8"]]
+ 0069929c ["CALL", null, ["callee:00c58210:8"]]
- 00672f54 bytes 1ba21594
+ 0069929c bytes ddfb1694
- 00672f7c ["INT_ADD", "register:40f0:8", ["const:672f7c:8", "const:4:8"]]
- 00672f7c ["CALL", null, ["ram:449aec:8"]]
- 00672f7c bytes dc5af797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7742f2272d096ce32480940eccc3224a"></a>

### [`006731f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/006731f0.md) → [`00699538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/00699538.md) _INIT_101

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 93.33% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00673220"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00673234"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00673238"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00673220",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067322c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00673234",
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
      "00699568",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00699574",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0069957c",
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

- 旧版 [`00673220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/006731f0.md#insn-00673220) · [`00673234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/006731f0.md#insn-00673234) · [`00673238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/006731f0.md#insn-00673238)

~~~diff
- 00673220 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00673220 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00673220 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00673220 bytes a9831ff8
- 00673234 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00673234 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00673234 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00673234 bytes ea130278
- 00673238 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00673238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00673238 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86b85605b0286cae3a89a232cc1dfbd4"></a>

### [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) → [`006998c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/006998c8.md) FUN_006998c8

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) · 呼出先 28件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) · 呼出先 28件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 74.57% / 新版 74.57%

CFGの説明率　旧版 38.25% / 新版 40.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 11件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006735cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006999c8",
      "incomplete_value": true,
      "site": "006999d8",
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
                "const:cfb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00673680",
      "incomplete_value": true,
      "site": "00673690",
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
                "const:8dd:8"
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
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00673788"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006735cc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006735cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "006999c8",
      "READ",
      [
        "storage",
        "0029f8dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00699914",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00699914",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "006999c8",
      "READ",
      [
        "storage",
        "002afcfb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006735cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md#insn-006735cc) · [`00673788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md#insn-00673788) · [`00673790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md#insn-00673790)

~~~diff
- 006735cc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:98:8"]]
- 006735cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006735cc bytes e84f00f9
- 00673788 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00673788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:4"]]
- 00673788 bytes 162000b9
- 00673790 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00673790 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00673790 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00673790 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00673790 bytes 1f7c00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60292784425e6bb414cfc6dc17e91063"></a>

### [`0067407c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067407c.md) → [`0069a3c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a3c4.md) FUN_0069a3c4

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 87.50% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00674098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067407c.md#insn-00674098) · [`006740a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067407c.md#insn-006740a8)
- 新版 [`0069a3e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a3c4.md#insn-0069a3e0) · [`0069a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a3c4.md#insn-0069a3f0)

~~~diff
- 00674098 ["INT_ADD", "register:40f0:8", ["const:674098:8", "const:4:8"]]
- 00674098 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0069a3e0 ["INT_ADD", "register:40f0:8", ["const:69a3e0:8", "const:4:8"]]
+ 0069a3e0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00674098 bytes f29b1594
+ 0069a3e0 bytes b4f51694
- 006740a8 ["INT_ADD", "register:40f0:8", ["const:6740a8:8", "const:4:8"]]
- 006740a8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 0069a3f0 ["INT_ADD", "register:40f0:8", ["const:69a3f0:8", "const:4:8"]]
+ 0069a3f0 ["CALL", null, ["callee:00c57ab0:8"]]
- 006740a8 bytes ee9b1594
+ 0069a3f0 bytes b0f51694
~~~


<a id="compare-13f73bdafb51f214f155a4426aeb721f"></a>

### [`006740d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/006740d0.md) → [`0069a418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a418.md) FUN_0069a418

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 3件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md)
- 新版 呼出元 2件 [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 3件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "0069a488",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00674140",
      "value": [
        "leaf",
        "ram:41fdf0:8"
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069a484",
      "incomplete_value": false,
      "site": "0069a488",
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
            "const:f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067413c",
      "incomplete_value": false,
      "site": "00674140",
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
            "const:bae:8"
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
      "0069a484",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "0069a488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "0069a484",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "0069a488",
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

- 旧版 [`00674140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/006740d0.md#insn-00674140) · [`006740e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/006740d0.md#insn-006740e4) · [`00674138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/006740d0.md#insn-00674138)
- 新版 [`0069a488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a418.md#insn-0069a488) · [`0069a42c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a418.md#insn-0069a42c) · [`0069a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a418.md#insn-0069a480)

~~~diff
- 00674140 ["INT_ADD", "register:40f0:8", ["const:674140:8", "const:4:8"]]
- 00674140 ["CALL", null, ["ram:41fdf0:8"]]
+ 0069a488 ["INT_ADD", "register:40f0:8", ["const:69a488:8", "const:4:8"]]
+ 0069a488 ["CALL", null, ["ram:4428f0:8"]]
- 00674140 bytes 2caff697
+ 0069a488 bytes 1aa1f697
- 006740e4 ["INT_ADD", "register:40f0:8", ["const:6740e4:8", "const:4:8"]]
- 006740e4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 0069a42c ["INT_ADD", "register:40f0:8", ["const:69a42c:8", "const:4:8"]]
+ 0069a42c ["CALL", null, ["callee:00c57ce0:8"]]
- 006740e4 bytes 6b9c1594
+ 0069a42c bytes 2df61694
- 00674138 ["COPY", "register:4000:8", ["const:290000:8"]]
+ 0069a480 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00674138 bytes e0e0ff90
+ 0069a480 bytes 20e0ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d5b4d3076a4048841e5e3d4ad496f6"></a>

### [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) → [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) FUN_0069a4c4

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) [`00a2ba68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2b/00a2ba68.md) · 呼出先 62件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00574784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574784.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md)
- 新版 呼出元 4件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) [`00a898d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a89/00a898d8.md) · 呼出先 62件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0059761c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/0059761c.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.32% / 新版 62.32%

CFGの説明率　旧版 27.81% / 新版 28.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `call_target` 6件, `store_condition` 14件, `unresolved_branch_alignment` 280件, `unresolved_call_alignment` 201件, `unresolved_store_alignment` 180件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006741d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00674228"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00674248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0069a50c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006741dc"
      ]
    ],
    [
      "unmatched:006741dc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:006741e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0099a654"
      ]
    ]
  ],
  "added": [
    [
      "0069a50c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0069a524"
      ]
    ],
    [
      "0069a524",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0069a52c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "009d0184"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006741d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md#insn-006741d8) · [`00674228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md#insn-00674228) · [`00674248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md#insn-00674248)

~~~diff
- 006741d8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 006741d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:a0:8"]]
- 006741d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 006741d8 bytes 28810239
- 00674228 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:3c:8"]]
- 00674228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00674228 bytes e03f00b9
- 00674248 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00674248 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00674248 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00674248 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00674248 bytes e82f01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a3081ef9e09fdc96daae104c28fe6f"></a>

### [`00678504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678504.md) → [`0069e84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e84c.md) FUN_0069e84c

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`0067c444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c444.md)
- 新版 呼出元 1件 [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`006a278c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a278c.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0069e870",
      "incomplete_value": true,
      "site": "0069e874",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": {
      "definition_site": "00678528",
      "incomplete_value": true,
      "site": "0067852c",
      "value": [
        "live",
        "register:4040:8"
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
      "definition_site": "00678510",
      "incomplete_value": true,
      "site": "0067852c",
      "value": [
        "LOAD",
        "8",
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
                "const:28:8"
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


#### 変更候補の命令位置

- 旧版 [`0067852c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678504.md#insn-0067852c) · [`00678528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678504.md#insn-00678528)
- 新版 [`0069e874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e84c.md#insn-0069e874) · [`0069e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e84c.md#insn-0069e870)

~~~diff
- 0067852c ["INT_ADD", "register:40f0:8", ["const:67852c:8", "const:4:8"]]
- 0067852c ["CALL", null, ["callee:006a278c:8"]]
+ 0069e874 ["INT_ADD", "register:40f0:8", ["const:69e874:8", "const:4:8"]]
+ 0069e874 ["CALL", null, ["callee:006a278c:8"]]
- 0067852c bytes c60f0094
+ 0069e874 bytes c60f0094
- 00678528 ["COPY", "register:4000:8", ["register:4098:8"]]
- 00678528 bytes e00313aa
+ 0069e870 ["COPY", "register:4000:8", ["register:4098:8"]]
+ 0069e870 bytes e00313aa
~~~


<a id="compare-d7a24cf0ef6a1b7af860d7aecf2341f4"></a>

### [`00678588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678588.md) → [`0069e8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069e8d0.md) FUN_0069e8d0

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00868b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868b14.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 10件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0060ee24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060e/0060ee24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`0089c00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089c/0089c00c.md) [`00a06c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a06/00a06c00.md) · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0063491c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00634/0063491c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.16% / 新版 72.16%

CFGの説明率　旧版 17.07% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067858c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00678588",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067858c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00678590",
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
      "0069e8d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0069e8d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0069e8d8",
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

- 旧版 [`00678588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678588.md#insn-00678588) · [`0067858c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678588.md#insn-0067858c) · [`00678590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678588.md#insn-00678590)

~~~diff
- 00678588 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00678588 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00678588 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00678588 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00678588 bytes fd7bbba9
- 0067858c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0067858c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0067858c bytes f90b00f9
- 00678590 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00678590 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00678590 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00678590 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00678590 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b53c5cc751eec627ae20add4b9fb15"></a>

### [`00678728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678728.md) → [`0069ea70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069ea70.md) FUN_0069ea70

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00678d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md) · 呼出先 5件 [`0052dadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dadc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)
- 新版 呼出元 1件 [`0069f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069f/0069f0bc.md) · 呼出先 5件 [`00550974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550974.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b50.md) [`00c57b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b60.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.86% / 新版 72.86%

CFGの説明率　旧版 23.33% / 新版 25.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067872c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067872c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678730"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067872c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00678730",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00678734",
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
      "0069ea74",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0069ea78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0069ea7c",
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

- 旧版 [`0067872c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678728.md#insn-0067872c) · [`00678730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678728.md#insn-00678730) · [`00678734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678728.md#insn-00678734)

~~~diff
- 0067872c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0067872c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0067872c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0067872c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067872c bytes fd7b09a9
- 00678730 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:a0:8"]]
- 00678730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00678730 bytes f55300f9
- 00678734 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00678734 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00678734 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00678734 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00678734 bytes f44f0ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad84a1eba011f3dbd48a49d8d642d58e"></a>

### [`00678884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678884.md) → [`0069ebcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069ebcc.md) FUN_0069ebcc

採用 · 移動量 `+0x26348` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-a01e6671ef7c67f2adf8984f1faf97da"></a>

### [`00678894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md) → [`0069ebdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069ebdc.md) FUN_0069ebdc

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00596128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00596/00596128.md) [`00821cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cbc.md) [`008226b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00822/008226b4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) · 呼出先 16件 [`0052dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052dad8.md) [`00678b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678b8c.md) [`0067c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c7f0.md) [`0067c988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c988.md) [`0067c98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c98c.md)
- 新版 呼出元 6件 [`005ba758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005ba758.md) [`00853c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c38.md) [`00854630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00854/00854630.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) · 呼出先 16件 [`00550970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00550/00550970.md) [`0069eed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069eed4.md) [`006a2b38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2b38.md) [`006a2cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2cd0.md) [`006a2cd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2cd4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 87.50% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006788dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006788dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006788e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006788dc",
      "DATA",
      [
        "storage",
        "00bf83d8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:006788dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "unmatched:006788e4",
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
      "0069ec24",
      "DATA",
      [
        "storage",
        "00c75500",
        null,
        "undefined *"
      ]
    ],
    [
      "0069ec24",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ],
    [
      "0069ec2c",
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

- 旧版 [`006788dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md#insn-006788dc) · [`006788e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md#insn-006788e4) · [`00678a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678894.md#insn-00678a2c)
- 新版 [`0069ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069e/0069ebdc.md#insn-0069ed74)

~~~diff
- 006788dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006788dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006788dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 006788dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006788dc bytes e84f02a9
- 006788e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 006788e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006788e4 bytes f32300f9
- 00678a2c ["INT_ADD", "register:40f0:8", ["const:678a2c:8", "const:4:8"]]
- 00678a2c ["CALL", null, ["callee:006a2d0c:8"]]
+ 0069ed74 ["INT_ADD", "register:40f0:8", ["const:69ed74:8", "const:4:8"]]
+ 0069ed74 ["CALL", null, ["callee:006a2d0c:8"]]
- 00678a2c bytes e60f0094
+ 0069ed74 bytes e60f0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21def1ff79f510087be94ab688873be9"></a>

### [`00678d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md) → [`0069f0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069f/0069f0bc.md) FUN_0069f0bc

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0067c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c990.md) [`0067d64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067d/0067d64c.md) · 呼出先 26件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`006a2cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a2cd8.md) [`006a3994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a3/006a3994.md) · 呼出先 26件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.39% / 新版 84.39%

CFGの説明率　旧版 56.15% / 新版 56.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `call_target` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678d9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678da4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00678ddc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00678d9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00678da4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00678ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0069f0e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c8]",
        null,
        null
      ]
    ],
    [
      "0069f0ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "0069f124",
      "WRITE",
      [
        "storage",
        "Stack[-0x170]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00678d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md#insn-00678d9c) · [`00678da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md#insn-00678da4) · [`00678ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00678/00678d74.md#insn-00678ddc)

~~~diff
- 00678d9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00678d9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00678d9c bytes e80700f9
- 00678da4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00678da4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00678da4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00678da4 bytes a8831ef8
- 00678ddc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 00678ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00678ddc bytes e83300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c4c1138ba5d71e5d1869ee7ad744bb"></a>

### [`00679ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md) → [`006a0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md) FUN_006a0204

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) [`00679ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md) [`00816bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00816/00816bf4.md) · 呼出先 2件 [`00679ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`006998c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/006998c8.md) [`006a0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md) [`008489ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00848/008489ec.md) · 呼出先 2件 [`006a0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00679ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md#insn-00679ebc) · [`00679ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md#insn-00679ed8) · [`00679ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679ebc.md#insn-00679ee4)
- 新版 [`006a0204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md#insn-006a0204) · [`006a0220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md#insn-006a0220) · [`006a022c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0204.md#insn-006a022c)

~~~diff
- 00679ebc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00679ebc ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 006a0204 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 006a0204 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00679ebc bytes 610200b4
+ 006a0204 bytes 610200b4
- 00679ed8 ["INT_ADD", "register:40f0:8", ["const:679ed8:8", "const:4:8"]]
- 00679ed8 ["CALL", null, ["local:b0:8"]]
+ 006a0220 ["INT_ADD", "register:40f0:8", ["const:6a0220:8", "const:4:8"]]
+ 006a0220 ["CALL", null, ["local:b0:8"]]
- 00679ed8 bytes f9ffff97
+ 006a0220 bytes f9ffff97
- 00679ee4 ["INT_ADD", "register:40f0:8", ["const:679ee4:8", "const:4:8"]]
- 00679ee4 ["CALL", null, ["local:b0:8"]]
+ 006a022c ["INT_ADD", "register:40f0:8", ["const:6a022c:8", "const:4:8"]]
+ 006a022c ["CALL", null, ["local:b0:8"]]
- 00679ee4 bytes f6ffff97
+ 006a022c bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f027068184331c25fba63c04ebabd548"></a>

### [`00679f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md) → [`006a0254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0254.md) FUN_006a0254

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0067a120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a120.md) [`0067a2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006998c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/006998c8.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006a0468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0468.md) [`006a0620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0620.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 84.68% / 新版 84.68%

CFGの説明率　旧版 75.76% / 新版 73.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00679f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00679fe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00679fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00679f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067a010",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067a030",
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
      "006a0284",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "006a0358",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "006a0378",
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

- 旧版 [`00679f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md#insn-00679f3c) · [`00679fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md#insn-00679fe4) · [`00679ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md#insn-00679ff0)

~~~diff
- 00679f3c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00679f3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00679f3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00679f3c bytes a8831ff8
- 00679fe4 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00679fe4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00679fe4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00679fe4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00679fe4 bytes 9f7e00a9
- 00679ff0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00679ff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00679ff0 bytes 2001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-933c1a48e640454654e6686e126c395c"></a>

### [`0067a120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a120.md) → [`006a0468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0468.md) FUN_006a0468

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00679f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006a0254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0254.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 38.10% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a17c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067a150",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0548"
      ]
    ],
    [
      "unmatched:0067a1d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0524"
      ]
    ]
  ],
  "added": [
    [
      "006a0498",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0548"
      ]
    ],
    [
      "006a0518",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0524"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067a150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a120.md#insn-0067a150) · [`0067a164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a120.md#insn-0067a164) · [`0067a168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a120.md#insn-0067a168)

~~~diff
- 0067a150 ["CBRANCH", null, ["local:b15:8", "register:101:1"]]
- 0067a150 bytes 80050054
- 0067a164 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
- 0067a164 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 0067a164 bytes 2a0900f9
- 0067a168 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0067a168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0067a168 bytes 2001803d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c846d4eca4ce8a1762ec20bb96b79c3d"></a>

### [`0067a24c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a24c.md) → [`006a0594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0594.md) FUN_006a0594

採用 · 移動量 `+0x26348` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 60.00% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a27c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a05c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a270"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067a270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a05f8"
      ]
    ],
    [
      "unmatched:0067a280",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a05d4"
      ]
    ]
  ],
  "added": [
    [
      "006a05b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a05f8"
      ]
    ],
    [
      "006a05c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a05d4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067a270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a24c.md#insn-0067a270) · [`0067a27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a24c.md#insn-0067a27c) · [`0067a280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a24c.md#insn-0067a280)

~~~diff
- 0067a270 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 0067a270 bytes 00020054
- 0067a27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 0067a27c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 0067a27c bytes 760a00f9
- 0067a280 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0067a280 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0067a280 bytes 600000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4a7fb6820043abdb64a04ad86e8fa29"></a>

### [`0067a2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md) → [`006a0620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0620.md) FUN_006a0620

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00679f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00679/00679f0c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006a0254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0254.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006a0630",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0067a2e8",
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
      "definition_site": "006a062c",
      "incomplete_value": false,
      "site": "006a0630",
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
      "definition_site": "0067a2e4",
      "incomplete_value": false,
      "site": "0067a2e8",
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
      "006a062c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006a0630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006a062c",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006a0630",
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

- 旧版 [`0067a2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md#insn-0067a2e8) · [`0067a2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md#insn-0067a2e0) · [`0067a2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2d8.md#insn-0067a2e4)
- 新版 [`006a0630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0620.md#insn-006a0630) · [`006a0628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0620.md#insn-006a0628) · [`006a062c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0620.md#insn-006a062c)

~~~diff
- 0067a2e8 ["INT_ADD", "register:40f0:8", ["const:67a2e8:8", "const:4:8"]]
- 0067a2e8 ["CALL", null, ["ram:418c38:8"]]
+ 006a0630 ["INT_ADD", "register:40f0:8", ["const:6a0630:8", "const:4:8"]]
+ 006a0630 ["CALL", null, ["ram:43b738:8"]]
- 0067a2e8 bytes 547af697
+ 006a0630 bytes 426cf697
- 0067a2e0 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006a0628 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0067a2e0 bytes 60e1ffb0
+ 006a0628 bytes a0e0fff0
- 0067a2e4 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0067a2e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006a062c ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006a062c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006a062c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006a062c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067a2e4 bytes 00740e91
+ 006a062c bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23e9510ffe40e94fe2c2958f7b622a7"></a>

### [`0067a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2ec.md) → [`006a0634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0634.md) FUN_006a0634

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 2件 [`006998c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/006998c8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "006a0644",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0067a2fc",
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
      "definition_site": "006a0640",
      "incomplete_value": false,
      "site": "006a0644",
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
      "definition_site": "0067a2f8",
      "incomplete_value": false,
      "site": "0067a2fc",
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
      "006a0640",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006a0644",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "006a0640",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006a0644",
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

- 旧版 [`0067a2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2ec.md#insn-0067a2fc) · [`0067a2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2ec.md#insn-0067a2f4) · [`0067a2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a2ec.md#insn-0067a2f8)
- 新版 [`006a0644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0634.md#insn-006a0644) · [`006a063c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0634.md#insn-006a063c) · [`006a0640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0634.md#insn-006a0640)

~~~diff
- 0067a2fc ["INT_ADD", "register:40f0:8", ["const:67a2fc:8", "const:4:8"]]
- 0067a2fc ["CALL", null, ["ram:41fdf0:8"]]
+ 006a0644 ["INT_ADD", "register:40f0:8", ["const:6a0644:8", "const:4:8"]]
+ 006a0644 ["CALL", null, ["ram:4428f0:8"]]
- 0067a2fc bytes bd96f697
+ 006a0644 bytes ab88f697
- 0067a2f4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006a063c ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 0067a2f4 bytes 60e1ffb0
+ 006a063c bytes a0e0fff0
- 0067a2f8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 0067a2f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006a0640 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006a0640 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006a0640 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006a0640 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0067a2f8 bytes 00740e91
+ 006a0640 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d829997026f7a5bea1f63fd6a07837b"></a>

### [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) → [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) FUN_006a0648

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00673580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00673/00673580.md) [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) [`0067a6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md) · 呼出先 5件 [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) [`0067a6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md) [`0067aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006998c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00699/006998c8.md) [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) [`006a09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a09f8.md) · 呼出先 5件 [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) [`006a09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a09f8.md) [`006a0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0d70.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 60.61% / 新版 54.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a5b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a63c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006a08fc"
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
      "unmatched:0067a51c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "006a09f8"
      ]
    ],
    [
      "unmatched:0067a5b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a095c"
      ]
    ],
    [
      "unmatched:0067a63c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0994"
      ]
    ]
  ],
  "added": [
    [
      "006a0864",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "006a09f8"
      ]
    ],
    [
      "006a08fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a095c"
      ]
    ],
    [
      "006a0984",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0994"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067a37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md#insn-0067a37c) · [`0067a448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md#insn-0067a448) · [`0067a4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md#insn-0067a4a4)
- 新版 [`006a06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md#insn-006a06c4) · [`006a0790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md#insn-006a0790) · [`006a07ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md#insn-006a07ec)

~~~diff
- 0067a37c ["INT_ADD", "register:40f0:8", ["const:67a37c:8", "const:4:8"]]
- 0067a37c ["CALL", null, ["callee:00802288:8"]]
+ 006a06c4 ["INT_ADD", "register:40f0:8", ["const:6a06c4:8", "const:4:8"]]
+ 006a06c4 ["CALL", null, ["callee:00802288:8"]]
- 0067a37c bytes 62530594
+ 006a06c4 bytes f1860594
- 0067a448 ["INT_ADD", "register:40f0:8", ["const:67a448:8", "const:4:8"]]
- 0067a448 ["CALL", null, ["callee:00802288:8"]]
+ 006a0790 ["INT_ADD", "register:40f0:8", ["const:6a0790:8", "const:4:8"]]
+ 006a0790 ["CALL", null, ["callee:00802288:8"]]
- 0067a448 bytes 2f530594
+ 006a0790 bytes be860594
- 0067a4a4 ["INT_ADD", "register:40f0:8", ["const:67a4a4:8", "const:4:8"]]
- 0067a4a4 ["CALL", null, ["local:b0:8"]]
+ 006a07ec ["INT_ADD", "register:40f0:8", ["const:6a07ec:8", "const:4:8"]]
+ 006a07ec ["CALL", null, ["local:b0:8"]]
- 0067a4a4 bytes 97ffff97
+ 006a07ec bytes 97ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a5c15bb94b9567288436b6512d5e80e"></a>

### [`0067a6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md) → [`006a09f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a09f8.md) FUN_006a09f8

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) · 呼出先 3件 [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) · 呼出先 3件 [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.34% / 新版 92.34%

CFGの説明率　旧版 45.95% / 新版 50.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 7件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a0c4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0067a77c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067a77c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0a88"
      ]
    ],
    [
      "unmatched:0067a7f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0ae0"
      ]
    ],
    [
      "unmatched:0067a844",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0b48"
      ]
    ]
  ],
  "added": [
    [
      "006a0b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0ae0"
      ]
    ],
    [
      "006a0b8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0b48"
      ]
    ],
    [
      "006a0bf0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a0ce0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067a720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md#insn-0067a720) · [`0067a77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md#insn-0067a77c) · [`0067a7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a6b0.md#insn-0067a7f8)
- 新版 [`006a0a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a09f8.md#insn-006a0a68)

~~~diff
- 0067a720 ["INT_ADD", "register:40f0:8", ["const:67a720:8", "const:4:8"]]
- 0067a720 ["CALL", null, ["callee:00802288:8"]]
+ 006a0a68 ["INT_ADD", "register:40f0:8", ["const:6a0a68:8", "const:4:8"]]
+ 006a0a68 ["CALL", null, ["callee:00802288:8"]]
- 0067a720 bytes 79520594
+ 006a0a68 bytes 08860594
- 0067a77c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 0067a77c bytes 20feff54
- 0067a7f8 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 0067a7f8 bytes 00fdff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7facb107df4a7310700edde5fb4621bc"></a>

### [`0067aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md) → [`006a0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0d70.md) FUN_006a0d70

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0067a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067a300.md) [`0067aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md) · 呼出先 4件 [`0067aa28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`006a0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0648.md) [`006a0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0d70.md) · 呼出先 4件 [`006a0d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a0/006a0d70.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.72% / 新版 93.72%

CFGの説明率　旧版 62.77% / 新版 59.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_condition` 3件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067aa3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067aa3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067aa40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067aa3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067aa40",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067aa48",
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
      "006a0d84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006a0d88",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006a0d90",
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

- 旧版 [`0067aa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md#insn-0067aa3c) · [`0067aa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md#insn-0067aa40) · [`0067aa48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067a/0067aa28.md#insn-0067aa48)

~~~diff
- 0067aa3c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0067aa3c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0067aa3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 0067aa3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067aa3c bytes f65708a9
- 0067aa40 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0067aa40 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0067aa40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0067aa40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067aa40 bytes f44f09a9
- 0067aa48 ["COPY", "tmp:0:8", ["register:4020:8"]]
- 0067aa48 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0067aa48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0067aa48 bytes a4831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f39a64a6c4a12d30d46b165c1c83d94"></a>

### [`0067b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md) → [`006a14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md) FUN_006a14b8

採用 · 移動量 `+0x26348` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0067b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md) [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 2件 [`0067b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006a14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md) [`0089e838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089e/0089e838.md) · 呼出先 2件 [`006a14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0067b194",
      "incomplete_value": true,
      "site": "0067b198",
      "value": [
        "live",
        "register:40a0:8"
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
      "definition_site": "0067b190",
      "incomplete_value": true,
      "site": "0067b198",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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


#### 変更候補の命令位置

- 旧版 [`0067b198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md#insn-0067b198) · [`0067b170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md#insn-0067b170) · [`0067b18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b170.md#insn-0067b18c)
- 新版 [`006a14e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md#insn-006a14e0) · [`006a14b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md#insn-006a14b8) · [`006a14d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a14b8.md#insn-006a14d4)

~~~diff
- 0067b198 ["INT_ADD", "register:40f0:8", ["const:67b198:8", "const:4:8"]]
- 0067b198 ["CALL", null, ["local:b0:8"]]
+ 006a14e0 ["INT_ADD", "register:40f0:8", ["const:6a14e0:8", "const:4:8"]]
+ 006a14e0 ["CALL", null, ["local:b0:8"]]
- 0067b198 bytes f6ffff97
+ 006a14e0 bytes f6ffff97
- 0067b170 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 0067b170 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 006a14b8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 006a14b8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0067b170 bytes 610200b4
+ 006a14b8 bytes 610200b4
- 0067b18c ["INT_ADD", "register:40f0:8", ["const:67b18c:8", "const:4:8"]]
- 0067b18c ["CALL", null, ["local:b0:8"]]
+ 006a14d4 ["INT_ADD", "register:40f0:8", ["const:6a14d4:8", "const:4:8"]]
+ 006a14d4 ["CALL", null, ["local:b0:8"]]
- 0067b18c bytes f9ffff97
+ 006a14d4 bytes f9ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0346bbbc5dcf336f706c53b293ea676"></a>

### [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) → [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) FUN_006a157c

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0067417c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00674/0067417c.md) [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) [`0067b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md) · 呼出先 6件 [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) [`0067b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md) [`0067bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md)
- 新版 呼出元 3件 [`0069a4c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0069a/0069a4c4.md) [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) [`006a19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a19f8.md) · 呼出先 6件 [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) [`006a19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a19f8.md) [`006a1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 36.89% / 新版 38.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b23c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067b238",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067b23c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067b240",
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
      "006a1580",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006a1584",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006a1588",
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

- 旧版 [`0067b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md#insn-0067b238) · [`0067b23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md#insn-0067b23c) · [`0067b240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md#insn-0067b240)

~~~diff
- 0067b238 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0067b238 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0067b238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0067b238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b238 bytes fd7b02a9
- 0067b23c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0067b23c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0067b23c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0067b23c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b23c bytes fc6f03a9
- 0067b240 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0067b240 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0067b240 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0067b240 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b240 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f968d1cf73a752f3a2bfc9e610b26d"></a>

### [`0067b6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md) → [`006a19f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a19f8.md) FUN_006a19f8

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) · 呼出先 4件 [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) · 呼出先 4件 [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.33% / 新版 82.33%

CFGの説明率　旧版 60.20% / 新版 56.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067b6b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0067b6b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067b6b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067b6bc",
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
      "006a19fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006a1a00",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006a1a04",
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

- 旧版 [`0067b6b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md#insn-0067b6b4) · [`0067b6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md#insn-0067b6b8) · [`0067b6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b6b0.md#insn-0067b6bc)

~~~diff
- 0067b6b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0067b6b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0067b6b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0067b6b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b6b4 bytes fd7b02a9
- 0067b6b8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0067b6b8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0067b6b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0067b6b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b6b8 bytes fc6f03a9
- 0067b6bc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0067b6bc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0067b6bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0067b6bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067b6bc bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-360855eeba9959c0a4ae0897c3b7ecfa"></a>

### [`0067bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md) → [`006a1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md) FUN_006a1e64

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0067b234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067b234.md) [`0067bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md) · 呼出先 6件 [`0067bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md) [`0067c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c214.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cf104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf104.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006a157c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a157c.md) [`006a1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md) · 呼出先 6件 [`006a1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md) [`006a255c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a255c.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00802288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802288.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.58% / 新版 90.58%

CFGの説明率　旧版 44.36% / 新版 45.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067bd70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067bd70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067bd74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006a1e8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0067c1c4"
      ]
    ],
    [
      "006a1eb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0067c1c4"
      ]
    ],
    [
      "006a1f58",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0067c1c4"
      ]
    ]
  ],
  "added": [
    [
      "006a1e8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a250c"
      ]
    ],
    [
      "006a1eb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a250c"
      ]
    ],
    [
      "006a1f58",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006a250c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067bd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md#insn-0067bd70) · [`0067bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md#insn-0067bd74) · [`0067be90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md#insn-0067be90)
- 新版 [`006a21d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md#insn-006a21d8)

~~~diff
- 0067bd70 ["COPY", "tmp:0:8", ["register:40c8:8"]]
- 0067bd70 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0067bd70 ["COPY", "tmp:2:8", ["register:8:8"]]
- 0067bd70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0067bd70 bytes f96f00a9
- 0067bd74 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0067bd74 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 0067bd74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0067bd74 bytes aa031ff8
- 0067be90 ["INT_ADD", "register:40f0:8", ["const:67be90:8", "const:4:8"]]
- 0067be90 ["CALL", null, ["callee:006a255c:8"]]
+ 006a21d8 ["INT_ADD", "register:40f0:8", ["const:6a21d8:8", "const:4:8"]]
+ 006a21d8 ["CALL", null, ["callee:006a255c:8"]]
- 0067be90 bytes e1000094
+ 006a21d8 bytes e1000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-395bc6ed743ee50be1385cc3e0862e8f"></a>

### [`0067c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c214.md) → [`006a255c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a2/006a255c.md) FUN_006a255c

採用 · 移動量 `+0x26348` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0067bb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067b/0067bb1c.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`006a1e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006a1/006a1e64.md) · 呼出先 2件 [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 38.46% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_condition` 4件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067c238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0067c318"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006a2580"
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
      "unmatched:0067c238",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0067c23c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a275c"
      ]
    ],
    [
      "006a25a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2624"
      ]
    ]
  ],
  "added": [
    [
      "006a2580",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "006a2584",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a275c"
      ]
    ],
    [
      "006a258c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006a2624"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067c238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c214.md#insn-0067c238) · [`0067c23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c214.md#insn-0067c23c) · [`0067c25c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0067c/0067c214.md#insn-0067c25c)

~~~diff
- 0067c238 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0067c238 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0067c238 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0067c238 bytes a8831ff8
- 0067c23c ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 0067c23c bytes c00e0054
- 0067c25c ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 0067c25c bytes 40060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

