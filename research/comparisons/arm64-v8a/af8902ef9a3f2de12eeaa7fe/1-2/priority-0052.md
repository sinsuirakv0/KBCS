# v15.7.4 → v16.0.0 · 最優先の変更候補 (52)

[一覧の目次](README.md)

<a id="compare-7222884ee1ba84334d9e7979ab68c6c4"></a>

### [`00a44bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md) → [`00aa2af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2af4.md) FUN_00aa2af4

採用 · 移動量 `+0x5df04` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.29% / 新版 94.29%

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
      "site": "00aa2b64",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a44c60",
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
      "definition_site": "00aa2b60",
      "incomplete_value": false,
      "site": "00aa2b64",
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
      "definition_site": "00a44c5c",
      "incomplete_value": false,
      "site": "00a44c60",
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
      "00aa2b60",
      "PARAM",
      [
        "storage",
        "00290bae",
        null,
        "string"
      ]
    ],
    [
      "00aa2b64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00aa2b60",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ],
    [
      "00aa2b64",
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

- 旧版 [`00a44c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md#insn-00a44c60) · [`00a44c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md#insn-00a44c58) · [`00a44c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44bf0.md#insn-00a44c5c)
- 新版 [`00aa2b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2af4.md#insn-00aa2b64) · [`00aa2b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2af4.md#insn-00aa2b5c) · [`00aa2b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2af4.md#insn-00aa2b60)

~~~diff
- 00a44c60 ["INT_ADD", "register:40f0:8", ["const:a44c60:8", "const:4:8"]]
- 00a44c60 ["CALL", null, ["ram:41fdf0:8"]]
+ 00aa2b64 ["INT_ADD", "register:40f0:8", ["const:aa2b64:8", "const:4:8"]]
+ 00aa2b64 ["CALL", null, ["ram:4428f0:8"]]
- 00a44c60 bytes 646ce797
+ 00aa2b64 bytes 637fe697
- 00a44c58 ["COPY", "register:4000:8", ["const:290000:8"]]
+ 00aa2b5c ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00a44c58 bytes 60c2ff90
+ 00aa2b5c bytes e0bfffd0
- 00a44c5c ["COPY", "tmp:0:8", ["const:bae:8"]]
- 00a44c5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a44c5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a44c5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aa2b60 ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00aa2b60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aa2b60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aa2b60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a44c5c bytes 00b82e91
+ 00aa2b60 bytes 00c00391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95e4cdda8a54129821c04de11551ea3"></a>

### [`00a44cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md) → [`00aa2bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2bfc.md) FUN_00aa2bfc

採用 · 移動量 `+0x5df04` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0078cd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078c/0078cd14.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`007acf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007acf88.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007bda04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bd/007bda04.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) [`007df0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007df/007df0a8.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 45.00% / 新版 47.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa2c18"
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
      "00aa2c10",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a44d18"
      ]
    ],
    [
      "unmatched:00a44d14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2c60"
      ]
    ],
    [
      "unmatched:00a44d20",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2c14"
      ]
    ]
  ],
  "added": [
    [
      "00aa2c10",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2c1c"
      ]
    ],
    [
      "00aa2c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2c60"
      ]
    ],
    [
      "00aa2c24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2c14"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a44d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md#insn-00a44d14) · [`00a44d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md#insn-00a44d20) · [`00a44d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md#insn-00a44d58)

~~~diff
- 00a44d14 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00a44d14 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a44d14 bytes 490200b4
- 00a44d20 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a44d20 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a44d20 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a44d20 ["CBRANCH", null, ["local:b2:8", "tmp:2:1"]]
- 00a44d20 bytes 8cffff54
- 00a44d58 ["INT_ADD", "register:40f0:8", ["const:a44d58:8", "const:4:8"]]
- 00a44d58 ["CALL", null, ["ram:41fdf0:8"]]
- 00a44d58 bytes 266ce797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-251b1ac9db2a7070e00d165b252d5756"></a>

### [`00a44d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44d74.md) → [`00aa2c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2c78.md) FUN_00aa2c78

採用 · 移動量 `+0x5df04` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00471738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00471/00471738.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`007cceac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007cc/007cceac.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004945d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00494/004945d0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 57.63% / 新版 59.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aa2dc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44e60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a44e60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2d4c"
      ]
    ],
    [
      "unmatched:00a44ea4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2db4"
      ]
    ],
    [
      "unmatched:00a44f18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2dcc"
      ]
    ]
  ],
  "added": [
    [
      "00aa2d64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2d4c"
      ]
    ],
    [
      "00aa2da8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2db4"
      ]
    ],
    [
      "00aa2e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa2dcc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a44e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44d74.md#insn-00a44e60) · [`00a44ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44d74.md#insn-00a44ea4) · [`00a44ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44d74.md#insn-00a44ec0)

~~~diff
- 00a44e60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a44e60 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a44e60 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a44e60 ["CBRANCH", null, ["local:b13:8", "tmp:2:1"]]
- 00a44e60 bytes 4cffff54
- 00a44ea4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a44ea4 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00a44ea4 bytes 680000b4
- 00a44ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:28:8"]]
- 00a44ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a44ec0 bytes 681600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff042b90f2224572e93ed7b8dc283bd4"></a>

### [`00a44f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44f88.md) → [`00aa2e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa2/00aa2e8c.md) _INIT_235

採用 · 移動量 `+0x5df04` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.62% / 新版 83.62%

CFGの説明率　旧版 51.22% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44fb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a44fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a45004"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a44fb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a44fc4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a44fe0",
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
      "00aa2ebc",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00aa2ec8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00aa2ee4",
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

- 旧版 [`00a44fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44f88.md#insn-00a44fb8) · [`00a44fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44f88.md#insn-00a44fe0) · [`00a45004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44f88.md#insn-00a45004)

~~~diff
- 00a44fb8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a44fb8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a44fb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a44fb8 bytes a9831ff8
- 00a44fe0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a44fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a44fe0 bytes e013813c
- 00a45004 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a45004 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a45004 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a7f76c0b28e06785fe4e9f287c4da01"></a>

### [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) → [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) FUN_00aa3c28

採用 · 移動量 `+0x5e004` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 40件 [`005a3eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a3/005a3eb8.md) [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) [`006052b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00605/006052b0.md) · 呼出先 47件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00589fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00589/00589fe4.md)
- 新版 呼出元 41件 [`005c8780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c8/005c8780.md) [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`0062ada8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0062a/0062ada8.md) · 呼出先 47件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00481e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00481/00481e40.md) [`004a680c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004a6/004a680c.md) [`005ae5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ae/005ae5a8.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 45.84% / 新版 45.57%

CFGの説明率　旧版 17.43% / 新版 21.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 47件, `call_count` 2件, `unresolved_branch_alignment` 34件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aa3c54",
      "incomplete_value": true,
      "site": "00aa3c54",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "leaf",
                "const:6a:4"
              ],
              [
                "live",
                "register:4040:4"
              ]
            ]
          ],
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
      "definition_site": "00a45c50",
      "incomplete_value": true,
      "site": "00a45c50",
      "value": [
        "BOOL_AND",
        "1",
        [
          [
            "INT_LESSEQUAL",
            "1",
            [
              [
                "leaf",
                "const:69:4"
              ],
              [
                "live",
                "register:4040:4"
              ]
            ]
          ],
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
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a45c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a45cf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aa3c68",
      "DATA",
      [
        "storage",
        "002f1a4c",
        "switchD_00a45c7c::switchdataD_002f1a4c",
        "ushort"
      ]
    ],
    [
      "00aa3c80",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00a464a8"
      ]
    ],
    [
      "00aa3c80",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00a45c80"
      ]
    ]
  ],
  "added": [
    [
      "00aa3c68",
      "DATA",
      [
        "storage",
        "0030744c",
        "switchD_00aa3c80::switchdataD_0030744c",
        "ushort"
      ]
    ],
    [
      "00aa3c80",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00aa4544"
      ]
    ],
    [
      "00aa3c80",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00aa3c84"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a45c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md#insn-00a45c50) · [`00a45c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md#insn-00a45c8c) · [`00a45cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md#insn-00a45cf0)
- 新版 [`00aa3c54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md#insn-00aa3c54)

~~~diff
- 00a45c50 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a45c50 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00a45c50 ["CBRANCH", null, ["local:b260:8", "tmp:1:1"]]
+ 00aa3c54 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00aa3c54 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00aa3c54 ["CBRANCH", null, ["local:b194:8", "tmp:1:1"]]
- 00a45c50 bytes e8a60054
+ 00aa3c54 bytes e8a70054
- 00a45c8c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a45c8c ["CBRANCH", null, ["local:b263:8", "tmp:0:1"]]
- 00a45c8c bytes a1cc0054
- 00a45cf0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a45cf0 ["CBRANCH", null, ["local:b263:8", "tmp:0:1"]]
- 00a45cf0 bytes 81c90054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd62ac9faebf2ab0c9641af4cb0a84f"></a>

### [`00a47708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47708.md) → [`00aa572c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa572c.md) FUN_00aa572c

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 24件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 60.23% / 新版 55.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 7件, `store_destination` 1件, `store_value` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47734"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47744"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a47728",
      "WRITE",
      [
        "storage",
        "Stack[-0x26c]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a47734",
      "WRITE",
      [
        "storage",
        "Stack[-0x278]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4773c",
      "PARAM",
      [
        "storage",
        "002a8b2e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa574c",
      "WRITE",
      [
        "storage",
        "Stack[-0x26c]",
        null,
        null
      ]
    ],
    [
      "00aa5758",
      "WRITE",
      [
        "storage",
        "Stack[-0x278]",
        null,
        null
      ]
    ],
    [
      "00aa5760",
      "PARAM",
      [
        "storage",
        "002b97f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a47728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47708.md#insn-00a47728) · [`00a47734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47708.md#insn-00a47734) · [`00a47744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47708.md#insn-00a47744)

~~~diff
- 00a47728 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:14:8"]]
- 00a47728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00a47728 bytes e11700b9
- 00a47734 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a47734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a47734 bytes e80700f9
- 00a47744 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a47744 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00a47744 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a47744 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d16a86dd4fa26611dba3452eb60a56d"></a>

### [`00a47ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47ec0.md) → [`00aa5ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa5ee4.md) FUN_00aa5ee4

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 31件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 31件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.36% / 新版 87.36%

CFGの説明率　旧版 77.01% / 新版 69.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件, `store_value` 8件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47ec0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a47ec4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a47ec0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a47ec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a47ec8",
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
      "00aa5ee4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aa5ee8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aa5eec",
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

- 旧版 [`00a47ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47ec0.md#insn-00a47ec0) · [`00a47ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47ec0.md#insn-00a47ec4) · [`00a47ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47ec0.md#insn-00a47ec8)

~~~diff
- 00a47ec0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a47ec0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a47ec0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a47ec0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a47ec0 bytes fd7bbaa9
- 00a47ec4 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a47ec4 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a47ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a47ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a47ec4 bytes fc6f01a9
- 00a47ec8 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a47ec8 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a47ec8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a47ec8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a47ec8 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7cb85bc66957ef2288f663041007c26"></a>

### [`00a48a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48a98.md) → [`00aa6abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6abc.md) FUN_00aa6abc

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 9件 [`006c06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c0/006c06f0.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 9件 [`006ea4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ea/006ea4b4.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.08% / 新版 73.08%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48ad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48b48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a48ad0",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a48ad0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a48afc",
      "DATA",
      [
        "storage",
        "002aaee0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa6af4",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "00aa6af4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00aa6b20",
      "DATA",
      [
        "storage",
        "002bbca9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a48ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48a98.md#insn-00a48ad0) · [`00a48afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48a98.md#insn-00a48afc) · [`00a48b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48a98.md#insn-00a48b00)

~~~diff
- 00a48ad0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 00a48ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a48ad0 bytes e83700f9
- 00a48afc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:58:8"]]
- 00a48afc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a48afc bytes e82f00f9
- 00a48b00 ["INT_ADD", "register:40f0:8", ["const:a48b00:8", "const:4:8"]]
- 00a48b00 ["CALL", null, ["callee:00c5a440:8"]]
- 00a48b00 bytes bc530694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e06d233c6bcb00664822ddc5303d4dd"></a>

### [`00a48d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48d84.md) → [`00aa6da8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6da8.md) FUN_00aa6da8

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.01% / 新版 69.01%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48db8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a48dbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a48db4",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a48db4",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a48db8",
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
      "00aa6dd8",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "00aa6dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00aa6ddc",
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

- 旧版 [`00a48db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48d84.md#insn-00a48db4) · [`00a48db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48d84.md#insn-00a48db8) · [`00a48dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48d84.md#insn-00a48dbc)

~~~diff
- 00a48db4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00a48db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a48db4 bytes e80f00f9
- 00a48db8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a48db8 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00a48db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00a48db8 bytes ff2300b9
- 00a48dbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a48dbc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a48dbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00a48dbc bytes ff1700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a0b1b4953ebf6b50c4365a99f036f45"></a>

### [`00a48efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48efc.md) → [`00aa6f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f20.md) FUN_00aa6f20

採用 · 移動量 `+0x5e024` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 1件 [`00a4e7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e7d4.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 1件 [`00aac7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac7f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa6f34",
      "incomplete_value": false,
      "site": "00aa6f38",
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
            "const:7f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a48f10",
      "incomplete_value": false,
      "site": "00a48f14",
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
            "const:b2e:8"
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
      "00aa6f34",
      "PARAM",
      [
        "storage",
        "002a8b2e",
        null,
        "string"
      ]
    ],
    [
      "00aa6f44",
      "PARAM",
      [
        "storage",
        "002a4d87",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa6f34",
      "PARAM",
      [
        "storage",
        "002b97f7",
        null,
        "string"
      ]
    ],
    [
      "00aa6f44",
      "PARAM",
      [
        "storage",
        "002b5717",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a48f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48efc.md#insn-00a48f14) · [`00a48f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48efc.md#insn-00a48f0c) · [`00a48f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48efc.md#insn-00a48f10)
- 新版 [`00aa6f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f20.md#insn-00aa6f38) · [`00aa6f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f20.md#insn-00aa6f30) · [`00aa6f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f20.md#insn-00aa6f34)

~~~diff
- 00a48f14 ["INT_ADD", "register:40f0:8", ["const:a48f14:8", "const:4:8"]]
- 00a48f14 ["CALL", null, ["callee:00aac7f8:8"]]
+ 00aa6f38 ["INT_ADD", "register:40f0:8", ["const:aa6f38:8", "const:4:8"]]
+ 00aa6f38 ["CALL", null, ["callee:00aac7f8:8"]]
- 00a48f14 bytes 30160094
+ 00aa6f38 bytes 30160094
- 00a48f0c ["COPY", "register:4000:8", ["const:2a8000:8"]]
+ 00aa6f30 ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 00a48f0c bytes 00c3ff90
+ 00aa6f30 bytes 80c0fff0
- 00a48f10 ["COPY", "tmp:0:8", ["const:b2e:8"]]
- 00a48f10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a48f10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a48f10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aa6f34 ["COPY", "tmp:0:8", ["const:7f7:8"]]
+ 00aa6f34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aa6f34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aa6f34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a48f10 bytes 00b82c91
+ 00aa6f34 bytes 00dc1f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a81257eab995dd4d03c5179cd84aadc"></a>

### [`00a4916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a4916c.md) → [`00aa7190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa7190.md) FUN_00aa7190

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 22件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 22件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.75% / 新版 78.75%

CFGの説明率　旧版 30.00% / 新版 25.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4916c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a49170"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4916c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a49170",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a49174",
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
      "00aa7190",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aa7194",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aa7198",
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

- 旧版 [`00a4916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a4916c.md#insn-00a4916c) · [`00a49170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a4916c.md#insn-00a49170) · [`00a49174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a4916c.md#insn-00a49174)

~~~diff
- 00a4916c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a4916c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a4916c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00a4916c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a4916c bytes fd7bbba9
- 00a49170 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a49170 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00a49170 bytes fc0b00f9
- 00a49174 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00a49174 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a49174 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a49174 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a49174 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d51faa65febe9b7730c1cc59dd52728e"></a>

### [`00a496c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md) → [`00aa76e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa76e4.md) FUN_00aa76e4

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 18件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0061811c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00618/0061811c.md) [`0061bfb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061b/0061bfb4.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 18件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0063dc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0063d/0063dc04.md) [`00641a9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00641/00641a9c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.24% / 新版 73.24%

CFGの説明率　旧版 36.15% / 新版 27.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 15件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 26件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a497ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a497f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a49800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4971c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00aa7754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0061811c"
      ]
    ],
    [
      "00aa7768",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a49754"
      ]
    ]
  ],
  "added": [
    [
      "00aa7720",
      "DATA",
      [
        "storage",
        "004347d8",
        null,
        "dword"
      ]
    ],
    [
      "00aa773c",
      "DATA",
      [
        "storage",
        "004347d0",
        null,
        "byte[39]"
      ]
    ],
    [
      "00aa7740",
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

- 旧版 [`00a497ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md#insn-00a497ec) · [`00a497f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md#insn-00a497f8) · [`00a49800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md#insn-00a49800)

~~~diff
- 00a497ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:158:8"]]
- 00a497ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00a497ec bytes e85b01b9
- 00a497f8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a497f8 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "const:61:8"]]
- 00a497f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00a497f8 bytes 491306b8
- 00a49800 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a49800 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:160:8"]]
- 00a49800 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a49800 bytes e8830539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9c0ce0cee591439825c2a868ebfdf9"></a>

### [`00a4a0e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a0e4.md) → [`00aa8108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8108.md) FUN_00aa8108

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a0ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4a0e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a0ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a0f0",
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
      "00aa810c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa8110",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa8114",
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

- 旧版 [`00a4a0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a0e4.md#insn-00a4a0e8) · [`00a4a0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a0e4.md#insn-00a4a0ec) · [`00a4a0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a0e4.md#insn-00a4a0f0)

~~~diff
- 00a4a0e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a4a0e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a4a0e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a4a0e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4a0e8 bytes fd7b06a9
- 00a4a0ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00a4a0ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a4a0ec bytes f53b00f9
- 00a4a0f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a4a0f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a4a0f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00a4a0f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4a0f0 bytes f44f08a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fff5fe401d1140c81d0e094687345a6f"></a>

### [`00a4a284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md) → [`00aa82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa82a8.md) FUN_00aa82a8

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 12件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0063c2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c2c0.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 12件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00662598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662598.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.10% / 新版 86.10%

CFGの説明率　旧版 66.67% / 新版 57.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a2b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a2b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a2c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4a2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a2b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x12b]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a2c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa82d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00aa82dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x12b]",
        null,
        null
      ]
    ],
    [
      "00aa82e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x130]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4a2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md#insn-00a4a2b0) · [`00a4a2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md#insn-00a4a2b8) · [`00a4a2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md#insn-00a4a2c0)

~~~diff
- 00a4a2b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4a2b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4a2b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4a2b0 bytes a8831ff8
- 00a4a2b8 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a4a2b8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:55:8"]]
- 00a4a2b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a4a2b8 bytes ea530578
- 00a4a2c0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a4a2c0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:50:8"]]
- 00a4a2c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a4a2c0 bytes e8430139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a42a0fcc521f510a54bb108a58dfd4eb"></a>

### [`00a4a7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a7d8.md) → [`00aa87fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa87fc.md) FUN_00aa87fc

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 22.53% / 新版 22.53%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 38件, `unresolved_store_alignment` 49件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a7e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a7e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4a800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4a7e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a800",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4a804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa8910"
      ]
    ]
  ],
  "added": [
    [
      "00aa880c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aa8824",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00aa8828",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa8910"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4a7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a7d8.md#insn-00a4a7e8) · [`00a4a800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a7d8.md#insn-00a4a800) · [`00a4a824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a7d8.md#insn-00a4a824)

~~~diff
- 00a4a7e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a4a7e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a4a7e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a4a7e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4a7e8 bytes f44f0da9
- 00a4a800 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4a800 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4a800 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4a800 bytes a8831ff8
- 00a4a824 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00a4a824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4a824 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c7df2194dc532c4f079ee0144d3e956"></a>

### [`00a4ad68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4ad68.md) → [`00aa8d8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8d8c.md) FUN_00aa8d8c

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 9件 [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 9件 [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 76.34% / 新版 76.34%

CFGの説明率　旧版 30.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ada8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4adec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ae0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4ada8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4adbc",
      "PARAM",
      [
        "storage",
        "0029820c",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a4adbc",
      "PARAM",
      [
        "storage",
        "002a0917",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa8dcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00aa8de0",
      "PARAM",
      [
        "storage",
        "002a7e44",
        null,
        "string"
      ]
    ],
    [
      "00aa8de0",
      "PARAM",
      [
        "storage",
        "002b0ed1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4ada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4ad68.md#insn-00a4ada8) · [`00a4adbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4ad68.md#insn-00a4adbc) · [`00a4adec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4ad68.md#insn-00a4adec)

~~~diff
- 00a4ada8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a4ada8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4ada8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4ada8 bytes a9831ff8
- 00a4adbc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a4adbc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00a4adbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4adbc ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00a4adbc bytes 2101889a
- 00a4adec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:48:8"]]
- 00a4adec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4adec bytes e82700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d71b72cef85e2b16feeef32c5495a618"></a>

### [`00a4af88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md) → [`00aa8fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa8fac.md) FUN_00aa8fac

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 55.65% / 新版 55.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4afb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4afc0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4afc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4afb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4afc0",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a4afc0",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa8fd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00aa8fe4",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "00aa8fe4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4afb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md#insn-00a4afb4) · [`00a4afc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md#insn-00a4afc0) · [`00a4afc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4af88.md#insn-00a4afc4)

~~~diff
- 00a4afb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4afb4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4afb4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4afb4 bytes a8831ff8
- 00a4afc0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00a4afc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4afc0 bytes e80f00f9
- 00a4afc4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a4afc4 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00a4afc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00a4afc4 bytes ff2300b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52eba0a2642ad86a4edeb9442a7e6267"></a>

### [`00a4b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md) → [`00aa9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa9/00aa9230.md) FUN_00aa9230

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 32件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 32件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 28.27% / 新版 28.27%

CFGの説明率　旧版 43.41% / 新版 38.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `call_target` 3件, `store_condition` 9件, `store_value` 1件, `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 277件, `unresolved_store_alignment` 368件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4b238"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4b270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4b27c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4b238",
      "WRITE",
      [
        "storage",
        "Stack[-0x3ac]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4b240",
      "READ",
      [
        "storage",
        "002ae24a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a4b270",
      "WRITE",
      [
        "storage",
        "Stack[-0x11f]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa925c",
      "WRITE",
      [
        "storage",
        "Stack[-0x3ac]",
        null,
        null
      ]
    ],
    [
      "00aa9264",
      "READ",
      [
        "storage",
        "002bf68f",
        null,
        "string"
      ]
    ],
    [
      "00aa9294",
      "WRITE",
      [
        "storage",
        "Stack[-0x11f]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4b238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md#insn-00a4b238) · [`00a4b270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md#insn-00a4b270) · [`00a4b27c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md#insn-00a4b27c)

~~~diff
- 00a4b238 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:24:8"]]
- 00a4b238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00a4b238 bytes e12700b9
- 00a4b270 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00a4b270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:49:8"]]
- 00a4b270 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4b270 bytes 0b9104f8
- 00a4b27c ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a4b27c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:1:8"]]
- 00a4b27c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00a4b27c bytes 0a1100b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8844e511ffc1240a2e82a3de23eda081"></a>

### [`00a4e048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e048.md) → [`00aac06c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac06c.md) FUN_00aac06c

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.55% / 新版 68.55%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e080"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e0ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e0c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4e080",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a4e080",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4e0ac",
      "DATA",
      [
        "storage",
        "002a8b3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aac0a4",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "00aac0a4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc8]",
        null,
        null
      ]
    ],
    [
      "00aac0d0",
      "DATA",
      [
        "storage",
        "002b9804",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4e080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e048.md#insn-00a4e080) · [`00a4e0ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e048.md#insn-00a4e0ac) · [`00a4e0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e048.md#insn-00a4e0b0)

~~~diff
- 00a4e080 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00a4e080 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4e080 bytes e80f00f9
- 00a4e0ac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a4e0ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4e0ac bytes e80700f9
- 00a4e0b0 ["INT_ADD", "register:40f0:8", ["const:a4e0b0:8", "const:4:8"]]
- 00a4e0b0 ["CALL", null, ["callee:00c5a440:8"]]
- 00a4e0b0 bytes 503e0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c3e80831fe8adad9ac53321072c0a98"></a>

### [`00a4e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e2cc.md) → [`00aac2f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac2f0.md) FUN_00aac2f0

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.06% / 新版 58.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e2dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e2f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4e2dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4e2f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4e304",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aac300",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aac31c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00aac328",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4e2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e2cc.md#insn-00a4e2dc) · [`00a4e2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e2cc.md#insn-00a4e2f8) · [`00a4e304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e2cc.md#insn-00a4e304)

~~~diff
- 00a4e2dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a4e2dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a4e2dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a4e2dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4e2dc bytes f44f0da9
- 00a4e2f8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4e2f8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4e2f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4e2f8 bytes a8831ff8
- 00a4e304 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00a4e304 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a4e304 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44f8962f35670b9b998dfd05033a4158"></a>

### [`00a4e550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e550.md) → [`00aac574`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac574.md) FUN_00aac574

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) · 呼出先 5件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 1件 [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) · 呼出先 5件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.29% / 新版 86.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aac5a8",
      "incomplete_value": false,
      "site": "00aac5ac",
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
            "const:ab4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e584",
      "incomplete_value": false,
      "site": "00a4e588",
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
            "const:72f:8"
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
      "definition_site": "00aac5cc",
      "incomplete_value": false,
      "site": "00aac5d8",
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
            "const:3da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e5a8",
      "incomplete_value": false,
      "site": "00a4e5b4",
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
            "const:57b:8"
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
      "definition_site": "00aac5f0",
      "incomplete_value": false,
      "site": "00aac5f8",
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
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a4e5cc",
      "incomplete_value": false,
      "site": "00a4e5d4",
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
            "const:7bc:8"
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
      "00aac5ac",
      "DATA",
      [
        "storage",
        "0029e72f",
        null,
        "string"
      ]
    ],
    [
      "00aac5d8",
      "DATA",
      [
        "storage",
        "0029957b",
        null,
        "string"
      ]
    ],
    [
      "00aac5f8",
      "DATA",
      [
        "storage",
        "002a17bc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aac5ac",
      "DATA",
      [
        "storage",
        "002aeab4",
        null,
        "string"
      ]
    ],
    [
      "00aac5d8",
      "DATA",
      [
        "storage",
        "002a93da",
        null,
        "string"
      ]
    ],
    [
      "00aac5f8",
      "DATA",
      [
        "storage",
        "002b1e08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a4e6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e550.md#insn-00a4e6d8) · [`00a4e580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e550.md#insn-00a4e580) · [`00a4e584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e550.md#insn-00a4e584)
- 新版 [`00aac6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac574.md#insn-00aac6fc) · [`00aac5a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac574.md#insn-00aac5a4) · [`00aac5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac574.md#insn-00aac5a8)

~~~diff
- 00a4e6d8 ["INT_ADD", "register:40f0:8", ["const:a4e6d8:8", "const:4:8"]]
- 00a4e6d8 ["CALL", null, ["callee:0087925c:8"]]
+ 00aac6fc ["INT_ADD", "register:40f0:8", ["const:aac6fc:8", "const:4:8"]]
+ 00aac6fc ["CALL", null, ["callee:0087925c:8"]]
- 00a4e6d8 bytes 26e2f797
+ 00aac6fc bytes d832f797
- 00a4e580 ["COPY", "register:4040:8", ["const:29e000:8"]]
+ 00aac5a4 ["COPY", "register:4040:8", ["const:2ae000:8"]]
- 00a4e580 bytes 88c2ff90
+ 00aac5a4 bytes 08c0ffd0
- 00a4e584 ["COPY", "tmp:0:8", ["const:72f:8"]]
- 00a4e584 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e584 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a4e584 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aac5a8 ["COPY", "tmp:0:8", ["const:ab4:8"]]
+ 00aac5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aac5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aac5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a4e584 bytes 08bd1c91
+ 00aac5a8 bytes 08d12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96b6de135ade10cdb8bb2a8bdd853d3a"></a>

### [`00a4e7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e7d4.md) → [`00aac7f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac7f8.md) FUN_00aac7f8

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00a45360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45360.md) [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md) [`00a47708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47708.md) [`00a47ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a47/00a47ec0.md) [`00a48efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a48/00a48efc.md) · 呼出先 10件 [`007cf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf4b0.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`007cfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfaa0.md) [`007cfcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cfcd8.md) [`007d0b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d0/007d0b74.md)
- 新版 呼出元 7件 [`00aa3264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3264.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md) [`00aa572c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa572c.md) [`00aa5ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa5/00aa5ee4.md) [`00aa6f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa6/00aa6f20.md) · 呼出先 10件 [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md) [`00802c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802c68.md) [`00802ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802ea0.md) [`00803d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00803/00803d3c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.23% / 新版 61.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e7d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e7d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4e7dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4e7d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4e7dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4e7e0",
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
      "00aac7fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aac800",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aac804",
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

- 旧版 [`00a4e7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e7d4.md#insn-00a4e7d8) · [`00a4e7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e7d4.md#insn-00a4e7dc) · [`00a4e7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4e7d4.md#insn-00a4e7e0)

~~~diff
- 00a4e7d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a4e7d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a4e7d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00a4e7d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4e7d8 bytes fd7b12a9
- 00a4e7dc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a4e7dc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00a4e7dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00a4e7dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4e7dc bytes fc5f13a9
- 00a4e7e0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a4e7e0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a4e7e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 00a4e7e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4e7e0 bytes f65714a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dbd3f1ded0bd97f9fd715b1b82cd6ef"></a>

### [`00a4ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md) → [`00aacca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aacca8.md) FUN_00aacca8

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00829bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829bb8.md) [`008594d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/008594d4.md) [`0087ab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087a/0087ab54.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`005bc058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc058.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00821cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00821/00821cb4.md)
- 新版 呼出元 5件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) [`0085bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bb30.md) [`0088c46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c46c.md) [`008adcf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ad/008adcf4.md) · 呼出先 12件 [`004476b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/004476b4.md) [`005e0d28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e0/005e0d28.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00853c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00853/00853c30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 45.11% / 新版 45.11%

CFGの説明率　旧版 26.09% / 新版 24.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 33件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 49件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ecb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ed20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ed24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4ecb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4ecbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a4ecf4"
      ]
    ],
    [
      "unmatched:00a4ecc0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "00aaccdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00aacce0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aacd18"
      ]
    ],
    [
      "00aacce4",
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

- 旧版 [`00a4ecb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md#insn-00a4ecb8) · [`00a4ed20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md#insn-00a4ed20) · [`00a4ed24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4e/00a4ec84.md#insn-00a4ed24)

~~~diff
- 00a4ecb8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4ecb8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4ecb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4ecb8 bytes a8831ff8
- 00a4ed20 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a4ed20 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "const:11:8"]]
- 00a4ed20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00a4ed20 bytes 2a1301b8
- 00a4ed24 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:1:8"]]
- 00a4ed24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a4ed24 bytes 2013803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f311ecced5b10f2175df692b439a7c"></a>

### [`00a4f47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md) → [`00aad4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aad4a0.md) FUN_00aad4a0

採用 · 移動量 `+0x5e024` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) · 呼出先 21件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md)
- 新版 呼出元 1件 [`0088c830`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0088c/0088c830.md) · 呼出先 21件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0046d450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d450.md) [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.42% / 新版 84.42%

CFGの説明率　旧版 61.76% / 新版 56.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f47c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f480"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4f480"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a4f47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4f480",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a4f484",
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
      "00aad4a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "00aad4a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aad4a8",
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

- 旧版 [`00a4f47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md#insn-00a4f47c) · [`00a4f480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md#insn-00a4f480) · [`00a4f484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4f47c.md#insn-00a4f484)

~~~diff
- 00a4f47c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffff90:8"]]
- 00a4f47c ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 00a4f47c bytes e80f19fc
- 00a4f480 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a4f480 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a4f480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a4f480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4f480 bytes fd7b01a9
- 00a4f484 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a4f484 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a4f484 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a4f484 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a4f484 bytes fc6f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35bf5576bab7b87118ca1db84b6416a1"></a>

### [`00a4fe00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md) → [`00aade24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aade24.md) FUN_00aade24

採用 · 移動量 `+0x5e024` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a4b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00aa9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa9/00aa9230.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 68.42% / 新版 63.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a4fe14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe14) · [`00a4fe1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe1c) · [`00a4fe24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4fe00.md#insn-00a4fe24)
- 新版 [`00aade38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aade24.md#insn-00aade38) · [`00aade40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aade24.md#insn-00aade40) · [`00aade48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aade24.md#insn-00aade48)

~~~diff
- 00a4fe14 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a4fe14 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a4fe14 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a4fe14 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aade38 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00aade38 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aade38 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aade38 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a4fe14 bytes c8020037
+ 00aade38 bytes c8020037
- 00a4fe1c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a4fe1c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a4fe1c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a4fe1c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aade40 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00aade40 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aade40 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aade40 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a4fe1c bytes 08030037
+ 00aade40 bytes 08030037
- 00a4fe24 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00a4fe24 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a4fe24 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a4fe24 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aade48 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00aade48 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aade48 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aade48 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a4fe24 bytes 48030037
+ 00aade48 bytes 48030037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2eaff5ac46aa3526f5923acc177bedf6"></a>

### [`00a4ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md) → [`00aadf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadf30.md) FUN_00aadf30

採用 · 移動量 `+0x5e024` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a4b20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4b/00a4b20c.md) [`00a4ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md) · 呼出先 3件 [`0062d1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d1a8.md) [`00a4ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00aa9230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa9/00aa9230.md) [`00aadf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadf30.md) · 呼出先 3件 [`00652c8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00652/00652c8c.md) [`00aadf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadf30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aadf4c",
      "incomplete_value": true,
      "site": "00aadf50",
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
      "definition_site": "00a4ff28",
      "incomplete_value": true,
      "site": "00a4ff2c",
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

- 旧版 [`00a4ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md#insn-00a4ff2c) · [`00a4ff0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md#insn-00a4ff0c) · [`00a4ff28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ff0c.md#insn-00a4ff28)
- 新版 [`00aadf50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadf30.md#insn-00aadf50) · [`00aadf30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadf30.md#insn-00aadf30)

~~~diff
- 00a4ff2c ["INT_ADD", "register:40f0:8", ["const:a4ff2c:8", "const:4:8"]]
- 00a4ff2c ["CALL", null, ["local:b0:8"]]
+ 00aadf50 ["INT_ADD", "register:40f0:8", ["const:aadf50:8", "const:4:8"]]
+ 00aadf50 ["CALL", null, ["local:b0:8"]]
- 00a4ff2c bytes f8ffff97
+ 00aadf50 bytes f8ffff97
- 00a4ff0c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00a4ff0c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aadf30 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aadf30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a4ff0c bytes 610200b4
+ 00aadf30 bytes 610200b4
- 00a4ff28 ["COPY", "register:4008:8", ["register:4040:8"]]
- 00a4ff28 bytes e10308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91132e8be2cba8f477c9a18616273c6f"></a>

### [`00a4ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md) → [`00aadfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadfd0.md) FUN_00aadfd0

採用 · 移動量 `+0x5e024` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a496c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md) [`00a4a284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00a500dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 2件 [`00aa76e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa76e4.md) [`00aa82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa82a8.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00aae100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae100.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 33.33% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a4ffe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a50084"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aae004"
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
      "unmatched:00a4ffe0",
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
      "00aae004",
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

- 旧版 [`00a4ffe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md#insn-00a4ffe0) · [`00a4ffe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md#insn-00a4ffe4) · [`00a50084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md#insn-00a50084)
- 新版 [`00aae008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadfd0.md#insn-00aae008)

~~~diff
- 00a4ffe0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a4ffe0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a4ffe0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a4ffe0 bytes a8831ff8
- 00a4ffe4 ["INT_ADD", "register:40f0:8", ["const:a4ffe4:8", "const:4:8"]]
- 00a4ffe4 ["CALL", null, ["callee:00aae100:8"]]
+ 00aae008 ["INT_ADD", "register:40f0:8", ["const:aae008:8", "const:4:8"]]
+ 00aae008 ["CALL", null, ["callee:00aae100:8"]]
- 00a4ffe4 bytes 3e000094
+ 00aae008 bytes 3e000094
- 00a50084 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00a50084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a50084 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53f6b3d649cf74323656dfb82ff6cdff"></a>

### [`00a500dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md) → [`00aae100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae100.md) FUN_00aae100

採用 · 移動量 `+0x5e024` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a4ffac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4f/00a4ffac.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00aadfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aad/00aadfd0.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 97.17% / 新版 97.17%

CFGの説明率　旧版 67.80% / 新版 60.61%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 2件

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a50130"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a501a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a50268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a50130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae214"
      ]
    ],
    [
      "unmatched:00a501a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae1ec"
      ]
    ],
    [
      "unmatched:00a50268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae26c"
      ]
    ]
  ],
  "added": [
    [
      "00aae154",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae214"
      ]
    ],
    [
      "00aae1c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae1ec"
      ]
    ],
    [
      "00aae28c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aae26c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a50130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md#insn-00a50130) · [`00a501a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md#insn-00a501a0) · [`00a50268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a500dc.md#insn-00a50268)

~~~diff
- 00a50130 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00a50130 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00a50130 bytes 0b0600b4
- 00a501a0 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00a501a0 ["CBRANCH", null, ["local:b24:8", "tmp:0:1"]]
- 00a501a0 bytes 4b0100b4
- 00a50268 ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00a50268 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
- 00a50268 bytes 0bffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73b6bbcd1267c2c6f5bacda265755efc"></a>

### [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) → [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) FUN_00aae2f8

採用 · 移動量 `+0x5e024` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`00a496c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a49/00a496c0.md) [`00a4a284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a4a/00a4a284.md) [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) · 呼出先 2件 [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`00aa76e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa7/00aa76e4.md) [`00aa82a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa8/00aa82a8.md) [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) · 呼出先 2件 [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a502d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a502d4) · [`00a502f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a502f0) · [`00a502fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a50/00a502d4.md#insn-00a502fc)
- 新版 [`00aae2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md#insn-00aae2f8) · [`00aae314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md#insn-00aae314) · [`00aae320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aae/00aae2f8.md#insn-00aae320)

~~~diff
- 00a502d4 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00a502d4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00aae2f8 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aae2f8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a502d4 bytes 610200b4
+ 00aae2f8 bytes 610200b4
- 00a502f0 ["INT_ADD", "register:40f0:8", ["const:a502f0:8", "const:4:8"]]
- 00a502f0 ["CALL", null, ["local:b0:8"]]
+ 00aae314 ["INT_ADD", "register:40f0:8", ["const:aae314:8", "const:4:8"]]
+ 00aae314 ["CALL", null, ["local:b0:8"]]
- 00a502f0 bytes f9ffff97
+ 00aae314 bytes f9ffff97
- 00a502fc ["INT_ADD", "register:40f0:8", ["const:a502fc:8", "const:4:8"]]
- 00a502fc ["CALL", null, ["local:b0:8"]]
+ 00aae320 ["INT_ADD", "register:40f0:8", ["const:aae320:8", "const:4:8"]]
+ 00aae320 ["CALL", null, ["local:b0:8"]]
- 00a502fc bytes f6ffff97
+ 00aae320 bytes f6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28a5d6a178a6ceb228a338d466eeedc2"></a>

### [`00a517d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md) → [`00aaf838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aaf/00aaf838.md) FUN_00aaf838

採用 · 移動量 `+0x5e068` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00b1f000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b1f/00b1f000.md) · 呼出先 19件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 72.00% / 新版 72.00%

CFGの説明率　旧版 48.54% / 新版 41.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 18件, `store_destination` 1件, `store_value` 3件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 30件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a517e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a517e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a517fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a517e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a517fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x210]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a51804",
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
      "00aaf84c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aaf864",
      "WRITE",
      [
        "storage",
        "Stack[-0x210]",
        null,
        null
      ]
    ],
    [
      "00aaf86c",
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

- 旧版 [`00a517e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md#insn-00a517e4) · [`00a517fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md#insn-00a517fc) · [`00a51804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md#insn-00a51804)

~~~diff
- 00a517e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a517e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a517e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a517e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a517e4 bytes f44f05a9
- 00a517fc ["COPY", "tmp:0:8", ["register:8:8"]]
- 00a517fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a517fc bytes e80300f9
- 00a51804 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a51804 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00a51804 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a51804 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44ef0e75fbaecd51b7b7665a12117810"></a>

### [`00a534e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534e4.md) → [`00ab1588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1588.md) FUN_00ab1588

採用 · 移動量 `+0x5e0a4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00a517d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a51/00a517d0.md) [`00a52754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52754.md) [`00a52948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a52/00a52948.md) [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 4件 [`00aaf838`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aaf/00aaf838.md) [`00ab07f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab07f8.md) [`00ab09ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab0/00ab09ec.md) [`00ab1860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1860.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00ab1598",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a534f4",
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
      "definition_site": "00ab1594",
      "incomplete_value": false,
      "site": "00ab1598",
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
      "definition_site": "00a534f0",
      "incomplete_value": false,
      "site": "00a534f4",
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
      "00ab1594",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00ab1598",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00ab1594",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00ab1598",
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

- 旧版 [`00a534f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534e4.md#insn-00a534f4) · [`00a534ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534e4.md#insn-00a534ec) · [`00a534f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534e4.md#insn-00a534f0)
- 新版 [`00ab1598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1588.md#insn-00ab1598) · [`00ab1590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1588.md#insn-00ab1590) · [`00ab1594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1588.md#insn-00ab1594)

~~~diff
- 00a534f4 ["INT_ADD", "register:40f0:8", ["const:a534f4:8", "const:4:8"]]
- 00a534f4 ["CALL", null, ["ram:418c38:8"]]
+ 00ab1598 ["INT_ADD", "register:40f0:8", ["const:ab1598:8", "const:4:8"]]
+ 00ab1598 ["CALL", null, ["ram:43b738:8"]]
- 00a534f4 bytes d115e797
+ 00ab1598 bytes 6828e697
- 00a534ec ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00ab1590 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a534ec bytes a0c2ff90
+ 00ab1590 bytes 20c0ffd0
- 00a534f0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a534f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a534f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a534f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ab1594 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00ab1594 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab1594 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab1594 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a534f0 bytes 00740e91
+ 00ab1594 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9907f785c17ce1008fd99d117b8d667"></a>

### [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md) → [`00ab1860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1860.md) FUN_00ab1860

採用 · 移動量 `+0x5e0a4` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a534f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534f8.md) · 呼出先 6件 [`00a53498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53498.md) [`00a534e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a534e4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00ab159c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab159c.md) · 呼出先 6件 [`00ab153c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab153c.md) [`00ab1588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1588.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a537bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a537bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a537c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a537bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a537c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a537c4",
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
      "00ab1860",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ab1864",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ab1868",
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

- 旧版 [`00a537bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md#insn-00a537bc) · [`00a537c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md#insn-00a537c0) · [`00a537c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a537bc.md#insn-00a537c4)

~~~diff
- 00a537bc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a537bc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a537bc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00a537bc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a537bc bytes fd7bbca9
- 00a537c0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a537c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00a537c0 bytes f70b00f9
- 00a537c4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a537c4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a537c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a537c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a537c4 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee60318e65adcf62484a3f81d79963f2"></a>

### [`00a53884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53884.md) → [`00ab1928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1928.md) _INIT_237

採用 · 移動量 `+0x5e0a4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.14% / 新版 75.14%

CFGの説明率　旧版 63.89% / 新版 76.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a538b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a538dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a53900"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a538b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a538c0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a538dc",
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
      "00ab1958",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ab1964",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ab1980",
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

- 旧版 [`00a538b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53884.md#insn-00a538b4) · [`00a538dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53884.md#insn-00a538dc) · [`00a53900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53884.md#insn-00a53900)

~~~diff
- 00a538b4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a538b4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a538b4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a538b4 bytes a9831ff8
- 00a538dc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a538dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a538dc bytes e013813c
- 00a53900 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a53900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a53900 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcb58372ff2f5c66c5da2f390a9bc710"></a>

### [`00a53c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53c14.md) → [`00ab1cb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab1/00ab1cb8.md) _INIT_238

採用 · 移動量 `+0x5e0a4` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 35.00% / 新版 41.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a53c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a53c58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a53c5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a53c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a53c50",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a53c58",
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
      "00ab1ce8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ab1cf4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ab1cfc",
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

- 旧版 [`00a53c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53c14.md#insn-00a53c44) · [`00a53c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53c14.md#insn-00a53c58) · [`00a53c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53c14.md#insn-00a53c5c)

~~~diff
- 00a53c44 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a53c44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a53c44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a53c44 bytes a9831ff8
- 00a53c58 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a53c58 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00a53c58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a53c58 bytes ea130278
- 00a53c5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a53c5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a53c5c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-117b0b12fb46d4c76b87542355f3b88c"></a>

### [`00a53fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53fa4.md) → [`00ab2048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2048.md) FUN_00ab2048

採用 · 移動量 `+0x5e0a4` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a54838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54838.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md) [`00832580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832580.md)
- 新版 呼出元 1件 [`00ab28dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab28dc.md) · 呼出先 12件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00633334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/00633334.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) [`0086369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00863/0086369c.md) [`008644f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00864/008644f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 43.36% / 新版 43.36%

CFGの説明率　旧版 20.00% / 新版 20.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 3件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 30件, `unresolved_store_alignment` 54件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a53fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a54040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a54044"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a53fe0",
      "DATA",
      [
        "storage",
        "00c0d748",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a54030",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00a54034",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab261c"
      ]
    ]
  ],
  "added": [
    [
      "00ab2084",
      "DATA",
      [
        "storage",
        "00c8cd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ab20d4",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00ab20d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab261c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a53fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53fa4.md#insn-00a53fe0) · [`00a54040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53fa4.md#insn-00a54040) · [`00a54044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a53/00a53fa4.md#insn-00a54044)

~~~diff
- 00a53fe0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a53fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a53fe0 bytes 680200f9
- 00a54040 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00a54040 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00a54040 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 00a54040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00a54040 bytes ffaf0039
- 00a54044 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a54044 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 00a54044 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a54044 bytes e8830039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b33906ffecb083ee498225733623f432"></a>

### [`00a59aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59aa0.md) → [`00ab7a58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7a58.md) FUN_00ab7a58

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a59ab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a59ae0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ab7a70"
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
      "unmatched:00a59ab8",
      "DATA",
      [
        "storage",
        "00c0d748",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a59ae0",
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
      "00ab7a70",
      "DATA",
      [
        "storage",
        "00c8cd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ab7a98",
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

- 旧版 [`00a59ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59aa0.md#insn-00a59ab8) · [`00a59ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59aa0.md#insn-00a59ae0) · [`00a59b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59aa0.md#insn-00a59b0c)
- 新版 [`00ab7ac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7a58.md#insn-00ab7ac4)

~~~diff
- 00a59ab8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a59ab8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a59ab8 bytes 080000f9
- 00a59ae0 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a59ae0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a59ae0 bytes 680200f9
- 00a59b0c ["INT_ADD", "register:40f0:8", ["const:a59b0c:8", "const:4:8"]]
- 00a59b0c ["CALL", null, ["callee:00c57a80:8"]]
+ 00ab7ac4 ["INT_ADD", "register:40f0:8", ["const:ab7ac4:8", "const:4:8"]]
+ 00ab7ac4 ["CALL", null, ["callee:00c57a80:8"]]
- 00a59b0c bytes 49050694
+ 00ab7ac4 bytes ef7f0694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6d81a7f1e7c6ebb911248bb0b04dbc1"></a>

### [`00a59b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59b20.md) → [`00ab7ad8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7ad8.md) FUN_00ab7ad8

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00672708`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00672/00672708.md) [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 12.50% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a59b20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a59b20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a59b24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a59b20",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a59b24",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a59b38",
      "DATA",
      [
        "storage",
        "00c0d748",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ab7ad8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ab7adc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ab7af0",
      "DATA",
      [
        "storage",
        "00c8cd68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59b20.md#insn-00a59b20) · [`00a59b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59b20.md#insn-00a59b24) · [`00a59b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59b20.md#insn-00a59b38)

~~~diff
- 00a59b20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a59b20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a59b20 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a59b20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a59b20 bytes fd7bbea9
- 00a59b24 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a59b24 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a59b24 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a59b24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a59b24 bytes f44f01a9
- 00a59b38 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a59b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a59b38 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73623fae6db043af75bf9cec4c6baa01"></a>

### [`00a59bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59bac.md) → [`00ab7b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7b64.md) FUN_00ab7b64

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ab7b88",
      "incomplete_value": false,
      "site": "00ab7b88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a59bd0",
      "incomplete_value": false,
      "site": "00a59bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:768:8"
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
      "00ab7b88",
      "DATA",
      [
        "storage",
        "00c0d768",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ab7b88",
      "DATA",
      [
        "storage",
        "00c8cd88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a59bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59bac.md#insn-00a59bc0) · [`00a59bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59bac.md#insn-00a59bc8) · [`00a59bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a59/00a59bac.md#insn-00a59bcc)
- 新版 [`00ab7b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7b64.md#insn-00ab7b78) · [`00ab7b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7b64.md#insn-00ab7b80) · [`00ab7b84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab7/00ab7b64.md#insn-00ab7b84)

~~~diff
- 00a59bc0 ["INT_ADD", "register:40f0:8", ["const:a59bc0:8", "const:4:8"]]
- 00a59bc0 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ab7b78 ["INT_ADD", "register:40f0:8", ["const:ab7b78:8", "const:4:8"]]
+ 00ab7b78 ["CALL", null, ["callee:00c57a90:8"]]
- 00a59bc0 bytes 20050694
+ 00ab7b78 bytes c67f0694
- 00a59bc8 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ab7b80 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a59bc8 bytes a80d0090
+ 00ab7b80 bytes a80e00b0
- 00a59bcc ["COPY", "tmp:0:8", ["const:768:8"]]
- 00a59bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a59bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a59bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ab7b84 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00ab7b84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ab7b84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ab7b84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a59bcc bytes 08a11d91
+ 00ab7b84 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d60ffae2f0228d9d6adfa3abdab4edc5"></a>

### [`00a5a360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a360.md) → [`00ab8318`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8318.md) _INIT_239

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 62.71% / 新版 62.71%

CFGの説明率　旧版 64.86% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_store_alignment` 28件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a390"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a3a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a3a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5a390",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5a39c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a5a3a4",
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
      "00ab8348",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ab8354",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ab835c",
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

- 旧版 [`00a5a390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a360.md#insn-00a5a390) · [`00a5a3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a360.md#insn-00a5a3a4) · [`00a5a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a360.md#insn-00a5a3a8)

~~~diff
- 00a5a390 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a5a390 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a5a390 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a5a390 bytes a9831ff8
- 00a5a3a4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a5a3a4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00a5a3a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a5a3a4 bytes ea130278
- 00a5a3a8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a5a3a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a5a3a8 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf85cd5b3a815eba64576100b356a85"></a>

### [`00a5a6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md) → [`00ab86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab86a8.md) FUN_00ab86a8

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_calls_and_string` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`004618e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/004618e8.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 20件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00484780`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/00484780.md) [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 73.96% / 新版 73.96%

CFGの説明率　旧版 37.82% / 新版 37.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_condition` 5件, `store_destination` 1件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 16件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 27件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a710"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a71c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5a724"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5a710",
      "WRITE",
      [
        "storage",
        "Stack[-0x220]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5a71c",
      "WRITE",
      [
        "storage",
        "Stack[-0x238]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5a724",
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
      "00ab86c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x220]",
        null,
        null
      ]
    ],
    [
      "00ab86d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x238]",
        null,
        null
      ]
    ],
    [
      "00ab86dc",
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

- 旧版 [`00a5a710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md#insn-00a5a710) · [`00a5a71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md#insn-00a5a71c) · [`00a5a724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md#insn-00a5a724)

~~~diff
- 00a5a710 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00a5a710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00a5a710 bytes e01300f9
- 00a5a71c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00a5a71c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a5a71c bytes e80700f9
- 00a5a724 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a5a724 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00a5a724 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a5a724 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1221076b1a3d514445952abc9b70c429"></a>

### [`00a5af8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5af8c.md) → [`00ab8f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8f44.md) FUN_00ab8f44

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 25.00% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5afb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5afcc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ab8f6c"
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
      "unmatched:00a5afb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab8f80"
      ]
    ],
    [
      "unmatched:00a5afcc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab8f74"
      ]
    ]
  ],
  "added": [
    [
      "00ab8f6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab8f80"
      ]
    ],
    [
      "00ab8f84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab8f74"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5afb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5af8c.md#insn-00a5afb4) · [`00a5afcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5af8c.md#insn-00a5afcc)
- 新版 [`00ab8f6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8f44.md#insn-00ab8f6c)

~~~diff
- 00a5afb4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a5afb4 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a5afb4 bytes a1000054
- 00a5afcc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a5afcc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a5afcc bytes 80ffffb4
+ 00ab8f6c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ab8f6c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00ab8f6c bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9724b385daf124e27cd2a442c9180c01"></a>

### [`00a5b004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md) → [`00ab8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md) FUN_00ab8fbc

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`00829f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829f50.md) [`00a54838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54838.md) [`00a54efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54efc.md) [`00a56a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a56/00a56a58.md) · 呼出先 3件 [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 10件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`0085bec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bec8.md) [`00ab28dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab28dc.md) [`00ab2fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2fa8.md) [`00ab4b04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab4/00ab4b04.md) · 呼出先 3件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 14.29% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b03c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b040"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b040"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5b050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9034"
      ]
    ]
  ],
  "added": [
    [
      "00ab9008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9034"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5b03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md#insn-00a5b03c) · [`00a5b040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md#insn-00a5b040) · [`00a5b048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md#insn-00a5b048)

~~~diff
- 00a5b03c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a5b03c ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 00a5b03c ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00a5b03c ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:1:8"]]
- 00a5b03c bytes 9f8e00f8
- 00a5b040 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00a5b040 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00a5b040 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a5b040 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00a5b040 bytes 7f7e01a9
- 00a5b048 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a5b048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00a5b048 bytes 680200b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11d0ce1bf020a3e6cfa1913983d350c5"></a>

### [`00a5b594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md) → [`00ab954c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab954c.md) FUN_00ab954c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a5b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b404.md) [`00a5b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00ab93bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab93bc.md) [`00ab95b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab95b4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00ab955c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a5b5a4",
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
      "definition_site": "00ab9558",
      "incomplete_value": false,
      "site": "00ab955c",
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
      "definition_site": "00a5b5a0",
      "incomplete_value": false,
      "site": "00a5b5a4",
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
      "00ab9558",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00ab955c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00ab9558",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00ab955c",
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

- 旧版 [`00a5b5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md#insn-00a5b5a4) · [`00a5b59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md#insn-00a5b59c) · [`00a5b5a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md#insn-00a5b5a0)
- 新版 [`00ab955c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab954c.md#insn-00ab955c) · [`00ab9554`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab954c.md#insn-00ab9554) · [`00ab9558`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab954c.md#insn-00ab9558)

~~~diff
- 00a5b5a4 ["INT_ADD", "register:40f0:8", ["const:a5b5a4:8", "const:4:8"]]
- 00a5b5a4 ["CALL", null, ["ram:418c38:8"]]
+ 00ab955c ["INT_ADD", "register:40f0:8", ["const:ab955c:8", "const:4:8"]]
+ 00ab955c ["CALL", null, ["ram:43b738:8"]]
- 00a5b5a4 bytes a5f5e697
+ 00ab955c bytes 7708e697
- 00a5b59c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00ab9554 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a5b59c bytes 60c2ff90
+ 00ab9554 bytes e0bfffd0
- 00a5b5a0 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a5b5a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a5b5a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a5b5a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ab9558 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00ab9558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab9558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ab9558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a5b5a0 bytes 00740e91
+ 00ab9558 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb92bcd1cda0c94e57774580a53e470a"></a>

### [`00a5b5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5a8.md) → [`00ab9560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9560.md) FUN_00ab9560

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a5b5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5a8.md#insn-00a5b5d8) · [`00a5b5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5a8.md#insn-00a5b5e8)
- 新版 [`00ab9590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9560.md#insn-00ab9590) · [`00ab95a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9560.md#insn-00ab95a0)

~~~diff
- 00a5b5d8 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
+ 00ab9590 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00a5b5d8 bytes c0000054
+ 00ab9590 bytes c0000054
- 00a5b5e8 ["INT_ADD", "register:40f0:8", ["const:a5b5e8:8", "const:4:8"]]
- 00a5b5e8 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00ab95a0 ["INT_ADD", "register:40f0:8", ["const:ab95a0:8", "const:4:8"]]
+ 00ab95a0 ["CALL", null, ["callee:00c57ab0:8"]]
- 00a5b5e8 bytes 9efe0594
+ 00ab95a0 bytes 44790694
~~~


<a id="compare-5dd14ef63ba43d5d47ab2b5e34b2d7bf"></a>

### [`00a5b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md) → [`00ab95b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab95b4.md) FUN_00ab95b4

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a5a6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5a/00a5a6f0.md) · 呼出先 6件 [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00a5b594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b594.md) [`00a5b87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b87c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00ab86a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab86a8.md) · 呼出先 6件 [`00470954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470954.md) [`00ab954c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab954c.md) [`00ab9834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9834.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.97% / 新版 87.97%

CFGの説明率　旧版 56.25% / 新版 48.21%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b6d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ab9688"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b65c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5b65c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9628"
      ]
    ],
    [
      "unmatched:00a5b698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab96c0"
      ]
    ],
    [
      "unmatched:00a5b6d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab97b8"
      ]
    ]
  ],
  "added": [
    [
      "00ab9614",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab9628"
      ]
    ],
    [
      "00ab9650",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab96c0"
      ]
    ],
    [
      "00ab968c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ab97b8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5b65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b65c) · [`00a5b698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b698) · [`00a5b6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b5fc.md#insn-00a5b6d0)

~~~diff
- 00a5b65c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a5b65c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00a5b65c bytes a1000054
- 00a5b698 ["CBRANCH", null, ["local:b13:8", "register:102:1"]]
- 00a5b698 bytes 82030054
- 00a5b6d0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:20:8"]]
- 00a5b6d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a5b6d0 bytes 291300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f52eb631a7a8d20700a4f4abcd9437"></a>

### [`00a5b9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b9c4.md) → [`00ab997c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab997c.md) _INIT_240

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 51.98% / 新版 51.98%

CFGの説明率　旧版 43.33% / 新版 27.08%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5b9f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5ba08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5ba0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5b9f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5ba00",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a5ba08",
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
      "00ab99ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ab99b8",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ab99c0",
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

- 旧版 [`00a5b9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b9c4.md#insn-00a5b9f4) · [`00a5ba08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b9c4.md#insn-00a5ba08) · [`00a5ba0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b9c4.md#insn-00a5ba0c)

~~~diff
- 00a5b9f4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a5b9f4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a5b9f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a5b9f4 bytes a9831ff8
- 00a5ba08 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00a5ba08 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00a5ba08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a5ba08 bytes ea130278
- 00a5ba0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00a5ba0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a5ba0c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9af95c627740887394a370e91b65c71d"></a>

### [`00a5bd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5bd68.md) → [`00ab9d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab9/00ab9d20.md) FUN_00ab9d20

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 17件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.53% / 新版 78.53%

CFGの説明率　旧版 51.28% / 新版 54.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件, `store_value` 5件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5bdac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5bdc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5bdcc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5bdac",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00a5bdac",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5bdc4",
      "READ",
      [
        "storage",
        "0029cd68",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ab9d64",
      "DATA",
      [
        "storage",
        "00c64938",
        null,
        "undefined *"
      ]
    ],
    [
      "00ab9d64",
      "WRITE",
      [
        "storage",
        "Stack[-0x1c0]",
        null,
        null
      ]
    ],
    [
      "00ab9d7c",
      "READ",
      [
        "storage",
        "002acfc8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5bdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5bd68.md#insn-00a5bdac) · [`00a5bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5bd68.md#insn-00a5bdc8) · [`00a5bdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5bd68.md#insn-00a5bdcc)

~~~diff
- 00a5bdac ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00a5bdac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a5bdac bytes e82300f9
- 00a5bdc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00a5bdc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00a5bdc8 bytes e93b00b9
- 00a5bdcc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00a5bdcc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00a5bdcc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:3c:8"]]
- 00a5bdcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00a5bdcc bytes fff30039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-720fff75975e848c87c1c9745692232b"></a>

### [`00a5c38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c38c.md) → [`00aba344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba344.md) FUN_00aba344

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`006c86d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c8/006c86d0.md) [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 4件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00ade610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ade/00ade610.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 6件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`006f2494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006f2/006f2494.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`0075eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075e/0075eb40.md) · 呼出先 4件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3dfe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3d/00b3dfe8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 41.51% / 新版 46.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c43c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c448"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aba378",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ade610"
      ]
    ],
    [
      "unmatched:00a5c438",
      "READ",
      [
        "storage",
        "002b2820",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a5c454",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a5c460"
      ]
    ]
  ],
  "added": [
    [
      "00aba378",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3dfe8"
      ]
    ],
    [
      "00aba3f0",
      "READ",
      [
        "storage",
        "002c3f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00aba40c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aba418"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5c3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c38c.md#insn-00a5c3c0) · [`00a5c43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c38c.md#insn-00a5c43c) · [`00a5c444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c38c.md#insn-00a5c444)
- 新版 [`00aba378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba344.md#insn-00aba378)

~~~diff
- 00a5c3c0 ["INT_ADD", "register:40f0:8", ["const:a5c3c0:8", "const:4:8"]]
- 00a5c3c0 ["CALL", null, ["ram:ade610:8"]]
+ 00aba378 ["INT_ADD", "register:40f0:8", ["const:aba378:8", "const:4:8"]]
+ 00aba378 ["CALL", null, ["ram:b3dfe8:8"]]
- 00a5c3c0 bytes 94080294
+ 00aba378 bytes 1c0f0294
- 00a5c43c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00a5c43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:8"]]
- 00a5c43c bytes 180800f9
- 00a5c444 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:1c:8"]]
- 00a5c444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 00a5c444 bytes 00c001fc
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17c451abd991e90defb3d9b99d2603f1"></a>

### [`00a5c61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c61c.md) → [`00aba5d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00aba5d4.md) _INIT_241

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.63% / 新版 57.63%

CFGの説明率　旧版 93.33% / 新版 90.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c64c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5c680"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5c64c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5c658",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a5c674",
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
      "00aba604",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00aba610",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00aba62c",
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

- 旧版 [`00a5c64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c61c.md#insn-00a5c64c) · [`00a5c674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c61c.md#insn-00a5c674) · [`00a5c680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5c61c.md#insn-00a5c680)

~~~diff
- 00a5c64c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a5c64c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a5c64c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a5c64c bytes a9831ff8
- 00a5c674 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a5c674 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a5c674 bytes e013813c
- 00a5c680 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a5c680 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 00a5c680 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a5c680 bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbc752fb17da619326bf27a62c6ff545"></a>

### [`00a5cb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cb24.md) → [`00abaadc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abaadc.md) FUN_00abaadc

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`00a54efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a54/00a54efc.md) [`00a58498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a58/00a58498.md) · 呼出先 6件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a5b004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5b/00a5b004.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00ab2fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab2/00ab2fa8.md) [`00ab6544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab6/00ab6544.md) · 呼出先 6件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ab8fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ab8/00ab8fbc.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 53.70% / 新版 46.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5cb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5cb28"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5cb2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5cb28",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5cb2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5cb30",
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
      "00abaae0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00abaae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00abaae8",
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

- 旧版 [`00a5cb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cb24.md#insn-00a5cb28) · [`00a5cb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cb24.md#insn-00a5cb2c) · [`00a5cb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5c/00a5cb24.md#insn-00a5cb30)

~~~diff
- 00a5cb28 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5cb28 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5cb28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a5cb28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5cb28 bytes fd7b04a9
- 00a5cb2c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a5cb2c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a5cb2c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a5cb2c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5cb2c bytes fc6f05a9
- 00a5cb30 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a5cb30 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a5cb30 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a5cb30 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5cb30 bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc924e407ba2f1ff032064b0e11637b"></a>

### [`00a5d058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d058.md) → [`00abb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abb/00abb010.md) _INIT_242

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 48.59% / 新版 48.59%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d05c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d060"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5d05c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d060",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d064",
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
      "00abb014",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00abb018",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abb01c",
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

- 旧版 [`00a5d05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d058.md#insn-00a5d05c) · [`00a5d060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d058.md#insn-00a5d060) · [`00a5d064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d058.md#insn-00a5d064)

~~~diff
- 00a5d05c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5d05c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5d05c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a5d05c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d05c bytes fd7b0fa9
- 00a5d060 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a5d060 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a5d060 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a5d060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d060 bytes fc5710a9
- 00a5d064 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a5d064 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a5d064 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a5d064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d064 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c528fb85d099083361d86ba461da245c"></a>

### [`00a5d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d3e8.md) → [`00abb3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abb/00abb3a0.md) _INIT_243

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 48.59% / 新版 48.59%

CFGの説明率　旧版 60.00% / 新版 43.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d3ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d3ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d3f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5d3ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d3f4",
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
      "00abb3a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00abb3a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abb3ac",
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

- 旧版 [`00a5d3ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d3e8.md#insn-00a5d3ec) · [`00a5d3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d3e8.md#insn-00a5d3f0) · [`00a5d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d3e8.md#insn-00a5d3f4)

~~~diff
- 00a5d3ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5d3ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5d3ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00a5d3ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d3ec bytes fd7b0fa9
- 00a5d3f0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a5d3f0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a5d3f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00a5d3f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d3f0 bytes fc5710a9
- 00a5d3f4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a5d3f4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a5d3f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a5d3f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d3f4 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a86c377c0f67ff688cb25f28202dbe89"></a>

### [`00a5d778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d778.md) → [`00abb730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abb/00abb730.md) FUN_00abb730

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.87% / 新版 71.87%

CFGの説明率　旧版 16.97% / 新版 14.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 26件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d78c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5d790"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5d78c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d790",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5d7a4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00abb744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00abb748",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00abb75c",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5d78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d778.md#insn-00a5d78c) · [`00a5d790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d778.md#insn-00a5d790) · [`00a5d7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5d/00a5d778.md#insn-00a5d7a4)

~~~diff
- 00a5d78c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a5d78c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a5d78c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00a5d78c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d78c bytes f6570aa9
- 00a5d790 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a5d790 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a5d790 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00a5d790 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5d790 bytes f44f0ba9
- 00a5d7a4 ["COPY", "tmp:0:8", ["register:8:8"]]
- 00a5d7a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a5d7a4 bytes e80300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4257a3076eb451bbf56187ed37906774"></a>

### [`00a5e660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md) → [`00abc618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abc618.md) FUN_00abc618

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) · 呼出先 4件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 呼出先 4件 [`004878ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878ec.md) [`00487a24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487a24.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.67% / 新版 83.67%

CFGの説明率　旧版 18.18% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e6c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e6d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5e688",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5e708",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abc6d8"
      ]
    ]
  ],
  "added": [
    [
      "00abc640",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00abc6c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abc6d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5e688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e688) · [`00a5e68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e68c) · [`00a5e6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e660.md#insn-00a5e6c8)
- 新版 [`00abc644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abc618.md#insn-00abc644)

~~~diff
- 00a5e688 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00a5e688 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a5e688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a5e688 bytes a8831ff8
- 00a5e68c ["INT_ADD", "register:40f0:8", ["const:a5e68c:8", "const:4:8"]]
- 00a5e68c ["CALL", null, ["callee:004878ec:8"]]
+ 00abc644 ["INT_ADD", "register:40f0:8", ["const:abc644:8", "const:4:8"]]
+ 00abc644 ["CALL", null, ["callee:004878ec:8"]]
- 00a5e68c bytes f218e897
+ 00abc644 bytes aa2ce797
- 00a5e6c8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:10:8"]]
- 00a5e6c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a5e6c8 bytes c80a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b652a483bea84fb5224a85e86715ccb1"></a>

### [`00a5e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) → [`00abc6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abc6dc.md) FUN_00abc6dc

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0450.md)
- 新版 呼出元 1件 [`00abe1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md) · 呼出先 14件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00615c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615c90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.35% / 新版 86.35%

CFGの説明率　旧版 42.45% / 新版 32.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `store_condition` 9件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5e72c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5e728",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5e72c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5e730",
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
      "00abc6e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00abc6e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00abc6e8",
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

- 旧版 [`00a5e728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e728) · [`00a5e72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e72c) · [`00a5e730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md#insn-00a5e730)

~~~diff
- 00a5e728 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5e728 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5e728 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a5e728 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5e728 bytes fd7b05a9
- 00a5e72c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a5e72c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a5e72c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00a5e72c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5e72c bytes fc6f06a9
- 00a5e730 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a5e730 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a5e730 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00a5e730 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5e730 bytes fa6707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1851a3e46036cfad694daaa274315e5b"></a>

### [`00a5ed00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md) → [`00abccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md) FUN_00abccb8

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a5e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5e724.md) · 呼出先 5件 [`007cd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd2ac.md) [`007cd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd560.md) [`007d22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007d2/007d22d4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a085a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a08/00a085a8.md)
- 新版 呼出元 1件 [`00abc6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abc6dc.md) · 呼出先 5件 [`00800338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/00800338.md) [`008005ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008005ec.md) [`008056ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00805/008056ac.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a65bf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a65/00a65bf4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.25% / 新版 94.25%

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
      "site": "00abcd04",
      "value": [
        "leaf",
        "ram:8056ac:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a5ed4c",
      "value": [
        "leaf",
        "ram:7d22d4:8"
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
      "site": "00abcd1c",
      "value": [
        "leaf",
        "ram:a65bf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a5ed64",
      "value": [
        "leaf",
        "ram:a085a8:8"
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
      "00abcd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007d22d4"
      ]
    ],
    [
      "00abcd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a085a8"
      ]
    ]
  ],
  "added": [
    [
      "00abcd04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008056ac"
      ]
    ],
    [
      "00abcd1c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00a65bf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5ed4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed4c) · [`00a5ed64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed64) · [`00a5ed24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md#insn-00a5ed24)
- 新版 [`00abcd04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md#insn-00abcd04) · [`00abcd1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md#insn-00abcd1c) · [`00abccdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md#insn-00abccdc)

~~~diff
- 00a5ed4c ["INT_ADD", "register:40f0:8", ["const:a5ed4c:8", "const:4:8"]]
- 00a5ed4c ["CALL", null, ["ram:7d22d4:8"]]
+ 00abcd04 ["INT_ADD", "register:40f0:8", ["const:abcd04:8", "const:4:8"]]
+ 00abcd04 ["CALL", null, ["ram:8056ac:8"]]
- 00a5ed4c bytes 62cdf597
+ 00abcd04 bytes 6a22f597
- 00a5ed64 ["INT_ADD", "register:40f0:8", ["const:a5ed64:8", "const:4:8"]]
- 00a5ed64 ["CALL", null, ["ram:a085a8:8"]]
+ 00abcd1c ["INT_ADD", "register:40f0:8", ["const:abcd1c:8", "const:4:8"]]
+ 00abcd1c ["CALL", null, ["ram:a65bf4:8"]]
- 00a5ed64 bytes 11a6fe97
+ 00abcd1c bytes b6a3fe97
- 00a5ed24 ["INT_ADD", "register:40f0:8", ["const:a5ed24:8", "const:4:8"]]
- 00a5ed24 ["CALL", null, ["callee:00800338:8"]]
+ 00abccdc ["INT_ADD", "register:40f0:8", ["const:abccdc:8", "const:4:8"]]
+ 00abccdc ["CALL", null, ["callee:00800338:8"]]
- 00a5ed24 bytes 62b9f597
+ 00abccdc bytes 970df597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e1d8d2fff0a05bee3d8535c0e6c8e5a"></a>

### [`00a5f128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md) → [`00abd0e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd0e0.md) FUN_00abd0e0

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a60644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) [`00a63b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005f0450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f0/005f0450.md)
- 新版 呼出元 2件 [`00abe5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe5fc.md) [`00ac1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b44.md) · 呼出先 16件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0049f3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0049f/0049f3b0.md) [`00615c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/00615c90.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 95.35% / 新版 94.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5f314"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abd2cc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00abd124",
      "value": [
        "leaf",
        "ram:860548:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a5f16c",
      "value": [
        "leaf",
        "ram:82e5d0:8"
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
      "00abd124",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082e5d0"
      ]
    ],
    [
      "unmatched:00a5f314",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abd454"
      ]
    ],
    [
      "00abd314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007d22d4"
      ]
    ]
  ],
  "added": [
    [
      "00abd124",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00860548"
      ]
    ],
    [
      "00abd2cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abd454"
      ]
    ],
    [
      "00abd314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008056ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5f16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f16c) · [`00a5f314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f314) · [`00a5f35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f128.md#insn-00a5f35c)
- 新版 [`00abd124`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd0e0.md#insn-00abd124) · [`00abd314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd0e0.md#insn-00abd314)

~~~diff
- 00a5f16c ["INT_ADD", "register:40f0:8", ["const:a5f16c:8", "const:4:8"]]
- 00a5f16c ["CALL", null, ["ram:82e5d0:8"]]
+ 00abd124 ["INT_ADD", "register:40f0:8", ["const:abd124:8", "const:4:8"]]
+ 00abd124 ["CALL", null, ["ram:860548:8"]]
- 00a5f16c bytes 193df797
+ 00abd124 bytes 098df697
- 00a5f314 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a5f314 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00a5f314 ["CBRANCH", null, ["local:b52:8", "tmp:1:1"]]
- 00a5f314 bytes 490c0054
- 00a5f35c ["INT_ADD", "register:40f0:8", ["const:a5f35c:8", "const:4:8"]]
- 00a5f35c ["CALL", null, ["ram:7d22d4:8"]]
+ 00abd314 ["INT_ADD", "register:40f0:8", ["const:abd314:8", "const:4:8"]]
+ 00abd314 ["CALL", null, ["ram:8056ac:8"]]
- 00a5f35c bytes decbf597
+ 00abd314 bytes e620f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5534df28c64d78ba3efeb30e33d9faf"></a>

### [`00a5f544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md) → [`00abd4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd4fc.md) FUN_00abd4fc

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0080d/0080dd1c.md) · 呼出先 3件 [`0044b8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8ec.md) [`0044c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c020.md) [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md)
- 新版 呼出元 1件 [`0083f844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0083f/0083f844.md) · 呼出先 3件 [`0046e784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e784.md) [`0046eeb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046eeb8.md) [`005c175c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c1/005c175c.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5f5b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00abd568"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a5f5a0",
      "incomplete_value": true,
      "site": "00a5f5b4",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a5f5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md#insn-00a5f5b0) · [`00a5f5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md#insn-00a5f5b4)
- 新版 [`00abd56c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd4fc.md#insn-00abd56c) · [`00abd568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd4fc.md#insn-00abd568)

~~~diff
- 00a5f5b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00a5f5b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a5f5b0 bytes 681e00f9
- 00a5f5b4 ["INT_ADD", "register:40f0:8", ["const:a5f5b4:8", "const:4:8"]]
- 00a5f5b4 ["CALL", null, ["callee:005c175c:8"]]
+ 00abd56c ["INT_ADD", "register:40f0:8", ["const:abd56c:8", "const:4:8"]]
+ 00abd56c ["CALL", null, ["callee:005c175c:8"]]
- 00a5f5b4 bytes def6ec97
+ 00abd56c bytes 7c10ec97
+ 00abd568 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
+ 00abd568 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00abd568 bytes 681e00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8df8a7ad7e7873f2e1cd70545f466152"></a>

### [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) → [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) FUN_00abd6f0

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 25件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 25件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`004883f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/004883f4.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.25% / 新版 77.25%

CFGの説明率　旧版 55.00% / 新版 48.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 2件, `unresolved_branch_alignment` 12件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 30件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5f738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5f738"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a5f73c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a5f738",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5f73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a5f740",
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
      "00abd6f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00abd6f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00abd6f8",
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

- 旧版 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md#insn-00a5f738) · [`00a5f73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md#insn-00a5f73c) · [`00a5f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md#insn-00a5f740)

~~~diff
- 00a5f738 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a5f738 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a5f738 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00a5f738 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a5f738 bytes fd7bbaa9
- 00a5f73c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a5f73c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a5f73c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a5f73c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5f73c bytes fc6f01a9
- 00a5f740 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a5f740 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a5f740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a5f740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a5f740 bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2fb6f9bf622d3c0f37c1f6e5c144038"></a>

### [`00a5fea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md) → [`00abde5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abde5c.md) FUN_00abde5c

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009c9134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009c9/009c9134.md) · 呼出先 11件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045d240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d240.md) [`0045d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d2a0.md)
- 新版 呼出元 1件 [`00a26020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a26/00a26020.md) · 呼出先 11件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`004800d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/004800d8.md) [`00480138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480138.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 71.79% / 新版 62.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60030"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abdfe8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00abdee0",
      "incomplete_value": true,
      "site": "00abdee4",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00a5ff28",
      "incomplete_value": true,
      "site": "00a5ff2c",
      "value": [
        "INT_SUB",
        "8",
        [
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
                "const:50:8"
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
      "unmatched:00a60030",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abdfc4"
      ]
    ]
  ],
  "added": [
    [
      "00abdfe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abdfc4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a5ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a5ff2c) · [`00a60030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a60030) · [`00a600ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5fea4.md#insn-00a600ec)
- 新版 [`00abdee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abde5c.md#insn-00abdee4)

~~~diff
- 00a5ff2c ["INT_ADD", "register:40f0:8", ["const:a5ff2c:8", "const:4:8"]]
- 00a5ff2c ["CALL", null, ["callee:005c175c:8"]]
+ 00abdee4 ["INT_ADD", "register:40f0:8", ["const:abdee4:8", "const:4:8"]]
+ 00abdee4 ["CALL", null, ["callee:005c175c:8"]]
- 00a5ff2c bytes 80f4ec97
+ 00abdee4 bytes 1e0eec97
- 00a60030 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a60030 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00a60030 bytes e3feff54
- 00a600ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a600ec ["RETURN", null, ["register:0:8"]]
- 00a600ec bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f3d43e3cde7a89736ac3b06b7cc56b9"></a>

### [`00a600fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md) → [`00abe0b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe0b4.md) FUN_00abe0b4

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009ce214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009ce/009ce214.md) · 呼出先 4件 [`0045dc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dc60.md) [`0045dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dcb8.md) [`0045dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045dd10.md) [`0045de70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045de70.md)
- 新版 呼出元 1件 [`00a2b0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a2b/00a2b0f0.md) · 呼出先 4件 [`00480af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480af8.md) [`00480b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480b50.md) [`00480ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480ba8.md) [`00480d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00480/00480d08.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 88.24% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a6011c",
      "incomplete_value": true,
      "site": "00a60124",
      "value": [
        "live",
        "register:4008:8"
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
      "definition_site": "00a60138",
      "incomplete_value": true,
      "site": "00a6013c",
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
      "definition_site": "00a60134",
      "incomplete_value": true,
      "site": "00a6013c",
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
    "ordinal": 2,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a60124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a60124) · [`00a6013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a6013c) · [`00a60130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a600fc.md#insn-00a60130)
- 新版 [`00abe0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe0b4.md#insn-00abe0dc) · [`00abe0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe0b4.md#insn-00abe0f4) · [`00abe0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe0b4.md#insn-00abe0e8)

~~~diff
- 00a60124 ["INT_ADD", "register:40f0:8", ["const:a60124:8", "const:4:8"]]
- 00a60124 ["CALL", null, ["callee:00480ba8:8"]]
+ 00abe0dc ["INT_ADD", "register:40f0:8", ["const:abe0dc:8", "const:4:8"]]
+ 00abe0dc ["CALL", null, ["callee:00480ba8:8"]]
- 00a60124 bytes fbf6e797
+ 00abe0dc bytes b30ae797
- 00a6013c ["INT_ADD", "register:40f0:8", ["const:a6013c:8", "const:4:8"]]
- 00a6013c ["CALL", null, ["callee:00480ba8:8"]]
+ 00abe0f4 ["INT_ADD", "register:40f0:8", ["const:abe0f4:8", "const:4:8"]]
+ 00abe0f4 ["CALL", null, ["callee:00480ba8:8"]]
- 00a6013c bytes f5f6e797
+ 00abe0f4 bytes ad0ae797
- 00a60130 ["INT_ADD", "register:40f0:8", ["const:a60130:8", "const:4:8"]]
- 00a60130 ["CALL", null, ["callee:00480ba8:8"]]
+ 00abe0e8 ["INT_ADD", "register:40f0:8", ["const:abe0e8:8", "const:4:8"]]
+ 00abe0e8 ["CALL", null, ["callee:00480ba8:8"]]
- 00a60130 bytes f8f6e797
+ 00abe0e8 bytes b00ae797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b8c2be8ba7ea53585d62e8b23dfbc50"></a>

### [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) → [`00abe1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md) FUN_00abe1c8

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`005e02b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e0/005e02b0.md) [`005e1a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005e1/005e1a5c.md) [`005ef020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ef/005ef020.md) [`00629194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00629/00629194.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a45c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a45/00a45c24.md)
- 新版 呼出元 8件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00605214`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00605/00605214.md) [`00606aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00606/00606aa4.md) [`006144ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00614/006144ec.md) [`0064ec78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0064e/0064ec78.md) · 呼出先 13件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00aa3c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aa3/00aa3c28.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.75% / 新版 96.75%

CFGの説明率　旧版 92.45% / 新版 90.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a602bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abe274"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00abe1fc",
      "value": [
        "leaf",
        "ram:b3dfe8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a60244",
      "value": [
        "leaf",
        "ram:ade610:8"
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
      "00abe1fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00ade610"
      ]
    ],
    [
      "unmatched:00a602bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe23c"
      ]
    ]
  ],
  "added": [
    [
      "00abe1fc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b3dfe8"
      ]
    ],
    [
      "00abe274",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe23c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a60244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md#insn-00a60244) · [`00a602bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md#insn-00a602bc)
- 新版 [`00abe1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md#insn-00abe1fc) · [`00abe274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md#insn-00abe274)

~~~diff
- 00a60244 ["INT_ADD", "register:40f0:8", ["const:a60244:8", "const:4:8"]]
- 00a60244 ["CALL", null, ["ram:ade610:8"]]
+ 00abe1fc ["INT_ADD", "register:40f0:8", ["const:abe1fc:8", "const:4:8"]]
+ 00abe1fc ["CALL", null, ["ram:b3dfe8:8"]]
- 00a60244 bytes f3f80194
+ 00abe1fc bytes 7bff0194
- 00a602bc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a602bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00a602bc bytes 41feff54
+ 00abe274 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00abe274 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00abe274 bytes 41feff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc4c02aef9539e8c12d8ac8e90a05cfa"></a>

### [`00a60478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md) → [`00abe430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe430.md) FUN_00abe430

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a60210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60210.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00abe1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe1c8.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 73.91% / 新版 65.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a604dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00abe494"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00a604dc"
      ],
      [
        "FALL_THROUGH",
        "00abe494"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00abe498",
      "value": [
        "live",
        "register:102:1"
      ]
    },
    "old": {
      "definition_site": "00a604d8",
      "incomplete_value": true,
      "site": "00a604e0",
      "value": [
        "INT_LESSEQUAL",
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
            "live",
            "register:40c0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a604dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe4e0"
      ]
    ]
  ],
  "added": [
    [
      "00abe494",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abe4e0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a604dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md#insn-00a604dc) · [`00a604b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60478.md#insn-00a604b0)
- 新版 [`00abe494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe430.md#insn-00abe494) · [`00abe468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe430.md#insn-00abe468)

~~~diff
- 00a604dc ["CBRANCH", null, ["local:b7:8", "register:102:1"]]
- 00a604dc bytes 62020054
+ 00abe494 ["CBRANCH", null, ["local:b9:8", "register:102:1"]]
+ 00abe494 bytes 62020054
- 00a604b0 ["INT_ADD", "register:40f0:8", ["const:a604b0:8", "const:4:8"]]
- 00a604b0 ["CALL", null, ["callee:00c58050:8"]]
+ 00abe468 ["INT_ADD", "register:40f0:8", ["const:abe468:8", "const:4:8"]]
+ 00abe468 ["CALL", null, ["callee:00c58050:8"]]
- 00a604b0 bytes 54ec0594
+ 00abe468 bytes fa660694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebe88b7a19c91bb9471d2eb28826ccfd"></a>

### [`00a60644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) → [`00abe5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe5fc.md) FUN_00abe5fc

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a622a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md) [`00a6510c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6510c.md) · 呼出先 28件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md)
- 新版 呼出元 2件 [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) [`00ac30c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac30c4.md) · 呼出先 28件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.37% / 新版 64.37%

CFGの説明率　旧版 27.02% / 新版 38.84%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 20件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 30件, `unresolved_call_alignment` 25件, `unresolved_store_alignment` 65件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a60648"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6064c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a60648",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a6064c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a60650",
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
      "00abe600",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00abe604",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00abe608",
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

- 旧版 [`00a60648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md#insn-00a60648) · [`00a6064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md#insn-00a6064c) · [`00a60650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md#insn-00a60650)

~~~diff
- 00a60648 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a60648 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a60648 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00a60648 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a60648 bytes fd7b11a9
- 00a6064c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a6064c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a6064c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 00a6064c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a6064c bytes fc6f12a9
- 00a60650 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a60650 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a60650 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:130:8"]]
- 00a60650 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a60650 bytes fa6713a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8c8bc47a06be7560003ecb9c4482c5"></a>

### [`00a615d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a615d0.md) → [`00abf588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf588.md) FUN_00abf588

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044c1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c1dc.md) [`0044d1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1ec.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 20件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046e730`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e730.md) [`0046ed4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046ed4c.md) [`0046f074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f074.md) [`00470084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470084.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 50.88% / 新版 43.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a616f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00abf738",
      "incomplete_value": true,
      "site": "00abf74c",
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
                "const:ea9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a61780",
      "incomplete_value": true,
      "site": "00a61794",
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
                "const:a8b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a61830"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00abf5b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "unmatched:00a6169c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf850"
      ]
    ],
    [
      "unmatched:00a616c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf694"
      ]
    ]
  ],
  "added": [
    [
      "00abf5b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00abf654",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf850"
      ]
    ],
    [
      "00abf678",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00abf694"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a61600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a615d0.md#insn-00a61600) · [`00a61618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a615d0.md#insn-00a61618) · [`00a6169c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a615d0.md#insn-00a6169c)
- 新版 [`00abf5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf588.md#insn-00abf5b8) · [`00abf5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf588.md#insn-00abf5d0)

~~~diff
- 00a61600 ["INT_ADD", "register:40f0:8", ["const:a61600:8", "const:4:8"]]
- 00a61600 ["CALL", null, ["ram:469e20:8"]]
+ 00abf5b8 ["INT_ADD", "register:40f0:8", ["const:abf5b8:8", "const:4:8"]]
+ 00abf5b8 ["CALL", null, ["ram:48ccb8:8"]]
- 00a61600 bytes 0822e897
+ 00abf5b8 bytes c035e797
- 00a61618 ["INT_ADD", "register:40f0:8", ["const:a61618:8", "const:4:8"]]
- 00a61618 ["CALL", null, ["callee:0082df10:8"]]
+ 00abf5d0 ["INT_ADD", "register:40f0:8", ["const:abf5d0:8", "const:4:8"]]
+ 00abf5d0 ["CALL", null, ["callee:0082df10:8"]]
- 00a61618 bytes 395df697
+ 00abf5d0 bytes 50baf597
- 00a6169c ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00a6169c ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 00a6169c bytes ea0f00b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2a851c28333486cb9f80129c19463c7"></a>

### [`00a618f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a618f4.md) → [`00abf8ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf8ac.md) FUN_00abf8ac

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a615d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a615d0.md) [`00adccd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccd8.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md)
- 新版 呼出元 2件 [`00abf588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf588.md) [`00b3c6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c6b0.md) · 呼出先 18件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0046e930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e930.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 49.61% / 新版 49.61%

CFGの説明率　旧版 15.13% / 新版 11.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 3件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 30件, `unresolved_store_alignment` 58件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a61950"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a61960"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a61964"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00abf8ec",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00a6194c",
      "READ",
      [
        "storage",
        "0029b8d5",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a61950",
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
      "00abf8ec",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00abf904",
      "READ",
      [
        "storage",
        "002ab964",
        null,
        "string"
      ]
    ],
    [
      "00abf908",
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

- 旧版 [`00a61950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a618f4.md#insn-00a61950) · [`00a61960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a618f4.md#insn-00a61960) · [`00a61964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a61/00a618f4.md#insn-00a61964)

~~~diff
- 00a61950 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a61950 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe0:8"]]
- 00a61950 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a61950 bytes a9031e38
- 00a61960 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a61960 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00a61960 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a61960 bytes a8831c38
- 00a61964 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffe1:8"]]
- 00a61964 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a61964 bytes a0139e3c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c26fbf3845f4a2c57662e221cc2eebf1"></a>

### [`00a621f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a621f0.md) → [`00ac01a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac01a8.md) FUN_00ac01a8

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c80c.md) [`0044d1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d1dc.md)
- 新版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 9件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`0046bd14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046b/0046bd14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046f6a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046f/0046f6a4.md) [`00470074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470074.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac01b8",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a62200",
      "value": [
        "leaf",
        "ram:469e20:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ac01f4",
      "incomplete_value": true,
      "site": "00ac01f8",
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
    "old": {
      "definition_site": "00a6223c",
      "incomplete_value": true,
      "site": "00a62240",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ac01e0",
      "incomplete_value": false,
      "site": "00ac01f8",
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
      "definition_site": "00a62228",
      "incomplete_value": false,
      "site": "00a62240",
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
      "00ac01b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "00ac01e0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00ac01e4",
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
      "00ac01b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00ac01e0",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00ac01e4",
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

- 旧版 [`00a62200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a621f0.md#insn-00a62200) · [`00a62240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a621f0.md#insn-00a62240) · [`00a6226c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a621f0.md#insn-00a6226c)
- 新版 [`00ac01b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac01a8.md#insn-00ac01b8) · [`00ac01f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac01a8.md#insn-00ac01f8) · [`00ac0224`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac01a8.md#insn-00ac0224)

~~~diff
- 00a62200 ["INT_ADD", "register:40f0:8", ["const:a62200:8", "const:4:8"]]
- 00a62200 ["CALL", null, ["ram:469e20:8"]]
+ 00ac01b8 ["INT_ADD", "register:40f0:8", ["const:ac01b8:8", "const:4:8"]]
+ 00ac01b8 ["CALL", null, ["ram:48ccb8:8"]]
- 00a62200 bytes 081fe897
+ 00ac01b8 bytes c032e797
- 00a62240 ["INT_ADD", "register:40f0:8", ["const:a62240:8", "const:4:8"]]
- 00a62240 ["CALL", null, ["callee:00c58210:8"]]
+ 00ac01f8 ["INT_ADD", "register:40f0:8", ["const:ac01f8:8", "const:4:8"]]
+ 00ac01f8 ["CALL", null, ["callee:00c58210:8"]]
- 00a62240 bytes 60e50594
+ 00ac01f8 bytes 06600694
- 00a6226c ["INT_ADD", "register:40f0:8", ["const:a6226c:8", "const:4:8"]]
- 00a6226c ["CALL", null, ["ram:449aec:8"]]
+ 00ac0224 ["INT_ADD", "register:40f0:8", ["const:ac0224:8", "const:4:8"]]
+ 00ac0224 ["CALL", null, ["ram:46c984:8"]]
- 00a6226c bytes 209ee797
+ 00ac0224 bytes d8b1e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d73d05d3c3f9d08a33eeac2ecec0c2c2"></a>

### [`00a622a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md) → [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) FUN_00ac0258

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 32件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) [`009e9808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009e9/009e9808.md)
- 新版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 32件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008b6fa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6fa8.md) [`00a46704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a46704.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.33% / 新版 72.33%

CFGの説明率　旧版 30.43% / 新版 27.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a622dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a622e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a622f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a622d4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a622d8",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00a622dc",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ac028c",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00ac0290",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "00ac0294",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a622dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md#insn-00a622dc) · [`00a622e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md#insn-00a622e0) · [`00a622f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md#insn-00a622f8)

~~~diff
- 00a622dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
- 00a622dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00a622dc bytes 095505f9
- 00a622e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
- 00a622e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00a622e0 bytes aa5e05f9
- 00a622f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ab8:8"]]
- 00a622f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00a622f8 bytes b45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-501d3553c4d4c4d65b468c639eebfb83"></a>

### [`00a62e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e1c.md) → [`00ac0dd4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dd4.md) FUN_00ac0dd4

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00ac0de4",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a62e2c",
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
      "definition_site": "00ac0de0",
      "incomplete_value": false,
      "site": "00ac0de4",
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
      "definition_site": "00a62e28",
      "incomplete_value": false,
      "site": "00a62e2c",
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
      "00ac0de0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00ac0de4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00ac0de0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00ac0de4",
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

- 旧版 [`00a62e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e1c.md#insn-00a62e2c) · [`00a62e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e1c.md#insn-00a62e24) · [`00a62e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e1c.md#insn-00a62e28)
- 新版 [`00ac0de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dd4.md#insn-00ac0de4) · [`00ac0ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dd4.md#insn-00ac0ddc) · [`00ac0de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dd4.md#insn-00ac0de0)

~~~diff
- 00a62e2c ["INT_ADD", "register:40f0:8", ["const:a62e2c:8", "const:4:8"]]
- 00a62e2c ["CALL", null, ["ram:418c38:8"]]
+ 00ac0de4 ["INT_ADD", "register:40f0:8", ["const:ac0de4:8", "const:4:8"]]
+ 00ac0de4 ["CALL", null, ["ram:43b738:8"]]
- 00a62e2c bytes 83d7e697
+ 00ac0de4 bytes 55eae597
- 00a62e24 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00ac0ddc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a62e24 bytes 20c2ffb0
+ 00ac0ddc bytes a0bffff0
- 00a62e28 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a62e28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ac0de0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00ac0de0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac0de0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac0de0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a62e28 bytes 00740e91
+ 00ac0de0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6330304c55c809b965e9f39fabe40c00"></a>

### [`00a62e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e44.md) → [`00ac0dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dfc.md) FUN_00ac0dfc

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a5f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f738.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00abd6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abd/00abd6f0.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)

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
      "site": "00ac0e0c",
      "value": [
        "leaf",
        "ram:43b738:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a62e54",
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
      "definition_site": "00ac0e08",
      "incomplete_value": false,
      "site": "00ac0e0c",
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
      "definition_site": "00a62e50",
      "incomplete_value": false,
      "site": "00a62e54",
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
      "00ac0e08",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00ac0e0c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00418c38"
      ]
    ]
  ],
  "added": [
    [
      "00ac0e08",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00ac0e0c",
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

- 旧版 [`00a62e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e44.md#insn-00a62e54) · [`00a62e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e44.md#insn-00a62e4c) · [`00a62e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e44.md#insn-00a62e50)
- 新版 [`00ac0e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dfc.md#insn-00ac0e0c) · [`00ac0e04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dfc.md#insn-00ac0e04) · [`00ac0e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0dfc.md#insn-00ac0e08)

~~~diff
- 00a62e54 ["INT_ADD", "register:40f0:8", ["const:a62e54:8", "const:4:8"]]
- 00a62e54 ["CALL", null, ["ram:418c38:8"]]
+ 00ac0e0c ["INT_ADD", "register:40f0:8", ["const:ac0e0c:8", "const:4:8"]]
+ 00ac0e0c ["CALL", null, ["ram:43b738:8"]]
- 00a62e54 bytes 79d7e697
+ 00ac0e0c bytes 4beae597
- 00a62e4c ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00ac0e04 ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a62e4c bytes 20c2ffb0
+ 00ac0e04 bytes a0bffff0
- 00a62e50 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a62e50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a62e50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ac0e08 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00ac0e08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac0e08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac0e08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a62e50 bytes 00740e91
+ 00ac0e08 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6b941a140db9aac1c6a2798e226ff72"></a>

### [`00a631d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md) → [`00ac118c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md) FUN_00ac118c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) · 呼出先 1件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md)
- 新版 呼出元 1件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) · 呼出先 1件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 96.88% / 新版 95.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a63244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md#insn-00a63244) · [`00a63270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md#insn-00a63270) · [`00a632a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a631d4.md#insn-00a632a8)
- 新版 [`00ac11fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac11fc) · [`00ac1228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac1228) · [`00ac1260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac118c.md#insn-00ac1260)

~~~diff
- 00a63244 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a63244 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00a63244 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00a63244 ["CBRANCH", null, ["local:b19:8", "tmp:2:1"]]
+ 00ac11fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ac11fc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
+ 00ac11fc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
+ 00ac11fc ["CBRANCH", null, ["local:b20:8", "tmp:2:1"]]
- 00a63244 bytes cc050054
+ 00ac11fc bytes cc050054
- 00a63270 ["BRANCH", null, ["local:b12:8"]]
+ 00ac1228 ["BRANCH", null, ["local:b13:8"]]
- 00a63270 bytes 08000014
+ 00ac1228 bytes 08000014
- 00a632a8 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00a632a8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00ac1260 ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ac1260 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a632a8 bytes 6afeff54
+ 00ac1260 bytes 6afeff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8161f9407183efb7e13ca5309db34730"></a>

### [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md) → [`00ac1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1464.md) FUN_00ac1464

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00a62e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a62e58.md) [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md) · 呼出先 1件 [`00a634ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md)
- 新版 呼出元 2件 [`00ac0e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0e10.md) [`00ac1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1464.md) · 呼出先 1件 [`00ac1464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1464.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 84.29% / 新版 79.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 4件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a634c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a634c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a634c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a634c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a634c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a63590",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac16c8"
      ]
    ]
  ],
  "added": [
    [
      "00ac1478",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac147c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac1548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac16c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a634c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md#insn-00a634c0) · [`00a634c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md#insn-00a634c4) · [`00a63590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a634ac.md#insn-00a63590)

~~~diff
- 00a634c0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a634c0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a634c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a634c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a634c0 bytes f65704a9
- 00a634c4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a634c4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a634c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00a634c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a634c4 bytes f44f05a9
- 00a63590 ["CBRANCH", null, ["local:b32:8", "register:101:1"]]
- 00a63590 bytes 000c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1eda6c2caa13da97099117fb369ccbaf"></a>

### [`00a63b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b1c.md) → [`00ac1ad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1ad4.md) FUN_00ac1ad4

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a60644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a60/00a60644.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`00abe5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abe/00abe5fc.md) · 呼出先 1件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md)

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
      "site": "00ac1ae4",
      "value": [
        "leaf",
        "ram:4428f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a63b2c",
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
      "definition_site": "00ac1ae0",
      "incomplete_value": false,
      "site": "00ac1ae4",
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
      "definition_site": "00a63b28",
      "incomplete_value": false,
      "site": "00a63b2c",
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
      "00ac1ae0",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ],
    [
      "00ac1ae4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0041fdf0"
      ]
    ]
  ],
  "added": [
    [
      "00ac1ae0",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ],
    [
      "00ac1ae4",
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

- 旧版 [`00a63b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b1c.md#insn-00a63b2c) · [`00a63b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b1c.md#insn-00a63b24) · [`00a63b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b1c.md#insn-00a63b28)
- 新版 [`00ac1ae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1ad4.md#insn-00ac1ae4) · [`00ac1adc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1ad4.md#insn-00ac1adc) · [`00ac1ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1ad4.md#insn-00ac1ae0)

~~~diff
- 00a63b2c ["INT_ADD", "register:40f0:8", ["const:a63b2c:8", "const:4:8"]]
- 00a63b2c ["CALL", null, ["ram:41fdf0:8"]]
+ 00ac1ae4 ["INT_ADD", "register:40f0:8", ["const:ac1ae4:8", "const:4:8"]]
+ 00ac1ae4 ["CALL", null, ["ram:4428f0:8"]]
- 00a63b2c bytes b1f0e697
+ 00ac1ae4 bytes 8303e697
- 00a63b24 ["COPY", "register:4000:8", ["const:2a7000:8"]]
+ 00ac1adc ["COPY", "register:4000:8", ["const:2b7000:8"]]
- 00a63b24 bytes 20c2ff90
+ 00ac1adc bytes a0bfffd0
- 00a63b28 ["COPY", "tmp:0:8", ["const:39d:8"]]
- 00a63b28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00a63b28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00a63b28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ac1ae0 ["COPY", "tmp:0:8", ["const:f0c:8"]]
+ 00ac1ae0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac1ae0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ac1ae0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00a63b28 bytes 00740e91
+ 00ac1ae0 bytes 00303c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ce31d393e0fdf4a001cbc773ae98c9e"></a>

### [`00a63b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b6c.md) → [`00ac1b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md) FUN_00ac1b24

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac1b28",
      "incomplete_value": false,
      "site": "00ac1b2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a63b70",
      "incomplete_value": false,
      "site": "00a63b74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      "00ac1b2c",
      "DATA",
      [
        "storage",
        "00c0d900",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac1b2c",
      "DATA",
      [
        "storage",
        "00c8cf20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a63b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b6c.md#insn-00a63b6c) · [`00a63b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b6c.md#insn-00a63b70)
- 新版 [`00ac1b24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md#insn-00ac1b24) · [`00ac1b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b24.md#insn-00ac1b28)

~~~diff
- 00a63b6c ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac1b24 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a63b6c bytes 480d00d0
+ 00ac1b24 bytes 480e00f0
- 00a63b70 ["COPY", "tmp:0:8", ["const:900:8"]]
- 00a63b70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a63b70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac1b28 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00ac1b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac1b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac1b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a63b70 bytes 08012491
+ 00ac1b28 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1f0b18797683b4ac2ecdc64c3adaea"></a>

### [`00a63b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md) → [`00ac1b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac1/00ac1b44.md) FUN_00ac1b44

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e7e8.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.10% / 新版 79.10%

CFGの説明率　旧版 62.11% / 新版 59.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 2件, `store_destination` 1件, `store_value` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a63b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a63b90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a63b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a63b90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a63b94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a63b98",
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
      "00ac1b48",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ac1b4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac1b50",
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

- 旧版 [`00a63b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md#insn-00a63b90) · [`00a63b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md#insn-00a63b94) · [`00a63b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a63/00a63b8c.md#insn-00a63b98)

~~~diff
- 00a63b90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a63b90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a63b90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00a63b90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a63b90 bytes fd7b0ba9
- 00a63b94 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00a63b94 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00a63b94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00a63b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a63b94 bytes f6570ca9
- 00a63b98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a63b98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a63b98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00a63b98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a63b98 bytes f44f0da9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-663b93ed3851e97074df0904cc33fd0e"></a>

### [`00a64084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64084.md) → [`00ac203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md) FUN_00ac203c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac2050",
      "incomplete_value": false,
      "site": "00ac2054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64098",
      "incomplete_value": false,
      "site": "00a6409c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00ac2054",
      "DATA",
      [
        "storage",
        "00c0d970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2054",
      "DATA",
      [
        "storage",
        "00c8cf90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64084.md#insn-00a64090) · [`00a64094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64084.md#insn-00a64094) · [`00a64098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64084.md#insn-00a64098)
- 新版 [`00ac2048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac2048) · [`00ac204c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac204c) · [`00ac2050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac2050)

~~~diff
- 00a64090 ["INT_ADD", "register:40f0:8", ["const:a64090:8", "const:4:8"]]
- 00a64090 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac2048 ["INT_ADD", "register:40f0:8", ["const:ac2048:8", "const:4:8"]]
+ 00ac2048 ["CALL", null, ["callee:00c57a90:8"]]
- 00a64090 bytes ecdb0594
+ 00ac2048 bytes 92560694
- 00a64094 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac204c ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a64094 bytes 480d00b0
+ 00ac204c bytes 480e00d0
- 00a64098 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00a64098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac2050 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00ac2050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64098 bytes 08c12591
+ 00ac2050 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca2baf441eec4ad3cdaca88c1d45c3d9"></a>

### [`00a640a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640a8.md) → [`00ac2060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md) FUN_00ac2060

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac2064",
      "incomplete_value": false,
      "site": "00ac2068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8c000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a640ac",
      "incomplete_value": false,
      "site": "00a640b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00ac2068",
      "DATA",
      [
        "storage",
        "00c0d970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2068",
      "DATA",
      [
        "storage",
        "00c8cf90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a640a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640a8.md#insn-00a640a8) · [`00a640ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640a8.md#insn-00a640ac)
- 新版 [`00ac2060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md#insn-00ac2060) · [`00ac2064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md#insn-00ac2064)

~~~diff
- 00a640a8 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac2060 ["COPY", "register:4040:8", ["const:c8c000:8"]]
- 00a640a8 bytes 480d00b0
+ 00ac2060 bytes 480e00d0
- 00a640ac ["COPY", "tmp:0:8", ["const:970:8"]]
- 00a640ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a640ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a640ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac2064 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00ac2064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a640ac bytes 08c12591
+ 00ac2064 bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e1356969ce22f39b8dc8f69835284b5"></a>

### [`00a640c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md) → [`00ac2078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md) FUN_00ac2078

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "site": "00ac2094",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a640dc",
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
      "00ac2094",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ]
  ],
  "added": [
    [
      "00ac2094",
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

- 旧版 [`00a640dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md#insn-00a640dc) · [`00a640e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a640c0.md#insn-00a640e8)
- 新版 [`00ac2094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md#insn-00ac2094) · [`00ac20a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md#insn-00ac20a0)

~~~diff
- 00a640dc ["INT_ADD", "register:40f0:8", ["const:a640dc:8", "const:4:8"]]
- 00a640dc ["CALL", null, ["ram:457e1c:8"]]
+ 00ac2094 ["INT_ADD", "register:40f0:8", ["const:ac2094:8", "const:4:8"]]
+ 00ac2094 ["CALL", null, ["ram:47acb4:8"]]
- 00a640dc bytes 50cfe797
+ 00ac2094 bytes 08e3e697
- 00a640e8 ["INT_ADD", "register:40f0:8", ["const:a640e8:8", "const:4:8"]]
- 00a640e8 ["CALL", null, ["callee:0047cd94:8"]]
+ 00ac20a0 ["INT_ADD", "register:40f0:8", ["const:ac20a0:8", "const:4:8"]]
+ 00ac20a0 ["CALL", null, ["callee:0047cd94:8"]]
- 00a640e8 bytes 85d7e797
+ 00ac20a0 bytes 3debe697
~~~


<a id="compare-9f157668ff456ee8f8d1cd795b553f72"></a>

### [`00a64128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64128.md) → [`00ac20e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md) FUN_00ac20e0

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a622a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md) · 呼出先 11件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00830c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/00830c98.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 11件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) [`00862c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00862/00862c10.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 26.24% / 新版 26.24%

CFGの説明率　旧版 6.76% / 新版 6.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 66件, `unresolved_call_alignment` 72件, `unresolved_store_alignment` 120件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64168"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a641c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a641c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a64168",
      "DATA",
      [
        "storage",
        "00c0da00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a641b4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00a641b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2a7c"
      ]
    ]
  ],
  "added": [
    [
      "00ac2120",
      "DATA",
      [
        "storage",
        "00c8d020",
        null,
        "pointer"
      ]
    ],
    [
      "00ac216c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "00ac2170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2a7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64128.md#insn-00a64168) · [`00a641c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64128.md#insn-00a641c4) · [`00a641c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64128.md#insn-00a641c8)

~~~diff
- 00a64168 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00a64168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a64168 bytes 680200f9
- 00a641c4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00a641c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00a641c4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 00a641c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00a641c4 bytes ffaf0039
- 00a641c8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00a641c8 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 00a641c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00a641c8 bytes e8830039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f138498bbfde53b915131ed76919589b"></a>

### [`00a64dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md) → [`00ac2da4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2da4.md) FUN_00ac2da4

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a64e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e00) · [`00a64e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e08) · [`00a64e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64dec.md#insn-00a64e10)
- 新版 [`00ac2db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2da4.md#insn-00ac2db8) · [`00ac2dc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2da4.md#insn-00ac2dc0) · [`00ac2dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2da4.md#insn-00ac2dc8)

~~~diff
- 00a64e00 ["INT_ADD", "register:40f0:8", ["const:a64e00:8", "const:4:8"]]
- 00a64e00 ["CALL", null, ["callee:0078dc6c:8"]]
+ 00ac2db8 ["INT_ADD", "register:40f0:8", ["const:ac2db8:8", "const:4:8"]]
+ 00ac2db8 ["CALL", null, ["callee:0078dc6c:8"]]
- 00a64e00 bytes 66faf397
+ 00ac2db8 bytes ad2bf397
- 00a64e08 ["INT_ADD", "register:40f0:8", ["const:a64e08:8", "const:4:8"]]
- 00a64e08 ["CALL", null, ["callee:0078dc6c:8"]]
+ 00ac2dc0 ["INT_ADD", "register:40f0:8", ["const:ac2dc0:8", "const:4:8"]]
+ 00ac2dc0 ["CALL", null, ["callee:0078dc6c:8"]]
- 00a64e08 bytes 64faf397
+ 00ac2dc0 bytes ab2bf397
- 00a64e10 ["INT_ADD", "register:40f0:8", ["const:a64e10:8", "const:4:8"]]
- 00a64e10 ["CALL", null, ["callee:0078dc6c:8"]]
+ 00ac2dc8 ["INT_ADD", "register:40f0:8", ["const:ac2dc8:8", "const:4:8"]]
+ 00ac2dc8 ["CALL", null, ["callee:0078dc6c:8"]]
- 00a64e10 bytes 62faf397
+ 00ac2dc8 bytes a92bf397
~~~


<a id="compare-ed7e5e8221d67c2463971176f39e4093"></a>

### [`00a64e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md) → [`00ac2ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md) FUN_00ac2ddc

採用 · 移動量 `+0x5dfb8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a64f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64f9c.md) · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00763798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00763/00763798.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`00ac2f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f54.md) · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 34.38% / 新版 35.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64e40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a64f5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac2df8"
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
      "unmatched:00a64e40",
      "DATA",
      [
        "storage",
        "00c0da00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00a64e54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2e28"
      ]
    ],
    [
      "unmatched:00a64f14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2ee8"
      ]
    ]
  ],
  "added": [
    [
      "00ac2df8",
      "DATA",
      [
        "storage",
        "00c8d020",
        null,
        "pointer"
      ]
    ],
    [
      "00ac2e0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2e28"
      ]
    ],
    [
      "00ac2ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2ee8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md#insn-00a64e40) · [`00a64e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md#insn-00a64e54) · [`00a64e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64e24.md#insn-00a64e6c)
- 新版 [`00ac2e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md#insn-00ac2e24)

~~~diff
- 00a64e40 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00a64e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a64e40 bytes 080000f9
- 00a64e54 ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00a64e54 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00a64e54 bytes e00000b5
- 00a64e6c ["INT_ADD", "register:40f0:8", ["const:a64e6c:8", "const:4:8"]]
- 00a64e6c ["CALL", null, ["callee:00c57a80:8"]]
+ 00ac2e24 ["INT_ADD", "register:40f0:8", ["const:ac2e24:8", "const:4:8"]]
+ 00ac2e24 ["CALL", null, ["callee:00c57a80:8"]]
- 00a64e6c bytes 71d80594
+ 00ac2e24 bytes 17530694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2689165e7f6e14fe4dc0f62ddd346785"></a>

### [`00a64fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64fc4.md) → [`00ac2f7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md) FUN_00ac2f7c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac2fa0",
      "incomplete_value": false,
      "site": "00ac2fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a64fe8",
      "incomplete_value": false,
      "site": "00a64fe8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00ac2fa0",
      "DATA",
      [
        "storage",
        "00c0da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2fa0",
      "DATA",
      [
        "storage",
        "00c8d040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64fc4.md#insn-00a64fd8) · [`00a64fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64fc4.md#insn-00a64fe0) · [`00a64fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64fc4.md#insn-00a64fe4)
- 新版 [`00ac2f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md#insn-00ac2f90) · [`00ac2f98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md#insn-00ac2f98) · [`00ac2f9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f7c.md#insn-00ac2f9c)

~~~diff
- 00a64fd8 ["INT_ADD", "register:40f0:8", ["const:a64fd8:8", "const:4:8"]]
- 00a64fd8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac2f90 ["INT_ADD", "register:40f0:8", ["const:ac2f90:8", "const:4:8"]]
+ 00ac2f90 ["CALL", null, ["callee:00c57a90:8"]]
- 00a64fd8 bytes 1ad80594
+ 00ac2f90 bytes c0520694
- 00a64fe0 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac2f98 ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00a64fe0 bytes 480d00b0
+ 00ac2f98 bytes 480e00f0
- 00a64fe4 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a64fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a64fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a64fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac2f9c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00ac2f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a64fe4 bytes 08812891
+ 00ac2f9c bytes 08010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ff58f5015f3149b3385dfced178a828"></a>

### [`00a64ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64ff8.md) → [`00ac2fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2fb0.md) FUN_00ac2fb0

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac2fbc",
      "incomplete_value": false,
      "site": "00ac2fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65004",
      "incomplete_value": false,
      "site": "00a65004",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:a20:8"
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
      "00ac2fbc",
      "DATA",
      [
        "storage",
        "00c0da20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2fbc",
      "DATA",
      [
        "storage",
        "00c8d040",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a64ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64ff8.md#insn-00a64ffc) · [`00a65000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a64/00a64ff8.md#insn-00a65000)
- 新版 [`00ac2fb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2fb0.md#insn-00ac2fb4) · [`00ac2fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2fb0.md#insn-00ac2fb8)

~~~diff
- 00a64ffc ["COPY", "register:4048:8", ["const:c0d000:8"]]
+ 00ac2fb4 ["COPY", "register:4048:8", ["const:c8d000:8"]]
- 00a64ffc bytes 490d00b0
+ 00ac2fb4 bytes 490e00f0
- 00a65000 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 00a65000 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a65000 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a65000 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac2fb8 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00ac2fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac2fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac2fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a65000 bytes 29812891
+ 00ac2fb8 bytes 29010191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a85ddda5f4b9cb73ccba69ae5928b7"></a>

### [`00a650b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a650b4.md) → [`00ac306c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md) FUN_00ac306c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac308c",
      "incomplete_value": false,
      "site": "00ac3090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a650d4",
      "incomplete_value": false,
      "site": "00a650d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
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
      "00ac3090",
      "DATA",
      [
        "storage",
        "00c0daa0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3090",
      "DATA",
      [
        "storage",
        "00c8d0c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a650c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a650b4.md#insn-00a650c8) · [`00a650d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a650b4.md#insn-00a650d0) · [`00a650d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a650b4.md#insn-00a650d4)
- 新版 [`00ac3080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac3080) · [`00ac3088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac3088) · [`00ac308c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac308c)

~~~diff
- 00a650c8 ["INT_ADD", "register:40f0:8", ["const:a650c8:8", "const:4:8"]]
- 00a650c8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac3080 ["INT_ADD", "register:40f0:8", ["const:ac3080:8", "const:4:8"]]
+ 00ac3080 ["CALL", null, ["callee:00c57a90:8"]]
- 00a650c8 bytes ded70594
+ 00ac3080 bytes 84520694
- 00a650d0 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac3088 ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00a650d0 bytes 480d0090
+ 00ac3088 bytes 480e00d0
- 00a650d4 ["COPY", "tmp:0:8", ["const:aa0:8"]]
- 00a650d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a650d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a650d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac308c ["COPY", "tmp:0:8", ["const:c0:8"]]
+ 00ac308c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac308c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac308c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a650d4 bytes 08812a91
+ 00ac308c bytes 08010391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d86869cebf9a17a10a8ee192abafd15"></a>

### [`00a6514c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6514c.md) → [`00ac3104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md) FUN_00ac3104

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

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
      "site": "00a6514c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6514c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65150"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6514c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a65150",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a65170",
      "DATA",
      [
        "storage",
        "00c0db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3104",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac3108",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac3128",
      "DATA",
      [
        "storage",
        "00c8d140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6514c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6514c.md#insn-00a6514c) · [`00a65150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6514c.md#insn-00a65150) · [`00a65160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6514c.md#insn-00a65160)
- 新版 [`00ac3118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md#insn-00ac3118)

~~~diff
- 00a6514c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a6514c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a6514c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a6514c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a6514c bytes fd7bbea9
- 00a65150 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a65150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00a65150 bytes f30b00f9
- 00a65160 ["INT_ADD", "register:40f0:8", ["const:a65160:8", "const:4:8"]]
- 00a65160 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac3118 ["INT_ADD", "register:40f0:8", ["const:ac3118:8", "const:4:8"]]
+ 00ac3118 ["CALL", null, ["callee:00c57a90:8"]]
- 00a65160 bytes b8d70594
+ 00ac3118 bytes 5e520694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba20d0db85edd82860393536f435741"></a>

### [`00a65180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65180.md) → [`00ac3138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3138.md) FUN_00ac3138

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac3144",
      "incomplete_value": false,
      "site": "00ac3144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6518c",
      "incomplete_value": false,
      "site": "00a6518c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "00ac3144",
      "DATA",
      [
        "storage",
        "00c0db20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3144",
      "DATA",
      [
        "storage",
        "00c8d140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65180.md#insn-00a65184) · [`00a65188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65180.md#insn-00a65188)
- 新版 [`00ac313c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3138.md#insn-00ac313c) · [`00ac3140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3138.md#insn-00ac3140)

~~~diff
- 00a65184 ["COPY", "register:4048:8", ["const:c0d000:8"]]
+ 00ac313c ["COPY", "register:4048:8", ["const:c8d000:8"]]
- 00a65184 bytes 490d0090
+ 00ac313c bytes 490e00d0
- 00a65188 ["COPY", "tmp:0:8", ["const:b20:8"]]
- 00a65188 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a65188 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a65188 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac3140 ["COPY", "tmp:0:8", ["const:140:8"]]
+ 00ac3140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac3140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac3140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a65188 bytes 29812c91
+ 00ac3140 bytes 29010591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5e9b96dfd1ed0124f29321f63be8030"></a>

### [`00a65400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65400.md) → [`00ac33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md) FUN_00ac33b8

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac33dc",
      "incomplete_value": false,
      "site": "00ac33dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65424",
      "incomplete_value": false,
      "site": "00a65424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00ac33dc",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac33dc",
      "DATA",
      [
        "storage",
        "00c8d240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65400.md#insn-00a65414) · [`00a6541c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65400.md#insn-00a6541c) · [`00a65420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65400.md#insn-00a65420)
- 新版 [`00ac33cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md#insn-00ac33cc) · [`00ac33d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md#insn-00ac33d4) · [`00ac33d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md#insn-00ac33d8)

~~~diff
- 00a65414 ["INT_ADD", "register:40f0:8", ["const:a65414:8", "const:4:8"]]
- 00a65414 ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac33cc ["INT_ADD", "register:40f0:8", ["const:ac33cc:8", "const:4:8"]]
+ 00ac33cc ["CALL", null, ["callee:00c57a90:8"]]
- 00a65414 bytes 0bd70594
+ 00ac33cc bytes b1510694
- 00a6541c ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac33d4 ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00a6541c bytes 480d0090
+ 00ac33d4 bytes 480e00d0
- 00a65420 ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a65420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a65420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a65420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac33d8 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00ac33d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac33d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac33d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a65420 bytes 08813091
+ 00ac33d8 bytes 08010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a90887257466be4ca4fbc9237a2bbd"></a>

### [`00a65434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65434.md) → [`00ac33ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33ec.md) FUN_00ac33ec

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac33f8",
      "incomplete_value": false,
      "site": "00ac33f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:240:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65440",
      "incomplete_value": false,
      "site": "00a65440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c20:8"
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
      "00ac33f8",
      "DATA",
      [
        "storage",
        "00c0dc20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac33f8",
      "DATA",
      [
        "storage",
        "00c8d240",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65434.md#insn-00a65438) · [`00a6543c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65434.md#insn-00a6543c)
- 新版 [`00ac33f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33ec.md#insn-00ac33f0) · [`00ac33f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33ec.md#insn-00ac33f4)

~~~diff
- 00a65438 ["COPY", "register:4048:8", ["const:c0d000:8"]]
+ 00ac33f0 ["COPY", "register:4048:8", ["const:c8d000:8"]]
- 00a65438 bytes 490d0090
+ 00ac33f0 bytes 490e00d0
- 00a6543c ["COPY", "tmp:0:8", ["const:c20:8"]]
- 00a6543c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a6543c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a6543c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac33f4 ["COPY", "tmp:0:8", ["const:240:8"]]
+ 00ac33f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac33f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac33f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a6543c bytes 29813091
+ 00ac33f4 bytes 29010991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cba9ccef0c9f24e0eb1373435b8bc29b"></a>

### [`00a65450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65450.md) → [`00ac3408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md) FUN_00ac3408

採用 · 移動量 `+0x5dfb8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f78.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0088482c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/0088482c.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.16% / 新版 87.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 3件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ac34a8",
      "incomplete_value": true,
      "site": "00ac34a8",
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
            "const:3478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a654f0",
      "incomplete_value": true,
      "site": "00a654f0",
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
            "const:3388:8"
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
      "definition_site": "00ac34ec",
      "incomplete_value": true,
      "site": "00ac3500",
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
                "const:b6a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65534",
      "incomplete_value": true,
      "site": "00a65548",
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
                "const:2fd:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac3518",
      "incomplete_value": false,
      "site": "00ac3520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a65560",
      "incomplete_value": false,
      "site": "00a65568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00ac3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00ac345c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00ac34ac",
      "DATA",
      [
        "storage",
        "00397054",
        "fde_00397054",
        "dword"
      ]
    ]
  ],
  "added": [
    [
      "00ac3440",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00ac345c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00ac34ac",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a65488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65450.md#insn-00a65488) · [`00a654a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65450.md#insn-00a654a4) · [`00a654f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a65450.md#insn-00a654f0)
- 新版 [`00ac3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac3440) · [`00ac345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac345c) · [`00ac34a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac34a8)

~~~diff
- 00a65488 ["INT_ADD", "register:40f0:8", ["const:a65488:8", "const:4:8"]]
- 00a65488 ["CALL", null, ["ram:457e1c:8"]]
+ 00ac3440 ["INT_ADD", "register:40f0:8", ["const:ac3440:8", "const:4:8"]]
+ 00ac3440 ["CALL", null, ["ram:47acb4:8"]]
- 00a65488 bytes 65cae797
+ 00ac3440 bytes 1ddee697
- 00a654a4 ["INT_ADD", "register:40f0:8", ["const:a654a4:8", "const:4:8"]]
- 00a654a4 ["CALL", null, ["ram:457e1c:8"]]
+ 00ac345c ["INT_ADD", "register:40f0:8", ["const:ac345c:8", "const:4:8"]]
+ 00ac345c ["CALL", null, ["ram:47acb4:8"]]
- 00a654a4 bytes 5ecae797
+ 00ac345c bytes 16dee697
- 00a654f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3388:8"]]
- 00a654f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
+ 00ac34a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3478:8"]]
+ 00ac34a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:4"]]
- 00a654f0 bytes 6a8a33b9
+ 00ac34a8 bytes 6a7a34b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d67cd8b86ef6acdd1f7da9a38c94fd90"></a>

### [`00a656c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656c0.md) → [`00ac3678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md) FUN_00ac3678

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac368c",
      "incomplete_value": false,
      "site": "00ac3690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a656d4",
      "incomplete_value": false,
      "site": "00a656d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00ac3690",
      "DATA",
      [
        "storage",
        "00c0dc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3690",
      "DATA",
      [
        "storage",
        "00c8d2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a656cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656c0.md#insn-00a656cc) · [`00a656d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656c0.md#insn-00a656d0) · [`00a656d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656c0.md#insn-00a656d4)
- 新版 [`00ac3684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md#insn-00ac3684) · [`00ac3688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md#insn-00ac3688) · [`00ac368c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md#insn-00ac368c)

~~~diff
- 00a656cc ["INT_ADD", "register:40f0:8", ["const:a656cc:8", "const:4:8"]]
- 00a656cc ["CALL", null, ["callee:00c57a90:8"]]
+ 00ac3684 ["INT_ADD", "register:40f0:8", ["const:ac3684:8", "const:4:8"]]
+ 00ac3684 ["CALL", null, ["callee:00c57a90:8"]]
- 00a656cc bytes 5dd60594
+ 00ac3684 bytes 03510694
- 00a656d0 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac3688 ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00a656d0 bytes 480d0090
+ 00ac3688 bytes 480e00d0
- 00a656d4 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00a656d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a656d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a656d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac368c ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00ac368c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac368c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac368c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a656d4 bytes 08413291
+ 00ac368c bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c4d32aaed405de66f6b92c1c33dae7b"></a>

### [`00a656e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656e4.md) → [`00ac369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac369c.md) FUN_00ac369c

採用 · 移動量 `+0x5dfb8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac36a0",
      "incomplete_value": false,
      "site": "00ac36a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a656e8",
      "incomplete_value": false,
      "site": "00a656ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:c90:8"
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
      "00ac36a4",
      "DATA",
      [
        "storage",
        "00c0dc90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac36a4",
      "DATA",
      [
        "storage",
        "00c8d2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a656e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656e4.md#insn-00a656e4) · [`00a656e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a656e4.md#insn-00a656e8)
- 新版 [`00ac369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac369c.md#insn-00ac369c) · [`00ac36a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac369c.md#insn-00ac36a0)

~~~diff
- 00a656e4 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00ac369c ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00a656e4 bytes 480d0090
+ 00ac369c bytes 480e00d0
- 00a656e8 ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00a656e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a656e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a656e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac36a0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00ac36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a656e8 bytes 08413291
+ 00ac36a0 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f23608fad302700f8296cf6779ee176"></a>

### [`00a6573c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6573c.md) → [`00ac36f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac36f4.md) _INIT_244

採用 · 移動量 `+0x5dfb8` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 57.63% / 新版 57.63%

CFGの説明率　旧版 66.67% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 37件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6576c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a65794"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a657a0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a6576c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a65778",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a65794",
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
      "00ac3724",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00ac3730",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ac374c",
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

- 旧版 [`00a6576c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6573c.md#insn-00a6576c) · [`00a65794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6573c.md#insn-00a65794) · [`00a657a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a65/00a6573c.md#insn-00a657a0)

~~~diff
- 00a6576c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a6576c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a6576c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a6576c bytes a9831ff8
- 00a65794 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00a65794 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a65794 bytes e013813c
- 00a657a0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00a657a0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 00a657a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00a657a0 bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b51c89ba19e4d08d2f7250d6380036f"></a>

### [`00a695e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a695e4.md) → [`00ac7578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md) _INIT_245

採用 · 移動量 `+0x5df94` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 78.53% / 新版 78.53%

CFGの説明率　旧版 80.65% / 新版 83.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 8件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac75b4",
      "incomplete_value": true,
      "site": "00ac75d0",
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
      "definition_site": "00a69620",
      "incomplete_value": true,
      "site": "00a6963c",
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
      "definition_site": "00ac75d8",
      "incomplete_value": true,
      "site": "00ac75f4",
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
      "definition_site": "00a69644",
      "incomplete_value": true,
      "site": "00a69660",
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
      "definition_site": "00ac75f8",
      "incomplete_value": true,
      "site": "00ac7614",
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
      "definition_site": "00a69664",
      "incomplete_value": true,
      "site": "00a69680",
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
      "00ac75b4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00ac75d8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00ac75f8",
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
      "00ac75b4",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ac75d8",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00ac75f8",
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

- 旧版 [`00a69744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a695e4.md#insn-00a69744) · [`00a69818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a695e4.md#insn-00a69818) · [`00a69828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a695e4.md#insn-00a69828)
- 新版 [`00ac76d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md#insn-00ac76d8)

~~~diff
- 00a69744 ["INT_ADD", "register:40f0:8", ["const:a69744:8", "const:4:8"]]
- 00a69744 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00ac76d8 ["INT_ADD", "register:40f0:8", ["const:ac76d8:8", "const:4:8"]]
+ 00ac76d8 ["CALL", null, ["callee:0043b7b8:8"]]
- 00a69744 bytes 5dbde697
+ 00ac76d8 bytes 38d0e597
- 00a69818 ["INT_ADD", "register:40f0:8", ["const:a69818:8", "const:4:8"]]
- 00a69818 ["CALL", null, ["callee:00c57a30:8"]]
- 00a69818 bytes f2c50594
- 00a69828 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00a69828 ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
- 00a69828 bytes 410a0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb465f57ddea48d8a2d963acfe18b97b"></a>

### [`00a69e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69e50.md) → [`00ac7de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md) FUN_00ac7de4

採用 · 移動量 `+0x5df94` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a699f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a699f8.md) · 呼出先 14件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md) [`0044ab70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ab70.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`00ac798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md) · 呼出先 14件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.08% / 新版 84.08%

CFGの説明率　旧版 80.34% / 新版 81.74%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 10件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 19件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac80e8",
      "incomplete_value": true,
      "site": "00ac80ec",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_MULT",
            "8",
            [
              "INT2FLOAT",
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a154",
      "incomplete_value": true,
      "site": "00a6a158",
      "value": [
        "TRUNC",
        "4",
        [
          [
            "FLOAT_MULT",
            "8",
            [
              "INT2FLOAT",
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a69eac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a0b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac7e28",
      "DATA",
      [
        "storage",
        "0032e9fc",
        null,
        "byte[27]"
      ]
    ],
    [
      "unmatched:00a69e9c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:00a69ea8",
      "DATA",
      [
        "storage",
        "0032ff50",
        null,
        "byte[43]"
      ]
    ]
  ],
  "added": [
    [
      "00ac7e28",
      "DATA",
      [
        "storage",
        "00332a24",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "00ac7e30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00ac7e3c",
      "DATA",
      [
        "storage",
        "00333f90",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a69e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69e50.md#insn-00a69e9c) · [`00a69eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69e50.md#insn-00a69eac) · [`00a69f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a69/00a69e50.md#insn-00a69f0c)
- 新版 [`00ac7ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md#insn-00ac7ea0)

~~~diff
- 00a69e9c ["INT_ADD", "register:40f0:8", ["const:a69e9c:8", "const:4:8"]]
- 00a69e9c ["CALL", null, ["callee:008514b8:8"]]
- 00a69e9c bytes b9d5f697
- 00a69eac ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a69eac ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
- 00a69eac bytes 88060035
- 00a69f0c ["INT_ADD", "register:40f0:8", ["const:a69f0c:8", "const:4:8"]]
- 00a69f0c ["CALL", null, ["ram:457e1c:8"]]
+ 00ac7ea0 ["INT_ADD", "register:40f0:8", ["const:ac7ea0:8", "const:4:8"]]
+ 00ac7ea0 ["CALL", null, ["ram:47acb4:8"]]
- 00a69f0c bytes c4b7e797
+ 00ac7ea0 bytes 85cbe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53447ca02423d21f8bf52e64aa969841"></a>

### [`00a6a330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a330.md) → [`00ac82c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac82c4.md) FUN_00ac82c4

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`005a2bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a2/005a2bb0.md) [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) [`006bd4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006bd/006bd4fc.md) [`00713660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00713/00713660.md) [`008a9f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a9f60.md) · 呼出先 8件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00827b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827b94.md) [`008292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292ec.md) [`008292f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292f4.md) [`0082931c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/0082931c.md)
- 新版 呼出元 10件 [`005c71e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c7/005c71e0.md) [`0067fd6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067f/0067fd6c.md) [`006e72c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e72c0.md) [`0073d764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073d/0073d764.md) [`008dde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dde04.md) · 呼出先 8件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md) [`0085b294`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b294.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac82dc",
      "value": [
        "leaf",
        "ram:859b0c:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a6a348",
      "value": [
        "leaf",
        "ram:827b94:8"
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
      "site": "00ac82e8",
      "value": [
        "leaf",
        "ram:85b294:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a6a354",
      "value": [
        "leaf",
        "ram:82931c:8"
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
      "site": "00ac830c",
      "value": [
        "leaf",
        "ram:85b264:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a6a378",
      "value": [
        "leaf",
        "ram:8292ec:8"
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
      "00ac82dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00827b94"
      ]
    ],
    [
      "00ac82e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0082931c"
      ]
    ],
    [
      "00ac830c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "008292ec"
      ]
    ]
  ],
  "added": [
    [
      "00ac82dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00859b0c"
      ]
    ],
    [
      "00ac82e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0085b294"
      ]
    ],
    [
      "00ac830c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0085b264"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6a348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a330.md#insn-00a6a348) · [`00a6a354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a330.md#insn-00a6a354) · [`00a6a378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a330.md#insn-00a6a378)
- 新版 [`00ac82dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac82c4.md#insn-00ac82dc) · [`00ac82e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac82c4.md#insn-00ac82e8) · [`00ac830c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac82c4.md#insn-00ac830c)

~~~diff
- 00a6a348 ["INT_ADD", "register:40f0:8", ["const:a6a348:8", "const:4:8"]]
- 00a6a348 ["CALL", null, ["ram:827b94:8"]]
+ 00ac82dc ["INT_ADD", "register:40f0:8", ["const:ac82dc:8", "const:4:8"]]
+ 00ac82dc ["CALL", null, ["ram:859b0c:8"]]
- 00a6a348 bytes 13f6f697
+ 00ac82dc bytes 0c46f697
- 00a6a354 ["INT_ADD", "register:40f0:8", ["const:a6a354:8", "const:4:8"]]
- 00a6a354 ["CALL", null, ["ram:82931c:8"]]
+ 00ac82e8 ["INT_ADD", "register:40f0:8", ["const:ac82e8:8", "const:4:8"]]
+ 00ac82e8 ["CALL", null, ["ram:85b294:8"]]
- 00a6a354 bytes f2fbf697
+ 00ac82e8 bytes eb4bf697
- 00a6a378 ["INT_ADD", "register:40f0:8", ["const:a6a378:8", "const:4:8"]]
- 00a6a378 ["CALL", null, ["ram:8292ec:8"]]
+ 00ac830c ["INT_ADD", "register:40f0:8", ["const:ac830c:8", "const:4:8"]]
+ 00ac830c ["CALL", null, ["ram:85b264:8"]]
- 00a6a378 bytes ddfbf697
+ 00ac830c bytes d64bf697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00795e533ec28fc2402746e55489a061"></a>

### [`00a6a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md) → [`00ac8440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md) FUN_00ac8440

採用 · 移動量 `+0x5df94` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`007f78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78a8.md) [`007ff184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff184.md) [`007ff240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ff/007ff240.md) [`0080735c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00807/0080735c.md) [`0089c82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089c82c.md) · 呼出先 3件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00884764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/00884764.md) [`008847e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00884/008847e4.md)
- 新版 呼出元 7件 [`0082ccbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccbc.md) [`00830af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830af0.md) [`00830bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00830/00830bac.md) [`00838cc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838cc8.md) [`008d06c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d0/008d06c4.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b7904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7904.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 51.85% / 新版 51.85%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ac8460",
      "incomplete_value": true,
      "site": "00ac8464",
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
      "definition_site": "00a6a4cc",
      "incomplete_value": true,
      "site": "00a6a4d0",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a4e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00a6a4ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac8468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a6a4ec"
      ]
    ],
    [
      "unmatched:00a6a4e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b7904"
      ]
    ],
    [
      "unmatched:00a6a4ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ]
  ],
  "added": [
    [
      "00ac8468",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac8480"
      ]
    ],
    [
      "00ac847c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b7904"
      ]
    ],
    [
      "00ac8480",
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

- 旧版 [`00a6a4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md#insn-00a6a4d0) · [`00a6a4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md#insn-00a6a4e8) · [`00a6a4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a4ac.md#insn-00a6a4ec)
- 新版 [`00ac8464`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8440.md#insn-00ac8464)

~~~diff
- 00a6a4d0 ["INT_ADD", "register:40f0:8", ["const:a6a4d0:8", "const:4:8"]]
- 00a6a4d0 ["CALL", null, ["callee:008b7984:8"]]
+ 00ac8464 ["INT_ADD", "register:40f0:8", ["const:ac8464:8", "const:4:8"]]
+ 00ac8464 ["CALL", null, ["callee:008b7984:8"]]
- 00a6a4d0 bytes c568f897
+ 00ac8464 bytes 48bdf797
- 00a6a4e8 ["INT_ADD", "register:40f0:8", ["const:a6a4e8:8", "const:4:8"]]
- 00a6a4e8 ["CALL", null, ["callee:008b7904:8"]]
- 00a6a4e8 bytes 9f68f897
- 00a6a4ec ["INT_ADD", "register:40f0:8", ["const:a6a4ec:8", "const:4:8"]]
- 00a6a4ec ["CALL", null, ["callee:008514b8:8"]]
- 00a6a4ec bytes 25d4f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db403de856f8a84b9d8659dcae5ad87b"></a>

### [`00a6a58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a58c.md) → [`00ac8520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md) FUN_00ac8520

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00a6b95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6b/00a6b95c.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`0046866c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/0046866c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00ac98f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md) · 呼出先 7件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`0046dab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046dab4.md) [`0048b504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048b504.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 86.96% / 新版 95.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a6a5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a58c.md#insn-00a6a5bc) · [`00a6a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a58c.md#insn-00a6a5f0) · [`00a6a61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a58c.md#insn-00a6a61c)
- 新版 [`00ac8550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md#insn-00ac8550) · [`00ac8584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md#insn-00ac8584) · [`00ac85b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8520.md#insn-00ac85b0)

~~~diff
- 00a6a5bc ["INT_ADD", "register:40f0:8", ["const:a6a5bc:8", "const:4:8"]]
- 00a6a5bc ["CALL", null, ["callee:0046dab4:8"]]
+ 00ac8550 ["INT_ADD", "register:40f0:8", ["const:ac8550:8", "const:4:8"]]
+ 00ac8550 ["CALL", null, ["callee:0046dab4:8"]]
- 00a6a5bc bytes 9881e797
+ 00ac8550 bytes 5995e697
- 00a6a5f0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 00a6a5f0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
+ 00ac8584 ["INT_NOTEQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
+ 00ac8584 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00a6a5f0 bytes 6a0500b5
+ 00ac8584 bytes 6a0500b5
- 00a6a61c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00a6a61c ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00ac85b0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00ac85b0 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00a6a61c bytes c80400b5
+ 00ac85b0 bytes c80400b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f59b3a483872c591c072b303497569"></a>

### [`00a6a6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a6cc.md) → [`00ac8660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md) FUN_00ac8660

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`007f7410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f7410.md) [`007f78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f7/007f78c4.md) [`0088fde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0088f/0088fde0.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a6a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md)
- 新版 呼出元 3件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md) [`006534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac86d8",
      "incomplete_value": false,
      "site": "00ac86dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a744",
      "incomplete_value": false,
      "site": "00a6a748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac86b8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a6a724",
      "value": [
        "leaf",
        "ram:449aec:8"
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
      "00ac86b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "00ac86dc",
      "DATA",
      [
        "storage",
        "00bf6310",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac872c",
      "READ",
      [
        "storage",
        "00bf6330",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac86b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00ac86dc",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac872c",
      "READ",
      [
        "storage",
        "00c73458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6a724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a6cc.md#insn-00a6a724) · [`00a6a720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a6cc.md#insn-00a6a720) · [`00a6a740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a6cc.md#insn-00a6a740)
- 新版 [`00ac86b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86b8) · [`00ac86b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86b4) · [`00ac86d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86d4)

~~~diff
- 00a6a724 ["INT_ADD", "register:40f0:8", ["const:a6a724:8", "const:4:8"]]
- 00a6a724 ["CALL", null, ["ram:449aec:8"]]
+ 00ac86b8 ["INT_ADD", "register:40f0:8", ["const:ac86b8:8", "const:4:8"]]
+ 00ac86b8 ["CALL", null, ["ram:46c984:8"]]
- 00a6a724 bytes f27ce797
+ 00ac86b8 bytes b390e697
- 00a6a720 ["INT_ADD", "register:40f0:8", ["const:a6a720:8", "const:4:8"]]
- 00a6a720 ["CALL", null, ["callee:008514b8:8"]]
+ 00ac86b4 ["INT_ADD", "register:40f0:8", ["const:ac86b4:8", "const:4:8"]]
+ 00ac86b4 ["CALL", null, ["callee:008514b8:8"]]
- 00a6a720 bytes 98d3f697
+ 00ac86b4 bytes 8123f697
- 00a6a740 ["COPY", "register:4040:8", ["const:bf6000:8"]]
+ 00ac86d4 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00a6a740 bytes 680c0090
+ 00ac86d4 bytes 480d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a735cdebbcb7be401d49350f1b012a28"></a>

### [`00a6a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md) → [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md) FUN_00ac87ac

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`0061d5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0061d/0061d5c8.md) [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`006baf70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ba/006baf70.md) [`007127f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00712/007127f8.md) [`008a8900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a8/008a8900.md) · 呼出先 5件 [`00a6ced8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6ced8.md) [`00a6d078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d078.md) [`00a6d07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d07c.md) [`00a6d0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6d0b0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 12件 [`006430b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00643/006430b0.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`008dc798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md) · 呼出先 5件 [`00acae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md) [`00acb00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb00c.md) [`00acb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb010.md) [`00acb044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb044.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8878",
      "incomplete_value": false,
      "site": "00ac888c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a8e4",
      "incomplete_value": false,
      "site": "00a6a8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8878",
      "incomplete_value": false,
      "site": "00ac8898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c8d000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6a8e4",
      "incomplete_value": false,
      "site": "00a6a904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac888c",
      "DATA",
      [
        "storage",
        "00c0dd20",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8898",
      "DATA",
      [
        "storage",
        "00c0dd20",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac88c4",
      "READ",
      [
        "storage",
        "00c0dd40",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac888c",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8898",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac88c4",
      "READ",
      [
        "storage",
        "00c8d360",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6a874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md#insn-00a6a874) · [`00a6a8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md#insn-00a6a8a0) · [`00a6a8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md#insn-00a6a8b0)
- 新版 [`00ac8808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8808) · [`00ac8834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8834) · [`00ac8844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8844)

~~~diff
- 00a6a874 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6a874 ["INT_ADD", "register:40f0:8", ["const:a6a874:8", "const:4:8"]]
- 00a6a874 ["CALLIND", null, ["register:0:8"]]
+ 00ac8808 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac8808 ["INT_ADD", "register:40f0:8", ["const:ac8808:8", "const:4:8"]]
+ 00ac8808 ["CALLIND", null, ["register:0:8"]]
- 00a6a874 bytes 00013fd6
+ 00ac8808 bytes 00013fd6
- 00a6a8a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00a6a8a0 ["INT_ADD", "register:40f0:8", ["const:a6a8a0:8", "const:4:8"]]
- 00a6a8a0 ["CALLIND", null, ["register:0:8"]]
+ 00ac8834 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac8834 ["INT_ADD", "register:40f0:8", ["const:ac8834:8", "const:4:8"]]
+ 00ac8834 ["CALLIND", null, ["register:0:8"]]
- 00a6a8a0 bytes 00013fd6
+ 00ac8834 bytes 00013fd6
- 00a6a8b0 ["INT_ADD", "register:40f0:8", ["const:a6a8b0:8", "const:4:8"]]
- 00a6a8b0 ["CALL", null, ["callee:00acae6c:8"]]
+ 00ac8844 ["INT_ADD", "register:40f0:8", ["const:ac8844:8", "const:4:8"]]
+ 00ac8844 ["CALL", null, ["callee:00acae6c:8"]]
- 00a6a8b0 bytes 8a090094
+ 00ac8844 bytes 8a090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8734e51251db0e569d1dd6d756082b3c"></a>

### [`00a6aae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6aae0.md) → [`00ac8a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md) FUN_00ac8a74

採用 · 移動量 `+0x5df94` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0075e798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075e/0075e798.md) [`007f99cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f99cc.md) [`00896c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00896/00896c7c.md) [`00a1450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a14/00a1450c.md) [`00a622a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a62/00a622a0.md) · 呼出先 6件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0062d9b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9b8.md) [`0062d9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d9bc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a6a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6a818.md)
- 新版 呼出元 5件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md) [`006534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8acc",
      "incomplete_value": false,
      "site": "00ac8ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c73000:8"
          ],
          [
            "leaf",
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a6ab38",
      "incomplete_value": false,
      "site": "00a6ab3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac8aac",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00a6ab18",
      "value": [
        "leaf",
        "ram:449aec:8"
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
      "00ac8aac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00449aec"
      ]
    ],
    [
      "00ac8ad0",
      "DATA",
      [
        "storage",
        "00bf6310",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8b20",
      "READ",
      [
        "storage",
        "00bf6330",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac8aac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00ac8ad0",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8b20",
      "READ",
      [
        "storage",
        "00c73458",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a6ab18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6aae0.md#insn-00a6ab18) · [`00a6ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6aae0.md#insn-00a6ab14) · [`00a6ab34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6a/00a6aae0.md#insn-00a6ab34)
- 新版 [`00ac8aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md#insn-00ac8aac) · [`00ac8aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md#insn-00ac8aa8) · [`00ac8ac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md#insn-00ac8ac8)

~~~diff
- 00a6ab18 ["INT_ADD", "register:40f0:8", ["const:a6ab18:8", "const:4:8"]]
- 00a6ab18 ["CALL", null, ["ram:449aec:8"]]
+ 00ac8aac ["INT_ADD", "register:40f0:8", ["const:ac8aac:8", "const:4:8"]]
+ 00ac8aac ["CALL", null, ["ram:46c984:8"]]
- 00a6ab18 bytes f57be797
+ 00ac8aac bytes b68fe697
- 00a6ab14 ["INT_ADD", "register:40f0:8", ["const:a6ab14:8", "const:4:8"]]
- 00a6ab14 ["CALL", null, ["callee:008514b8:8"]]
+ 00ac8aa8 ["INT_ADD", "register:40f0:8", ["const:ac8aa8:8", "const:4:8"]]
+ 00ac8aa8 ["CALL", null, ["callee:008514b8:8"]]
- 00a6ab14 bytes 9bd2f697
+ 00ac8aa8 bytes 8422f697
- 00a6ab34 ["COPY", "register:4040:8", ["const:bf6000:8"]]
+ 00ac8ac8 ["COPY", "register:4040:8", ["const:c73000:8"]]
- 00a6ab34 bytes 680c0090
+ 00ac8ac8 bytes 480d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

