# v15.7.4 → v16.0.0 · 最優先の変更候補 (30)

[一覧の目次](README.md)

<a id="compare-2041546ea759702465243c7f60862fab"></a>

### [`006ad0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad0c0.md) → [`006d5f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d5/006d5f88.md) FUN_006d5f88

採用 · 移動量 `+0x28ec8` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006acf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ac/006acf9c.md) [`00761728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761728.md) · 呼出先 0件 
- 新版 呼出元 2件 [`006d5e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d5/006d5e64.md) [`0078bbfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078b/0078bbfc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 91.67% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006ad1fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006d60c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "006ad204",
      "incomplete_value": true,
      "site": "006ad20c",
      "value": [
        "live",
        "register:4018:8"
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
      "unmatched:006ad1fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d60d8"
      ]
    ]
  ],
  "added": [
    [
      "006d60c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d60d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad1fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad0c0.md#insn-006ad1fc) · [`006ad1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad0c0.md#insn-006ad1f0)
- 新版 `006d60c4`（命令位置の公開資料なし） · `006d60b8`（命令位置の公開資料なし）

~~~diff
- 006ad1fc ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006ad1fc ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 006ad1fc bytes aa000054
+ 006d60c4 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 006d60c4 ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
+ 006d60c4 bytes aa000054
- 006ad1f0 ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
+ 006d60b8 ["CBRANCH", null, ["local:b31:8", "register:101:1"]]
- 006ad1f0 bytes 80000054
+ 006d60b8 bytes 80000054
~~~


<a id="compare-8f52e2a67627980f894a16a106f9ec8f"></a>

### [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) → [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) FUN_006d7048

採用 · 移動量 `+0x29dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 呼出先 10件 [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)
- 新版 呼出元 1件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 呼出先 10件 [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 88.24% / 新版 84.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ad3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006d7180"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006ad3c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006ad3c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7278"
      ]
    ],
    [
      "006d7308",
      "PARAM",
      [
        "storage",
        "0029a021",
        null,
        "string"
      ]
    ],
    [
      "006d730c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ad854"
      ]
    ]
  ],
  "added": [
    [
      "006d7184",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7278"
      ]
    ],
    [
      "006d7308",
      "PARAM",
      [
        "storage",
        "002a9f04",
        null,
        "string"
      ]
    ],
    [
      "006d730c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006d7610"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md#insn-006ad3c4) · [`006ad3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md#insn-006ad3c8) · [`006ad4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md#insn-006ad4f0)
- 新版 `006d72ac`（命令位置の公開資料なし）

~~~diff
- 006ad3c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:40:8"]]
- 006ad3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006ad3c4 bytes 882200f9
- 006ad3c8 ["CBRANCH", null, ["local:b21:8", "register:101:1"]]
- 006ad3c8 bytes a0070054
- 006ad4f0 ["INT_ADD", "register:40f0:8", ["const:6ad4f0:8", "const:4:8"]]
- 006ad4f0 ["CALL", null, ["callee:00c5a490:8"]]
+ 006d72ac ["INT_ADD", "register:40f0:8", ["const:6d72ac:8", "const:4:8"]]
+ 006d72ac ["CALL", null, ["callee:00c5a490:8"]]
- 006ad4f0 bytes 54c11494
+ 006d72ac bytes 790c1694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2c43ac2fcfbe145a01a2b567ad2ac44"></a>

### [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) → [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) FUN_006d734c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) · 呼出先 8件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.87% / 新版 98.87%

CFGの説明率　旧版 81.82% / 新版 73.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006ad818"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006d75d4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006ad658",
      "incomplete_value": true,
      "site": "006ad680",
      "value": [
        "live",
        "register:4098:8"
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
      "unmatched:006ad818",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d760c"
      ]
    ]
  ],
  "added": [
    [
      "006d75d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d760c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md#insn-006ad680) · [`006ad818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md#insn-006ad818) · [`006ad834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md#insn-006ad834)
- 新版 `006d743c`（命令位置の公開資料なし） · `006d75f0`（命令位置の公開資料なし）

~~~diff
- 006ad680 ["INT_ADD", "register:40f0:8", ["const:6ad680:8", "const:4:8"]]
- 006ad680 ["CALL", null, ["callee:00c5a4a0:8"]]
+ 006d743c ["INT_ADD", "register:40f0:8", ["const:6d743c:8", "const:4:8"]]
+ 006d743c ["CALL", null, ["callee:00c5a4a0:8"]]
- 006ad680 bytes f4c01494
+ 006d743c bytes 190c1694
- 006ad818 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006ad818 ["CBRANCH", null, ["local:b29:8", "tmp:0:1"]]
- 006ad818 bytes c1010054
- 006ad834 ["INT_ADD", "register:40f0:8", ["const:6ad834:8", "const:4:8"]]
- 006ad834 ["CALL", null, ["callee:00c57ab0:8"]]
+ 006d75f0 ["INT_ADD", "register:40f0:8", ["const:6d75f0:8", "const:4:8"]]
+ 006d75f0 ["CALL", null, ["callee:00c57ab0:8"]]
- 006ad834 bytes 0bb61494
+ 006d75f0 bytes 30011694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb25096d0195a22d6d17bbe3c080ed1"></a>

### [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) → [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) FUN_006d7660

採用 · 移動量 `+0x29dbc` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 25件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) [`006ad28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad28c.md) [`006ad590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad590.md) [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md) [`007c1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1c70.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 25件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) [`006d7048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7048.md) [`006d734c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d734c.md) [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md) [`007f3e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f3/007f3e4c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006d7670",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ad8b4",
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
      "definition_site": "006d766c",
      "incomplete_value": false,
      "site": "006d7670",
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
            "const:ee3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ad8b0",
      "incomplete_value": false,
      "site": "006ad8b4",
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
            "const:24c:8"
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
      "006d766c",
      "PARAM",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ],
    [
      "006d7670",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006d766c",
      "PARAM",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ],
    [
      "006d7670",
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

- 旧版 [`006ad8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md#insn-006ad8b4) · [`006ad8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md#insn-006ad8ac) · [`006ad8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md#insn-006ad8b0)
- 新版 `006d7670`（命令位置の公開資料なし） · `006d7668`（命令位置の公開資料なし） · `006d766c`（命令位置の公開資料なし）

~~~diff
- 006ad8b4 ["INT_ADD", "register:40f0:8", ["const:6ad8b4:8", "const:4:8"]]
- 006ad8b4 ["CALL", null, ["ram:418c38:8"]]
+ 006d7670 ["INT_ADD", "register:40f0:8", ["const:6d7670:8", "const:4:8"]]
+ 006d7670 ["CALL", null, ["ram:43b738:8"]]
- 006ad8b4 bytes e1acf597
+ 006d7670 bytes 3290f597
- 006ad8ac ["COPY", "register:4000:8", ["const:2a9000:8"]]
+ 006d7668 ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 006ad8ac bytes e0dfff90
+ 006d7668 bytes 00dfffd0
- 006ad8b0 ["COPY", "tmp:0:8", ["const:24c:8"]]
- 006ad8b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006d766c ["COPY", "tmp:0:8", ["const:ee3:8"]]
+ 006d766c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006d766c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006d766c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006ad8b0 bytes 00300991
+ 006d766c bytes 008c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeeb2d22136c39bf751c3b2feb7a17a2"></a>

### [`006ad980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md) → [`006d773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md) FUN_006d773c

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006a6d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a6/006a6d68.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`006ad854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad854.md) [`006add94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`006cfeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006cf/006cfeac.md) · 呼出先 9件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`006d7610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7610.md) [`006d7b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7b50.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.36% / 新版 91.36%

CFGの説明率　旧版 46.15% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ad9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ada84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006d77a4"
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
      "unmatched:006ada84",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006adc98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7ad0"
      ]
    ],
    [
      "unmatched:006add20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7b4c"
      ]
    ]
  ],
  "added": [
    [
      "006d7840",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006d7a54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7ad0"
      ]
    ],
    [
      "006d7adc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7b4c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ad9e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md#insn-006ad9e8) · [`006ada58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md#insn-006ada58) · [`006ada80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md#insn-006ada80)

~~~diff
- 006ad9e8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 006ad9e8 ["COPY", "tmp:1:8", ["register:40c0:8"]]
- 006ad9e8 ["INT_ADD", "register:40c0:8", ["register:40c0:8", "const:1:8"]]
- 006ad9e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 006ad9e8 bytes 08170038
- 006ada58 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006ada58 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006ada58 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006ada58 ["COPY", "register:4008:8", ["tmp:0:8"]]
- 006ada58 bytes 2101889a
- 006ada80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006ada80 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 006ada80 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 006ada80 ["INT_ADD", "tmp:1:8", ["register:4098:8", "const:1:8"]]
- 006ada80 bytes 3715939a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b60240e7853241ddfb4df4f9fd5a315"></a>

### [`006add94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md) → [`006d7b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7b50.md) FUN_006d7b50

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006ad980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad980.md) [`007c1f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007c1/007c1f74.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)
- 新版 呼出元 2件 [`006d773c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d773c.md) [`007f4150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007f4/007f4150.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 88.96% / 新版 88.96%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006addbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006adefc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006adf88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006addbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:006ade04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7bf8"
      ]
    ],
    [
      "unmatched:006adefc",
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
      "006d7b78",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "006d7bc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7bf8"
      ]
    ],
    [
      "006d7cb8",
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

- 旧版 [`006addbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md#insn-006addbc) · [`006adddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md#insn-006adddc) · [`006adde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006add94.md#insn-006adde0)

~~~diff
- 006addbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006addbc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006addbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006addbc bytes a8831ff8
- 006adddc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006adddc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006adddc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 006adddc ["COPY", "register:40a8:8", ["tmp:0:8"]]
- 006adddc bytes 35018b9a
- 006adde0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006adde0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006adde0 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 006adde0 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 006adde0 bytes 08018a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb24c11038f1c2f90e8a4bfc23a1ace9"></a>

### [`006ae060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae060.md) → [`006d7e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e1c.md) FUN_006d7e1c

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d7e28",
      "incomplete_value": false,
      "site": "006d7e28",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae06c",
      "incomplete_value": false,
      "site": "006ae06c",
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
            "const:df0:8"
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
      "006d7e28",
      "DATA",
      [
        "storage",
        "00bf8df0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d7e28",
      "DATA",
      [
        "storage",
        "00c75f18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae060.md#insn-006ae064) · [`006ae068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae060.md#insn-006ae068)
- 新版 `006d7e20`（命令位置の公開資料なし） · `006d7e24`（命令位置の公開資料なし）

~~~diff
- 006ae064 ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 006d7e20 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 006ae064 bytes 492a00d0
+ 006d7e20 bytes e92c00d0
- 006ae068 ["COPY", "tmp:0:8", ["const:df0:8"]]
- 006ae068 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae068 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d7e24 ["COPY", "tmp:0:8", ["const:f18:8"]]
+ 006d7e24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d7e24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d7e24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae068 bytes 29c13791
+ 006d7e24 bytes 29613c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29a7551eb840ed718d2a6c37e6f65f5e"></a>

### [`006ae07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae07c.md) → [`006d7e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7e38.md) FUN_006d7e38

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`006abb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ab/006abb50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006d4c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4c04.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 62.50% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006ae09c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d7e64",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ae0a8",
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
    "kind": "call_position_unpaired",
    "new": {
      "site": "006d7e58"
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
      "unmatched:006ae09c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006ae0a4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7e6c"
      ]
    ],
    [
      "006d7e64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006d7e58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d7e60",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "006d7e6c"
      ]
    ],
    [
      "006d7e64",
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

- 旧版 [`006ae09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae07c.md#insn-006ae09c) · [`006ae0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae07c.md#insn-006ae0a8)
- 新版 `006d7e64`（命令位置の公開資料なし） · `006d7e58`（命令位置の公開資料なし）

~~~diff
- 006ae09c ["INT_ADD", "register:40f0:8", ["const:6ae09c:8", "const:4:8"]]
- 006ae09c ["CALL", null, ["ram:457e1c:8"]]
- 006ae09c bytes 60a7f697
- 006ae0a8 ["INT_ADD", "register:40f0:8", ["const:6ae0a8:8", "const:4:8"]]
- 006ae0a8 ["CALL", null, ["ram:457e1c:8"]]
+ 006d7e64 ["INT_ADD", "register:40f0:8", ["const:6d7e64:8", "const:4:8"]]
+ 006d7e64 ["CALL", null, ["ram:47acb4:8"]]
- 006ae0a8 bytes 5da7f697
+ 006d7e64 bytes 948bf697
+ 006d7e58 ["INT_ADD", "register:40f0:8", ["const:6d7e58:8", "const:4:8"]]
+ 006d7e58 ["CALL", null, ["ram:47acb4:8"]]
+ 006d7e58 bytes 978bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59e1f056e5f13ac3724b270ec9cab098"></a>

### [`006ae40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md) → [`006d81c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81c8.md) FUN_006d81c8

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d81ec",
      "incomplete_value": false,
      "site": "006d81ec",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae430",
      "incomplete_value": false,
      "site": "006ae430",
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
            "const:e70:8"
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
      "006d81ec",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d81ec",
      "DATA",
      [
        "storage",
        "00c75f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md#insn-006ae420) · [`006ae428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md#insn-006ae428) · [`006ae42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae40c.md#insn-006ae42c)
- 新版 `006d81dc`（命令位置の公開資料なし） · `006d81e4`（命令位置の公開資料なし） · `006d81e8`（命令位置の公開資料なし）

~~~diff
- 006ae420 ["INT_ADD", "register:40f0:8", ["const:6ae420:8", "const:4:8"]]
- 006ae420 ["CALL", null, ["callee:00c57a90:8"]]
+ 006d81dc ["INT_ADD", "register:40f0:8", ["const:6d81dc:8", "const:4:8"]]
+ 006d81dc ["CALL", null, ["callee:00c57a90:8"]]
- 006ae420 bytes 08b31494
+ 006d81dc bytes 2dfe1594
- 006ae428 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 006d81e4 ["COPY", "register:4040:8", ["const:c75000:8"]]
- 006ae428 bytes 482a00d0
+ 006d81e4 bytes e82c00b0
- 006ae42c ["COPY", "tmp:0:8", ["const:e70:8"]]
- 006ae42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d81e8 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 006d81e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d81e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d81e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae42c bytes 08c13991
+ 006d81e8 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8332675c1beeb510a95785df6441de0a"></a>

### [`006ae440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae440.md) → [`006d81fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d81fc.md) FUN_006d81fc

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d8208",
      "incomplete_value": false,
      "site": "006d8208",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae44c",
      "incomplete_value": false,
      "site": "006ae44c",
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
            "const:e70:8"
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
      "006d8208",
      "DATA",
      [
        "storage",
        "00bf8e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8208",
      "DATA",
      [
        "storage",
        "00c75f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae440.md#insn-006ae444) · [`006ae448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae440.md#insn-006ae448)
- 新版 `006d8200`（命令位置の公開資料なし） · `006d8204`（命令位置の公開資料なし）

~~~diff
- 006ae444 ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 006d8200 ["COPY", "register:4048:8", ["const:c75000:8"]]
- 006ae444 bytes 492a00d0
+ 006d8200 bytes e92c00b0
- 006ae448 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 006ae448 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae448 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d8204 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 006d8204 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8204 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8204 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae448 bytes 29c13991
+ 006d8204 bytes 29613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf745867d96c2a18fbb2a8eb65b34ed"></a>

### [`006ae5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5d0.md) → [`006d838c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d838c.md) FUN_006d838c

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d8398",
      "incomplete_value": false,
      "site": "006d8398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae5dc",
      "incomplete_value": false,
      "site": "006ae5dc",
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
      "006d8398",
      "DATA",
      [
        "storage",
        "00bf8ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8398",
      "DATA",
      [
        "storage",
        "00c76018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5d0.md#insn-006ae5d4) · [`006ae5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5d0.md#insn-006ae5d8)
- 新版 `006d8390`（命令位置の公開資料なし） · `006d8394`（命令位置の公開資料なし）

~~~diff
- 006ae5d4 ["COPY", "register:4048:8", ["const:bf8000:8"]]
+ 006d8390 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006ae5d4 bytes 492a00d0
+ 006d8390 bytes e92c00d0
- 006ae5d8 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 006ae5d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006d8394 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 006d8394 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8394 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006d8394 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006ae5d8 bytes 29c13b91
+ 006d8394 bytes 29610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f051228cdff860c9709d501320e267"></a>

### [`006ae5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5ec.md) → [`006d83a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d83a8.md) FUN_006d83a8

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`0069eac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069eac8.md) [`006a80d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a80d4.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00676a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/00676a20.md) [`006c4e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4e2c.md) [`006d1218`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1218.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.06% / 新版 73.06%

CFGの説明率　旧版 48.84% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ae5f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ae5f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006ae5f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006ae5f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:006ae5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:006ae5f8",
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
      "006d83ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006d83b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "006d83b4",
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

- 旧版 [`006ae5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5ec.md#insn-006ae5f0) · [`006ae5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5ec.md#insn-006ae5f4) · [`006ae5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae5ec.md#insn-006ae5f8)

~~~diff
- 006ae5f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006ae5f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006ae5f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 006ae5f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006ae5f0 bytes fd7b02a9
- 006ae5f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 006ae5f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 006ae5f4 bytes f91b00f9
- 006ae5f8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 006ae5f8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 006ae5f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006ae5f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006ae5f8 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-409d723fc5ba66eb6ea451da0d9e5a06"></a>

### [`006ae91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md) → [`006d86d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d86d8.md) FUN_006d86d8

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d86fc",
      "incomplete_value": false,
      "site": "006d86fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006ae940",
      "incomplete_value": false,
      "site": "006ae940",
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
            "const:f70:8"
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
      "006d86fc",
      "DATA",
      [
        "storage",
        "00bf8f70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d86fc",
      "DATA",
      [
        "storage",
        "00c76098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006ae930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md#insn-006ae930) · [`006ae938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md#insn-006ae938) · [`006ae93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae91c.md#insn-006ae93c)
- 新版 `006d86ec`（命令位置の公開資料なし） · `006d86f4`（命令位置の公開資料なし） · `006d86f8`（命令位置の公開資料なし）

~~~diff
- 006ae930 ["INT_ADD", "register:40f0:8", ["const:6ae930:8", "const:4:8"]]
- 006ae930 ["CALL", null, ["callee:00c57a90:8"]]
+ 006d86ec ["INT_ADD", "register:40f0:8", ["const:6d86ec:8", "const:4:8"]]
+ 006d86ec ["CALL", null, ["callee:00c57a90:8"]]
- 006ae930 bytes c4b11494
+ 006d86ec bytes e9fc1594
- 006ae938 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 006d86f4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006ae938 bytes 482a00d0
+ 006d86f4 bytes e82c00d0
- 006ae93c ["COPY", "tmp:0:8", ["const:f70:8"]]
- 006ae93c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006ae93c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d86f8 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 006d86f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d86f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d86f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006ae93c bytes 08c13d91
+ 006d86f8 bytes 08610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c55eebc7fb8bc097f9037db802cab24d"></a>

### [`006aeeb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md) → [`006d8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d8/006d8c70.md) FUN_006d8c70

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d8c94",
      "incomplete_value": false,
      "site": "006d8c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006aeed8",
      "incomplete_value": false,
      "site": "006aeed8",
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
            "const:ff0:8"
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
      "006d8c94",
      "DATA",
      [
        "storage",
        "00bf8ff0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d8c94",
      "DATA",
      [
        "storage",
        "00c76118",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006aeec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md#insn-006aeec8) · [`006aeed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md#insn-006aeed0) · [`006aeed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006aeeb4.md#insn-006aeed4)
- 新版 `006d8c84`（命令位置の公開資料なし） · `006d8c8c`（命令位置の公開資料なし） · `006d8c90`（命令位置の公開資料なし）

~~~diff
- 006aeec8 ["INT_ADD", "register:40f0:8", ["const:6aeec8:8", "const:4:8"]]
- 006aeec8 ["CALL", null, ["callee:00c57a90:8"]]
+ 006d8c84 ["INT_ADD", "register:40f0:8", ["const:6d8c84:8", "const:4:8"]]
+ 006d8c84 ["CALL", null, ["callee:00c57a90:8"]]
- 006aeec8 bytes 5eb01494
+ 006d8c84 bytes 83fb1594
- 006aeed0 ["COPY", "register:4040:8", ["const:bf8000:8"]]
+ 006d8c8c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006aeed0 bytes 482a00d0
+ 006d8c8c bytes e82c00d0
- 006aeed4 ["COPY", "tmp:0:8", ["const:ff0:8"]]
- 006aeed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d8c90 ["COPY", "tmp:0:8", ["const:118:8"]]
+ 006d8c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d8c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006aeed4 bytes 08c13f91
+ 006d8c90 bytes 08610491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58325bca55a9250976dad8b6cf101d38"></a>

### [`006afa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa88.md) → [`006d9844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9844.md) FUN_006d9844

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e97e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97e4.md) [`009e97fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e97fc.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466e0.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.60% / 新版 76.60%

CFGの説明率　旧版 27.78% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006afa88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006afa88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006afa8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006afa88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006afa8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006afaa0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d9874"
      ]
    ]
  ],
  "added": [
    [
      "006d9844",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006d9848",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006d985c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d9874"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa88.md#insn-006afa88) · [`006afa8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa88.md#insn-006afa8c) · [`006afaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afa88.md#insn-006afaa0)

~~~diff
- 006afa88 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006afa88 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006afa88 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 006afa88 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 006afa88 bytes fd7bbea9
- 006afa8c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 006afa8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 006afa8c bytes f30b00f9
- 006afaa0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006afaa0 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006afaa0 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006afaa0 ["CBRANCH", null, ["local:b5:8", "tmp:2:1"]]
- 006afaa0 bytes cc000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daf783a73618b16565a908e54271cfc3"></a>

### [`006afbc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afbc0.md) → [`006d997c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d997c.md) FUN_006d997c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 83.33% / 新版 76.92%

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
      "site": "006d99ec",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006afc30",
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
      "site": "006d9a14",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006afc58",
      "value": [
        "leaf",
        "ram:457e1c:8"
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
      "006d99ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006d9a14",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006d99ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9a14",
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

- 旧版 [`006afc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afbc0.md#insn-006afc30) · [`006afc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afbc0.md#insn-006afc58) · [`006afbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afbc0.md#insn-006afbd8)
- 新版 `006d99ec`（命令位置の公開資料なし） · `006d9a14`（命令位置の公開資料なし） · `006d9994`（命令位置の公開資料なし）

~~~diff
- 006afc30 ["INT_ADD", "register:40f0:8", ["const:6afc30:8", "const:4:8"]]
- 006afc30 ["CALL", null, ["ram:457e1c:8"]]
+ 006d99ec ["INT_ADD", "register:40f0:8", ["const:6d99ec:8", "const:4:8"]]
+ 006d99ec ["CALL", null, ["ram:47acb4:8"]]
- 006afc30 bytes 7ba0f697
+ 006d99ec bytes b284f697
- 006afc58 ["INT_ADD", "register:40f0:8", ["const:6afc58:8", "const:4:8"]]
- 006afc58 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9a14 ["INT_ADD", "register:40f0:8", ["const:6d9a14:8", "const:4:8"]]
+ 006d9a14 ["CALL", null, ["ram:47acb4:8"]]
- 006afc58 bytes 71a0f697
+ 006d9a14 bytes a884f697
- 006afbd8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006afbd8 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 006afbd8 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 006afbd8 ["CBRANCH", null, ["local:b4:8", "tmp:2:1"]]
+ 006d9994 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 006d9994 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 006d9994 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 006d9994 ["CBRANCH", null, ["local:b5:8", "tmp:2:1"]]
- 006afbd8 bytes cc000054
+ 006d9994 bytes cc000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9f10b2a83fee27793e5e56b45683330"></a>

### [`006afc9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md) → [`006d9a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9a58.md) FUN_006d9a58

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d9a7c",
      "incomplete_value": false,
      "site": "006d9a7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006afcc0",
      "incomplete_value": false,
      "site": "006afcc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:170:8"
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
      "006d9a7c",
      "DATA",
      [
        "storage",
        "00bf9170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9a7c",
      "DATA",
      [
        "storage",
        "00c76298",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md#insn-006afcb0) · [`006afcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md#insn-006afcb8) · [`006afcbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afc9c.md#insn-006afcbc)
- 新版 `006d9a6c`（命令位置の公開資料なし） · `006d9a74`（命令位置の公開資料なし） · `006d9a78`（命令位置の公開資料なし）

~~~diff
- 006afcb0 ["INT_ADD", "register:40f0:8", ["const:6afcb0:8", "const:4:8"]]
- 006afcb0 ["CALL", null, ["callee:00c57a90:8"]]
+ 006d9a6c ["INT_ADD", "register:40f0:8", ["const:6d9a6c:8", "const:4:8"]]
+ 006d9a6c ["CALL", null, ["callee:00c57a90:8"]]
- 006afcb0 bytes e4ac1494
+ 006d9a6c bytes 09f81594
- 006afcb8 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006d9a74 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006afcb8 bytes 482a00d0
+ 006d9a74 bytes e82c00b0
- 006afcbc ["COPY", "tmp:0:8", ["const:170:8"]]
- 006afcbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006afcbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9a78 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 006d9a78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9a78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9a78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006afcbc bytes 08c10591
+ 006d9a78 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-456843a9153dcb685344f93d4f3cc671"></a>

### [`006afcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md) → [`006d9aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9aa8.md) FUN_006d9aa8

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md) [`006abb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ab/006abb50.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0068c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068c/0068c5d0.md) [`006d4c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4c04.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 82.61% / 新版 76.00%

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
      "site": "006d9ae0",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006afd24",
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
      "site": "006d9afc",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006afd40",
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
      "site": "006d9b34",
      "value": [
        "leaf",
        "ram:6d4c04:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006afd78",
      "value": [
        "leaf",
        "ram:6abb50:8"
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
      "006d9ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006d9afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006d9b34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006abb50"
      ]
    ]
  ],
  "added": [
    [
      "006d9ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9afc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9b34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006d4c04"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006afd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md#insn-006afd24) · [`006afd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md#insn-006afd40) · [`006afd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md#insn-006afd78)
- 新版 `006d9ae0`（命令位置の公開資料なし） · `006d9afc`（命令位置の公開資料なし） · `006d9b34`（命令位置の公開資料なし）

~~~diff
- 006afd24 ["INT_ADD", "register:40f0:8", ["const:6afd24:8", "const:4:8"]]
- 006afd24 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9ae0 ["INT_ADD", "register:40f0:8", ["const:6d9ae0:8", "const:4:8"]]
+ 006d9ae0 ["CALL", null, ["ram:47acb4:8"]]
- 006afd24 bytes 3ea0f697
+ 006d9ae0 bytes 7584f697
- 006afd40 ["INT_ADD", "register:40f0:8", ["const:6afd40:8", "const:4:8"]]
- 006afd40 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9afc ["INT_ADD", "register:40f0:8", ["const:6d9afc:8", "const:4:8"]]
+ 006d9afc ["CALL", null, ["ram:47acb4:8"]]
- 006afd40 bytes 37a0f697
+ 006d9afc bytes 6e84f697
- 006afd78 ["INT_ADD", "register:40f0:8", ["const:6afd78:8", "const:4:8"]]
- 006afd78 ["CALL", null, ["ram:6abb50:8"]]
+ 006d9b34 ["INT_ADD", "register:40f0:8", ["const:6d9b34:8", "const:4:8"]]
+ 006d9b34 ["CALL", null, ["ram:6d4c04:8"]]
- 006afd78 bytes 76efff97
+ 006d9b34 bytes 34ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43c7bff12b1949b0d635edc636f710a3"></a>

### [`006afec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afec0.md) → [`006d9c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9c7c.md) FUN_006d9c7c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 46.27% / 新版 54.39%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006afee4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006aff48"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006aff7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006afee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d9ce4"
      ]
    ],
    [
      "006d9cb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006d9cbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006d9ca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006d9ce4"
      ]
    ],
    [
      "006d9cb0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9cbc",
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

- 旧版 [`006afee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afec0.md#insn-006afee4) · [`006afef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afec0.md#insn-006afef4) · [`006aff00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afec0.md#insn-006aff00)
- 新版 `006d9cb0`（命令位置の公開資料なし） · `006d9cbc`（命令位置の公開資料なし）

~~~diff
- 006afee4 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 006afee4 bytes 20020054
- 006afef4 ["INT_ADD", "register:40f0:8", ["const:6afef4:8", "const:4:8"]]
- 006afef4 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9cb0 ["INT_ADD", "register:40f0:8", ["const:6d9cb0:8", "const:4:8"]]
+ 006d9cb0 ["CALL", null, ["ram:47acb4:8"]]
- 006afef4 bytes ca9ff697
+ 006d9cb0 bytes 0184f697
- 006aff00 ["INT_ADD", "register:40f0:8", ["const:6aff00:8", "const:4:8"]]
- 006aff00 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9cbc ["INT_ADD", "register:40f0:8", ["const:6d9cbc:8", "const:4:8"]]
+ 006d9cbc ["CALL", null, ["ram:47acb4:8"]]
- 006aff00 bytes c79ff697
+ 006d9cbc bytes fe83f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c121ea809aea7aa5ce405ccaec45989"></a>

### [`006b0184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md) → [`006d9f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f40.md) FUN_006d9f40

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006d9f60",
      "incomplete_value": false,
      "site": "006d9f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b01a4",
      "incomplete_value": false,
      "site": "006b01a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:270:8"
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
      "006d9f64",
      "DATA",
      [
        "storage",
        "00bf9270",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006d9f64",
      "DATA",
      [
        "storage",
        "00c76398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md#insn-006b0198) · [`006b01a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md#insn-006b01a0) · [`006b01a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0184.md#insn-006b01a4)
- 新版 `006d9f54`（命令位置の公開資料なし） · `006d9f5c`（命令位置の公開資料なし） · `006d9f60`（命令位置の公開資料なし）

~~~diff
- 006b0198 ["INT_ADD", "register:40f0:8", ["const:6b0198:8", "const:4:8"]]
- 006b0198 ["CALL", null, ["callee:00c57a90:8"]]
+ 006d9f54 ["INT_ADD", "register:40f0:8", ["const:6d9f54:8", "const:4:8"]]
+ 006d9f54 ["CALL", null, ["callee:00c57a90:8"]]
- 006b0198 bytes aaab1494
+ 006d9f54 bytes cff61594
- 006b01a0 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006d9f5c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b01a0 bytes 482a00b0
+ 006d9f5c bytes e82c00b0
- 006b01a4 ["COPY", "tmp:0:8", ["const:270:8"]]
- 006b01a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006d9f60 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 006d9f60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9f60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006d9f60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b01a4 bytes 08c10991
+ 006d9f60 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d38007898654f6f7d555f2f60821617"></a>

### [`006b01dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01dc.md) → [`006d9f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d9/006d9f98.md) FUN_006d9f98

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 76.67% / 新版 68.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0264"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b02d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0310"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006d9fcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006d9fd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006b0264",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006b02a0"
      ]
    ]
  ],
  "added": [
    [
      "006d9fcc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006d9fd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006da05c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01dc.md#insn-006b0210) · [`006b021c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01dc.md#insn-006b021c) · [`006b0264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b01dc.md#insn-006b0264)
- 新版 `006d9fcc`（命令位置の公開資料なし） · `006d9fd8`（命令位置の公開資料なし）

~~~diff
- 006b0210 ["INT_ADD", "register:40f0:8", ["const:6b0210:8", "const:4:8"]]
- 006b0210 ["CALL", null, ["ram:457e1c:8"]]
+ 006d9fcc ["INT_ADD", "register:40f0:8", ["const:6d9fcc:8", "const:4:8"]]
+ 006d9fcc ["CALL", null, ["ram:47acb4:8"]]
- 006b0210 bytes 039ff697
+ 006d9fcc bytes 3a83f697
- 006b021c ["INT_ADD", "register:40f0:8", ["const:6b021c:8", "const:4:8"]]
- 006b021c ["CALL", null, ["ram:457e1c:8"]]
+ 006d9fd8 ["INT_ADD", "register:40f0:8", ["const:6d9fd8:8", "const:4:8"]]
+ 006d9fd8 ["CALL", null, ["ram:47acb4:8"]]
- 006b021c bytes 009ff697
+ 006d9fd8 bytes 3783f697
- 006b0264 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006b0264 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 006b0264 bytes e80100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ed61f9336250129b2e7d10e5fb52289"></a>

### [`006b0524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0524.md) → [`006da2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da2e0.md) FUN_006da2e0

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md) [`009e9ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9ac4.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.50% / 新版 89.50%

CFGの説明率　旧版 55.56% / 新版 44.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0534"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0534"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0538"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b0534",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0538",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b057c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006b07d0"
      ]
    ]
  ],
  "added": [
    [
      "006da2f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006da2f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006da338",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006da58c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0524.md#insn-006b0534) · [`006b0538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0524.md#insn-006b0538) · [`006b057c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0524.md#insn-006b057c)

~~~diff
- 006b0534 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006b0534 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006b0534 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006b0534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0534 bytes f65704a9
- 006b0538 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006b0538 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006b0538 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 006b0538 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0538 bytes f44f05a9
- 006b057c ["CBRANCH", null, ["local:b41:8", "register:101:1"]]
- 006b057c bytes a0120054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e5fdf64d08469f43af874acff8fce42"></a>

### [`006b0824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md) → [`006da5e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da5e0.md) FUN_006da5e0

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006da604",
      "incomplete_value": false,
      "site": "006da604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0848",
      "incomplete_value": false,
      "site": "006b0848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:370:8"
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
      "006da604",
      "DATA",
      [
        "storage",
        "00bf9370",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006da604",
      "DATA",
      [
        "storage",
        "00c76498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b0838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md#insn-006b0838) · [`006b0840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md#insn-006b0840) · [`006b0844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0824.md#insn-006b0844)
- 新版 `006da5f4`（命令位置の公開資料なし） · `006da5fc`（命令位置の公開資料なし） · `006da600`（命令位置の公開資料なし）

~~~diff
- 006b0838 ["INT_ADD", "register:40f0:8", ["const:6b0838:8", "const:4:8"]]
- 006b0838 ["CALL", null, ["callee:00c57a90:8"]]
+ 006da5f4 ["INT_ADD", "register:40f0:8", ["const:6da5f4:8", "const:4:8"]]
+ 006da5f4 ["CALL", null, ["callee:00c57a90:8"]]
- 006b0838 bytes 02aa1494
+ 006da5f4 bytes 27f51594
- 006b0840 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006da5fc ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006b0840 bytes 482a00b0
+ 006da5fc bytes e82c0090
- 006b0844 ["COPY", "tmp:0:8", ["const:370:8"]]
- 006b0844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006b0844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006da600 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 006da600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006da600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006da600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006b0844 bytes 08c10d91
+ 006da600 bytes 08611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5383f2c6e2c2b80e8534fcb83304b3da"></a>

### [`006b0874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0874.md) → [`006da630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da630.md) FUN_006da630

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046f248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f248.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`004920e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/004920e0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.71% / 新版 81.71%

CFGの説明率　旧版 85.00% / 新版 80.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_destination` 1件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "006da6dc",
      "incomplete_value": true,
      "site": "006da6dc",
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
            "const:3478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0920",
      "incomplete_value": true,
      "site": "006b0920",
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
            "const:3388:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006da700",
      "incomplete_value": true,
      "site": "006da700",
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
                "const:2ca000:8"
              ],
              [
                "leaf",
                "const:9a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b0944",
      "incomplete_value": true,
      "site": "006b0944",
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
                "const:2b9000:8"
              ],
              [
                "leaf",
                "const:290:8"
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
      "definition_site": "006da704",
      "incomplete_value": true,
      "site": "006da704",
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
      "definition_site": "006b0948",
      "incomplete_value": true,
      "site": "006b0948",
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
      "unmatched:006b08a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006b08b0",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b08b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006da7b0"
      ]
    ]
  ],
  "added": [
    [
      "006da664",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006da66c",
      "READ",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "006da674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006da7b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b08a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0874.md#insn-006b08a8) · [`006b08b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0874.md#insn-006b08b8) · [`006b08c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0874.md#insn-006b08c4)
- 新版 `006da680`（命令位置の公開資料なし）

~~~diff
- 006b08a8 ["INT_ADD", "register:40f0:8", ["const:6b08a8:8", "const:4:8"]]
- 006b08a8 ["CALL", null, ["ram:457e1c:8"]]
- 006b08a8 bytes 5d9df697
- 006b08b8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006b08b8 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 006b08b8 bytes e1090054
- 006b08c4 ["INT_ADD", "register:40f0:8", ["const:6b08c4:8", "const:4:8"]]
- 006b08c4 ["CALL", null, ["ram:457e1c:8"]]
+ 006da680 ["INT_ADD", "register:40f0:8", ["const:6da680:8", "const:4:8"]]
+ 006da680 ["CALL", null, ["ram:47acb4:8"]]
- 006b08c4 bytes 569df697
+ 006da680 bytes 8d81f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6c4d5de3d08587bcd3ce60d8a1a0a0e"></a>

### [`006b0a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md) → [`006da7dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006da7dc.md) _INIT_109

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.27% / 新版 76.27%

CFGの説明率　旧版 63.33% / 新版 51.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0a50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0a78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0a9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b0a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0a5c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006b0a78",
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
      "006da80c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "006da818",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "006da834",
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

- 旧版 [`006b0a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md#insn-006b0a50) · [`006b0a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md#insn-006b0a78) · [`006b0a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0a20.md#insn-006b0a9c)

~~~diff
- 006b0a50 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 006b0a50 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006b0a50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006b0a50 bytes a9831ff8
- 006b0a78 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 006b0a78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006b0a78 bytes e013813c
- 006b0a9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 006b0a9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006b0a9c bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf3a305ea858a6a2d0f8c64abebbf44f"></a>

### [`006b0db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md) → [`006dab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) FUN_006dab6c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`006d00e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`006dad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`006f9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9e98.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.45% / 新版 77.45%

CFGの説明率　旧版 31.58% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0db8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b0db4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0db8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0dbc",
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
      "006dab70",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006dab74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006dab78",
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

- 旧版 [`006b0db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md#insn-006b0db4) · [`006b0db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md#insn-006b0db8) · [`006b0dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md#insn-006b0dbc)

~~~diff
- 006b0db4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006b0db4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006b0db4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 006b0db4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0db4 bytes fd7b01a9
- 006b0db8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 006b0db8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 006b0db8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 006b0db8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0db8 bytes fc6f02a9
- 006b0dbc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 006b0dbc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 006b0dbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 006b0dbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0dbc bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3f90aae8c2dc3daaf2580d2d86e545e"></a>

### [`006b0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md) → [`006dad34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dad34.md) FUN_006dad34

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 9件 [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`006b0db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md) [`00ab1234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1234.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 9件 [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`006dab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.00% / 新版 61.00%

CFGの説明率　旧版 15.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0f7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b0f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b0f7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0f80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b0f84",
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
      "006dad38",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "006dad3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006dad40",
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

- 旧版 [`006b0f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b0f7c) · [`006b0f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b0f80) · [`006b0f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0f78.md#insn-006b0f84)

~~~diff
- 006b0f7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006b0f7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006b0f7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 006b0f7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0f7c bytes fd7b18a9
- 006b0f80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:190:8"]]
- 006b0f80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 006b0f80 bytes fccb00f9
- 006b0f84 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006b0f84 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006b0f84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 006b0f84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b0f84 bytes f6571aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72ffebe5e4771ba6a1b7d5eac9149f8b"></a>

### [`006b12cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md) → [`006db088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db088.md) FUN_006db088

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 12件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 85.39% / 新版 85.39%

CFGの説明率　旧版 76.92% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 8件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006db0c8",
      "incomplete_value": false,
      "site": "006db0cc",
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
      "definition_site": "006b130c",
      "incomplete_value": false,
      "site": "006b1310",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006db0e8",
      "incomplete_value": true,
      "site": "006db0f4",
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b132c",
      "incomplete_value": true,
      "site": "006b1338",
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
                "const:300:8"
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
      "definition_site": "006db0e4",
      "incomplete_value": true,
      "site": "006db0f8",
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
                "const:9c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b1328",
      "incomplete_value": true,
      "site": "006b133c",
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
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:739:8"
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
      "006db0cc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006db0e4",
      "READ",
      [
        "storage",
        "0029d739",
        null,
        "string"
      ]
    ],
    [
      "006db0e4",
      "READ",
      [
        "storage",
        "0029d749",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006db0cc",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "006db0e4",
      "READ",
      [
        "storage",
        "002ad9c3",
        null,
        "string"
      ]
    ],
    [
      "006db0e4",
      "READ",
      [
        "storage",
        "002ad9d3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b1404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md#insn-006b1404) · [`006b1474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md#insn-006b1474) · [`006b158c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b12cc.md#insn-006b158c)

~~~diff
- 006b1404 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 006b1404 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 006b1404 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 006b1404 ["INT_ZEXT", "register:40d8:8", ["tmp:0:4"]]
- 006b1404 bytes 1b00881a
- 006b1474 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 006b1474 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 006b1474 bytes 28ffffb5
- 006b158c ["COPY", "register:0:8", ["register:40f0:8"]]
- 006b158c ["RETURN", null, ["register:0:8"]]
- 006b158c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69afc8ba0eb8f9c3181bce9a77033a9"></a>

### [`006b15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md) → [`006db3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006db3a0.md) FUN_006db3a0

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068d810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d810.md) · 呼出先 27件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`006b3b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3b64.md) · 呼出先 27件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.78% / 新版 83.78%

CFGの説明率　旧版 63.21% / 新版 58.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `store_value` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b16b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b16d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b16dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006db3d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f2f8c"
      ]
    ],
    [
      "006db41c",
      "READ",
      [
        "storage",
        "00c27e14",
        null,
        "undefined4"
      ]
    ],
    [
      "006db438",
      "READ",
      [
        "storage",
        "00c27e10",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "006db3d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071cff4"
      ]
    ],
    [
      "006db41c",
      "READ",
      [
        "storage",
        "00ca7914",
        null,
        "undefined4"
      ]
    ],
    [
      "006db438",
      "READ",
      [
        "storage",
        "00ca7910",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b1618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b1618) · [`006b1690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b1690) · [`006b16b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md#insn-006b16b4)
- 新版 `006db3d4`（命令位置の公開資料なし）

~~~diff
- 006b1618 ["INT_ADD", "register:40f0:8", ["const:6b1618:8", "const:4:8"]]
- 006b1618 ["CALL", null, ["ram:6f2f8c:8"]]
+ 006db3d4 ["INT_ADD", "register:40f0:8", ["const:6db3d4:8", "const:4:8"]]
+ 006db3d4 ["CALL", null, ["ram:71cff4:8"]]
- 006b1618 bytes 5d060194
+ 006db3d4 bytes 08070194
- 006b1690 ["INT_ADD", "register:40f0:8", ["const:6b1690:8", "const:4:8"]]
- 006b1690 ["CALL", null, ["ram:6fe890:8"]]
- 006b1690 bytes 80340194
- 006b16b4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:1:8"]]
- 006b16b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006b16b4 bytes e012803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95c4e0f4faeff6a323499fdcd1e38a99"></a>

### [`006b1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md) → [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) FUN_006dbb2c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`006d02ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`006fa0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0a0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 68.99% / 新版 68.99%

CFGの説明率　旧版 42.86% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1d9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b1d74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b1d9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b1da4",
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
      "006dbb30",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "006dbb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "006dbb60",
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

- 旧版 [`006b1d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md#insn-006b1d74) · [`006b1d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md#insn-006b1d9c) · [`006b1da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md#insn-006b1da4)

~~~diff
- 006b1d74 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006b1d74 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006b1d74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 006b1d74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b1d74 bytes fd7b03a9
- 006b1d9c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 006b1d9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b1d9c bytes e80700f9
- 006b1da4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006b1da4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006b1da4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006b1da4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d662e8ba145d33f1aa47076d99c97fd"></a>

### [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) → [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) FUN_006dbd68

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c4ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`006b1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md) [`006b2318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md) [`006b25f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b25f4.md)
- 新版 呼出元 1件 [`006eec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006eec6c.md) · 呼出先 13件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) [`006dc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md) [`006dc3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc3b0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.87% / 新版 86.87%

CFGの説明率　旧版 67.14% / 新版 73.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1fc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b1fc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b1fc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b1fc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b1fe0",
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
      "006dbd7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006dbd80",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006dbd9c",
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

- 旧版 [`006b1fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md#insn-006b1fc0) · [`006b1fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md#insn-006b1fc4) · [`006b1fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md#insn-006b1fe0)

~~~diff
- 006b1fc0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006b1fc0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006b1fc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 006b1fc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b1fc0 bytes f6570aa9
- 006b1fc4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006b1fc4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006b1fc4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 006b1fc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b1fc4 bytes f44f0ba9
- 006b1fe0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006b1fe0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006b1fe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006b1fe0 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d86a2f946a0ae2fcbf06e6f5d9dde8e"></a>

### [`006b2318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md) → [`006dc0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc0d4.md) FUN_006dc0d4

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`006f2f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f2f8c.md) [`006fe6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fe6f8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0071cff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071c/0071cff4.md) [`007287f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00728/007287f8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.43% / 新版 87.43%

CFGの説明率　旧版 74.42% / 新版 77.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b24b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006dc26c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b243c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dc194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f2f8c"
      ]
    ],
    [
      "unmatched:006b243c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc21c"
      ]
    ],
    [
      "unmatched:006b2450",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc270"
      ]
    ]
  ],
  "added": [
    [
      "006dc194",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0071cff4"
      ]
    ],
    [
      "006dc1f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc21c"
      ]
    ],
    [
      "006dc20c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dc270"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b23d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md#insn-006b23d8) · [`006b243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md#insn-006b243c) · [`006b2450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2318.md#insn-006b2450)
- 新版 `006dc194`（命令位置の公開資料なし）

~~~diff
- 006b23d8 ["INT_ADD", "register:40f0:8", ["const:6b23d8:8", "const:4:8"]]
- 006b23d8 ["CALL", null, ["ram:6f2f8c:8"]]
+ 006dc194 ["INT_ADD", "register:40f0:8", ["const:6dc194:8", "const:4:8"]]
+ 006dc194 ["CALL", null, ["ram:71cff4:8"]]
- 006b23d8 bytes ed020194
+ 006dc194 bytes 98030194
- 006b243c ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 006b243c ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 006b243c bytes 290100b4
- 006b2450 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006b2450 ["CBRANCH", null, ["local:b28:8", "tmp:0:1"]]
- 006b2450 bytes 2a030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-495a1066f44c04a99934843d88780d15"></a>

### [`006b28b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b28b0.md) → [`006dc66c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc66c.md) FUN_006dc66c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 2件 [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045df50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045df50.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 2件 [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480de8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480de8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 46.67% / 新版 53.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006dc6c4",
      "incomplete_value": true,
      "site": "006dc6c8",
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
    "new": {
      "definition_site": "006dc6c0",
      "incomplete_value": true,
      "site": "006dc6c8",
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
    "old": null,
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006b290c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b28b0.md#insn-006b290c) · [`006b28d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b28b0.md#insn-006b28d4) · [`006b28e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b28b0.md#insn-006b28e4)
- 新版 `006dc6c8`（命令位置の公開資料なし） · `006dc690`（命令位置の公開資料なし） · `006dc6a0`（命令位置の公開資料なし）

~~~diff
- 006b290c ["INT_ADD", "register:40f0:8", ["const:6b290c:8", "const:4:8"]]
- 006b290c ["CALL", null, ["callee:00480ba8:8"]]
+ 006dc6c8 ["INT_ADD", "register:40f0:8", ["const:6dc6c8:8", "const:4:8"]]
+ 006dc6c8 ["CALL", null, ["callee:00480ba8:8"]]
- 006b290c bytes 01adf697
+ 006dc6c8 bytes 3891f697
- 006b28d4 ["INT_ADD", "register:40f0:8", ["const:6b28d4:8", "const:4:8"]]
- 006b28d4 ["CALL", null, ["callee:00480ba8:8"]]
+ 006dc690 ["INT_ADD", "register:40f0:8", ["const:6dc690:8", "const:4:8"]]
+ 006dc690 ["CALL", null, ["callee:00480ba8:8"]]
- 006b28d4 bytes 0fadf697
+ 006dc690 bytes 4691f697
- 006b28e4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006b28e4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 006dc6a0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 006dc6a0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 006b28e4 bytes 01010054
+ 006dc6a0 bytes 01010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df545439c44a968639b9f71a2ee9992"></a>

### [`006b294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md) → [`006dc708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc708.md) FUN_006dc708

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0045d300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d300.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00480198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480198.md) [`004803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004803b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 80.95% / 新版 77.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006b2974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md#insn-006b2974) · [`006b297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md#insn-006b297c) · [`006b298c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b294c.md#insn-006b298c)
- 新版 `006dc730`（命令位置の公開資料なし） · `006dc738`（命令位置の公開資料なし） · `006dc748`（命令位置の公開資料なし）

~~~diff
- 006b2974 ["INT_ADD", "register:40f0:8", ["const:6b2974:8", "const:4:8"]]
- 006b2974 ["CALL", null, ["callee:00480198:8"]]
+ 006dc730 ["INT_ADD", "register:40f0:8", ["const:6dc730:8", "const:4:8"]]
+ 006dc730 ["CALL", null, ["callee:00480198:8"]]
- 006b2974 bytes 63aaf697
+ 006dc730 bytes 9a8ef697
- 006b297c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006b297c ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 006dc738 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 006dc738 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 006b297c bytes 8b060054
+ 006dc738 bytes 8b060054
- 006b298c ["BRANCH", null, ["local:b4:8"]]
+ 006dc748 ["BRANCH", null, ["local:b5:8"]]
- 006b298c bytes 0a000014
+ 006dc748 bytes 0a000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-324e01872b9da0c6cb9ec6d114caee8e"></a>

### [`006b2b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md) → [`006dc900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dc/006dc900.md) FUN_006dc900

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c6850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md) · 呼出先 18件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044c794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c794.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md)
- 新版 呼出元 1件 [`006f0614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md) · 呼出先 18件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`0046f62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f62c.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 59.00% / 新版 59.00%

CFGの説明率　旧版 23.85% / 新版 24.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件, `unresolved_branch_alignment` 22件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 44件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b2b70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b2b8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b2b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b2b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b2b74",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:006b2b78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dcfcc"
      ]
    ]
  ],
  "added": [
    [
      "006dc92c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "006dc930",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dc934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dcfcc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b2b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md#insn-006b2b70) · [`006b2b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md#insn-006b2b8c) · [`006b2b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b2/006b2b44.md#insn-006b2b94)

~~~diff
- 006b2b70 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006b2b70 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 006b2b70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006b2b70 bytes a8831ff8
- 006b2b8c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 006b2b8c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 006b2b8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 006b2b8c bytes a8031b38
- 006b2b94 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 006b2b94 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc1:8"]]
- 006b2b94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 006b2b94 bytes a8131c78
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253ab8d75e3dd7ba8e3f251e4f4fe802"></a>

### [`006b3674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md) → [`006dd430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006dd/006dd430.md) FUN_006dd430

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 10件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006dd474",
      "incomplete_value": true,
      "site": "006dd484",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:292:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36b8",
      "incomplete_value": true,
      "site": "006b36c8",
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
                "const:b82:8"
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
      "definition_site": "006dd4a4",
      "incomplete_value": true,
      "site": "006dd4b8",
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
                "const:2b2000:8"
              ],
              [
                "leaf",
                "const:e43:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b36e8",
      "incomplete_value": true,
      "site": "006b36fc",
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
                "const:2a2000:8"
              ],
              [
                "leaf",
                "const:782:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006dd618",
      "incomplete_value": false,
      "site": "006dd618",
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
      "definition_site": "006b385c",
      "incomplete_value": false,
      "site": "006b385c",
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
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dd460",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd474",
      "READ",
      [
        "storage",
        "00292b82",
        null,
        "string"
      ]
    ],
    [
      "006dd4a4",
      "READ",
      [
        "storage",
        "002a2782",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006dd460",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006dd474",
      "READ",
      [
        "storage",
        "002a2292",
        null,
        "string"
      ]
    ],
    [
      "006dd4a4",
      "READ",
      [
        "storage",
        "002b2e43",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b3730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md#insn-006b3730) · [`006b3834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md#insn-006b3834) · [`006b3874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b3/006b3674.md#insn-006b3874)
- 新版 `006dd4ec`（命令位置の公開資料なし） · `006dd5f0`（命令位置の公開資料なし） · `006dd630`（命令位置の公開資料なし）

~~~diff
- 006b3730 ["INT_ADD", "register:40f0:8", ["const:6b3730:8", "const:4:8"]]
- 006b3730 ["CALL", null, ["callee:0047e5cc:8"]]
+ 006dd4ec ["INT_ADD", "register:40f0:8", ["const:6dd4ec:8", "const:4:8"]]
+ 006dd4ec ["CALL", null, ["callee:0047e5cc:8"]]
- 006b3730 bytes 01a0f697
+ 006dd4ec bytes 3884f697
- 006b3834 ["INT_ADD", "register:40f0:8", ["const:6b3834:8", "const:4:8"]]
- 006b3834 ["CALL", null, ["callee:00c57a50:8"]]
+ 006dd5f0 ["INT_ADD", "register:40f0:8", ["const:6dd5f0:8", "const:4:8"]]
+ 006dd5f0 ["CALL", null, ["callee:00c57a50:8"]]
- 006b3834 bytes f39d1494
+ 006dd5f0 bytes 18e91594
- 006b3874 ["INT_ADD", "register:40f0:8", ["const:6b3874:8", "const:4:8"]]
- 006b3874 ["CALL", null, ["callee:00c57a30:8"]]
+ 006dd630 ["INT_ADD", "register:40f0:8", ["const:6dd630:8", "const:4:8"]]
+ 006dd630 ["CALL", null, ["callee:00c57a30:8"]]
- 006b3874 bytes db9d1494
+ 006dd630 bytes 00e91594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3fa968fd379330cd5cd5e074bdb3496"></a>

### [`006b4a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4a1c.md) → [`006de7d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006de/006de7d8.md) FUN_006de7d8

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf80.md) [`0044d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d208.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.00% / 新版 56.00%

CFGの説明率　旧版 2.56% / 新版 3.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b4bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b4bf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006de9ac"
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
      "unmatched:006b4a58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "unmatched:006b4ae0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:006b4af0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "006de814",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006de89c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "006de8ac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b4a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4a1c.md#insn-006b4a58) · [`006b4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4a1c.md#insn-006b4ac4) · [`006b4ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b4/006b4a1c.md#insn-006b4ae0)
- 新版 `006de880`（命令位置の公開資料なし）

~~~diff
- 006b4a58 ["INT_ADD", "register:40f0:8", ["const:6b4a58:8", "const:4:8"]]
- 006b4a58 ["CALL", null, ["ram:449aec:8"]]
- 006b4a58 bytes 2554f697
- 006b4ac4 ["INT_ADD", "register:40f0:8", ["const:6b4ac4:8", "const:4:8"]]
- 006b4ac4 ["CALL", null, ["callee:0046ee18:8"]]
+ 006de880 ["INT_ADD", "register:40f0:8", ["const:6de880:8", "const:4:8"]]
+ 006de880 ["CALL", null, ["callee:0046ee18:8"]]
- 006b4ac4 bytes 2f5df697
+ 006de880 bytes 6641f697
- 006b4ae0 ["INT_ADD", "register:40f0:8", ["const:6b4ae0:8", "const:4:8"]]
- 006b4ae0 ["CALL", null, ["callee:008514b8:8"]]
- 006b4ae0 bytes a8aa0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f33ef50c0da37c35c24fc28c3f42835"></a>

### [`006b5748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5748.md) → [`006df504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006df504.md) FUN_006df504

採用 · 移動量 `+0x29dbc` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`008b11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md) · 呼出先 0件 
- 新版 呼出元 1件 [`008e5048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008e5/008e5048.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-5e0388369b9026c2a8eb103b24b4a831"></a>

### [`006b5918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md) → [`006df6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006df6d4.md) FUN_006df6d4

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md)
- 新版 呼出元 1件 [`006f1648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.98% / 新版 67.98%

CFGの説明率　旧版 54.29% / 新版 53.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_condition` 4件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5928"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b592c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b5928",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b592c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b5930",
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
      "006df6e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "006df6e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006df6ec",
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

- 旧版 [`006b5928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md#insn-006b5928) · [`006b592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md#insn-006b592c) · [`006b5930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5918.md#insn-006b5930)

~~~diff
- 006b5928 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 006b5928 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 006b5928 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 006b5928 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b5928 bytes fa6706a9
- 006b592c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 006b592c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 006b592c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 006b592c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b592c bytes f85f07a9
- 006b5930 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006b5930 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006b5930 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 006b5930 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b5930 bytes f65708a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d85ccdff9ba1cde053364e622b040c75"></a>

### [`006b5d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5d40.md) → [`006dfafc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfafc.md) FUN_006dfafc

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) [`0099a654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0099a/0099a654.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 6件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`00716d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00716/00716d50.md) [`008c5c08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c5c08.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`009d0184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009d0/009d0184.md) · 呼出先 5件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 38.89% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5d50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006dfb0c"
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
      "unmatched:006b5d50",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b5d64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dfb30"
      ]
    ]
  ],
  "added": [
    [
      "006dfb0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006dfb20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dfb30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5d40.md#insn-006b5d50) · [`006b5d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5d40.md#insn-006b5d64)
- 新版 `006dfb0c`（命令位置の公開資料なし）

~~~diff
- 006b5d50 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006b5d50 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006b5d50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006b5d50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b5d50 bytes f44f04a9
- 006b5d64 ["CBRANCH", null, ["local:b4:8", "register:102:1"]]
- 006b5d64 bytes 82000054
+ 006dfb0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 006dfb0c ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 006dfb0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
+ 006dfb0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 006dfb0c bytes f44f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f26865cfca9470da18f18d83b4ed2a"></a>

### [`006b5e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md) → [`006dfbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfbec.md) FUN_006dfbec

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 7件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007d2920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d2920.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0082a194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0082a/0082a194.md)
- 新版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 7件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`00805cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/00805cf4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085c10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085c/0085c10c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.47% / 新版 84.47%

CFGの説明率　旧版 20.59% / 新版 25.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006dfd68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5ee4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006dfc1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006b5ecc"
      ]
    ],
    [
      "unmatched:006b5ecc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:006b5ee4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dfd70"
      ]
    ]
  ],
  "added": [
    [
      "006dfc1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dfc88"
      ]
    ],
    [
      "006dfc88",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "006dfca0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006dfd70"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b5e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md#insn-006b5e84) · [`006b5ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md#insn-006b5ecc) · [`006b5ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5e30.md#insn-006b5ee4)
- 新版 `006dfc40`（命令位置の公開資料なし）

~~~diff
- 006b5e84 ["INT_ADD", "register:40f0:8", ["const:6b5e84:8", "const:4:8"]]
- 006b5e84 ["CALL", null, ["callee:00c58050:8"]]
+ 006dfc40 ["INT_ADD", "register:40f0:8", ["const:6dfc40:8", "const:4:8"]]
+ 006dfc40 ["CALL", null, ["callee:00c58050:8"]]
- 006b5e84 bytes df951494
+ 006dfc40 bytes 04e11594
- 006b5ecc ["INT_ADD", "register:40f0:8", ["const:6b5ecc:8", "const:4:8"]]
- 006b5ecc ["CALL", null, ["callee:008514b8:8"]]
- 006b5ecc bytes ada50594
- 006b5ee4 ["CBRANCH", null, ["local:b25:8", "register:101:1"]]
- 006b5ee4 bytes 80060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-464d6070025e9204bc495e9b6595df7d"></a>

### [`006b5fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md) → [`006dfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md) FUN_006dfd88

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ab1ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ab1/00ab1ecc.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00b1195c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b11/00b1195c.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.67% / 新版 85.67%

CFGの説明率　旧版 57.63% / 新版 71.58%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b5ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6028"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b5ff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c8]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b6004",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b6028",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006dfdb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x2c8]",
        null,
        null
      ]
    ],
    [
      "006dfdc0",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "006dfde4",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b5ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md#insn-006b5ff8) · [`006b6004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md#insn-006b6004) · [`006b6028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md#insn-006b6028)

~~~diff
- 006b5ff8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 006b5ff8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b5ff8 bytes e80700f9
- 006b6004 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 006b6004 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 006b6004 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 006b6004 bytes a8831ef8
- 006b6028 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:100:8"]]
- 006b6028 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b6028 bytes e88300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8edbc185016eb5c7c9d0d435a76fa39b"></a>

### [`006b66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md) → [`006e046c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e046c.md) FUN_006e046c

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

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
      "site": "006e04b0",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006b66f4",
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
      "definition_site": "006e04ac",
      "incomplete_value": false,
      "site": "006e04b0",
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
      "definition_site": "006b66f0",
      "incomplete_value": false,
      "site": "006b66f4",
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
      "006e04ac",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "006e04b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "006e04ac",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "006e04b0",
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

- 旧版 [`006b66f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md#insn-006b66f4) · [`006b66ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md#insn-006b66ec) · [`006b66f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b66b0.md#insn-006b66f0)
- 新版 `006e04b0`（命令位置の公開資料なし） · `006e04a8`（命令位置の公開資料なし） · `006e04ac`（命令位置の公開資料なし）

~~~diff
- 006b66f4 ["INT_ADD", "register:40f0:8", ["const:6b66f4:8", "const:4:8"]]
- 006b66f4 ["CALL", null, ["ram:41fdf0:8"]]
+ 006e04b0 ["INT_ADD", "register:40f0:8", ["const:6e04b0:8", "const:4:8"]]
+ 006e04b0 ["CALL", null, ["ram:4428f0:8"]]
- 006b66f4 bytes bfa5f597
+ 006e04b0 bytes 1089f597
- 006b66ec ["COPY", "register:4000:8", ["const:290000:8"]]
+ 006e04a8 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 006b66ec bytes c0deffd0
+ 006e04a8 bytes 00deff90
- 006b66f0 ["COPY", "tmp:0:8", ["const:bae:8"]]
- 006b66f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006b66f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006b66f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006e04ac ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 006e04ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006e04ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006e04ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006b66f0 bytes 00b82e91
+ 006e04ac bytes 00c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34af0675d74e712399b6c956a2d72dca"></a>

### [`006b6b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md) → [`006e0924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e0924.md) FUN_006e0924

採用 · 移動量 `+0x29dbc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b6c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6c84.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`006e0a40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e0/006e0a40.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 21.13% / 新版 21.13%

CFGの説明率　旧版 6.06% / 新版 6.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 9件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b6bc0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006e0930",
      "READ",
      [
        "storage",
        "00c27cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "006e0934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006b6b88"
      ]
    ],
    [
      "unmatched:006b6b80",
      "READ",
      [
        "storage",
        "00c27cd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e0930",
      "READ",
      [
        "storage",
        "00ca77c0",
        null,
        "undefined1"
      ]
    ],
    [
      "006e0934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006e0944"
      ]
    ],
    [
      "006e093c",
      "READ",
      [
        "storage",
        "00ca77d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b6b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b84) · [`006b6b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b90) · [`006b6b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b6/006b6b68.md#insn-006b6b9c)

~~~diff
- 006b6b84 ["INT_ADD", "register:40f0:8", ["const:6b6b84:8", "const:4:8"]]
- 006b6b84 ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6b84 bytes 37911494
- 006b6b90 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 006b6b90 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 006b6b90 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 006b6b90 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 006b6b90 bytes 88000036
- 006b6b9c ["INT_ADD", "register:40f0:8", ["const:6b6b9c:8", "const:4:8"]]
- 006b6b9c ["CALL", null, ["callee:00c57ab0:8"]]
- 006b6b9c bytes 31911494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eea23bba9f6dde59a1ed27b57717653c"></a>

### [`006b77e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md) → [`006e15a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e15a0.md) FUN_006e15a0

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md)
- 新版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.01% / 新版 88.01%

CFGの説明率　旧版 84.03% / 新版 87.72%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e16d0",
      "incomplete_value": true,
      "site": "006e16d0",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7914",
      "incomplete_value": true,
      "site": "006b7914",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:e09:8"
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
      "site": "006b792c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e17dc",
      "incomplete_value": true,
      "site": "006e17dc",
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b7a20",
      "incomplete_value": true,
      "site": "006b7a20",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b7860",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "unmatched:006b7864",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ],
    [
      "006e1654",
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
      "006e15d0",
      "DATA",
      [
        "storage",
        "00434658",
        null,
        "dword"
      ]
    ],
    [
      "006e15d8",
      "DATA",
      [
        "storage",
        "00434680",
        null,
        "byte[35]"
      ]
    ],
    [
      "006e161c",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b7864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b7864) · [`006b792c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b792c) · [`006b7968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b77e4.md#insn-006b7968)
- 新版 `006e1724`（命令位置の公開資料なし）

~~~diff
- 006b7864 ["INT_ADD", "register:40f0:8", ["const:6b7864:8", "const:4:8"]]
- 006b7864 ["CALL", null, ["ram:41fdf0:8"]]
- 006b7864 bytes 63a1f597
- 006b792c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 006b792c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 006b792c bytes e81b00f9
- 006b7968 ["INT_ADD", "register:40f0:8", ["const:6b7968:8", "const:4:8"]]
- 006b7968 ["CALL", null, ["callee:0047e5cc:8"]]
+ 006e1724 ["INT_ADD", "register:40f0:8", ["const:6e1724:8", "const:4:8"]]
+ 006e1724 ["CALL", null, ["callee:0047e5cc:8"]]
- 006b7968 bytes 738ff697
+ 006e1724 bytes aa73f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b9c417c98e5eddb78de708c35359c8c"></a>

### [`006b7fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7fe4.md) → [`006e1da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e1/006e1da0.md) FUN_006e1da0

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf80.md) [`0044d208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d208.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 5件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d770`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d770.md) [`0046ee18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ee18.md) [`004700a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/004700a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8058"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006e1e14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006b800c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b8000",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "unmatched:006b8044",
      "READ",
      [
        "storage",
        "002b2870",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e1dbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006e1e00",
      "READ",
      [
        "storage",
        "002c3f50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7fe4.md#insn-006b8000) · [`006b800c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7fe4.md#insn-006b800c) · [`006b8018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b7/006b7fe4.md#insn-006b8018)
- 新版 `006e1dd4`（命令位置の公開資料なし）

~~~diff
- 006b8000 ["INT_ADD", "register:40f0:8", ["const:6b8000:8", "const:4:8"]]
- 006b8000 ["CALL", null, ["ram:449aec:8"]]
- 006b8000 bytes bb46f697
- 006b800c ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006b800c ["COPY", "tmp:1:4", ["register:4000:4"]]
- 006b800c ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 006b800c ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 006b800c bytes 08a4801a
- 006b8018 ["INT_ADD", "register:40f0:8", ["const:6b8018:8", "const:4:8"]]
- 006b8018 ["CALL", null, ["callee:0046d770:8"]]
+ 006e1dd4 ["INT_ADD", "register:40f0:8", ["const:6e1dd4:8", "const:4:8"]]
+ 006e1dd4 ["CALL", null, ["callee:0046d770:8"]]
- 006b8018 bytes 304af697
+ 006e1dd4 bytes 672ef697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e24cb54bbddc8b4bccd2c719fbd8711"></a>

### [`006b8ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8ae0.md) → [`006e289c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e289c.md) FUN_006e289c

採用 · 移動量 `+0x29dbc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006ce8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`0044b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8c8.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`006f8688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f8688.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046e760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e760.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 84.06% / 新版 84.06%

CFGの説明率　旧版 50.00% / 新版 8.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006b8ba0",
      "incomplete_value": true,
      "site": "006b8bc8",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006b8b98",
      "incomplete_value": true,
      "site": "006b8bc8",
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
      "unmatched:006b8b80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "006e293c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8ae0.md#insn-006b8b80) · [`006b8bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8ae0.md#insn-006b8bc8)
- 新版 `006e2984`（命令位置の公開資料なし） · `006e293c`（命令位置の公開資料なし）

~~~diff
- 006b8b80 ["INT_ADD", "register:40f0:8", ["const:6b8b80:8", "const:4:8"]]
- 006b8b80 ["CALL", null, ["callee:008514b8:8"]]
- 006b8b80 bytes 809a0594
- 006b8bc8 ["INT_ADD", "register:40f0:8", ["const:6b8bc8:8", "const:4:8"]]
- 006b8bc8 ["CALL", null, ["callee:0046bd14:8"]]
+ 006e2984 ["INT_ADD", "register:40f0:8", ["const:6e2984:8", "const:4:8"]]
+ 006e2984 ["CALL", null, ["callee:0046bd14:8"]]
- 006b8bc8 bytes ad40f697
+ 006e2984 bytes e424f697
+ 006e293c ["INT_ADD", "register:40f0:8", ["const:6e293c:8", "const:4:8"]]
+ 006e293c ["CALL", null, ["callee:008514b8:8"]]
+ 006e293c bytes dfba0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-713bd79daa13e17cf047175b6e093b18"></a>

### [`006b8bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md) → [`006e29b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e29b0.md) FUN_006e29b0

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006b8e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ac4.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006e2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md) · 呼出先 11件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`0048795c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/0048795c.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.01% / 新版 78.01%

CFGの説明率　旧版 93.75% / 新版 90.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 15件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8bf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b8bfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b8bf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b8bfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:006b8c00",
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
      "006e29b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "006e29b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "006e29bc",
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

- 旧版 [`006b8bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md#insn-006b8bf8) · [`006b8bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md#insn-006b8bfc) · [`006b8c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8bf4.md#insn-006b8c00)

~~~diff
- 006b8bf8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 006b8bf8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 006b8bf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 006b8bf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b8bf8 bytes fd7b18a9
- 006b8bfc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:190:8"]]
- 006b8bfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 006b8bfc bytes fccb00f9
- 006b8c00 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006b8c00 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006b8c00 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 006b8c00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006b8c00 bytes f6571aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22f0dac6e09c55a5b41cec81d4e604b9"></a>

### [`006b8e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md) → [`006e2c34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e2/006e2c34.md) FUN_006e2c34

採用 · 移動量 `+0x29dbc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00440f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440f30.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.13% / 新版 88.13%

CFGの説明率　旧版 75.56% / 新版 79.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006e2d0c",
      "incomplete_value": true,
      "site": "006e2d0c",
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
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:3a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b8f50",
      "incomplete_value": true,
      "site": "006b8f50",
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
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:e09:8"
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
      "definition_site": "006e2e1c",
      "incomplete_value": true,
      "site": "006e2e1c",
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006b9060",
      "incomplete_value": true,
      "site": "006b9060",
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
                "const:299000:8"
              ],
              [
                "leaf",
                "const:df:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006b92a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006b8ecc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006e2cfc",
      "READ",
      [
        "storage",
        "002afe09",
        null,
        "string"
      ]
    ],
    [
      "006e2d50",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "006e2c88",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "006e2cfc",
      "READ",
      [
        "storage",
        "002c13a7",
        null,
        "string"
      ]
    ],
    [
      "006e2d50",
      "PARAM",
      [
        "storage",
        "00ca4b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006b8fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b8fa8) · [`006b911c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b911c) · [`006b91b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b8/006b8e78.md#insn-006b91b0)
- 新版 `006e2d64`（命令位置の公開資料なし） · `006e2ed8`（命令位置の公開資料なし）

~~~diff
- 006b8fa8 ["INT_ADD", "register:40f0:8", ["const:6b8fa8:8", "const:4:8"]]
- 006b8fa8 ["CALL", null, ["callee:0047e5cc:8"]]
+ 006e2d64 ["INT_ADD", "register:40f0:8", ["const:6e2d64:8", "const:4:8"]]
+ 006e2d64 ["CALL", null, ["callee:0047e5cc:8"]]
- 006b8fa8 bytes e389f697
+ 006e2d64 bytes 1a6ef697
- 006b911c ["INT_ADD", "register:40f0:8", ["const:6b911c:8", "const:4:8"]]
- 006b911c ["CALL", null, ["callee:004700a0:8"]]
+ 006e2ed8 ["INT_ADD", "register:40f0:8", ["const:6e2ed8:8", "const:4:8"]]
+ 006e2ed8 ["CALL", null, ["callee:004700a0:8"]]
- 006b911c bytes 3b50f697
+ 006e2ed8 bytes 7234f697
- 006b91b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006b91b0 ["CBRANCH", null, ["local:b56:8", "tmp:0:1"]]
- 006b91b0 bytes 41150054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5d6aea206efcf557cadd194f5a33a66"></a>

### [`006bed50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bed50.md) → [`006e8b14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8b14.md) FUN_006e8b14

採用 · 移動量 `+0x29dc4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) · 呼出先 3件 [`0069de1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de1c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) · 呼出先 3件 [`006c4180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006c4/006c4180.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`006bed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bed50.md#insn-006bed64) · [`006bed6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bed50.md#insn-006bed6c) · [`006bed74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bed50.md#insn-006bed74)
- 新版 `006e8b28`（命令位置の公開資料なし） · `006e8b30`（命令位置の公開資料なし） · `006e8b38`（命令位置の公開資料なし）

~~~diff
- 006bed64 ["INT_ADD", "register:40f0:8", ["const:6bed64:8", "const:4:8"]]
- 006bed64 ["CALL", null, ["callee:006c4180:8"]]
+ 006e8b28 ["INT_ADD", "register:40f0:8", ["const:6e8b28:8", "const:4:8"]]
+ 006e8b28 ["CALL", null, ["callee:006c4180:8"]]
- 006bed64 bytes 2e7cff97
+ 006e8b28 bytes 966dff97
- 006bed6c ["INT_ADD", "register:40f0:8", ["const:6bed6c:8", "const:4:8"]]
- 006bed6c ["CALL", null, ["callee:006c4180:8"]]
+ 006e8b30 ["INT_ADD", "register:40f0:8", ["const:6e8b30:8", "const:4:8"]]
+ 006e8b30 ["CALL", null, ["callee:006c4180:8"]]
- 006bed6c bytes 2c7cff97
+ 006e8b30 bytes 946dff97
- 006bed74 ["INT_ADD", "register:40f0:8", ["const:6bed74:8", "const:4:8"]]
- 006bed74 ["CALL", null, ["callee:006c4180:8"]]
+ 006e8b38 ["INT_ADD", "register:40f0:8", ["const:6e8b38:8", "const:4:8"]]
+ 006e8b38 ["CALL", null, ["callee:006c4180:8"]]
- 006bed74 bytes 2a7cff97
+ 006e8b38 bytes 926dff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2cf9c3427e61217b6250a092cfba747"></a>

### [`006bedc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006be/006bedc8.md) → [`006e8b8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e8/006e8b8c.md) FUN_006e8b8c

採用 · 移動量 `+0x29dc4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`0068c0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c0b0.md) [`0068c364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c364.md) · 呼出先 0件 
- 新版 呼出元 2件 [`006b23f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b23f8.md) [`006b26ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b26ac.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-68cd0b8515acd290448b1ae3ccf05202"></a>

### [`006c6608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6608.md) → [`006f03cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f03cc.md) FUN_006f03cc

採用 · 移動量 `+0x29dc4` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`006c5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md) [`006d3c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md) [`00906b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00906/00906b9c.md) [`00a56a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a56/00a56a58.md) · 呼出先 5件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 4件 [`006ef704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md) [`006fd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md) [`0093b5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0093b/0093b5d4.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 5件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 78.57% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f0480",
      "incomplete_value": true,
      "site": "006f0484",
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
            "const:18:8"
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
      "definition_site": "006f047c",
      "incomplete_value": true,
      "site": "006f0484",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006f047c",
      "incomplete_value": true,
      "site": "006f0484",
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
                "const:8:8"
              ]
            ]
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

- 旧版 [`006c66c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6608.md#insn-006c66c0) · [`006c662c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6608.md#insn-006c662c) · [`006c6634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6608.md#insn-006c6634)
- 新版 `006f0484`（命令位置の公開資料なし） · `006f03f0`（命令位置の公開資料なし） · `006f03f8`（命令位置の公開資料なし）

~~~diff
- 006c66c0 ["INT_ADD", "register:40f0:8", ["const:6c66c0:8", "const:4:8"]]
- 006c66c0 ["CALL", null, ["callee:0043bae0:8"]]
+ 006f0484 ["INT_ADD", "register:40f0:8", ["const:6f0484:8", "const:4:8"]]
+ 006f0484 ["CALL", null, ["callee:0043bae0:8"]]
- 006c66c0 bytes 484af597
+ 006f0484 bytes 972df597
- 006c662c ["INT_ADD", "register:40f0:8", ["const:6c662c:8", "const:4:8"]]
- 006c662c ["CALL", null, ["callee:00c57be0:8"]]
+ 006f03f0 ["INT_ADD", "register:40f0:8", ["const:6f03f0:8", "const:4:8"]]
+ 006f03f0 ["CALL", null, ["callee:00c57be0:8"]]
- 006c662c bytes d9521494
+ 006f03f0 bytes fc9d1594
- 006c6634 ["CBRANCH", null, ["local:b11:8", "register:102:1"]]
+ 006f03f8 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 006c6634 bytes 22050054
+ 006f03f8 bytes 22050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46bbc5767fd86aef2c22241d576ef3fe"></a>

### [`006c6850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md) → [`006f0614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f0614.md) FUN_006f0614

採用 · 移動量 `+0x29dc4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006c7884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c7/006c7884.md) · 呼出先 23件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md)
- 新版 呼出元 1件 [`006f1648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f1/006f1648.md) · 呼出先 23件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046e740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e740.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.90% / 新版 55.90%

CFGの説明率　旧版 6.39% / 新版 10.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 61件, `store_value` 4件, `unresolved_branch_alignment` 28件, `unresolved_call_alignment` 59件, `unresolved_store_alignment` 83件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c68e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c68e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006c68ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f064c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:006c6894",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:006c689c",
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
      "006f064c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006f0658",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f0660",
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

- 旧版 [`006c68e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c68e4) · [`006c68e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c68e8) · [`006c68ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c6850.md#insn-006c68ec)

~~~diff
- 006c68e4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 006c68e4 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 006c68e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 006c68e4 bytes 09400079
- 006c68e8 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffd0:8"]]
- 006c68e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 006c68e8 bytes a0039d3c
- 006c68ec ["COPY", "tmp:0:8", ["register:4000:8"]]
- 006c68ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 006c68ec ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 006c68ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 006c68ec bytes 010800ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab8852a9cbc2a0987941ac048304b56"></a>

### [`006ce8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md) → [`006f8688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f8688.md) FUN_006f8688

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 11件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`0044b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8c8.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 11件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046e760`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e760.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.63% / 新版 96.63%

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
      "site": "006f87f8",
      "value": [
        "leaf",
        "ram:6df514:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006cea44",
      "value": [
        "leaf",
        "ram:6b5758:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006f8978",
      "value": [
        "leaf",
        "ram:6e3cfc:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006cebc4",
      "value": [
        "leaf",
        "ram:6b9f40:8"
      ]
    },
    "ordinal": 17,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006f87c4",
      "READ",
      [
        "storage",
        "00c1b6b0",
        null,
        "pointer"
      ]
    ],
    [
      "006f87ec",
      "DATA",
      [
        "storage",
        "00c2459c",
        null,
        null
      ]
    ],
    [
      "006f87f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006b5758"
      ]
    ]
  ],
  "added": [
    [
      "006f87c4",
      "READ",
      [
        "storage",
        "00c9b0a8",
        null,
        "pointer"
      ]
    ],
    [
      "006f87ec",
      "DATA",
      [
        "storage",
        "00ca4084",
        null,
        null
      ]
    ],
    [
      "006f87f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006df514"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006cea44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md#insn-006cea44) · [`006cebc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md#insn-006cebc4) · [`006ce8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006ce8d4.md#insn-006ce8f8)
- 新版 `006f87f8`（命令位置の公開資料なし） · `006f8978`（命令位置の公開資料なし） · `006f86ac`（命令位置の公開資料なし）

~~~diff
- 006cea44 ["INT_ADD", "register:40f0:8", ["const:6cea44:8", "const:4:8"]]
- 006cea44 ["CALL", null, ["ram:6b5758:8"]]
+ 006f87f8 ["INT_ADD", "register:40f0:8", ["const:6f87f8:8", "const:4:8"]]
+ 006f87f8 ["CALL", null, ["ram:6df514:8"]]
- 006cea44 bytes 459bff97
+ 006f87f8 bytes 479bff97
- 006cebc4 ["INT_ADD", "register:40f0:8", ["const:6cebc4:8", "const:4:8"]]
- 006cebc4 ["CALL", null, ["ram:6b9f40:8"]]
+ 006f8978 ["INT_ADD", "register:40f0:8", ["const:6f8978:8", "const:4:8"]]
+ 006f8978 ["CALL", null, ["ram:6e3cfc:8"]]
- 006cebc4 bytes dfacff97
+ 006f8978 bytes e1acff97
- 006ce8f8 ["INT_ADD", "register:40f0:8", ["const:6ce8f8:8", "const:4:8"]]
- 006ce8f8 ["CALL", null, ["callee:00467820:8"]]
+ 006f86ac ["INT_ADD", "register:40f0:8", ["const:6f86ac:8", "const:4:8"]]
+ 006f86ac ["CALL", null, ["callee:00467820:8"]]
- 006ce8f8 bytes 24d8f597
+ 006f86ac bytes 5dbcf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b40d9552d26b11f97889aabd016d2f36"></a>

### [`006cec14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md) → [`006f89c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f8/006f89c8.md) FUN_006f89c8

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 30件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`006b3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b3/006b3440.md) · 呼出先 30件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467edc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467edc.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.80% / 新版 79.80%

CFGの説明率　旧版 51.52% / 新版 41.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 44件, `call_target` 9件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 57件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006cf434"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006f91e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "006f8a14",
      "incomplete_value": true,
      "site": "006f8a14",
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
      "definition_site": "006cec60",
      "incomplete_value": true,
      "site": "006cec60",
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
      "006f8a00",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8a1c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8a24",
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
      "006f8a00",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "006f8a1c",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "006f8a24",
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

- 旧版 [`006cec78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006cec78) · [`006cecc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006cecc4) · [`006ced10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ce/006cec14.md#insn-006ced10)
- 新版 `006f8a2c`（命令位置の公開資料なし） · `006f8a78`（命令位置の公開資料なし） · `006f8ac4`（命令位置の公開資料なし）

~~~diff
- 006cec78 ["INT_ADD", "register:40f0:8", ["const:6cec78:8", "const:4:8"]]
- 006cec78 ["CALL", null, ["callee:00c58210:8"]]
+ 006f8a2c ["INT_ADD", "register:40f0:8", ["const:6f8a2c:8", "const:4:8"]]
+ 006f8a2c ["CALL", null, ["callee:00c58210:8"]]
- 006cec78 bytes d2321494
+ 006f8a2c bytes f97d1594
- 006cecc4 ["INT_ADD", "register:40f0:8", ["const:6cecc4:8", "const:4:8"]]
- 006cecc4 ["CALL", null, ["ram:449aec:8"]]
+ 006f8a78 ["INT_ADD", "register:40f0:8", ["const:6f8a78:8", "const:4:8"]]
+ 006f8a78 ["CALL", null, ["ram:46c984:8"]]
- 006cecc4 bytes 8aebf597
+ 006f8a78 bytes c3cff597
- 006ced10 ["INT_ADD", "register:40f0:8", ["const:6ced10:8", "const:4:8"]]
- 006ced10 ["CALL", null, ["callee:008b7984:8"]]
+ 006f8ac4 ["INT_ADD", "register:40f0:8", ["const:6f8ac4:8", "const:4:8"]]
+ 006f8ac4 ["CALL", null, ["callee:008b7984:8"]]
- 006ced10 bytes b5d60694
+ 006f8ac4 bytes b0fb0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d1b57d8e94b1defa2f2137913859da"></a>

### [`006d00e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md) → [`006f9e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9e98.md) FUN_006f9e98

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006b0db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b0/006b0db0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006dab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006da/006dab6c.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006f9ea8",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d00f4",
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
      "definition_site": "006f9ea4",
      "incomplete_value": false,
      "site": "006f9ea8",
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
      "definition_site": "006d00f0",
      "incomplete_value": false,
      "site": "006d00f4",
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
      "006f9ea4",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006f9ea8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006f9ea4",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006f9ea8",
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

- 旧版 [`006d00f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md#insn-006d00f4) · [`006d00ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md#insn-006d00ec) · [`006d00f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d00e4.md#insn-006d00f0)
- 新版 `006f9ea8`（命令位置の公開資料なし） · `006f9ea0`（命令位置の公開資料なし） · `006f9ea4`（命令位置の公開資料なし）

~~~diff
- 006d00f4 ["INT_ADD", "register:40f0:8", ["const:6d00f4:8", "const:4:8"]]
- 006d00f4 ["CALL", null, ["ram:418c38:8"]]
+ 006f9ea8 ["INT_ADD", "register:40f0:8", ["const:6f9ea8:8", "const:4:8"]]
+ 006f9ea8 ["CALL", null, ["ram:43b738:8"]]
- 006d00f4 bytes d122f597
+ 006f9ea8 bytes 2406f597
- 006d00ec ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006f9ea0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 006d00ec bytes a0defff0
+ 006f9ea0 bytes e0ddffd0
- 006d00f0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 006d00f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006f9ea4 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006f9ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006f9ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006f9ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d00f0 bytes 00740e91
+ 006f9ea4 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0703483d24ccbafffa7b11a905ae2b"></a>

### [`006d014c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d014c.md) → [`006f9f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f00.md) FUN_006f9f00

採用 · 移動量 `+0x29db4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

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
      "site": "006f9f18",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0164",
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
      "site": "006f9f44",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d0190",
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
      "006f9f18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006f9f44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006f9f18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006f9f44",
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

- 旧版 [`006d0164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d014c.md#insn-006d0164) · [`006d0190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d014c.md#insn-006d0190) · [`006d019c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d014c.md#insn-006d019c)
- 新版 `006f9f18`（命令位置の公開資料なし） · `006f9f44`（命令位置の公開資料なし） · `006f9f50`（命令位置の公開資料なし）

~~~diff
- 006d0164 ["INT_ADD", "register:40f0:8", ["const:6d0164:8", "const:4:8"]]
- 006d0164 ["CALL", null, ["ram:457e1c:8"]]
+ 006f9f18 ["INT_ADD", "register:40f0:8", ["const:6f9f18:8", "const:4:8"]]
+ 006f9f18 ["CALL", null, ["ram:47acb4:8"]]
- 006d0164 bytes 2e1ff697
+ 006f9f18 bytes 6703f697
- 006d0190 ["INT_ADD", "register:40f0:8", ["const:6d0190:8", "const:4:8"]]
- 006d0190 ["CALL", null, ["ram:457e1c:8"]]
+ 006f9f44 ["INT_ADD", "register:40f0:8", ["const:6f9f44:8", "const:4:8"]]
+ 006f9f44 ["CALL", null, ["ram:47acb4:8"]]
- 006d0190 bytes 231ff697
+ 006f9f44 bytes 5c03f697
- 006d019c ["INT_ADD", "register:40f0:8", ["const:6d019c:8", "const:4:8"]]
- 006d019c ["CALL", null, ["callee:0047cd94:8"]]
+ 006f9f50 ["INT_ADD", "register:40f0:8", ["const:6f9f50:8", "const:4:8"]]
+ 006f9f50 ["CALL", null, ["callee:0047cd94:8"]]
- 006d019c bytes 5827f697
+ 006f9f50 bytes 910bf697
~~~


<a id="compare-a5d571ca0faa5585426d28748994e5b5"></a>

### [`006d01e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md) → [`006f9f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9f9c.md) FUN_006f9f9c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006f9fc0",
      "incomplete_value": false,
      "site": "006f9fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d020c",
      "incomplete_value": false,
      "site": "006d020c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "006f9fc0",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006f9fc0",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d01fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md#insn-006d01fc) · [`006d0204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md#insn-006d0204) · [`006d0208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d01e8.md#insn-006d0208)
- 新版 `006f9fb0`（命令位置の公開資料なし） · `006f9fb8`（命令位置の公開資料なし） · `006f9fbc`（命令位置の公開資料なし）

~~~diff
- 006d01fc ["INT_ADD", "register:40f0:8", ["const:6d01fc:8", "const:4:8"]]
- 006d01fc ["CALL", null, ["callee:00c57a90:8"]]
+ 006f9fb0 ["INT_ADD", "register:40f0:8", ["const:6f9fb0:8", "const:4:8"]]
+ 006f9fb0 ["CALL", null, ["callee:00c57a90:8"]]
- 006d01fc bytes 912b1494
+ 006f9fb0 bytes b8761594
- 006d0204 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006f9fb8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d0204 bytes 482900b0
+ 006f9fb8 bytes e82b00b0
- 006d0208 ["COPY", "tmp:0:8", ["const:470:8"]]
- 006d0208 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d0208 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006f9fbc ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006f9fbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9fbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006f9fbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d0208 bytes 08c11191
+ 006f9fbc bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f2478fbc375b61ca90c820ae885c29d"></a>

### [`006d021c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d021c.md) → [`006f9fd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f9/006f9fd0.md) FUN_006f9fd0

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006f9fdc",
      "incomplete_value": false,
      "site": "006f9fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d0228",
      "incomplete_value": false,
      "site": "006d0228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:470:8"
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
      "006f9fdc",
      "DATA",
      [
        "storage",
        "00bf9470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006f9fdc",
      "DATA",
      [
        "storage",
        "00c76598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d0220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d021c.md#insn-006d0220) · [`006d0224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d021c.md#insn-006d0224)
- 新版 `006f9fd4`（命令位置の公開資料なし） · `006f9fd8`（命令位置の公開資料なし）

~~~diff
- 006d0220 ["COPY", "register:4048:8", ["const:bf9000:8"]]
+ 006f9fd4 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006d0220 bytes 492900b0
+ 006f9fd4 bytes e92b00b0
- 006d0224 ["COPY", "tmp:0:8", ["const:470:8"]]
- 006d0224 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d0224 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006f9fd8 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 006f9fd8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006f9fd8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006f9fd8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d0224 bytes 29c11191
+ 006f9fd8 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed212843b558178de23310edb8d4b0f"></a>

### [`006d02ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md) → [`006fa0a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0a0.md) FUN_006fa0a0

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`006b1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1d70.md) [`006b1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1fac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`006dbb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbb2c.md) [`006dbd68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006db/006dbd68.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "006fa0b0",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d02fc",
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
      "definition_site": "006fa0ac",
      "incomplete_value": false,
      "site": "006fa0b0",
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
      "definition_site": "006d02f8",
      "incomplete_value": false,
      "site": "006d02fc",
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
      "006fa0ac",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "006fa0b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "006fa0ac",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "006fa0b0",
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

- 旧版 [`006d02fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md#insn-006d02fc) · [`006d02f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md#insn-006d02f4) · [`006d02f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d02ec.md#insn-006d02f8)
- 新版 `006fa0b0`（命令位置の公開資料なし） · `006fa0a8`（命令位置の公開資料なし） · `006fa0ac`（命令位置の公開資料なし）

~~~diff
- 006d02fc ["INT_ADD", "register:40f0:8", ["const:6d02fc:8", "const:4:8"]]
- 006d02fc ["CALL", null, ["ram:418c38:8"]]
+ 006fa0b0 ["INT_ADD", "register:40f0:8", ["const:6fa0b0:8", "const:4:8"]]
+ 006fa0b0 ["CALL", null, ["ram:43b738:8"]]
- 006d02fc bytes 4f22f597
+ 006fa0b0 bytes a205f597
- 006d02f4 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 006fa0a8 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 006d02f4 bytes a0defff0
+ 006fa0a8 bytes e0ddffb0
- 006d02f8 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 006d02f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ac ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 006fa0ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 006fa0ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 006d02f8 bytes 00740e91
+ 006fa0ac bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1a29203fe27c17a5c0d89682f40d4df"></a>

### [`006d0300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md) → [`006fa0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0b4.md) FUN_006fa0b4

採用 · 移動量 `+0x29db4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006b5fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md) [`006d0300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md) [`008350b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00835/008350b0.md) · 呼出先 2件 [`006d0300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`006dfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md) [`006fa0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0b4.md) [`00867028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00867/00867028.md) · 呼出先 2件 [`006fa0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa0b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.33% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006d0314",
      "incomplete_value": true,
      "site": "006d031c",
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

- 旧版 [`006d031c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md#insn-006d031c) · [`006d0300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md#insn-006d0300) · [`006d0328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d0300.md#insn-006d0328)
- 新版 `006fa0d0`（命令位置の公開資料なし） · `006fa0b4`（命令位置の公開資料なし） · `006fa0dc`（命令位置の公開資料なし）

~~~diff
- 006d031c ["INT_ADD", "register:40f0:8", ["const:6d031c:8", "const:4:8"]]
- 006d031c ["CALL", null, ["local:b0:8"]]
+ 006fa0d0 ["INT_ADD", "register:40f0:8", ["const:6fa0d0:8", "const:4:8"]]
+ 006fa0d0 ["CALL", null, ["local:b0:8"]]
- 006d031c bytes f9ffff97
+ 006fa0d0 bytes f9ffff97
- 006d0300 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 006d0300 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 006fa0b4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 006fa0b4 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 006d0300 bytes 210300b4
+ 006fa0b4 bytes 210300b4
- 006d0328 ["INT_ADD", "register:40f0:8", ["const:6d0328:8", "const:4:8"]]
- 006d0328 ["CALL", null, ["local:b0:8"]]
+ 006fa0dc ["INT_ADD", "register:40f0:8", ["const:6fa0dc:8", "const:4:8"]]
+ 006fa0dc ["CALL", null, ["local:b0:8"]]
- 006d0328 bytes f6ffff97
+ 006fa0dc bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497200dd84b8b630974d59086348d912"></a>

### [`006d039c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d039c.md) → [`006fa150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fa/006fa150.md) FUN_006fa150

採用 · 移動量 `+0x29db4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006b5fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5fcc.md) · 呼出先 2件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`006dfd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006df/006dfd88.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.89% / 新版 84.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "006d04c8",
      "incomplete_value": true,
      "site": "006d04dc",
      "value": [
        "live",
        "register:40a0:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`006d040c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d039c.md#insn-006d040c) · [`006d04ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d0/006d039c.md#insn-006d04ac)
- 新版 `006fa1c0`（命令位置の公開資料なし） · `006fa260`（命令位置の公開資料なし）

~~~diff
- 006d040c ["INT_ADD", "register:40f0:8", ["const:6d040c:8", "const:4:8"]]
- 006d040c ["CALL", null, ["callee:00c57a90:8"]]
+ 006fa1c0 ["INT_ADD", "register:40f0:8", ["const:6fa1c0:8", "const:4:8"]]
+ 006fa1c0 ["CALL", null, ["callee:00c57a90:8"]]
- 006d040c bytes 0d2b1494
+ 006fa1c0 bytes 34761594
- 006d04ac ["INT_ADD", "register:40f0:8", ["const:6d04ac:8", "const:4:8"]]
- 006d04ac ["CALL", null, ["callee:0043bb64:8"]]
+ 006fa260 ["INT_ADD", "register:40f0:8", ["const:6fa260:8", "const:4:8"]]
+ 006fa260 ["CALL", null, ["callee:0043bb64:8"]]
- 006d04ac bytes ee22f597
+ 006fa260 bytes 4106f597
~~~


<a id="compare-bbdfc252706014e2189dd21b7f0aea92"></a>

### [`006d12f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md) → [`006fb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb0a8.md) FUN_006fb0a8

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fb0bc",
      "incomplete_value": false,
      "site": "006fb0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:618:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1308",
      "incomplete_value": false,
      "site": "006d130c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:4f0:8"
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
      "006fb0c0",
      "DATA",
      [
        "storage",
        "00bf94f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb0c0",
      "DATA",
      [
        "storage",
        "00c76618",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md#insn-006d1300) · [`006d1304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md#insn-006d1304) · [`006d1308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d12f4.md#insn-006d1308)
- 新版 `006fb0b4`（命令位置の公開資料なし） · `006fb0b8`（命令位置の公開資料なし） · `006fb0bc`（命令位置の公開資料なし）

~~~diff
- 006d1300 ["INT_ADD", "register:40f0:8", ["const:6d1300:8", "const:4:8"]]
- 006d1300 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fb0b4 ["INT_ADD", "register:40f0:8", ["const:6fb0b4:8", "const:4:8"]]
+ 006fb0b4 ["CALL", null, ["callee:00c57a90:8"]]
- 006d1300 bytes 50271494
+ 006fb0b4 bytes 77721594
- 006d1304 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fb0b8 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d1304 bytes 48290090
+ 006fb0b8 bytes c82b00f0
- 006d1308 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 006d1308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb0bc ["COPY", "tmp:0:8", ["const:618:8"]]
+ 006fb0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1308 bytes 08c11391
+ 006fb0bc bytes 08611891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a956e911d113aa74dd7106c5886d49c4"></a>

### [`006d1398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md) → [`006fb14c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb14c.md) FUN_006fb14c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fb170",
      "incomplete_value": false,
      "site": "006fb174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d13bc",
      "incomplete_value": false,
      "site": "006d13c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:570:8"
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
      "006fb174",
      "DATA",
      [
        "storage",
        "00bf9570",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb174",
      "DATA",
      [
        "storage",
        "00c76698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d13ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md#insn-006d13ac) · [`006d13b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md#insn-006d13b8) · [`006d13bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1398.md#insn-006d13bc)
- 新版 `006fb160`（命令位置の公開資料なし） · `006fb16c`（命令位置の公開資料なし） · `006fb170`（命令位置の公開資料なし）

~~~diff
- 006d13ac ["INT_ADD", "register:40f0:8", ["const:6d13ac:8", "const:4:8"]]
- 006d13ac ["CALL", null, ["callee:00c57a90:8"]]
+ 006fb160 ["INT_ADD", "register:40f0:8", ["const:6fb160:8", "const:4:8"]]
+ 006fb160 ["CALL", null, ["callee:00c57a90:8"]]
- 006d13ac bytes 25271494
+ 006fb160 bytes 4c721594
- 006d13b8 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fb16c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d13b8 bytes 48290090
+ 006fb16c bytes c82b00f0
- 006d13bc ["COPY", "tmp:0:8", ["const:570:8"]]
- 006d13bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d13bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb170 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 006fb170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d13bc bytes 08c11591
+ 006fb170 bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bd7aff71b478c43092512152a48d0da"></a>

### [`006d1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md) → [`006fb1b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb1b4.md) FUN_006fb1b4

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 24件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.88% / 新版 86.88%

CFGの説明率　旧版 57.45% / 新版 62.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 2件, `store_value` 4件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb2d8",
      "incomplete_value": true,
      "site": "006fb2ec",
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
                "const:e9f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1524",
      "incomplete_value": true,
      "site": "006d1538",
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
                "const:7c5:8"
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
      "definition_site": "006fb338",
      "incomplete_value": true,
      "site": "006fb338",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:c4b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1584",
      "incomplete_value": true,
      "site": "006d1584",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:bd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fb33c",
      "incomplete_value": true,
      "site": "006fb33c",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1588",
      "incomplete_value": true,
      "site": "006d1588",
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
                "const:5:8"
              ]
            ]
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
      "unmatched:006d144c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006d1468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fb820"
      ]
    ],
    [
      "unmatched:006d147c",
      "READ",
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
      "006fb200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fb21c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fb820"
      ]
    ],
    [
      "006fb230",
      "READ",
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

- 旧版 [`006d144c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md#insn-006d144c) · [`006d1468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md#insn-006d1468) · [`006d14b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1400.md#insn-006d14b0)
- 新版 `006fb264`（命令位置の公開資料なし）

~~~diff
- 006d144c ["INT_ADD", "register:40f0:8", ["const:6d144c:8", "const:4:8"]]
- 006d144c ["CALL", null, ["ram:457e1c:8"]]
- 006d144c bytes 741af697
- 006d1468 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006d1468 ["CBRANCH", null, ["local:b60:8", "tmp:0:1"]]
- 006d1468 bytes 21300054
- 006d14b0 ["INT_ADD", "register:40f0:8", ["const:6d14b0:8", "const:4:8"]]
- 006d14b0 ["CALL", null, ["ram:6c3fe0:8"]]
+ 006fb264 ["INT_ADD", "register:40f0:8", ["const:6fb264:8", "const:4:8"]]
+ 006fb264 ["CALL", null, ["ram:6edda4:8"]]
- 006d14b0 bytes cccaff97
+ 006fb264 bytes d0caff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedabafad26066d960280d89c8880467"></a>

### [`006d1acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md) → [`006fb880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb880.md) FUN_006fb880

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fb8a4",
      "incomplete_value": false,
      "site": "006fb8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1af0",
      "incomplete_value": false,
      "site": "006d1af0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "006fb8a4",
      "DATA",
      [
        "storage",
        "00bf95e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb8a4",
      "DATA",
      [
        "storage",
        "00c76708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md#insn-006d1ae0) · [`006d1ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md#insn-006d1ae8) · [`006d1aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1acc.md#insn-006d1aec)
- 新版 `006fb894`（命令位置の公開資料なし） · `006fb89c`（命令位置の公開資料なし） · `006fb8a0`（命令位置の公開資料なし）

~~~diff
- 006d1ae0 ["INT_ADD", "register:40f0:8", ["const:6d1ae0:8", "const:4:8"]]
- 006d1ae0 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fb894 ["INT_ADD", "register:40f0:8", ["const:6fb894:8", "const:4:8"]]
+ 006fb894 ["CALL", null, ["callee:00c57a90:8"]]
- 006d1ae0 bytes 58251494
+ 006fb894 bytes 7f701594
- 006d1ae8 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fb89c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d1ae8 bytes 48290090
+ 006fb89c bytes c82b00f0
- 006d1aec ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 006d1aec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1aec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fb8a0 ["COPY", "tmp:0:8", ["const:708:8"]]
+ 006fb8a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb8a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fb8a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1aec bytes 08811791
+ 006fb8a0 bytes 08211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96427b94af90011ea3ce4d0a715a5e2a"></a>

### [`006d1b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b00.md) → [`006fb8b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb8b4.md) FUN_006fb8b4

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fb8c0",
      "incomplete_value": false,
      "site": "006fb8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1b0c",
      "incomplete_value": false,
      "site": "006d1b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:5e0:8"
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
      "006fb8c0",
      "DATA",
      [
        "storage",
        "00bf95e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fb8c0",
      "DATA",
      [
        "storage",
        "00c76708",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b00.md#insn-006d1b04) · [`006d1b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1b00.md#insn-006d1b08)
- 新版 `006fb8b8`（命令位置の公開資料なし） · `006fb8bc`（命令位置の公開資料なし）

~~~diff
- 006d1b04 ["COPY", "register:4048:8", ["const:bf9000:8"]]
+ 006fb8b8 ["COPY", "register:4048:8", ["const:c76000:8"]]
- 006d1b04 bytes 49290090
+ 006fb8b8 bytes c92b00f0
- 006d1b08 ["COPY", "tmp:0:8", ["const:5e0:8"]]
- 006d1b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006fb8bc ["COPY", "tmp:0:8", ["const:708:8"]]
+ 006fb8bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006fb8bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006fb8bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006d1b08 bytes 29811791
+ 006fb8bc bytes 29211c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ec252e4033b0374bbf88ef2378c14c4"></a>

### [`006d1c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md) → [`006fb9f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fb9f8.md) FUN_006fb9f8

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fba18",
      "incomplete_value": false,
      "site": "006fba1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1c64",
      "incomplete_value": false,
      "site": "006d1c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:670:8"
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
      "006fba1c",
      "DATA",
      [
        "storage",
        "00bf9670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fba1c",
      "DATA",
      [
        "storage",
        "00c76798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md#insn-006d1c58) · [`006d1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md#insn-006d1c60) · [`006d1c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1c44.md#insn-006d1c64)
- 新版 `006fba0c`（命令位置の公開資料なし） · `006fba14`（命令位置の公開資料なし） · `006fba18`（命令位置の公開資料なし）

~~~diff
- 006d1c58 ["INT_ADD", "register:40f0:8", ["const:6d1c58:8", "const:4:8"]]
- 006d1c58 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fba0c ["INT_ADD", "register:40f0:8", ["const:6fba0c:8", "const:4:8"]]
+ 006fba0c ["CALL", null, ["callee:00c57a90:8"]]
- 006d1c58 bytes fa241494
+ 006fba0c bytes 21701594
- 006d1c60 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fba14 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d1c60 bytes 48290090
+ 006fba14 bytes c82b00f0
- 006d1c64 ["COPY", "tmp:0:8", ["const:670:8"]]
- 006d1c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fba18 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 006fba18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fba18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1c64 bytes 08c11991
+ 006fba18 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-426d240f981cddfb861fff45c757650a"></a>

### [`006d1e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md) → [`006fbc1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc1c.md) FUN_006fbc1c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fbc40",
      "incomplete_value": false,
      "site": "006fbc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:818:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d1e8c",
      "incomplete_value": false,
      "site": "006d1e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:6f0:8"
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
      "006fbc40",
      "DATA",
      [
        "storage",
        "00bf96f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fbc40",
      "DATA",
      [
        "storage",
        "00c76818",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d1e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md#insn-006d1e7c) · [`006d1e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md#insn-006d1e84) · [`006d1e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1e68.md#insn-006d1e88)
- 新版 `006fbc30`（命令位置の公開資料なし） · `006fbc38`（命令位置の公開資料なし） · `006fbc3c`（命令位置の公開資料なし）

~~~diff
- 006d1e7c ["INT_ADD", "register:40f0:8", ["const:6d1e7c:8", "const:4:8"]]
- 006d1e7c ["CALL", null, ["callee:00c57a90:8"]]
+ 006fbc30 ["INT_ADD", "register:40f0:8", ["const:6fbc30:8", "const:4:8"]]
+ 006fbc30 ["CALL", null, ["callee:00c57a90:8"]]
- 006d1e7c bytes 71241494
+ 006fbc30 bytes 986f1594
- 006d1e84 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fbc38 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d1e84 bytes 48290090
+ 006fbc38 bytes c82b00f0
- 006d1e88 ["COPY", "tmp:0:8", ["const:6f0:8"]]
- 006d1e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fbc3c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 006fbc3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbc3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fbc3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d1e88 bytes 08c11b91
+ 006fbc3c bytes 08612091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a265622f460b0e02374fbdcd28a32ce5"></a>

### [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) → [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) FUN_006fbd90

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006bb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bb5d0.md) [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) [`006d2368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md) · 呼出先 5件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) [`006d2368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md) [`006d26b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) · 呼出先 5件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 94.27% / 新版 94.27%

CFGの説明率　旧版 88.89% / 新版 84.85%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006d22d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006fc08c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fbde8",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d2034",
      "value": [
        "leaf",
        "ram:6bacc8:8"
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
      "006fbde8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fbdfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fbe78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fbde8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fbdfc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fbe78",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d2034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md#insn-006d2034) · [`006d2048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md#insn-006d2048) · [`006d20c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md#insn-006d20c4)
- 新版 `006fbde8`（命令位置の公開資料なし） · `006fbdfc`（命令位置の公開資料なし） · `006fbe78`（命令位置の公開資料なし）

~~~diff
- 006d2034 ["INT_ADD", "register:40f0:8", ["const:6d2034:8", "const:4:8"]]
- 006d2034 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fbde8 ["INT_ADD", "register:40f0:8", ["const:6fbde8:8", "const:4:8"]]
+ 006fbde8 ["CALL", null, ["ram:6e4a84:8"]]
- 006d2034 bytes 25a3ff97
+ 006fbde8 bytes 27a3ff97
- 006d2048 ["INT_ADD", "register:40f0:8", ["const:6d2048:8", "const:4:8"]]
- 006d2048 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fbdfc ["INT_ADD", "register:40f0:8", ["const:6fbdfc:8", "const:4:8"]]
+ 006fbdfc ["CALL", null, ["ram:6e4a84:8"]]
- 006d2048 bytes 20a3ff97
+ 006fbdfc bytes 22a3ff97
- 006d20c4 ["INT_ADD", "register:40f0:8", ["const:6d20c4:8", "const:4:8"]]
- 006d20c4 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fbe78 ["INT_ADD", "register:40f0:8", ["const:6fbe78:8", "const:4:8"]]
+ 006fbe78 ["CALL", null, ["ram:6e4a84:8"]]
- 006d20c4 bytes 01a3ff97
+ 006fbe78 bytes 03a3ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6cc14dbcb51847ea014740117b5ea4"></a>

### [`006d2368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md) → [`006fc11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc11c.md) FUN_006fc11c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) · 呼出先 3件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) · 呼出先 3件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.62% / 新版 89.62%

CFGの説明率　旧版 84.38% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006d2484"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006d2498"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006fc238"
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
      "006fc16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fc180",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "unmatched:006d2464",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fc16c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc180",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc218",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d23b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md#insn-006d23b8) · [`006d23cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md#insn-006d23cc) · [`006d2464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2368.md#insn-006d2464)
- 新版 `006fc16c`（命令位置の公開資料なし） · `006fc180`（命令位置の公開資料なし）

~~~diff
- 006d23b8 ["INT_ADD", "register:40f0:8", ["const:6d23b8:8", "const:4:8"]]
- 006d23b8 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fc16c ["INT_ADD", "register:40f0:8", ["const:6fc16c:8", "const:4:8"]]
+ 006fc16c ["CALL", null, ["ram:6e4a84:8"]]
- 006d23b8 bytes 44a2ff97
+ 006fc16c bytes 46a2ff97
- 006d23cc ["INT_ADD", "register:40f0:8", ["const:6d23cc:8", "const:4:8"]]
- 006d23cc ["CALL", null, ["ram:6bacc8:8"]]
+ 006fc180 ["INT_ADD", "register:40f0:8", ["const:6fc180:8", "const:4:8"]]
+ 006fc180 ["CALL", null, ["ram:6e4a84:8"]]
- 006d23cc bytes 3fa2ff97
+ 006fc180 bytes 41a2ff97
- 006d2464 ["INT_ADD", "register:40f0:8", ["const:6d2464:8", "const:4:8"]]
- 006d2464 ["CALL", null, ["ram:6bacc8:8"]]
- 006d2464 bytes 19a2ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92d8908af0281776d3d470f9a295c97"></a>

### [`006d26b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md) → [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) FUN_006fc46c

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006d1fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d1/006d1fdc.md) [`006d26b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md) · 呼出先 4件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d26b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`006fbd90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbd90.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) · 呼出先 4件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fc46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fc46c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 96.31% / 新版 96.31%

CFGの説明率　旧版 90.30% / 新版 93.80%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006d2880"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "006d2c18"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "006fc634"
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
      "006fc4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fc4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fc570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fc4d8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc4ec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fc570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d2724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md#insn-006d2724) · [`006d2738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md#insn-006d2738) · [`006d27bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d26b8.md#insn-006d27bc)
- 新版 `006fc4d8`（命令位置の公開資料なし） · `006fc4ec`（命令位置の公開資料なし） · `006fc570`（命令位置の公開資料なし）

~~~diff
- 006d2724 ["INT_ADD", "register:40f0:8", ["const:6d2724:8", "const:4:8"]]
- 006d2724 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fc4d8 ["INT_ADD", "register:40f0:8", ["const:6fc4d8:8", "const:4:8"]]
+ 006fc4d8 ["CALL", null, ["ram:6e4a84:8"]]
- 006d2724 bytes 69a1ff97
+ 006fc4d8 bytes 6ba1ff97
- 006d2738 ["INT_ADD", "register:40f0:8", ["const:6d2738:8", "const:4:8"]]
- 006d2738 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fc4ec ["INT_ADD", "register:40f0:8", ["const:6fc4ec:8", "const:4:8"]]
+ 006fc4ec ["CALL", null, ["ram:6e4a84:8"]]
- 006d2738 bytes 64a1ff97
+ 006fc4ec bytes 66a1ff97
- 006d27bc ["INT_ADD", "register:40f0:8", ["const:6d27bc:8", "const:4:8"]]
- 006d27bc ["CALL", null, ["ram:6bacc8:8"]]
+ 006fc570 ["INT_ADD", "register:40f0:8", ["const:6fc570:8", "const:4:8"]]
+ 006fc570 ["CALL", null, ["ram:6e4a84:8"]]
- 006d27bc bytes 43a1ff97
+ 006fc570 bytes 45a1ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fab9498d48ff3c83441c64c60e5afdc6"></a>

### [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) → [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) FUN_006fcb34

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006bb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bb5d0.md) [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) [`006d310c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md) · 呼出先 5件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) [`006d310c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md) [`006d345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) · 呼出先 5件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 92.51% / 新版 92.51%

CFGの説明率　旧版 61.76% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 6件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fcb8c",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d2dd8",
      "value": [
        "leaf",
        "ram:6bacc8:8"
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
      "site": "006fcba0",
      "value": [
        "leaf",
        "ram:6e4a84:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d2dec",
      "value": [
        "leaf",
        "ram:6bacc8:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006d2e5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d2dac",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d2db0",
      "DATA",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006fcb8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fcb60",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "006fcb64",
      "DATA",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "006fcb8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d2db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md#insn-006d2db4) · [`006d2dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md#insn-006d2dd8) · [`006d2dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md#insn-006d2dec)
- 新版 `006fcb8c`（命令位置の公開資料なし） · `006fcba0`（命令位置の公開資料なし）

~~~diff
- 006d2db4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006d2db4 ["RETURN", null, ["register:0:8"]]
- 006d2db4 bytes c0035fd6
- 006d2dd8 ["INT_ADD", "register:40f0:8", ["const:6d2dd8:8", "const:4:8"]]
- 006d2dd8 ["CALL", null, ["ram:6bacc8:8"]]
+ 006fcb8c ["INT_ADD", "register:40f0:8", ["const:6fcb8c:8", "const:4:8"]]
+ 006fcb8c ["CALL", null, ["ram:6e4a84:8"]]
- 006d2dd8 bytes bc9fff97
+ 006fcb8c bytes be9fff97
- 006d2dec ["INT_ADD", "register:40f0:8", ["const:6d2dec:8", "const:4:8"]]
- 006d2dec ["CALL", null, ["ram:6bacc8:8"]]
+ 006fcba0 ["INT_ADD", "register:40f0:8", ["const:6fcba0:8", "const:4:8"]]
+ 006fcba0 ["CALL", null, ["ram:6e4a84:8"]]
- 006d2dec bytes b79fff97
+ 006fcba0 bytes b99fff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-526bd483f467e7be99d14988ee594280"></a>

### [`006d310c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md) → [`006fcec0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcec0.md) FUN_006fcec0

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) · 呼出先 3件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) · 呼出先 3件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.92% / 新版 92.92%

CFGの説明率　旧版 80.60% / 新版 84.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d3120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d3120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d3124"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d3120",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d3124",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006fcf10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fced4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "006fced8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "006fcf10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md#insn-006d3120) · [`006d3124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md#insn-006d3124) · [`006d315c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d310c.md#insn-006d315c)
- 新版 `006fcf10`（命令位置の公開資料なし）

~~~diff
- 006d3120 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 006d3120 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 006d3120 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 006d3120 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d3120 bytes f65704a9
- 006d3124 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 006d3124 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 006d3124 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 006d3124 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 006d3124 bytes f44f05a9
- 006d315c ["INT_ADD", "register:40f0:8", ["const:6d315c:8", "const:4:8"]]
- 006d315c ["CALL", null, ["ram:6bacc8:8"]]
+ 006fcf10 ["INT_ADD", "register:40f0:8", ["const:6fcf10:8", "const:4:8"]]
+ 006fcf10 ["CALL", null, ["ram:6e4a84:8"]]
- 006d315c bytes db9eff97
+ 006fcf10 bytes dd9eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9afcb790d3fe0630b1962d1ff50f4068"></a>

### [`006d345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md) → [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) FUN_006fd210

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006d2d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d2/006d2d80.md) [`006d345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md) · 呼出先 4件 [`006bacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006bacc8.md) [`006d345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 2件 [`006fcb34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fc/006fcb34.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) · 呼出先 4件 [`006e4a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4a84.md) [`006fd210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd210.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 93.78% / 新版 93.78%

CFGの説明率　旧版 70.63% / 新版 78.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件, `store_condition` 5件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d38c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d38c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "006fd678"
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
      "unmatched:006d34c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "unmatched:006d34dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ],
    [
      "006fd314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bacc8"
      ]
    ]
  ],
  "added": [
    [
      "006fd27c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fd290",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ],
    [
      "006fd314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e4a84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d34c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md#insn-006d34c8) · [`006d34dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md#insn-006d34dc) · [`006d3514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d345c.md#insn-006d3514)

~~~diff
- 006d34c8 ["INT_ADD", "register:40f0:8", ["const:6d34c8:8", "const:4:8"]]
- 006d34c8 ["CALL", null, ["ram:6bacc8:8"]]
- 006d34c8 bytes 009eff97
- 006d34dc ["INT_ADD", "register:40f0:8", ["const:6d34dc:8", "const:4:8"]]
- 006d34dc ["CALL", null, ["ram:6bacc8:8"]]
- 006d34dc bytes fb9dff97
- 006d3514 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 006d3514 ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 006d3514 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 006d3514 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 006d3514 bytes 48a79a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fa7faac50aa0c00f0f9cda3ec8fbd1b"></a>

### [`006d3b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md) → [`006fd8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd8dc.md) FUN_006fd8dc

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fd8f0",
      "incomplete_value": false,
      "site": "006fd8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3b3c",
      "incomplete_value": false,
      "site": "006d3b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:770:8"
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
      "006fd8f4",
      "DATA",
      [
        "storage",
        "00bf9770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fd8f4",
      "DATA",
      [
        "storage",
        "00c76898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md#insn-006d3b34) · [`006d3b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md#insn-006d3b38) · [`006d3b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b28.md#insn-006d3b3c)
- 新版 `006fd8e8`（命令位置の公開資料なし） · `006fd8ec`（命令位置の公開資料なし） · `006fd8f0`（命令位置の公開資料なし）

~~~diff
- 006d3b34 ["INT_ADD", "register:40f0:8", ["const:6d3b34:8", "const:4:8"]]
- 006d3b34 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fd8e8 ["INT_ADD", "register:40f0:8", ["const:6fd8e8:8", "const:4:8"]]
+ 006fd8e8 ["CALL", null, ["callee:00c57a90:8"]]
- 006d3b34 bytes 431d1494
+ 006fd8e8 bytes 6a681594
- 006d3b38 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fd8ec ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d3b38 bytes 282900d0
+ 006fd8ec bytes c82b00b0
- 006d3b3c ["COPY", "tmp:0:8", ["const:770:8"]]
- 006d3b3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fd8f0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 006fd8f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd8f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd8f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3b3c bytes 08c11d91
+ 006fd8f0 bytes 08612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b127a2240921b7cfda37630147bf598"></a>

### [`006d3b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b64.md) → [`006fd918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd918.md) FUN_006fd918

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "006fd934",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d3b80",
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
      "006fd934",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006fd934",
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

- 旧版 [`006d3b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b64.md#insn-006d3b80) · [`006d3b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3b64.md#insn-006d3b8c)
- 新版 `006fd934`（命令位置の公開資料なし） · `006fd940`（命令位置の公開資料なし）

~~~diff
- 006d3b80 ["INT_ADD", "register:40f0:8", ["const:6d3b80:8", "const:4:8"]]
- 006d3b80 ["CALL", null, ["ram:457e1c:8"]]
+ 006fd934 ["INT_ADD", "register:40f0:8", ["const:6fd934:8", "const:4:8"]]
+ 006fd934 ["CALL", null, ["ram:47acb4:8"]]
- 006d3b80 bytes a710f697
+ 006fd934 bytes e0f4f597
- 006d3b8c ["INT_ADD", "register:40f0:8", ["const:6d3b8c:8", "const:4:8"]]
- 006d3b8c ["CALL", null, ["callee:0047cd94:8"]]
+ 006fd940 ["INT_ADD", "register:40f0:8", ["const:6fd940:8", "const:4:8"]]
+ 006fd940 ["CALL", null, ["callee:0047cd94:8"]]
- 006d3b8c bytes dc18f697
+ 006fd940 bytes 15fdf597
~~~


<a id="compare-433e8ac9d2892276585cd8e55524d194"></a>

### [`006d3bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md) → [`006fd984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd984.md) FUN_006fd984

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fd9a8",
      "incomplete_value": false,
      "site": "006fd9ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3bf4",
      "incomplete_value": false,
      "site": "006d3bf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
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
      "006fd9ac",
      "DATA",
      [
        "storage",
        "00bf97f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fd9ac",
      "DATA",
      [
        "storage",
        "00c76918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md#insn-006d3be4) · [`006d3bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md#insn-006d3bf0) · [`006d3bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3bd0.md#insn-006d3bf4)
- 新版 `006fd998`（命令位置の公開資料なし） · `006fd9a4`（命令位置の公開資料なし） · `006fd9a8`（命令位置の公開資料なし）

~~~diff
- 006d3be4 ["INT_ADD", "register:40f0:8", ["const:6d3be4:8", "const:4:8"]]
- 006d3be4 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fd998 ["INT_ADD", "register:40f0:8", ["const:6fd998:8", "const:4:8"]]
+ 006fd998 ["CALL", null, ["callee:00c57a90:8"]]
- 006d3be4 bytes 171d1494
+ 006fd998 bytes 3e681594
- 006d3bf0 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fd9a4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d3bf0 bytes 282900d0
+ 006fd9a4 bytes c82b00b0
- 006d3bf4 ["COPY", "tmp:0:8", ["const:7f0:8"]]
- 006d3bf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fd9a8 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 006fd9a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd9a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fd9a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d3bf4 bytes 08c11f91
+ 006fd9a8 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35e52ccea6f4e4d06057c75d34d16297"></a>

### [`006d3c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md) → [`006fd9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fd/006fd9ec.md) FUN_006fd9ec

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 87.84% / 新版 87.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 3件, `store_value` 6件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006fdaf0",
      "incomplete_value": true,
      "site": "006fdb04",
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
                "const:e9f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d3c",
      "incomplete_value": true,
      "site": "006d3d50",
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
                "const:7c5:8"
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
      "definition_site": "006fdb44",
      "incomplete_value": true,
      "site": "006fdb44",
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
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:c4b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d90",
      "incomplete_value": true,
      "site": "006d3d90",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:bd3:8"
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
      "definition_site": "006fdb48",
      "incomplete_value": true,
      "site": "006fdb48",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d3d94",
      "incomplete_value": true,
      "site": "006d3d94",
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
                "const:5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fda38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006fda98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c3fe0"
      ]
    ],
    [
      "unmatched:006d3ce8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "006fda38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fda98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006edda4"
      ]
    ],
    [
      "006fda9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d3c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3c84) · [`006d3ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3ce4) · [`006d3ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d3/006d3c38.md#insn-006d3ce8)
- 新版 `006fda38`（命令位置の公開資料なし） · `006fda98`（命令位置の公開資料なし）

~~~diff
- 006d3c84 ["INT_ADD", "register:40f0:8", ["const:6d3c84:8", "const:4:8"]]
- 006d3c84 ["CALL", null, ["ram:457e1c:8"]]
+ 006fda38 ["INT_ADD", "register:40f0:8", ["const:6fda38:8", "const:4:8"]]
+ 006fda38 ["CALL", null, ["ram:47acb4:8"]]
- 006d3c84 bytes 6610f697
+ 006fda38 bytes 9ff4f597
- 006d3ce4 ["INT_ADD", "register:40f0:8", ["const:6d3ce4:8", "const:4:8"]]
- 006d3ce4 ["CALL", null, ["ram:6c3fe0:8"]]
+ 006fda98 ["INT_ADD", "register:40f0:8", ["const:6fda98:8", "const:4:8"]]
+ 006fda98 ["CALL", null, ["ram:6edda4:8"]]
- 006d3ce4 bytes bfc0ff97
+ 006fda98 bytes c3c0ff97
- 006d3ce8 ["INT_ADD", "register:40f0:8", ["const:6d3ce8:8", "const:4:8"]]
- 006d3ce8 ["CALL", null, ["callee:008514b8:8"]]
- 006d3ce8 bytes 262e0594
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-630d333c09ceff16c7f40616af30a22c"></a>

### [`006d4344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md) → [`006fe0f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe0f8.md) FUN_006fe0f8

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fe118",
      "incomplete_value": false,
      "site": "006fe11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4364",
      "incomplete_value": false,
      "site": "006d4368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "006fe11c",
      "DATA",
      [
        "storage",
        "00bf9860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe11c",
      "DATA",
      [
        "storage",
        "00c76988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md#insn-006d4358) · [`006d4360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md#insn-006d4360) · [`006d4364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4344.md#insn-006d4364)
- 新版 `006fe10c`（命令位置の公開資料なし） · `006fe114`（命令位置の公開資料なし） · `006fe118`（命令位置の公開資料なし）

~~~diff
- 006d4358 ["INT_ADD", "register:40f0:8", ["const:6d4358:8", "const:4:8"]]
- 006d4358 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fe10c ["INT_ADD", "register:40f0:8", ["const:6fe10c:8", "const:4:8"]]
+ 006fe10c ["CALL", null, ["callee:00c57a90:8"]]
- 006d4358 bytes 3a1b1494
+ 006fe10c bytes 61661594
- 006d4360 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fe114 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d4360 bytes 282900b0
+ 006fe114 bytes c82b0090
- 006d4364 ["COPY", "tmp:0:8", ["const:860:8"]]
- 006d4364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe118 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 006fe118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4364 bytes 08812191
+ 006fe118 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1543a027bc1eef51c2e17b98fd5fdca"></a>

### [`006d437c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d437c.md) → [`006fe130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe130.md) FUN_006fe130

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fe134",
      "incomplete_value": false,
      "site": "006fe138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4380",
      "incomplete_value": false,
      "site": "006d4384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:860:8"
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
      "006fe138",
      "DATA",
      [
        "storage",
        "00bf9860",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe138",
      "DATA",
      [
        "storage",
        "00c76988",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d437c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d437c.md#insn-006d437c) · [`006d4380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d437c.md#insn-006d4380)
- 新版 `006fe130`（命令位置の公開資料なし） · `006fe134`（命令位置の公開資料なし）

~~~diff
- 006d437c ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fe130 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d437c bytes 282900b0
+ 006fe130 bytes c82b0090
- 006d4380 ["COPY", "tmp:0:8", ["const:860:8"]]
- 006d4380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe134 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 006fe134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4380 bytes 08812191
+ 006fe134 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-333d7ecfa8377fe8d1cea6debb38fb41"></a>

### [`006d439c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d439c.md) → [`006fe150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe150.md) FUN_006fe150

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) [`006c66fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c66fc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_target, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 91.11% / 新版 91.11%

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
      "site": "006fe17c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d43c8",
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
      "site": "006fe1d0",
      "value": [
        "leaf",
        "ram:6f04c0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d441c",
      "value": [
        "leaf",
        "ram:6c66fc:8"
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
      "006fe17c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006fe1d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c66fc"
      ]
    ],
    [
      "006fe1e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006c0784"
      ]
    ]
  ],
  "added": [
    [
      "006fe17c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe1d0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f04c0"
      ]
    ],
    [
      "006fe1e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006ea548"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d43c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d439c.md#insn-006d43c8) · [`006d441c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d439c.md#insn-006d441c) · [`006d43d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d439c.md#insn-006d43d4)
- 新版 `006fe17c`（命令位置の公開資料なし） · `006fe1d0`（命令位置の公開資料なし） · `006fe188`（命令位置の公開資料なし）

~~~diff
- 006d43c8 ["INT_ADD", "register:40f0:8", ["const:6d43c8:8", "const:4:8"]]
- 006d43c8 ["CALL", null, ["ram:457e1c:8"]]
+ 006fe17c ["INT_ADD", "register:40f0:8", ["const:6fe17c:8", "const:4:8"]]
+ 006fe17c ["CALL", null, ["ram:47acb4:8"]]
- 006d43c8 bytes 950ef697
+ 006fe17c bytes cef2f597
- 006d441c ["INT_ADD", "register:40f0:8", ["const:6d441c:8", "const:4:8"]]
- 006d441c ["CALL", null, ["ram:6c66fc:8"]]
+ 006fe1d0 ["INT_ADD", "register:40f0:8", ["const:6fe1d0:8", "const:4:8"]]
+ 006fe1d0 ["CALL", null, ["ram:6f04c0:8"]]
- 006d441c bytes b8c8ff97
+ 006fe1d0 bytes bcc8ff97
- 006d43d4 ["INT_ADD", "register:40f0:8", ["const:6d43d4:8", "const:4:8"]]
- 006d43d4 ["CALL", null, ["callee:0047cd94:8"]]
+ 006fe188 ["INT_ADD", "register:40f0:8", ["const:6fe188:8", "const:4:8"]]
+ 006fe188 ["CALL", null, ["callee:0047cd94:8"]]
- 006d43d4 bytes ca16f697
+ 006fe188 bytes 03fbf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a18706aa98b609552399bde3a4b063f0"></a>

### [`006d447c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md) → [`006fe230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe230.md) FUN_006fe230

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fe250",
      "incomplete_value": false,
      "site": "006fe254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d449c",
      "incomplete_value": false,
      "site": "006d44a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "006fe254",
      "DATA",
      [
        "storage",
        "00bf98f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe254",
      "DATA",
      [
        "storage",
        "00c76a18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md#insn-006d4490) · [`006d4498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md#insn-006d4498) · [`006d449c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d447c.md#insn-006d449c)
- 新版 `006fe244`（命令位置の公開資料なし） · `006fe24c`（命令位置の公開資料なし） · `006fe250`（命令位置の公開資料なし）

~~~diff
- 006d4490 ["INT_ADD", "register:40f0:8", ["const:6d4490:8", "const:4:8"]]
- 006d4490 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fe244 ["INT_ADD", "register:40f0:8", ["const:6fe244:8", "const:4:8"]]
+ 006fe244 ["CALL", null, ["callee:00c57a90:8"]]
- 006d4490 bytes ec1a1494
+ 006fe244 bytes 13661594
- 006d4498 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fe24c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d4498 bytes 282900b0
+ 006fe24c bytes c82b0090
- 006d449c ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 006d449c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d449c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe250 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 006fe250 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe250 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe250 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d449c bytes 08c12391
+ 006fe250 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e859c6db108cf24601f88fb49acbe45"></a>

### [`006d46f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46f8.md) → [`006fe4ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe4ac.md) FUN_006fe4ac

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`006c0784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c0784.md) [`006c66fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c6/006c66fc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`006ea548`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea548.md) [`006f04c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f0/006f04c0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 75.68% / 新版 75.68%

CFGの説明率　旧版 41.67% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fe4d4",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4720",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4764"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "006fe518"
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
      "006fe4d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006fe4f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006d4780"
      ]
    ],
    [
      "006fe4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:006d4780"
      ]
    ]
  ],
  "added": [
    [
      "006fe4d4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe4f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fe534"
      ]
    ],
    [
      "006fe4fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fe534"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46f8.md#insn-006d4720) · [`006d4764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46f8.md#insn-006d4764) · [`006d4788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d46f8.md#insn-006d4788)
- 新版 `006fe4d4`（命令位置の公開資料なし）

~~~diff
- 006d4720 ["INT_ADD", "register:40f0:8", ["const:6d4720:8", "const:4:8"]]
- 006d4720 ["CALL", null, ["ram:457e1c:8"]]
+ 006fe4d4 ["INT_ADD", "register:40f0:8", ["const:6fe4d4:8", "const:4:8"]]
+ 006fe4d4 ["CALL", null, ["ram:47acb4:8"]]
- 006d4720 bytes bf0df697
+ 006fe4d4 bytes f8f1f597
- 006d4764 ["INT_ADD", "register:40f0:8", ["const:6d4764:8", "const:4:8"]]
- 006d4764 ["CALL", null, ["ram:6c66fc:8"]]
- 006d4764 bytes e6c7ff97
- 006d4788 ["COPY", "register:0:8", ["register:40f0:8"]]
- 006d4788 ["RETURN", null, ["register:0:8"]]
- 006d4788 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21906d8e3627e41c60da47ce59063a40"></a>

### [`006d47b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md) → [`006fe56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe56c.md) FUN_006fe56c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fe58c",
      "incomplete_value": false,
      "site": "006fe590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d47d8",
      "incomplete_value": false,
      "site": "006d47dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:9f0:8"
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
      "006fe590",
      "DATA",
      [
        "storage",
        "00bf99f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe590",
      "DATA",
      [
        "storage",
        "00c76b18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d47cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md#insn-006d47cc) · [`006d47d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md#insn-006d47d4) · [`006d47d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d47b8.md#insn-006d47d8)
- 新版 `006fe580`（命令位置の公開資料なし） · `006fe588`（命令位置の公開資料なし） · `006fe58c`（命令位置の公開資料なし）

~~~diff
- 006d47cc ["INT_ADD", "register:40f0:8", ["const:6d47cc:8", "const:4:8"]]
- 006d47cc ["CALL", null, ["callee:00c57a90:8"]]
+ 006fe580 ["INT_ADD", "register:40f0:8", ["const:6fe580:8", "const:4:8"]]
+ 006fe580 ["CALL", null, ["callee:00c57a90:8"]]
- 006d47cc bytes 1d1a1494
+ 006fe580 bytes 44651594
- 006d47d4 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fe588 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d47d4 bytes 282900b0
+ 006fe588 bytes c82b0090
- 006d47d8 ["COPY", "tmp:0:8", ["const:9f0:8"]]
- 006d47d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe58c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 006fe58c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe58c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe58c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d47d8 bytes 08c12791
+ 006fe58c bytes 08612c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d747b1a31cfed99db7a17653620d62e4"></a>

### [`006d4810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md) → [`006fe5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe5c4.md) FUN_006fe5c4

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006bb5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bb/006bb5d0.md) [`006c5940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c5/006c5940.md)
- 新版 呼出元 0件  · 呼出先 11件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`006e5394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e5/006e5394.md) [`006ef704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ef/006ef704.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.20% / 新版 81.20%

CFGの説明率　旧版 88.89% / 新版 84.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4924"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4928"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006fe600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006fe620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "006fe65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006bb5d0"
      ]
    ]
  ],
  "added": [
    [
      "006fe600",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006e5394"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d484c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md#insn-006d484c) · [`006d486c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md#insn-006d486c) · [`006d48a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4810.md#insn-006d48a8)
- 新版 `006fe600`（命令位置の公開資料なし） · `006fe620`（命令位置の公開資料なし） · `006fe65c`（命令位置の公開資料なし）

~~~diff
- 006d484c ["INT_ADD", "register:40f0:8", ["const:6d484c:8", "const:4:8"]]
- 006d484c ["CALL", null, ["ram:457e1c:8"]]
+ 006fe600 ["INT_ADD", "register:40f0:8", ["const:6fe600:8", "const:4:8"]]
+ 006fe600 ["CALL", null, ["ram:47acb4:8"]]
- 006d484c bytes 740df697
+ 006fe600 bytes adf1f597
- 006d486c ["INT_ADD", "register:40f0:8", ["const:6d486c:8", "const:4:8"]]
- 006d486c ["CALL", null, ["ram:457e1c:8"]]
+ 006fe620 ["INT_ADD", "register:40f0:8", ["const:6fe620:8", "const:4:8"]]
+ 006fe620 ["CALL", null, ["ram:47acb4:8"]]
- 006d486c bytes 6c0df697
+ 006fe620 bytes a5f1f597
- 006d48a8 ["INT_ADD", "register:40f0:8", ["const:6d48a8:8", "const:4:8"]]
- 006d48a8 ["CALL", null, ["ram:6bb5d0:8"]]
+ 006fe65c ["INT_ADD", "register:40f0:8", ["const:6fe65c:8", "const:4:8"]]
+ 006fe65c ["CALL", null, ["ram:6e5394:8"]]
- 006d48a8 bytes 4a9bff97
+ 006fe65c bytes 4e9bff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeeaa55e006362da6f1216a1d651ee79"></a>

### [`006d4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ac4.md) → [`006fe878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe878.md) FUN_006fe878

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fe87c",
      "incomplete_value": false,
      "site": "006fe880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4ac8",
      "incomplete_value": false,
      "site": "006d4acc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "006fe880",
      "DATA",
      [
        "storage",
        "00bf9a60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fe880",
      "DATA",
      [
        "storage",
        "00c76b88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ac4.md#insn-006d4ac4) · [`006d4ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ac4.md#insn-006d4ac8)
- 新版 `006fe878`（命令位置の公開資料なし） · `006fe87c`（命令位置の公開資料なし）

~~~diff
- 006d4ac4 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fe878 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d4ac4 bytes 282900b0
+ 006fe878 bytes c82b0090
- 006d4ac8 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 006d4ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fe87c ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 006fe87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fe87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4ac8 bytes 08812991
+ 006fe87c bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65c91229346933a211eb76e7914b2e34"></a>

### [`006d4adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4adc.md) → [`006fe890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe890.md) FUN_006fe890

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "006fe8ac",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4af8",
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
      "006fe8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006fe8ac",
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

- 旧版 [`006d4af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4adc.md#insn-006d4af8) · [`006d4b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4adc.md#insn-006d4b04)
- 新版 `006fe8ac`（命令位置の公開資料なし） · `006fe8b8`（命令位置の公開資料なし）

~~~diff
- 006d4af8 ["INT_ADD", "register:40f0:8", ["const:6d4af8:8", "const:4:8"]]
- 006d4af8 ["CALL", null, ["ram:457e1c:8"]]
+ 006fe8ac ["INT_ADD", "register:40f0:8", ["const:6fe8ac:8", "const:4:8"]]
+ 006fe8ac ["CALL", null, ["ram:47acb4:8"]]
- 006d4af8 bytes c90cf697
+ 006fe8ac bytes 02f1f597
- 006d4b04 ["INT_ADD", "register:40f0:8", ["const:6d4b04:8", "const:4:8"]]
- 006d4b04 ["CALL", null, ["callee:0047cd94:8"]]
+ 006fe8b8 ["INT_ADD", "register:40f0:8", ["const:6fe8b8:8", "const:4:8"]]
+ 006fe8b8 ["CALL", null, ["callee:0047cd94:8"]]
- 006d4b04 bytes fe14f697
+ 006fe8b8 bytes 37f9f597
~~~


<a id="compare-8b307020bb7c743e5b32d0c12f1460ac"></a>

### [`006d4ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ba0.md) → [`006fe954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fe954.md) FUN_006fe954

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0052dcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0052d/0052dcc0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 64.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "006d4ca4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:006d4bdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006d4be4",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:006d4bec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fec58"
      ]
    ]
  ],
  "added": [
    [
      "006fe990",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006fe998",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "006fe9a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "006fec58"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ba0.md#insn-006d4bdc) · [`006d4bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ba0.md#insn-006d4bec) · [`006d4bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4ba0.md#insn-006d4bf8)
- 新版 `006fe9ac`（命令位置の公開資料なし）

~~~diff
- 006d4bdc ["INT_ADD", "register:40f0:8", ["const:6d4bdc:8", "const:4:8"]]
- 006d4bdc ["CALL", null, ["ram:457e1c:8"]]
- 006d4bdc bytes 900cf697
- 006d4bec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 006d4bec ["CBRANCH", null, ["local:b34:8", "tmp:0:1"]]
- 006d4bec bytes c1150054
- 006d4bf8 ["INT_ADD", "register:40f0:8", ["const:6d4bf8:8", "const:4:8"]]
- 006d4bf8 ["CALL", null, ["ram:457e1c:8"]]
+ 006fe9ac ["INT_ADD", "register:40f0:8", ["const:6fe9ac:8", "const:4:8"]]
+ 006fe9ac ["CALL", null, ["ram:47acb4:8"]]
- 006d4bf8 bytes 890cf697
+ 006fe9ac bytes c2f0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf09e4059ba6b45ea6933cf033c52002"></a>

### [`006d4f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4f68.md) → [`006fed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed1c.md) FUN_006fed1c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "006fed38",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d4f84",
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
      "006fed38",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006fed38",
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

- 旧版 [`006d4f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4f68.md#insn-006d4f84) · [`006d4f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4f68.md#insn-006d4f90)
- 新版 `006fed38`（命令位置の公開資料なし） · `006fed44`（命令位置の公開資料なし）

~~~diff
- 006d4f84 ["INT_ADD", "register:40f0:8", ["const:6d4f84:8", "const:4:8"]]
- 006d4f84 ["CALL", null, ["ram:457e1c:8"]]
+ 006fed38 ["INT_ADD", "register:40f0:8", ["const:6fed38:8", "const:4:8"]]
+ 006fed38 ["CALL", null, ["ram:47acb4:8"]]
- 006d4f84 bytes a60bf697
+ 006fed38 bytes dfeff597
- 006d4f90 ["INT_ADD", "register:40f0:8", ["const:6d4f90:8", "const:4:8"]]
- 006d4f90 ["CALL", null, ["callee:0047cd94:8"]]
+ 006fed44 ["INT_ADD", "register:40f0:8", ["const:6fed44:8", "const:4:8"]]
+ 006fed44 ["CALL", null, ["callee:0047cd94:8"]]
- 006d4f90 bytes db13f697
+ 006fed44 bytes 14f8f597
~~~


<a id="compare-8c37c0e830a4314e60acc429276d6085"></a>

### [`006d4fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md) → [`006fed88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fed88.md) FUN_006fed88

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fed9c",
      "incomplete_value": false,
      "site": "006feda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d4fe8",
      "incomplete_value": false,
      "site": "006d4fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "006feda0",
      "DATA",
      [
        "storage",
        "00bf9bf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006feda0",
      "DATA",
      [
        "storage",
        "00c76d18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d4fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md#insn-006d4fe0) · [`006d4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md#insn-006d4fe4) · [`006d4fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d4/006d4fd4.md#insn-006d4fe8)
- 新版 `006fed94`（命令位置の公開資料なし） · `006fed98`（命令位置の公開資料なし） · `006fed9c`（命令位置の公開資料なし）

~~~diff
- 006d4fe0 ["INT_ADD", "register:40f0:8", ["const:6d4fe0:8", "const:4:8"]]
- 006d4fe0 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fed94 ["INT_ADD", "register:40f0:8", ["const:6fed94:8", "const:4:8"]]
+ 006fed94 ["CALL", null, ["callee:00c57a90:8"]]
- 006d4fe0 bytes 18181494
+ 006fed94 bytes 3f631594
- 006d4fe4 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fed98 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d4fe4 bytes 282900b0
+ 006fed98 bytes c82b0090
- 006d4fe8 ["COPY", "tmp:0:8", ["const:bf0:8"]]
- 006d4fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fed9c ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 006fed9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fed9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d4fe8 bytes 08c12f91
+ 006fed9c bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-788eb4b0bfb5c59d837be10e79dd82e3"></a>

### [`006d51a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md) → [`006fef58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fef58.md) FUN_006fef58

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006fef7c",
      "incomplete_value": false,
      "site": "006fef7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:e18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d51c8",
      "incomplete_value": false,
      "site": "006d51c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
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
      "006fef7c",
      "DATA",
      [
        "storage",
        "00bf9cf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006fef7c",
      "DATA",
      [
        "storage",
        "00c76e18",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d51b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md#insn-006d51b8) · [`006d51c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md#insn-006d51c0) · [`006d51c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51a4.md#insn-006d51c4)
- 新版 `006fef6c`（命令位置の公開資料なし） · `006fef74`（命令位置の公開資料なし） · `006fef78`（命令位置の公開資料なし）

~~~diff
- 006d51b8 ["INT_ADD", "register:40f0:8", ["const:6d51b8:8", "const:4:8"]]
- 006d51b8 ["CALL", null, ["callee:00c57a90:8"]]
+ 006fef6c ["INT_ADD", "register:40f0:8", ["const:6fef6c:8", "const:4:8"]]
+ 006fef6c ["CALL", null, ["callee:00c57a90:8"]]
- 006d51b8 bytes a2171494
+ 006fef6c bytes c9621594
- 006d51c0 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006fef74 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d51c0 bytes 28290090
+ 006fef74 bytes c82b0090
- 006d51c4 ["COPY", "tmp:0:8", ["const:cf0:8"]]
- 006d51c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006fef78 ["COPY", "tmp:0:8", ["const:e18:8"]]
+ 006fef78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006fef78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006fef78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d51c4 bytes 08c13391
+ 006fef78 bytes 08613891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06199d37963ab664e2d6ed7002ee98a1"></a>

### [`006d51f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51f4.md) → [`006fefa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fe/006fefa8.md) FUN_006fefa8

採用 · 移動量 `+0x29db4` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 57.14% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006fefd8",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5224",
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006d524c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "006d5250",
      "incomplete_value": false,
      "site": "006d5258",
      "value": [
        "leaf",
        "const:b:8"
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
      "006fefd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "unmatched:006d524c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006fefd8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "006ff000",
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

- 旧版 [`006d5224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51f4.md#insn-006d5224) · [`006d524c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51f4.md#insn-006d524c) · [`006d5258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d51f4.md#insn-006d5258)
- 新版 `006fefd8`（命令位置の公開資料なし） · `006ff00c`（命令位置の公開資料なし）

~~~diff
- 006d5224 ["INT_ADD", "register:40f0:8", ["const:6d5224:8", "const:4:8"]]
- 006d5224 ["CALL", null, ["ram:457e1c:8"]]
+ 006fefd8 ["INT_ADD", "register:40f0:8", ["const:6fefd8:8", "const:4:8"]]
+ 006fefd8 ["CALL", null, ["ram:47acb4:8"]]
- 006d5224 bytes fe0af697
+ 006fefd8 bytes 37eff597
- 006d524c ["INT_ADD", "register:40f0:8", ["const:6d524c:8", "const:4:8"]]
- 006d524c ["CALL", null, ["ram:457e1c:8"]]
- 006d524c bytes f40af697
- 006d5258 ["INT_ADD", "register:40f0:8", ["const:6d5258:8", "const:4:8"]]
- 006d5258 ["CALL", null, ["callee:0047cd94:8"]]
+ 006ff00c ["INT_ADD", "register:40f0:8", ["const:6ff00c:8", "const:4:8"]]
+ 006ff00c ["CALL", null, ["callee:0047cd94:8"]]
- 006d5258 bytes 2913f697
+ 006ff00c bytes 62f7f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2895c4df5a29caac8fa4ec0ea49cbc55"></a>

### [`006d5298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md) → [`006ff04c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff04c.md) FUN_006ff04c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ff060",
      "incomplete_value": false,
      "site": "006ff064",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d52ac",
      "incomplete_value": false,
      "site": "006d52b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "006ff064",
      "DATA",
      [
        "storage",
        "00bf9d70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff064",
      "DATA",
      [
        "storage",
        "00c76e98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d52a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md#insn-006d52a4) · [`006d52a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md#insn-006d52a8) · [`006d52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5298.md#insn-006d52ac)
- 新版 `006ff058`（命令位置の公開資料なし） · `006ff05c`（命令位置の公開資料なし） · `006ff060`（命令位置の公開資料なし）

~~~diff
- 006d52a4 ["INT_ADD", "register:40f0:8", ["const:6d52a4:8", "const:4:8"]]
- 006d52a4 ["CALL", null, ["callee:00c57a90:8"]]
+ 006ff058 ["INT_ADD", "register:40f0:8", ["const:6ff058:8", "const:4:8"]]
+ 006ff058 ["CALL", null, ["callee:00c57a90:8"]]
- 006d52a4 bytes 67171494
+ 006ff058 bytes 8e621594
- 006d52a8 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006ff05c ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d52a8 bytes 28290090
+ 006ff05c bytes a82b00f0
- 006d52ac ["COPY", "tmp:0:8", ["const:d70:8"]]
- 006d52ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d52ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d52ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff060 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 006ff060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d52ac bytes 08c13591
+ 006ff060 bytes 08613a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8202d2d3791108af0f1e17c4b251374d"></a>

### [`006d5408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5408.md) → [`006ff1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff1bc.md) FUN_006ff1bc

採用 · 移動量 `+0x29db4` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff1f8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5444",
      "value": [
        "leaf",
        "ram:449aec:8"
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "006d5470"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006ff228",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d5474",
      "value": [
        "leaf",
        "ram:449aec:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006ff1f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "unmatched:006d5470",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "006ff228",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ]
  ],
  "added": [
    [
      "006ff1f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "006ff224",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "006ff228",
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

- 旧版 [`006d5444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5408.md#insn-006d5444) · [`006d5470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5408.md#insn-006d5470) · [`006d5474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5408.md#insn-006d5474)
- 新版 `006ff1f8`（命令位置の公開資料なし） · `006ff228`（命令位置の公開資料なし）

~~~diff
- 006d5444 ["INT_ADD", "register:40f0:8", ["const:6d5444:8", "const:4:8"]]
- 006d5444 ["CALL", null, ["ram:449aec:8"]]
+ 006ff1f8 ["INT_ADD", "register:40f0:8", ["const:6ff1f8:8", "const:4:8"]]
+ 006ff1f8 ["CALL", null, ["ram:46c984:8"]]
- 006d5444 bytes aad1f597
+ 006ff1f8 bytes e3b5f597
- 006d5470 ["INT_ADD", "register:40f0:8", ["const:6d5470:8", "const:4:8"]]
- 006d5470 ["CALL", null, ["callee:008514b8:8"]]
- 006d5470 bytes 44280594
- 006d5474 ["INT_ADD", "register:40f0:8", ["const:6d5474:8", "const:4:8"]]
- 006d5474 ["CALL", null, ["ram:449aec:8"]]
+ 006ff228 ["INT_ADD", "register:40f0:8", ["const:6ff228:8", "const:4:8"]]
+ 006ff228 ["CALL", null, ["ram:46c984:8"]]
- 006d5474 bytes 9ed1f597
+ 006ff228 bytes d7b5f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f4e88001034b87b7c3febe5c87f464"></a>

### [`006d54d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d54d4.md) → [`006ff288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff288.md) FUN_006ff288

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ff2ac",
      "incomplete_value": false,
      "site": "006ff2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c76000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d54f8",
      "incomplete_value": false,
      "site": "006d54f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      "006ff2ac",
      "DATA",
      [
        "storage",
        "00bf9e70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff2ac",
      "DATA",
      [
        "storage",
        "00c76f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d54e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d54d4.md#insn-006d54e8) · [`006d54f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d54d4.md#insn-006d54f0) · [`006d54f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d54d4.md#insn-006d54f4)
- 新版 `006ff29c`（命令位置の公開資料なし） · `006ff2a4`（命令位置の公開資料なし） · `006ff2a8`（命令位置の公開資料なし）

~~~diff
- 006d54e8 ["INT_ADD", "register:40f0:8", ["const:6d54e8:8", "const:4:8"]]
- 006d54e8 ["CALL", null, ["callee:00c57a90:8"]]
+ 006ff29c ["INT_ADD", "register:40f0:8", ["const:6ff29c:8", "const:4:8"]]
+ 006ff29c ["CALL", null, ["callee:00c57a90:8"]]
- 006d54e8 bytes d6161494
+ 006ff29c bytes fd611594
- 006d54f0 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006ff2a4 ["COPY", "register:4040:8", ["const:c76000:8"]]
- 006d54f0 bytes 28290090
+ 006ff2a4 bytes a82b00f0
- 006d54f4 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 006d54f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff2a8 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 006ff2a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff2a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff2a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d54f4 bytes 08c13991
+ 006ff2a8 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82200167101b518dcb228b00550ca8a6"></a>

### [`006d5810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5810.md) → [`006ff5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff5c4.md) FUN_006ff5c4

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ff5d8",
      "incomplete_value": false,
      "site": "006ff5dc",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d5824",
      "incomplete_value": false,
      "site": "006d5828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
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
      "006ff5dc",
      "DATA",
      [
        "storage",
        "00bf9ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ff5dc",
      "DATA",
      [
        "storage",
        "00c77008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5810.md#insn-006d581c) · [`006d5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5810.md#insn-006d5820) · [`006d5824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d5810.md#insn-006d5824)
- 新版 `006ff5d0`（命令位置の公開資料なし） · `006ff5d4`（命令位置の公開資料なし） · `006ff5d8`（命令位置の公開資料なし）

~~~diff
- 006d581c ["INT_ADD", "register:40f0:8", ["const:6d581c:8", "const:4:8"]]
- 006d581c ["CALL", null, ["callee:00c57a90:8"]]
+ 006ff5d0 ["INT_ADD", "register:40f0:8", ["const:6ff5d0:8", "const:4:8"]]
+ 006ff5d0 ["CALL", null, ["callee:00c57a90:8"]]
- 006d581c bytes 09161494
+ 006ff5d0 bytes 30611594
- 006d5820 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006ff5d4 ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d5820 bytes 28290090
+ 006ff5d4 bytes c82b0090
- 006d5824 ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 006d5824 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d5824 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d5824 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d8 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 006ff5d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ff5d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d5824 bytes 08813b91
+ 006ff5d8 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e62a8a7f02ab3e3be6b758fbc30c6efa"></a>

### [`006d6008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6008.md) → [`006ffdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffdbc.md) FUN_006ffdbc

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ffdd0",
      "incomplete_value": false,
      "site": "006ffdd4",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d601c",
      "incomplete_value": false,
      "site": "006d6020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      "006ffdd4",
      "DATA",
      [
        "storage",
        "00bf9f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffdd4",
      "DATA",
      [
        "storage",
        "00c77078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d6014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6008.md#insn-006d6014) · [`006d6018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6008.md#insn-006d6018) · [`006d601c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6008.md#insn-006d601c)
- 新版 `006ffdc8`（命令位置の公開資料なし） · `006ffdcc`（命令位置の公開資料なし） · `006ffdd0`（命令位置の公開資料なし）

~~~diff
- 006d6014 ["INT_ADD", "register:40f0:8", ["const:6d6014:8", "const:4:8"]]
- 006d6014 ["CALL", null, ["callee:00c57a90:8"]]
+ 006ffdc8 ["INT_ADD", "register:40f0:8", ["const:6ffdc8:8", "const:4:8"]]
+ 006ffdc8 ["CALL", null, ["callee:00c57a90:8"]]
- 006d6014 bytes 0b141494
+ 006ffdc8 bytes 325f1594
- 006d6018 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006ffdcc ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d6018 bytes 082900f0
+ 006ffdcc bytes c82b0090
- 006d601c ["COPY", "tmp:0:8", ["const:f50:8"]]
- 006d601c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d601c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d601c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffdd0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006ffdd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffdd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffdd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d601c bytes 08413d91
+ 006ffdd0 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94b32874cd30b72d2a198a7e32bfd8fb"></a>

### [`006d60b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60b8.md) → [`006ffe6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffe6c.md) FUN_006ffe6c

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006ffe80",
      "incomplete_value": false,
      "site": "006ffe84",
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
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006d60cc",
      "incomplete_value": false,
      "site": "006d60d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf9000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      "006ffe84",
      "DATA",
      [
        "storage",
        "00bf9fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006ffe84",
      "DATA",
      [
        "storage",
        "00c770f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006d60c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60b8.md#insn-006d60c4) · [`006d60c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60b8.md#insn-006d60c8) · [`006d60cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60b8.md#insn-006d60cc)
- 新版 `006ffe78`（命令位置の公開資料なし） · `006ffe7c`（命令位置の公開資料なし） · `006ffe80`（命令位置の公開資料なし）

~~~diff
- 006d60c4 ["INT_ADD", "register:40f0:8", ["const:6d60c4:8", "const:4:8"]]
- 006d60c4 ["CALL", null, ["callee:00c57a90:8"]]
+ 006ffe78 ["INT_ADD", "register:40f0:8", ["const:6ffe78:8", "const:4:8"]]
+ 006ffe78 ["CALL", null, ["callee:00c57a90:8"]]
- 006d60c4 bytes df131494
+ 006ffe78 bytes 065f1594
- 006d60c8 ["COPY", "register:4040:8", ["const:bf9000:8"]]
+ 006ffe7c ["COPY", "register:4040:8", ["const:c77000:8"]]
- 006d60c8 bytes 082900f0
+ 006ffe7c bytes c82b0090
- 006d60cc ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 006d60cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006d60cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006d60cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006ffe80 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 006ffe80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffe80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006ffe80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006d60cc bytes 08413f91
+ 006ffe80 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a031f5d8f485c34c83aefddad3511d5c"></a>

### [`006d60f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60f4.md) → [`006ffea8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ffea8.md) FUN_006ffea8

採用 · 移動量 `+0x29db4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "006ffecc",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "006d6118",
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
      "006ffecc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "006ffecc",
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

- 旧版 [`006d6118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60f4.md#insn-006d6118) · [`006d6124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d60f4.md#insn-006d6124)
- 新版 `006ffecc`（命令位置の公開資料なし） · `006ffed8`（命令位置の公開資料なし）

~~~diff
- 006d6118 ["INT_ADD", "register:40f0:8", ["const:6d6118:8", "const:4:8"]]
- 006d6118 ["CALL", null, ["ram:457e1c:8"]]
+ 006ffecc ["INT_ADD", "register:40f0:8", ["const:6ffecc:8", "const:4:8"]]
+ 006ffecc ["CALL", null, ["ram:47acb4:8"]]
- 006d6118 bytes 4107f697
+ 006ffecc bytes 7aebf597
- 006d6124 ["INT_ADD", "register:40f0:8", ["const:6d6124:8", "const:4:8"]]
- 006d6124 ["CALL", null, ["callee:0047cd94:8"]]
+ 006ffed8 ["INT_ADD", "register:40f0:8", ["const:6ffed8:8", "const:4:8"]]
+ 006ffed8 ["CALL", null, ["callee:0047cd94:8"]]
- 006d6124 bytes 760ff697
+ 006ffed8 bytes aff3f597
~~~


