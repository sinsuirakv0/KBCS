# v16.0.2 → v16.0.3 · 最優先の変更候補 (39)

[一覧の目次](README.md)

<a id="compare-1d142dee32de4d52a0031c5d06daab4f"></a>

### [`0078ed44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed44.md) → [`0078f120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f120.md) FUN_0078f120

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, local_def_use, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0078f144",
      "incomplete_value": false,
      "site": "0078f144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ed68",
      "incomplete_value": false,
      "site": "0078ed68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "0078f144",
      "DATA",
      [
        "storage",
        "00c79bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078f144",
      "DATA",
      [
        "storage",
        "00c7ab88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078ed4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed44.md#insn-0078ed4c) · [`0078ed58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed44.md#insn-0078ed58) · [`0078ed60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed44.md#insn-0078ed60)
- 新版 [`0078f134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f120.md#insn-0078f134) · [`0078f13c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f120.md#insn-0078f13c)

~~~diff
- 0078ed4c ["COPY", "register:40e8:8", ["register:8:8"]]
- 0078ed4c bytes fd030091
- 0078ed58 ["INT_ADD", "register:40f0:8", ["const:78ed58:8", "const:4:8"]]
- 0078ed58 ["CALL", null, ["callee:00c58f30:8"]]
+ 0078f134 ["INT_ADD", "register:40f0:8", ["const:78f134:8", "const:4:8"]]
+ 0078f134 ["CALL", null, ["callee:00c58f30:8"]]
- 0078ed58 bytes 82241394
+ 0078f134 bytes 7f271394
- 0078ed60 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0078f13c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0078ed60 bytes 482700f0
+ 0078f13c bytes 482700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-424da8cf3760414930965b36bb9a9bbf"></a>

### [`0078ed78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed78.md) → [`0078f154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f154.md) FUN_0078f154

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0078f160",
      "incomplete_value": false,
      "site": "0078f160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0078ed84",
      "incomplete_value": false,
      "site": "0078ed84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "0078f160",
      "DATA",
      [
        "storage",
        "00c79bb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0078f160",
      "DATA",
      [
        "storage",
        "00c7ab88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078ed7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed78.md#insn-0078ed7c) · [`0078ed80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ed78.md#insn-0078ed80)
- 新版 [`0078f158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f154.md#insn-0078f158) · [`0078f15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f154.md#insn-0078f15c)

~~~diff
- 0078ed7c ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0078f158 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0078ed7c bytes 492700f0
+ 0078f158 bytes 492700f0
- 0078ed80 ["COPY", "tmp:0:8", ["const:bb8:8"]]
- 0078ed80 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0078ed80 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0078ed80 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0078f15c ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 0078f15c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0078f15c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0078f15c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0078ed80 bytes 29e12e91
+ 0078f15c bytes 29212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfb3c7d52fa33fc45fae916d35d24bbf"></a>

### [`0078ee0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ee0c.md) → [`0078f1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f1e8.md) _INIT_136

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 80.79% / 新版 80.79%

CFGの説明率　旧版 35.90% / 新版 35.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ee3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ee64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ee88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078ee3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078ee48",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0078ee64",
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
      "0078f218",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0078f224",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0078f240",
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

- 旧版 [`0078ee3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ee0c.md#insn-0078ee3c) · [`0078ee64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ee0c.md#insn-0078ee64) · [`0078ee88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078e/0078ee0c.md#insn-0078ee88)

~~~diff
- 0078ee3c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0078ee3c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0078ee3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0078ee3c bytes a9831ff8
- 0078ee64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 0078ee64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0078ee64 bytes e013813c
- 0078ee88 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 0078ee88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0078ee88 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7effbbbe791bfbe327224b2022d34d53"></a>

### [`0078f19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f19c.md) → [`0078f578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f578.md) FUN_0078f578

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 54.17% / 新版 54.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-26df63280ecf2e9eda4453d82d985319"></a>

### [`0078f4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md) → [`0078f8b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f8b4.md) FUN_0078f8b4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 2件 [`00480bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480bd0.md) [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 2件 [`00480ef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480ef0.md) [`004810a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 31.25% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f50c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f558"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0078f8e8"
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
      "unmatched:0078f50c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f908"
      ]
    ],
    [
      "unmatched:0078f558",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f92c"
      ]
    ]
  ],
  "added": [
    [
      "0078f8e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f908"
      ]
    ],
    [
      "0078f934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078f92c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078f50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f50c) · [`0078f538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f538) · [`0078f558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f4d8.md#insn-0078f558)
- 新版 [`0078f914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f8b4.md#insn-0078f914)

~~~diff
- 0078f50c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0078f50c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0078f50c bytes 01010054
- 0078f538 ["INT_ADD", "register:40f0:8", ["const:78f538:8", "const:4:8"]]
- 0078f538 ["CALL", null, ["callee:00480ef0:8"]]
+ 0078f914 ["INT_ADD", "register:40f0:8", ["const:78f914:8", "const:4:8"]]
+ 0078f914 ["CALL", null, ["callee:00480ef0:8"]]
- 0078f538 bytes a6c5f397
+ 0078f914 bytes 77c5f397
- 0078f558 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 0078f558 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0078f558 bytes c9ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932093743d2d542df290d03ab44b10df"></a>

### [`0078f578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md) → [`0078f954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078f954.md) FUN_0078f954

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 5件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`004801b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/004801b8.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 5件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`004804d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/004804d8.md) [`00480658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 54.17% / 新版 54.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f57c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f57c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f580"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078f57c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078f580",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078f584",
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
      "0078f958",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0078f95c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0078f960",
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

- 旧版 [`0078f57c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f57c) · [`0078f580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f580) · [`0078f584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f578.md#insn-0078f584)

~~~diff
- 0078f57c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0078f57c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0078f57c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0078f57c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f57c bytes fd7b01a9
- 0078f580 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0078f580 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0078f580 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0078f580 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f580 bytes fc6f02a9
- 0078f584 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0078f584 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0078f584 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0078f584 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f584 bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b7c02ed3276729665b367cdd00c66d5"></a>

### [`0078f768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md) → [`0078fb44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fb44.md) FUN_0078fb44

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480158.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00480478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480478.md) [`00480750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480750.md) [`00480aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480aa4.md) [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 23.08% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f768"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f76c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f76c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078f768",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078f76c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078f770",
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
      "0078fb44",
      "WRITE",
      [
        "storage",
        "Stack[-0x70]",
        null,
        null
      ]
    ],
    [
      "0078fb48",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0078fb4c",
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

- 旧版 [`0078f768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f768) · [`0078f76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f76c) · [`0078f770`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f768.md#insn-0078f770)

~~~diff
- 0078f768 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffff90:8"]]
- 0078f768 ["STORE", null, ["const:1b1:8", "register:8:8", "register:5100:8"]]
- 0078f768 bytes e80f19fc
- 0078f76c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0078f76c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0078f76c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0078f76c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f76c bytes fd7b01a9
- 0078f770 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0078f770 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0078f770 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0078f770 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f770 bytes fc6f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1237b7cbfa293b58a0f8925abd96d4"></a>

### [`0078f8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md) → [`0078fc84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fc84.md) FUN_0078fc84

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a2b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a2b/00a2b33c.md) · 呼出先 3件 [`00480d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480d88.md) [`00480e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480e68.md) [`004810d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/004810d8.md)
- 新版 呼出元 1件 [`00a2c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2c/00a2c310.md) · 呼出先 3件 [`004810a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004810a8.md) [`00481188`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/00481188.md) [`004813f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00481/004813f8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 87.32% / 新版 87.32%

CFGの説明率　旧版 21.43% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f8e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f998"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f9bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078f8e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fcfc"
      ]
    ],
    [
      "unmatched:0078f998",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fd88"
      ]
    ],
    [
      "0078fd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0078f99c"
      ]
    ]
  ],
  "added": [
    [
      "0078fcbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fcfc"
      ]
    ],
    [
      "0078fd74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fd88"
      ]
    ],
    [
      "0078fd80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fd78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078f8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f8e0) · [`0078f8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f8ec) · [`0078f92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f8a8.md#insn-0078f92c)
- 新版 [`0078fcc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fc84.md#insn-0078fcc8) · [`0078fd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fc84.md#insn-0078fd08)

~~~diff
- 0078f8e0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0078f8e0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 0078f8e0 bytes 01020054
- 0078f8ec ["INT_ADD", "register:40f0:8", ["const:78f8ec:8", "const:4:8"]]
- 0078f8ec ["CALL", null, ["callee:00481188:8"]]
+ 0078fcc8 ["INT_ADD", "register:40f0:8", ["const:78fcc8:8", "const:4:8"]]
+ 0078fcc8 ["CALL", null, ["callee:00481188:8"]]
- 0078f8ec bytes 5fc5f397
+ 0078fcc8 bytes 30c5f397
- 0078f92c ["INT_ADD", "register:40f0:8", ["const:78f92c:8", "const:4:8"]]
- 0078f92c ["CALL", null, ["callee:00481188:8"]]
+ 0078fd08 ["INT_ADD", "register:40f0:8", ["const:78fd08:8", "const:4:8"]]
+ 0078fd08 ["CALL", null, ["callee:00481188:8"]]
- 0078f92c bytes 4fc5f397
+ 0078fd08 bytes 20c5f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15b01867e1dd20ed6536796ad2e1a433"></a>

### [`0078f9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md) → [`0078fda0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fda0.md) FUN_0078fda0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00a26210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a26/00a26210.md) · 呼出先 7件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00480338`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480338.md) [`00480430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480430.md) [`00480784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00480/00480784.md) [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md)
- 新版 呼出元 1件 [`00a271bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a27/00a271bc.md) · 呼出先 7件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00480658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480658.md) [`00480750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480750.md) [`00480aa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00480/00480aa4.md) [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 96.53% / 新版 96.53%

CFGの説明率　旧版 47.92% / 新版 47.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078f9dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0078fdb8"
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
      "unmatched:0078f9dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078fad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fe00"
      ]
    ],
    [
      "unmatched:0078fbd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fef8"
      ]
    ]
  ],
  "added": [
    [
      "0078fdb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0078feb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fe00"
      ]
    ],
    [
      "0078ffb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0078fef8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078f9dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078f9dc) · [`0078faac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078faac) · [`0078fad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078f9c4.md#insn-0078fad4)
- 新版 [`0078fe88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078fda0.md#insn-0078fe88)

~~~diff
- 0078f9dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0078f9dc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0078f9dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0078f9dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078f9dc bytes f44f06a9
- 0078faac ["INT_ADD", "register:40f0:8", ["const:78faac:8", "const:4:8"]]
- 0078faac ["CALL", null, ["callee:00c58f30:8"]]
+ 0078fe88 ["INT_ADD", "register:40f0:8", ["const:78fe88:8", "const:4:8"]]
+ 0078fe88 ["CALL", null, ["callee:00c58f30:8"]]
- 0078faac bytes 2d211394
+ 0078fe88 bytes 2a241394
- 0078fad4 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0078fad4 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0078fad4 bytes 88faffb4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-320bc064b1bb4e3d06aee5a9c6576fa6"></a>

### [`0078fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md) → [`0078ffe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0078f/0078ffe0.md) FUN_0078ffe0

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084e5f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0084e/0084e5f4.md) · 呼出先 3件 [`005c1c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005c1/005c1c30.md) [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md) [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md)
- 新版 呼出元 1件 [`0084f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0084f/0084f5a0.md) · 呼出先 3件 [`005c1fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005c1/005c1fe0.md) [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md) [`007900a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/007900a8.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 86.84% / 新版 86.84%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fc04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fc04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078fc08"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078fc04",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078fc08",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078fc0c",
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
      "0078ffe0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0078ffe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0078ffe8",
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

- 旧版 [`0078fc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc04) · [`0078fc08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc08) · [`0078fc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc04.md#insn-0078fc0c)

~~~diff
- 0078fc04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0078fc04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0078fc04 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0078fc04 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0078fc04 bytes fd7bbda9
- 0078fc08 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0078fc08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0078fc08 bytes f50b00f9
- 0078fc0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0078fc0c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0078fc0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0078fc0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078fc0c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd4794c073a7eb08a9cf858ba3e6796e"></a>

### [`0078fc9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc9c.md) → [`00790078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790078.md) FUN_00790078

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 1件 [`00676aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00676/00676aa0.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 1件 [`00676e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00676/00676e50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0078fcb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fc9c.md#insn-0078fcb4)
- 新版 [`00790090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790078.md#insn-00790090)

~~~diff
- 0078fcb4 ["INT_ADD", "register:40f0:8", ["const:78fcb4:8", "const:4:8"]]
- 0078fcb4 ["CALL", null, ["callee:00676e50:8"]]
+ 00790090 ["INT_ADD", "register:40f0:8", ["const:790090:8", "const:4:8"]]
+ 00790090 ["CALL", null, ["callee:00676e50:8"]]
- 0078fcb4 bytes 7b9bfb97
+ 00790090 bytes 709bfb97
~~~


<a id="compare-2e8f9fad93eb1fb5985c1749e445bb30"></a>

### [`0078ff2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078ff2c.md) → [`00790308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790308.md) FUN_00790308

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 15件 [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0047e64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e64c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`0079025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md) [`007948d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007948d0.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 15件 [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`0047e96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047e96c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00790638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790638.md) [`00794cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cac.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.71% / 新版 68.71%

CFGの説明率　旧版 29.79% / 新版 31.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ff54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ffbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0078ffbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0078ff54",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0078ff60",
      "READ",
      [
        "storage",
        "00ca5038",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:0078ff64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00790538"
      ]
    ]
  ],
  "added": [
    [
      "00790330",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0079033c",
      "READ",
      [
        "storage",
        "00ca5ff8",
        null,
        "undefined1"
      ]
    ],
    [
      "00790340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00790538"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0078ff54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078ff2c.md#insn-0078ff54) · [`0078ff64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078ff2c.md#insn-0078ff64) · [`0078ffbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078ff2c.md#insn-0078ffbc)

~~~diff
- 0078ff54 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0078ff54 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0078ff54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0078ff54 bytes a8831ff8
- 0078ff64 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0078ff64 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0078ff64 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0078ff64 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0078ff64 bytes c80f0036
- 0078ffbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0078ffbc ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 0078ffbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0078ffbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0078ffbc bytes e85304a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e135e8a0ea7261bd40086c181d3b9a28"></a>

### [`0079025c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md) → [`00790638`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790638.md) FUN_00790638

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0078ff2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078ff2c.md) · 呼出先 12件 [`005d8c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005d8/005d8c08.md) [`007951d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007951d4.md) [`008b6f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b6/008b6f68.md) [`008b7044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b7/008b7044.md) [`00a467d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a46/00a467d8.md)
- 新版 呼出元 1件 [`00790308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790308.md) · 呼出先 12件 [`005d8fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005d8/005d8fb8.md) [`007955b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007955b0.md) [`008b7f14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7f14.md) [`008b7ff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008b7/008b7ff0.md) [`00a477cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a47/00a477cc.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.80% / 新版 80.80%

CFGの説明率　旧版 15.85% / 新版 17.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00790270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00790270"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00790274"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00790270",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00790274",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00790314",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0079064c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00790650",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "007906f0",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00790270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md#insn-00790270) · [`00790274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md#insn-00790274) · [`00790294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/0079025c.md#insn-00790294)

~~~diff
- 00790270 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00790270 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00790270 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00790270 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00790270 bytes f6570da9
- 00790274 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00790274 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00790274 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00790274 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00790274 bytes f44f0ea9
- 00790294 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00790294 ["COPY", "tmp:1:4", ["register:4028:4"]]
- 00790294 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00790294 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00790294 bytes a8a4851a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a32bb9e26b0eaeea1c432c61db72ade1"></a>

### [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) → [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) FUN_00790a90

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0075ebd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0075e/0075ebd8.md) · 呼出先 14件 [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`00615f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md) [`0065258c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/0065258c.md) [`0078fccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0078f/0078fccc.md) [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md)
- 新版 呼出元 1件 [`0075ef88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0075e/0075ef88.md) · 呼出先 14件 [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`006162bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00616/006162bc.md) [`0065293c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/0065293c.md) [`007900a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/007900a8.md) [`00791658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.03% / 新版 80.03%

CFGの説明率　旧版 43.06% / 新版 42.03%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 27件, `store_condition` 13件, `unresolved_branch_alignment` 30件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007906b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007906b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007906bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007906b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:007906bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:007906c0",
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
      "00790a94",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00790a98",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00790a9c",
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

- 旧版 [`007906b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md#insn-007906b8) · [`007906bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md#insn-007906bc) · [`007906c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md#insn-007906c0)

~~~diff
- 007906b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007906b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007906b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:150:8"]]
- 007906b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007906b8 bytes fd7b15a9
- 007906bc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 007906bc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 007906bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 007906bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007906bc bytes fc6f16a9
- 007906c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 007906c0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 007906c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:170:8"]]
- 007906c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007906c0 bytes fa6717a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db5f1684c2a9a6aaf0550ebf974a46d"></a>

### [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md) → [`00791658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md) FUN_00791658

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md)
- 新版 呼出元 1件 [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.36% / 新版 87.36%

CFGの説明率　旧版 41.67% / 新版 40.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 14件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00791400"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00791404"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007914d4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007912d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00791984"
      ]
    ],
    [
      "unmatched:007913a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079178c"
      ]
    ],
    [
      "unmatched:0079140c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007917f4"
      ]
    ]
  ],
  "added": [
    [
      "007916b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00791984"
      ]
    ],
    [
      "0079177c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079178c"
      ]
    ],
    [
      "007917e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007917f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007912d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-007912d4) · [`007912f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-007912f0) · [`00791308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md#insn-00791308)
- 新版 [`007916cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md#insn-007916cc) · [`007916e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md#insn-007916e4)

~~~diff
- 007912d4 ["CBRANCH", null, ["local:b56:8", "register:101:1"]]
- 007912d4 bytes a0160054
- 007912f0 ["CBRANCH", null, ["local:b56:8", "register:101:1"]]
+ 007916cc ["CBRANCH", null, ["local:b58:8", "register:101:1"]]
- 007912f0 bytes c0150054
+ 007916cc bytes c0150054
- 00791308 ["INT_RIGHT", "tmp:0:8", ["register:40d0:8", "const:3f:4"]]
- 00791308 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
- 00791308 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
- 00791308 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 007916e4 ["INT_RIGHT", "tmp:0:8", ["register:40d0:8", "const:3f:4"]]
+ 007916e4 ["INT_AND", "tmp:1:8", ["tmp:0:8", "const:1:8"]]
+ 007916e4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:8", "const:0:8"]]
+ 007916e4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00791308 bytes da22f8b7
+ 007916e4 bytes da22f8b7
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e172a11fb072c1f8bbd769bc2070985d"></a>

### [`00791eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md) → [`00792294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792294.md) FUN_00792294

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007906b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00790/007906b4.md) · 呼出先 12件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md)
- 新版 呼出元 1件 [`00790a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00790/00790a90.md) · 呼出先 12件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 88.97% / 新版 88.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007921b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079224c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079258c"
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
      "unmatched:00792050",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00792438"
      ]
    ],
    [
      "unmatched:0079224c",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0079242c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00792438"
      ]
    ],
    [
      "00792628",
      "WRITE",
      [
        "storage",
        "Stack[-0xd8]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00792050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-00792050) · [`00792174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-00792174) · [`007921b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md#insn-007921b0)

~~~diff
- 00792050 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00792050 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00792050 bytes 680000b4
- 00792174 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00792174 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00792174 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00792174 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00792174 bytes 3731889a
- 007921b0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 007921b0 ["COPY", "tmp:1:8", ["register:40b0:8"]]
- 007921b0 ["INT_ADD", "register:40b0:8", ["register:40b0:8", "const:4:8"]]
- 007921b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 007921b0 bytes c84600b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f337131bd9b97b8d6e66d50a8a410de5"></a>

### [`00792f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md) → [`007932e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/007932e8.md) FUN_007932e8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`007738ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00773/007738ec.md) · 呼出先 14件 [`00467b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00467/00467b6c.md) [`00468844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00468/00468844.md) [`0046ca04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046c/0046ca04.md) [`0063678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00636/0063678c.md) [`00794f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794f4c.md)
- 新版 呼出元 1件 [`00773cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00773/00773cc8.md) · 呼出先 14件 [`00467e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00467/00467e8c.md) [`00468b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00468/00468b64.md) [`0046cd24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046c/0046cd24.md) [`00636b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00636/00636b3c.md) [`00795328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795328.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 97.49% / 新版 97.49%

CFGの説明率　旧版 84.95% / 新版 84.04%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079348c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00793650"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007936cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00793488",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "unmatched:0079348c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00793848"
      ]
    ],
    [
      "00793a2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00793a20"
      ]
    ]
  ],
  "added": [
    [
      "00793864",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c54d90"
      ]
    ],
    [
      "00793868",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00793848"
      ]
    ],
    [
      "00793a0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b89cc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00793274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md#insn-00793274) · [`00793488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md#insn-00793488) · [`0079348c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/00792f0c.md#insn-0079348c)
- 新版 [`00793650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/007932e8.md#insn-00793650)

~~~diff
- 00793274 ["CBRANCH", null, ["local:b66:8", "register:101:1"]]
+ 00793650 ["CBRANCH", null, ["local:b67:8", "register:101:1"]]
- 00793274 bytes 20120054
+ 00793650 bytes 20120054
- 00793488 ["INT_ADD", "register:40f0:8", ["const:793488:8", "const:4:8"]]
- 00793488 ["CALL", null, ["callee:00c54d90:8"]]
- 00793488 bytes 46021394
- 0079348c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079348c ["CBRANCH", null, ["local:b60:8", "tmp:0:1"]]
- 0079348c bytes 00ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6217a3400eeaad726237f6070b8114a7"></a>

### [`00793960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md) → [`00793d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md) FUN_00793d3c

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00793868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793868.md) [`007948d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007948d8.md) [`00794960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794960.md) · 呼出先 18件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00470880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00470/00470880.md) [`0048cec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048cec4.md) [`00615f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00615/00615f0c.md) [`00652500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00652/00652500.md)
- 新版 呼出元 3件 [`00793c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793c44.md) [`00794cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cb4.md) [`00794d3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d3c.md) · 呼出先 18件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00470ba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00470/00470ba0.md) [`0048d1e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1e4.md) [`006162bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00616/006162bc.md) [`006528b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00652/006528b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 83.24% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00794128",
      "incomplete_value": true,
      "site": "0079412c",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079426c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00793e9c"
      ]
    ],
    [
      "unmatched:00793e98",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "007943fc"
      ]
    ],
    [
      "007943a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00793fd4"
      ]
    ]
  ],
  "added": [
    [
      "0079426c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00794278"
      ]
    ],
    [
      "00794274",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "007943fc"
      ]
    ],
    [
      "007943a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007943b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079412c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md#insn-0079412c) · [`007939b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md#insn-007939b4) · [`007939b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00793/00793960.md#insn-007939b8)
- 新版 [`00794508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md#insn-00794508) · [`00793d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md#insn-00793d90) · [`00793d94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00793/00793d3c.md#insn-00793d94)

~~~diff
- 0079412c ["INT_ADD", "register:40f0:8", ["const:79412c:8", "const:4:8"]]
- 0079412c ["CALL", null, ["callee:006528b0:8"]]
+ 00794508 ["INT_ADD", "register:40f0:8", ["const:794508:8", "const:4:8"]]
+ 00794508 ["CALL", null, ["callee:006528b0:8"]]
- 0079412c bytes f5f8fa97
+ 00794508 bytes eaf8fa97
- 007939b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 007939b4 ["CBRANCH", null, ["local:b112:8", "tmp:0:1"]]
+ 00793d90 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00793d90 ["CBRANCH", null, ["local:b113:8", "tmp:0:1"]]
- 007939b4 bytes 41370054
+ 00793d90 bytes 41370054
- 007939b8 ["INT_ADD", "register:40f0:8", ["const:7939b8:8", "const:4:8"]]
- 007939b8 ["CALL", null, ["callee:008524fc:8"]]
+ 00793d94 ["INT_ADD", "register:40f0:8", ["const:793d94:8", "const:4:8"]]
+ 00793d94 ["CALL", null, ["callee:008524fc:8"]]
- 007939b8 bytes e6f60294
+ 00793d94 bytes daf90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2779ae1a12a9100246b3a53983859f73"></a>

### [`007941cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007941cc.md) → [`007945a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/007945a8.md) FUN_007945a8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`0072a374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0072a/0072a374.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0072a724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0072a/0072a724.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 84.62% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-026112a1205d5f1ffc727bceebdabec4"></a>

### [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md) → [`00794608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794608.md) FUN_00794608

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0079127c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/0079127c.md) [`00791968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791968.md) [`00791eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00791/00791eb8.md) [`007924dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00792/007924dc.md) · 呼出先 16件 [`0047e91c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047e91c.md) [`0047edf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047e/0047edf4.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`0054079c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054079c.md) [`0063678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00636/0063678c.md)
- 新版 呼出元 4件 [`00791658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791658.md) [`00791d44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00791/00791d44.md) [`00792294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/00792294.md) [`007928b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00792/007928b8.md) · 呼出先 16件 [`0047ec3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047e/0047ec3c.md) [`0047f114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047f/0047f114.md) [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) [`00540abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540abc.md) [`00636b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00636/00636b3c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 94.79% / 新版 95.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00794230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00794230"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00794234"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00794230",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00794234",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00794238",
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
      "0079460c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00794610",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00794614",
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

- 旧版 [`00794230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md#insn-00794230) · [`00794234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md#insn-00794234) · [`00794238`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md#insn-00794238)

~~~diff
- 00794230 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00794230 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00794230 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00794230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00794230 bytes fd7b0aa9
- 00794234 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00794234 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00794234 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00794234 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00794234 bytes fc6f0ba9
- 00794238 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00794238 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00794238 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00794238 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00794238 bytes fa670ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7d4f77baa209b33c2979dcc4c3c5b72"></a>

### [`00794888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794888.md) → [`00794c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c64.md) FUN_00794c64

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00794c88",
      "incomplete_value": false,
      "site": "00794c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007948ac",
      "incomplete_value": false,
      "site": "007948ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00794c88",
      "DATA",
      [
        "storage",
        "00c79c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794c88",
      "DATA",
      [
        "storage",
        "00c7ac08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079489c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794888.md#insn-0079489c) · [`007948a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794888.md#insn-007948a4) · [`007948a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794888.md#insn-007948a8)
- 新版 [`00794c78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c64.md#insn-00794c78) · [`00794c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c64.md#insn-00794c80) · [`00794c84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c64.md#insn-00794c84)

~~~diff
- 0079489c ["INT_ADD", "register:40f0:8", ["const:79489c:8", "const:4:8"]]
- 0079489c ["CALL", null, ["callee:00c58f30:8"]]
+ 00794c78 ["INT_ADD", "register:40f0:8", ["const:794c78:8", "const:4:8"]]
+ 00794c78 ["CALL", null, ["callee:00c58f30:8"]]
- 0079489c bytes b10d1394
+ 00794c78 bytes ae101394
- 007948a4 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 00794c80 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 007948a4 bytes 282700b0
+ 00794c80 bytes 282700d0
- 007948a8 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 007948a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007948a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007948a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00794c84 ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 00794c84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00794c84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00794c84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007948a8 bytes 08e13091
+ 00794c84 bytes 08213091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-171a5bb5af5351c087e3824e803e8538"></a>

### [`007948bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007948bc.md) → [`00794c98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c98.md) FUN_00794c98

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00794ca4",
      "incomplete_value": false,
      "site": "00794ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007948c8",
      "incomplete_value": false,
      "site": "007948c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "00794ca4",
      "DATA",
      [
        "storage",
        "00c79c38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794ca4",
      "DATA",
      [
        "storage",
        "00c7ac08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007948c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007948bc.md#insn-007948c0) · [`007948c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/007948bc.md#insn-007948c4)
- 新版 [`00794c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c98.md#insn-00794c9c) · [`00794ca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794c98.md#insn-00794ca0)

~~~diff
- 007948c0 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 00794c9c ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 007948c0 bytes 292700b0
+ 00794c9c bytes 292700d0
- 007948c4 ["COPY", "tmp:0:8", ["const:c38:8"]]
- 007948c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007948c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007948c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00794ca0 ["COPY", "tmp:0:8", ["const:c08:8"]]
+ 00794ca0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00794ca0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00794ca0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007948c4 bytes 29e13091
+ 00794ca0 bytes 29213091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30ff2d5b2b38b8eefb91b5fddbc589fd"></a>

### [`00794910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794910.md) → [`00794cec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cec.md) FUN_00794cec

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "00794d10",
      "incomplete_value": false,
      "site": "00794d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794934",
      "incomplete_value": false,
      "site": "00794934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "00794d10",
      "DATA",
      [
        "storage",
        "00c79cb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794d10",
      "DATA",
      [
        "storage",
        "00c7ac88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794910.md#insn-00794924) · [`0079492c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794910.md#insn-0079492c) · [`00794930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794910.md#insn-00794930)
- 新版 [`00794d00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cec.md#insn-00794d00) · [`00794d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cec.md#insn-00794d08) · [`00794d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794cec.md#insn-00794d0c)

~~~diff
- 00794924 ["INT_ADD", "register:40f0:8", ["const:794924:8", "const:4:8"]]
- 00794924 ["CALL", null, ["callee:00c58f30:8"]]
+ 00794d00 ["INT_ADD", "register:40f0:8", ["const:794d00:8", "const:4:8"]]
+ 00794d00 ["CALL", null, ["callee:00c58f30:8"]]
- 00794924 bytes 8f0d1394
+ 00794d00 bytes 8c101394
- 0079492c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 00794d08 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079492c bytes 282700b0
+ 00794d08 bytes 282700d0
- 00794930 ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 00794930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00794930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00794930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00794d0c ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00794d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00794d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00794d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00794930 bytes 08e13291
+ 00794d0c bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2add9cc42715ab0fb8ed74952b210223"></a>

### [`00794944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794944.md) → [`00794d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d20.md) FUN_00794d20

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00794d2c",
      "incomplete_value": false,
      "site": "00794d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794950",
      "incomplete_value": false,
      "site": "00794950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "00794d2c",
      "DATA",
      [
        "storage",
        "00c79cb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00794d2c",
      "DATA",
      [
        "storage",
        "00c7ac88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794944.md#insn-00794948) · [`0079494c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794944.md#insn-0079494c)
- 新版 [`00794d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d20.md#insn-00794d24) · [`00794d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d20.md#insn-00794d28)

~~~diff
- 00794948 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 00794d24 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 00794948 bytes 292700b0
+ 00794d24 bytes 292700d0
- 0079494c ["COPY", "tmp:0:8", ["const:cb8:8"]]
- 0079494c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079494c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079494c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00794d28 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00794d28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00794d28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00794d28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079494c bytes 29e13291
+ 00794d28 bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c04ec256e6b31d4c144a4edd0c0db82"></a>

### [`00794bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md) → [`00794fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fa0.md) FUN_00794fa0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00794994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794994.md) [`0080d8b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0080d/0080d8b8.md) [`00b2ac68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b2a/00b2ac68.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 3件 [`00794d70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794d70.md) [`0080e81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0080e/0080e81c.md) [`00b2bc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b2b/00b2bc5c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00794fac",
      "incomplete_value": false,
      "site": "00794fb0",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00794bd0",
      "incomplete_value": false,
      "site": "00794bd4",
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
            "const:f8c:8"
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
      "00794fac",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00794fac",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794bd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md#insn-00794bd4) · [`00794bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md#insn-00794bcc) · [`00794bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794bc4.md#insn-00794bd0)
- 新版 [`00794fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fa0.md#insn-00794fb0) · [`00794fa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fa0.md#insn-00794fa8) · [`00794fac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794fa0.md#insn-00794fac)

~~~diff
- 00794bd4 ["INT_ADD", "register:40f0:8", ["const:794bd4:8", "const:4:8"]]
- 00794bd4 ["CALL", null, ["callee:0043bad8:8"]]
+ 00794fb0 ["INT_ADD", "register:40f0:8", ["const:794fb0:8", "const:4:8"]]
+ 00794fb0 ["CALL", null, ["callee:0043bad8:8"]]
- 00794bd4 bytes f99af297
+ 00794fb0 bytes ca9af297
- 00794bcc ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00794fa8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 00794bcc bytes 00d9fff0
+ 00794fa8 bytes 20d9ff90
- 00794bd0 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 00794bd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00794bd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00794bd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00794fac ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00794fac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00794fac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00794fac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00794bd0 bytes 00303e91
+ 00794fac bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a5abf4152b5a0eb0115b56cbdc45072"></a>

### [`00794da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md) → [`00795180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795180.md) FUN_00795180

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00794c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794c80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0079505c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079505c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 93.40% / 新版 93.40%

CFGの説明率　旧版 52.38% / 新版 52.38%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

アドレスに依存する影響 `unresolved_branch_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00794dac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00794e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00794e8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00794dac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079519c"
      ]
    ],
    [
      "unmatched:00794e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007951dc"
      ]
    ],
    [
      "unmatched:00794e8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795248"
      ]
    ]
  ],
  "added": [
    [
      "00795188",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079519c"
      ]
    ],
    [
      "007951e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007951dc"
      ]
    ],
    [
      "00795268",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795248"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00794dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md#insn-00794dac) · [`00794e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md#insn-00794e08) · [`00794e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/00794da4.md#insn-00794e8c)

~~~diff
- 00794dac ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00794dac bytes a0000054
- 00794e08 ["INT_NOTEQUAL", "tmp:0:1", ["register:4060:8", "const:0:8"]]
- 00794e08 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00794e08 bytes ccffffb5
- 00794e8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 00794e8c ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00794e8c bytes 0bffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8fa78b5f5146f7edea50c8db1b76b66"></a>

### [`00795000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795000.md) → [`007953dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007953dc.md) FUN_007953dc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "007953e8",
      "incomplete_value": false,
      "site": "007953f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079500c",
      "incomplete_value": false,
      "site": "00795018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "007953f4",
      "DATA",
      [
        "storage",
        "00c79d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007953f4",
      "DATA",
      [
        "storage",
        "00c7ad08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795000.md#insn-00795008) · [`0079500c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795000.md#insn-0079500c)
- 新版 [`007953e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007953dc.md#insn-007953e4) · [`007953e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/007953dc.md#insn-007953e8)

~~~diff
- 00795008 ["COPY", "register:4050:8", ["const:c79000:8"]]
+ 007953e4 ["COPY", "register:4050:8", ["const:c7a000:8"]]
- 00795008 bytes 2a270090
+ 007953e4 bytes 2a2700b0
- 0079500c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0079500c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079500c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079500c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 007953e8 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 007953e8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 007953e8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 007953e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079500c bytes 4ae13491
+ 007953e8 bytes 4a213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214eaab0a36acbfec4b0c15362eaef66"></a>

### [`00795044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795044.md) → [`00795420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795420.md) FUN_00795420

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 75.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00795438",
      "incomplete_value": false,
      "site": "00795444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079505c",
      "incomplete_value": false,
      "site": "00795068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "00795444",
      "DATA",
      [
        "storage",
        "00c79d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00795444",
      "DATA",
      [
        "storage",
        "00c7ad08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795044.md#insn-00795058) · [`0079505c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795044.md#insn-0079505c) · [`0079508c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795044.md#insn-0079508c)
- 新版 [`00795434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795420.md#insn-00795434) · [`00795438`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795420.md#insn-00795438) · [`00795468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795420.md#insn-00795468)

~~~diff
- 00795058 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 00795434 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 00795058 bytes 28270090
+ 00795434 bytes 282700b0
- 0079505c ["COPY", "tmp:0:8", ["const:d38:8"]]
- 0079505c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079505c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079505c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00795438 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00795438 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00795438 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00795438 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079505c bytes 08e13491
+ 00795438 bytes 08213491
- 0079508c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079508c ["INT_ADD", "register:40f0:8", ["const:79508c:8", "const:4:8"]]
- 0079508c ["CALLIND", null, ["register:0:8"]]
+ 00795468 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00795468 ["INT_ADD", "register:40f0:8", ["const:795468:8", "const:4:8"]]
+ 00795468 ["CALLIND", null, ["register:0:8"]]
- 0079508c bytes 00013fd6
+ 00795468 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7638a8626577ff4ac5405977886913b2"></a>

### [`007950a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007950a0.md) → [`0079547c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079547c.md) FUN_0079547c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.52% / 新版 65.52%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007950cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007954a8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007950d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007950cc",
      "DATA",
      [
        "storage",
        "00c79d38",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:007950d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007954c8"
      ]
    ],
    [
      "unmatched:007950dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007954d0"
      ]
    ]
  ],
  "added": [
    [
      "007954a8",
      "DATA",
      [
        "storage",
        "00c7ad08",
        null,
        "undefined *"
      ]
    ],
    [
      "007954ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007954c8"
      ]
    ],
    [
      "007954b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007954d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007950cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007950a0.md#insn-007950cc) · [`007950d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007950a0.md#insn-007950d0) · [`007950dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007950a0.md#insn-007950dc)

~~~diff
- 007950cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 007950cc ["COPY", "tmp:1:8", ["register:4008:8"]]
- 007950cc ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 007950cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 007950cc bytes 280401f8
- 007950d0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 007950d0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 007950d0 bytes e00000b4
- 007950dc ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 007950dc bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c42c754bcd5bef3481e64ad8e485063"></a>

### [`00795128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795128.md) → [`00795504`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795504.md) FUN_00795504

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 28.57% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795128"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079512c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00795128",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079512c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00795144",
      "DATA",
      [
        "storage",
        "00c79d38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00795504",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00795508",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00795520",
      "DATA",
      [
        "storage",
        "00c7ad08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795128.md#insn-00795128) · [`0079512c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795128.md#insn-0079512c) · [`00795144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795128.md#insn-00795144)

~~~diff
- 00795128 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00795128 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00795128 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00795128 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00795128 bytes fd7bbea9
- 0079512c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079512c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0079512c bytes f30b00f9
- 00795144 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00795144 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00795144 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00795144 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00795144 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac805ebf892cf10e77d541aab4a93cf6"></a>

### [`00795224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795224.md) → [`00795600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795600.md) FUN_00795600

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 76.00% / 新版 76.00%

CFGの説明率　旧版 33.33% / 新版 36.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00795234"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079523c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00795268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00795234",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795640"
      ]
    ],
    [
      "unmatched:0079523c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079562c"
      ]
    ],
    [
      "00795620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "00795610",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00795640"
      ]
    ],
    [
      "00795618",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079562c"
      ]
    ],
    [
      "00795620",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795224.md#insn-00795234) · [`0079523c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795224.md#insn-0079523c) · [`00795244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795224.md#insn-00795244)
- 新版 [`00795620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795600.md#insn-00795620)

~~~diff
- 00795234 ["CBRANCH", null, ["local:b8:8", "register:101:1"]]
- 00795234 bytes 80010054
- 0079523c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 0079523c bytes a0000054
- 00795244 ["INT_ADD", "register:40f0:8", ["const:795244:8", "const:4:8"]]
- 00795244 ["CALL", null, ["ram:47ad34:8"]]
+ 00795620 ["INT_ADD", "register:40f0:8", ["const:795620:8", "const:4:8"]]
+ 00795620 ["CALL", null, ["ram:47b054:8"]]
- 00795244 bytes bc96f397
+ 00795620 bytes 8d96f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae19182be840c5c3dea9e4d72da0d975"></a>

### [`007952b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md) → [`0079568c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079568c.md) FUN_0079568c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079422c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00794/0079422c.md) · 呼出先 8件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007954ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007954ac.md) [`007956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00794608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00794/00794608.md) · 呼出先 8件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00795888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795888.md) [`00795aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795aa8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.29% / 新版 87.29%

CFGの説明率　旧版 52.27% / 新版 53.49%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007952b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007952b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "007952b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007952b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:007952b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:007952bc",
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
      "00795690",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00795694",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00795698",
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

- 旧版 [`007952b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-007952b4) · [`007952b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-007952b8) · [`007952bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md#insn-007952bc)

~~~diff
- 007952b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 007952b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 007952b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 007952b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007952b4 bytes fd7b03a9
- 007952b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 007952b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 007952b8 bytes f92300f9
- 007952bc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 007952bc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 007952bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 007952bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 007952bc bytes f85f05a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbc5b0448db53627a8580f466867dcb8"></a>

### [`007956cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md) → [`00795aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795aa8.md) FUN_00795aa8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`007952b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007952b0.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0079568c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/0079568c.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00795ab4",
      "incomplete_value": false,
      "site": "00795ab8",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007956d8",
      "incomplete_value": false,
      "site": "007956dc",
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
            "const:f8c:8"
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
      "00795ab4",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00795ab4",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007956dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md#insn-007956dc) · [`007956d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md#insn-007956d4) · [`007956d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/007956cc.md#insn-007956d8)
- 新版 [`00795ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795aa8.md#insn-00795ab8) · [`00795ab0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795aa8.md#insn-00795ab0) · [`00795ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795aa8.md#insn-00795ab4)

~~~diff
- 007956dc ["INT_ADD", "register:40f0:8", ["const:7956dc:8", "const:4:8"]]
- 007956dc ["CALL", null, ["callee:0043bad8:8"]]
+ 00795ab8 ["INT_ADD", "register:40f0:8", ["const:795ab8:8", "const:4:8"]]
+ 00795ab8 ["CALL", null, ["callee:0043bad8:8"]]
- 007956dc bytes 3798f297
+ 00795ab8 bytes 0898f297
- 007956d4 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 00795ab0 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 007956d4 bytes 00d9ffd0
+ 00795ab0 bytes 00d9fff0
- 007956d8 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 007956d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007956d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007956d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00795ab4 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 00795ab4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00795ab4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00795ab4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007956d8 bytes 00303e91
+ 00795ab4 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e3c3e57d8e566139280b52e708f931e"></a>

### [`00795aec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795aec.md) → [`00795ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00795/00795ec8.md) _INIT_138

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 79.10% / 新版 79.10%

CFGの説明率　旧版 61.11% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795b1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795b30"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795b34"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00795b1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00795b28",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00795b30",
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
      "00795ef8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00795f04",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00795f0c",
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

- 旧版 [`00795b1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795aec.md#insn-00795b1c) · [`00795b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795aec.md#insn-00795b30) · [`00795b34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795aec.md#insn-00795b34)

~~~diff
- 00795b1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00795b1c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00795b1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00795b1c bytes a9831ff8
- 00795b30 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00795b30 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00795b30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00795b30 bytes ea130278
- 00795b34 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00795b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00795b34 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9819ba14ea68b4c734eaef3d88c800b0"></a>

### [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) → [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) FUN_00796258

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 22件 [`0059aa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059aa68.md) [`0059b178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b178.md) [`005adbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ad/005adbd0.md) [`005aecd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ae/005aecd4.md) [`005b2214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2214.md) · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00796280",
      "incomplete_value": true,
      "site": "00796280",
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
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00795ea4",
      "incomplete_value": true,
      "site": "00795ea4",
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
            "const:fd0:8"
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
      "definition_site": "0079626c",
      "incomplete_value": true,
      "site": "0079626c",
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
      "definition_site": "00795e90",
      "incomplete_value": true,
      "site": "00795e90",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00795e90"
      ],
      [
        "FALL_THROUGH",
        "0079626c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0079626c",
      "incomplete_value": true,
      "site": "00796278",
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
      "definition_site": "00795e90",
      "incomplete_value": true,
      "site": "00795e9c",
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
      "00796268",
      "READ",
      [
        "storage",
        "00ca7fd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00796280",
      "WRITE",
      [
        "storage",
        "00ca7fd0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00796268",
      "READ",
      [
        "storage",
        "00ca8f90",
        null,
        "undefined8"
      ]
    ],
    [
      "00796280",
      "WRITE",
      [
        "storage",
        "00ca8f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00795ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md#insn-00795ea4) · [`00795e88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md#insn-00795e88) · [`00795e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md#insn-00795e8c)
- 新版 [`00796280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md#insn-00796280) · [`00796264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md#insn-00796264) · [`00796268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md#insn-00796268)

~~~diff
- 00795ea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd0:8"]]
- 00795ea4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00796280 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f90:8"]]
+ 00796280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00795ea4 bytes 60ea07f9
+ 00796280 bytes 60ca07f9
- 00795e88 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 00796264 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 00795e88 bytes 932800d0
+ 00796264 bytes 932800d0
- 00795e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fd0:8"]]
- 00795e8c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00796268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:f90:8"]]
+ 00796268 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00795e8c bytes 60ea47f9
+ 00796268 bytes 60ca47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac39ad3ecec4e302855e40abd7d3d2f"></a>

### [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md) → [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md) FUN_00796290

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 18件 [`005b1e64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b1/005b1e64.md) [`005b279c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b2/005b279c.md) [`005b3638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3638.md) [`005b3bb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b3/005b3bb4.md) [`005b4060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b4/005b4060.md) · 呼出先 2件 [`0079615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md)
- 新版 呼出元 18件 [`005b2214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2214.md) [`005b2b4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b2/005b2b4c.md) [`005b39e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b39e8.md) [`005b3f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b3/005b3f64.md) [`005b4410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b4/005b4410.md) · 呼出先 2件 [`00796538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796538.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md)

変更の種類 call_argument_candidate, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 40.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795ec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00795ec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "007962a0"
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
      "unmatched:00795ec4",
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
      "007962a0",
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

- 旧版 [`00795ec4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md#insn-00795ec4) · [`00795ef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md#insn-00795ef4)
- 新版 [`007962d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md#insn-007962d0) · [`007962a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md#insn-007962a0)

~~~diff
- 00795ec4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00795ec4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00795ec4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00795ec4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00795ec4 bytes f44f02a9
- 00795ef4 ["INT_ADD", "register:40f0:8", ["const:795ef4:8", "const:4:8"]]
- 00795ef4 ["CALL", null, ["callee:00c54d60:8"]]
+ 007962d0 ["INT_ADD", "register:40f0:8", ["const:7962d0:8", "const:4:8"]]
+ 007962d0 ["CALL", null, ["callee:00c54d60:8"]]
- 00795ef4 bytes 9ff71294
+ 007962d0 bytes a4fa1294
+ 007962a0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
+ 007962a0 ["COPY", "tmp:1:8", ["register:4098:8"]]
+ 007962a0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
+ 007962a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 007962a0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b0373e5d6c33ee4927a6f3a131be2ec"></a>

### [`00795f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md) → [`00796310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796310.md) FUN_00796310

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 4件 [`0059a748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059a748.md) [`0059ae58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059a/0059ae58.md) [`005ad820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ad/005ad820.md) [`005ae924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ae/005ae924.md) · 呼出先 3件 [`0079603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 4件 [`0059aa68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059a/0059aa68.md) [`0059b178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059b178.md) [`005adbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ad/005adbd0.md) [`005aecd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005ae/005aecd4.md) · 呼出先 3件 [`00796418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796418.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 89.29% / 新版 92.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00795f4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-00795f4c) · [`00795f90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-00795f90) · [`00795f98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md#insn-00795f98)
- 新版 [`00796328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796310.md#insn-00796328) · [`0079636c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796310.md#insn-0079636c) · [`00796374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796310.md#insn-00796374)

~~~diff
- 00795f4c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00795f4c ["CBRANCH", null, ["local:b17:8", "tmp:0:1"]]
+ 00796328 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00796328 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00795f4c bytes e80600b4
+ 00796328 bytes e80600b4
- 00795f90 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00795f90 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 0079636c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0079636c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00795f90 bytes e1010054
+ 0079636c bytes e1010054
- 00795f98 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
+ 00796374 ["CBRANCH", null, ["local:b16:8", "register:101:1"]]
- 00795f98 bytes 80040054
+ 00796374 bytes 80040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe280fa4210e765f67e16b93f81fb956"></a>

### [`0079603c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md) → [`00796418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796418.md) FUN_00796418

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00795f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795f34.md) · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00796310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796310.md) · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 87.50% / 新版 91.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0079612c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079650c",
      "incomplete_value": true,
      "site": "00796510",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": null,
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00796508"
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
      "unmatched:0079612c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00796508",
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

- 旧版 [`0079612c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md#insn-0079612c) · [`00796134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079603c.md#insn-00796134)
- 新版 [`00796510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796418.md#insn-00796510) · [`00796508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796418.md#insn-00796508)

~~~diff
- 0079612c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079612c ["INT_ADD", "register:40f0:8", ["const:79612c:8", "const:4:8"]]
- 0079612c ["CALLIND", null, ["register:0:8"]]
- 0079612c bytes 00013fd6
- 00796134 ["INT_ADD", "register:40f0:8", ["const:796134:8", "const:4:8"]]
- 00796134 ["CALL", null, ["callee:00c58f20:8"]]
+ 00796510 ["INT_ADD", "register:40f0:8", ["const:796510:8", "const:4:8"]]
+ 00796510 ["CALL", null, ["callee:00c58f20:8"]]
- 00796134 bytes 87071394
+ 00796510 bytes 840a1394
+ 00796508 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00796508 ["INT_ADD", "register:40f0:8", ["const:796508:8", "const:4:8"]]
+ 00796508 ["CALLIND", null, ["register:0:8"]]
+ 00796508 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68af3f10736d5dc30a1c180cad49bffd"></a>

### [`0079615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md) → [`00796538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796538.md) FUN_00796538

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md) · 呼出先 7件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`007962b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md) · 呼出先 7件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`00796694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796694.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 88.51% / 新版 88.51%

CFGの説明率　旧版 70.97% / 新版 73.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007961a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007961b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "007961b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:007961b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007965b0"
      ]
    ],
    [
      "unmatched:007961c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00796690"
      ]
    ]
  ],
  "added": [
    [
      "00796594",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007965b0"
      ]
    ],
    [
      "0079659c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00796690"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007961a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-007961a8) · [`007961b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-007961b4) · [`007961b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md#insn-007961b8)

~~~diff
- 007961a8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 007961a8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 007961a8 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 007961a8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 007961a8 bytes 4881889a
- 007961b4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 007961b4 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 007961b4 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 007961b4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 007961b4 bytes 1831899a
- 007961b8 ["INT_EQUAL", "tmp:0:1", ["register:40c0:8", "const:0:8"]]
- 007961b8 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 007961b8 bytes f80000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68e62050fb7731d47fcf8e959509aad9"></a>

### [`007962b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md) → [`00796694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796694.md) FUN_00796694

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079615c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079615c.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`00796538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796538.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007966a0",
      "incomplete_value": false,
      "site": "007966a4",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007962c4",
      "incomplete_value": false,
      "site": "007962c8",
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
            "const:f8c:8"
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
      "007966a0",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007966a0",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007962c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md#insn-007962c8) · [`007962c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md#insn-007962c0) · [`007962c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962b8.md#insn-007962c4)
- 新版 [`007966a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796694.md#insn-007966a4) · [`0079669c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796694.md#insn-0079669c) · [`007966a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796694.md#insn-007966a0)

~~~diff
- 007962c8 ["INT_ADD", "register:40f0:8", ["const:7962c8:8", "const:4:8"]]
- 007962c8 ["CALL", null, ["callee:0043bad8:8"]]
+ 007966a4 ["INT_ADD", "register:40f0:8", ["const:7966a4:8", "const:4:8"]]
+ 007966a4 ["CALL", null, ["callee:0043bad8:8"]]
- 007962c8 bytes 3c95f297
+ 007966a4 bytes 0d95f297
- 007962c0 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0079669c ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 007962c0 bytes 00d9ffb0
+ 0079669c bytes 00d9ffd0
- 007962c4 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 007962c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007962c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007962c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007966a0 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 007966a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007966a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007966a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007962c4 bytes 00303e91
+ 007966a0 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-453c5dbd35decc130aa39420de91d8fc"></a>

### [`007962cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962cc.md) → [`007966a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/007966a8.md) _INIT_139

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

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
      "definition_site": "007966e4",
      "incomplete_value": true,
      "site": "00796700",
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
                "const:35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796308",
      "incomplete_value": true,
      "site": "00796324",
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
                "const:f66:8"
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
      "definition_site": "00796708",
      "incomplete_value": true,
      "site": "00796724",
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
                "const:48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079632c",
      "incomplete_value": true,
      "site": "00796348",
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
                "const:f79:8"
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
      "definition_site": "00796728",
      "incomplete_value": true,
      "site": "00796744",
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
                "const:e3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079634c",
      "incomplete_value": true,
      "site": "00796368",
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
                "const:d6e:8"
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
      "007966e4",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "00796708",
      "READ",
      [
        "storage",
        "002b7f79",
        null,
        "string"
      ]
    ],
    [
      "00796728",
      "READ",
      [
        "storage",
        "002b8d6e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007966e4",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00796708",
      "READ",
      [
        "storage",
        "002b8048",
        null,
        "string"
      ]
    ],
    [
      "00796728",
      "READ",
      [
        "storage",
        "002b8e3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079642c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962cc.md#insn-0079642c) · [`00796500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962cc.md#insn-00796500) · [`007962f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/007962cc.md#insn-007962f4)
- 新版 [`00796808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/007966a8.md#insn-00796808) · [`007968dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/007966a8.md#insn-007968dc) · [`007966d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/007966a8.md#insn-007966d0)

~~~diff
- 0079642c ["INT_ADD", "register:40f0:8", ["const:79642c:8", "const:4:8"]]
- 0079642c ["CALL", null, ["callee:0043bb58:8"]]
+ 00796808 ["INT_ADD", "register:40f0:8", ["const:796808:8", "const:4:8"]]
+ 00796808 ["CALL", null, ["callee:0043bb58:8"]]
- 0079642c bytes 0395f297
+ 00796808 bytes d494f297
- 00796500 ["INT_ADD", "register:40f0:8", ["const:796500:8", "const:4:8"]]
- 00796500 ["CALL", null, ["callee:00c58ed0:8"]]
+ 007968dc ["INT_ADD", "register:40f0:8", ["const:7968dc:8", "const:4:8"]]
+ 007968dc ["CALL", null, ["callee:00c58ed0:8"]]
- 00796500 bytes 80061394
+ 007968dc bytes 7d091394
- 007962f4 ["COPY", "register:4098:8", ["const:ca7000:8"]]
+ 007966d0 ["COPY", "register:4098:8", ["const:ca8000:8"]]
- 007962f4 bytes 932800b0
+ 007966d0 bytes 932800d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1725d8c1a91af68949b0d47f5c2437bd"></a>

### [`0079668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md) → [`00796a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a68.md) FUN_00796a68

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079665c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`00797024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md)
- 新版 呼出元 1件 [`00796a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a38.md) · 呼出先 11件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`00797400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797400.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 57.97% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00796a1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00796a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00796df8"
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
      "00796c10",
      "PARAM",
      [
        "storage",
        "002a0170",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00796870",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "unmatched:00796884",
      "PARAM",
      [
        "storage",
        "00ca8008",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00796c10",
      "PARAM",
      [
        "storage",
        "002a01b0",
        null,
        "string"
      ]
    ],
    [
      "00796c4c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007647b8"
      ]
    ],
    [
      "00796c60",
      "PARAM",
      [
        "storage",
        "00ca8fc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md#insn-0079673c) · [`00796768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md#insn-00796768) · [`00796838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md#insn-00796838)
- 新版 [`00796b44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a68.md#insn-00796b44) · [`00796c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a68.md#insn-00796c14)

~~~diff
- 0079673c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0079673c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0079673c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0079673c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0079673c bytes 7633999a
- 00796768 ["INT_ADD", "register:40f0:8", ["const:796768:8", "const:4:8"]]
- 00796768 ["CALL", null, ["callee:00c590f0:8"]]
+ 00796b44 ["INT_ADD", "register:40f0:8", ["const:796b44:8", "const:4:8"]]
+ 00796b44 ["CALL", null, ["callee:00c590f0:8"]]
- 00796768 bytes 6e061394
+ 00796b44 bytes 6b091394
- 00796838 ["INT_ADD", "register:40f0:8", ["const:796838:8", "const:4:8"]]
- 00796838 ["CALL", null, ["callee:00442c90:8"]]
+ 00796c14 ["INT_ADD", "register:40f0:8", ["const:796c14:8", "const:4:8"]]
+ 00796c14 ["CALL", null, ["callee:00442c90:8"]]
- 00796838 bytes 4eb0f297
+ 00796c14 bytes 1fb0f297
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06480a46d57fb66f9a88da25e6bcb497"></a>

### [`00796b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md) → [`00796f2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796f2c.md) FUN_00796f2c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079665c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079665c.md) · 呼出先 7件 [`007842d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00784/007842d8.md) [`00878448`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00878/00878448.md) [`008792f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00879/008792f4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c5a900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a900.md)
- 新版 呼出元 1件 [`00796a38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a38.md) · 呼出先 7件 [`007846b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00784/007846b4.md) [`008793f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00879/008793f4.md) [`0087a2a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0087a/0087a2a0.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b8d0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.10% / 新版 86.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 9件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00796f68",
      "incomplete_value": false,
      "site": "00796f70",
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
            "const:413:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796b8c",
      "incomplete_value": false,
      "site": "00796b94",
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
            "const:344:8"
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
      "definition_site": "00796f90",
      "incomplete_value": false,
      "site": "00796f98",
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
            "const:176:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796bb4",
      "incomplete_value": false,
      "site": "00796bbc",
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
            "const:98:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00796fec",
      "incomplete_value": false,
      "site": "00796ff4",
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
            "const:54a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00796c10",
      "incomplete_value": false,
      "site": "00796c18",
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
            "const:47f:8"
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
      "00796f70",
      "DATA",
      [
        "storage",
        "002b9344",
        null,
        "string"
      ]
    ],
    [
      "00796f98",
      "DATA",
      [
        "storage",
        "002b4098",
        null,
        "string"
      ]
    ],
    [
      "00796fdc",
      "PARAM",
      [
        "storage",
        "00ca8008",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00796f70",
      "DATA",
      [
        "storage",
        "002b9413",
        null,
        "string"
      ]
    ],
    [
      "00796f98",
      "DATA",
      [
        "storage",
        "002b4176",
        null,
        "string"
      ]
    ],
    [
      "00796fdc",
      "PARAM",
      [
        "storage",
        "00ca8fc8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00796c08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md#insn-00796c08) · [`00796cf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md#insn-00796cf4) · [`00796da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/00796b50.md#insn-00796da8)
- 新版 [`00796fe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796f2c.md#insn-00796fe4) · [`007970d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796f2c.md#insn-007970d0)

~~~diff
- 00796c08 ["INT_ADD", "register:40f0:8", ["const:796c08:8", "const:4:8"]]
- 00796c08 ["CALL", null, ["callee:007846b4:8"]]
+ 00796fe4 ["INT_ADD", "register:40f0:8", ["const:796fe4:8", "const:4:8"]]
+ 00796fe4 ["CALL", null, ["callee:007846b4:8"]]
- 00796c08 bytes b4b5ff97
+ 00796fe4 bytes b4b5ff97
- 00796cf4 ["INT_ADD", "register:40f0:8", ["const:796cf4:8", "const:4:8"]]
- 00796cf4 ["CALL", null, ["callee:0087a2a0:8"]]
+ 007970d0 ["INT_ADD", "register:40f0:8", ["const:7970d0:8", "const:4:8"]]
+ 007970d0 ["CALL", null, ["callee:0087a2a0:8"]]
- 00796cf4 bytes 80890394
+ 007970d0 bytes 748c0394
- 00796da8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:68:8"]]
- 00796da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00796da8 bytes e83700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baad93a68f562dc18c4fe1aa508abc03"></a>

### [`00797024`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md) → [`00797400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797400.md) FUN_00797400

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079668c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00796/0079668c.md) · 呼出先 14件 [`0048796c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/0048796c.md) [`00487aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487aa4.md) [`00487e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00487/00487e60.md) [`00488698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00488/00488698.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md)
- 新版 呼出元 1件 [`00796a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796a68.md) · 呼出先 14件 [`00487c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487c8c.md) [`00487dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/00487dc4.md) [`00488180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/00488180.md) [`004889b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00488/004889b8.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 83.97% / 新版 83.97%

CFGの説明率　旧版 37.50% / 新版 34.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079704c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079704c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00797050",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00488180"
      ]
    ],
    [
      "unmatched:00797060",
      "DATA",
      [
        "storage",
        "00c64e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00797428",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0079742c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00488180"
      ]
    ],
    [
      "0079743c",
      "DATA",
      [
        "storage",
        "00c65dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079704c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md#insn-0079704c) · [`00797050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md#insn-00797050) · [`00797060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797024.md#insn-00797060)

~~~diff
- 0079704c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079704c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079704c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079704c bytes a8831ff8
- 00797050 ["INT_ADD", "register:40f0:8", ["const:797050:8", "const:4:8"]]
- 00797050 ["CALL", null, ["callee:00488180:8"]]
- 00797050 bytes 84c3f397
- 00797060 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:70:8"]]
- 00797060 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00797060 bytes e83b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-797bd88e2afe032765b6a22a70eb90d3"></a>

### [`007972ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007972ec.md) → [`007976c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/007976c8.md) _INIT_140

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00bc488c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc488c.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00bc5880`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc5/00bc5880.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_store_alignment

命令の説明率　旧版 75.96% / 新版 75.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 4件, `store_value` 6件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079731c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797334"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079731c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00797328",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00797330",
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
      "007976f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00797704",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "0079770c",
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

- 旧版 [`0079731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007972ec.md#insn-0079731c) · [`00797330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007972ec.md#insn-00797330) · [`00797334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007972ec.md#insn-00797334)

~~~diff
- 0079731c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0079731c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079731c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079731c bytes a9831ff8
- 00797330 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00797330 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00797330 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00797330 bytes ea130278
- 00797334 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00797334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00797334 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd04b1064cc95fb0e263f9b5c63a08ff"></a>

### [`007976f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007976f8.md) → [`00797ad4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797ad4.md) _INIT_141

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043aeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043a/0043aeb0.md) [`0043b838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b838.md) [`00c57f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f00.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043b1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043b1d0.md) [`0043bb58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bb58.md) [`00c58ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58ed0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.18% / 新版 84.18%

CFGの説明率　旧版 77.78% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00797728",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00797734",
      "READ",
      [
        "storage",
        "002b7f66",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00797750",
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
      "00797b04",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00797b10",
      "READ",
      [
        "storage",
        "002b8035",
        null,
        "string"
      ]
    ],
    [
      "00797b2c",
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

- 旧版 [`00797728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007976f8.md#insn-00797728) · [`00797750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007976f8.md#insn-00797750) · [`00797774`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/007976f8.md#insn-00797774)

~~~diff
- 00797728 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00797728 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00797728 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00797728 bytes a9831ff8
- 00797750 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00797750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00797750 bytes e013813c
- 00797774 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00797774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00797774 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21c3cbf6747bbef968585d8f27bdf289"></a>

### [`00797a88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md) → [`00797e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797e64.md) FUN_00797e64

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 2件 [`0079fe88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079fe88.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 2件 [`007a0264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0264.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00797ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md#insn-00797ad0) · [`00797ad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797a88.md#insn-00797ad8)
- 新版 [`00797eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797e64.md#insn-00797eac) · [`00797eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797e64.md#insn-00797eb4)

~~~diff
- 00797ad0 ["INT_ADD", "register:40f0:8", ["const:797ad0:8", "const:4:8"]]
- 00797ad0 ["CALL", null, ["callee:00c58f30:8"]]
+ 00797eac ["INT_ADD", "register:40f0:8", ["const:797eac:8", "const:4:8"]]
+ 00797eac ["CALL", null, ["callee:00c58f30:8"]]
- 00797ad0 bytes 24011394
+ 00797eac bytes 21041394
- 00797ad8 ["INT_ADD", "register:40f0:8", ["const:797ad8:8", "const:4:8"]]
- 00797ad8 ["CALL", null, ["callee:007a0264:8"]]
+ 00797eb4 ["INT_ADD", "register:40f0:8", ["const:797eb4:8", "const:4:8"]]
+ 00797eb4 ["CALL", null, ["callee:007a0264:8"]]
- 00797ad8 bytes ec200094
+ 00797eb4 bytes ec200094
~~~


<a id="compare-5777a382308fb2ae22057c1e905bc7b8"></a>

### [`00797b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md) → [`00797f0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md) FUN_00797f0c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0083a178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0083a/0083a178.md) [`00848608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00848/00848608.md) [`0085155c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/0085155c.md) · 呼出先 4件 [`0079d130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d130.md) [`0079d1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d1d0.md) [`0079d240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d240.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 3件 [`0083b124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0083b/0083b124.md) [`008495b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00849/008495b4.md) [`00852508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/00852508.md) · 呼出先 4件 [`0079d50c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d50c.md) [`0079d5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d5ac.md) [`0079d61c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d61c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 35.29% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00797b58"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00797f34"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00797b98",
      "incomplete_value": true,
      "site": "00797b9c",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00797b58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00797f48"
      ]
    ]
  ],
  "added": [
    [
      "00797f34",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00797f48"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00797b58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md#insn-00797b58) · [`00797b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797b30.md#insn-00797b9c)
- 新版 [`00797f78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md#insn-00797f78) · [`00797f34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797f0c.md#insn-00797f34)

~~~diff
- 00797b58 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00797b58 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00797b58 bytes a1000054
- 00797b9c ["INT_ADD", "register:40f0:8", ["const:797b9c:8", "const:4:8"]]
- 00797b9c ["CALL", null, ["callee:0079d50c:8"]]
+ 00797f78 ["INT_ADD", "register:40f0:8", ["const:797f78:8", "const:4:8"]]
+ 00797f78 ["CALL", null, ["callee:0079d50c:8"]]
- 00797b9c bytes 65150094
+ 00797f78 bytes 65150094
+ 00797f34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00797f34 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00797f34 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fb92617e7f103d8585bba0a63d56a7d"></a>

### [`00797bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md) → [`00797fb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00797/00797fb8.md) FUN_00797fb8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0079d2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d2b0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0088d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d124.md) [`00a8b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8b/00a8b47c.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`0079d68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d68c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 49.30% / 新版 51.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 3件, `unresolved_branch_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797c10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797d7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00797fec"
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
      "unmatched:00797c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00797c18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079803c"
      ]
    ],
    [
      "unmatched:00797c38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00798000"
      ]
    ]
  ],
  "added": [
    [
      "00797fec",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00797ff4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079803c"
      ]
    ],
    [
      "00798014",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00798000"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00797c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797c10) · [`00797c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797c18) · [`00797c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797bdc.md#insn-00797c38)

~~~diff
- 00797c10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00797c10 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00797c10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00797c10 bytes a8831ff8
- 00797c18 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00797c18 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00797c18 bytes 400200b4
- 00797c38 ["INT_NOTEQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00797c38 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00797c38 bytes 69ffffb5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c78c146f23e9d40ffafb53332ed94423"></a>

### [`00797e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md) → [`00798210`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798210.md) FUN_00798210

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0088c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0088c/0088c178.md) [`00a8a488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8a/00a8a488.md) · 呼出先 6件 [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00494650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494650.md) [`0057bee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0057b/0057bee8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`0088d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0088d/0088d124.md) [`00a8b47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8b/00a8b47c.md) · 呼出先 6件 [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00494970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494970.md) [`0057c208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0057c/0057c208.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 46.48% / 新版 46.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797e68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00797f0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00798244"
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
      "unmatched:00797e68",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:00797ea8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079829c"
      ]
    ],
    [
      "unmatched:00797ed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007982a4"
      ]
    ]
  ],
  "added": [
    [
      "00798244",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "00798284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079829c"
      ]
    ],
    [
      "007982ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "007982a4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00797e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797e68) · [`00797ea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797ea4) · [`00797ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00797/00797e34.md#insn-00797ea8)

~~~diff
- 00797e68 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00797e68 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00797e68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00797e68 bytes a8831ff8
- 00797ea4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00797ea4 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00797ea4 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00797ea4 ["COPY", "tmp:3:8", ["register:40c0:8"]]
- 00797ea4 bytes 16c3889a
- 00797ea8 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00797ea8 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00797ea8 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00797ea8 bytes cd000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab71b0ae735e2fdfb45d6b60a135ca2"></a>

### [`007980b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md) → [`00798494`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798494.md) FUN_00798494

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a8e624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8e/00a8e624.md) · 呼出先 10件 [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`0079d450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d450.md) [`0079d454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d454.md) [`007a07a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07a4.md) [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md)
- 新版 呼出元 1件 [`00a8f618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a8f/00a8f618.md) · 呼出先 10件 [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`0079d82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d82c.md) [`0079d830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d830.md) [`007a0b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0b80.md) [`007a0bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007984f8",
      "incomplete_value": true,
      "site": "0079850c",
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
                "const:2c3000:8"
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
    "old": {
      "definition_site": "0079811c",
      "incomplete_value": true,
      "site": "00798130",
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
                "const:2c3000:8"
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00798504",
      "incomplete_value": true,
      "site": "00798514",
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
                "const:c99:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00798128",
      "incomplete_value": true,
      "site": "00798138",
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
                "const:bc2:8"
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
      "definition_site": "00798504",
      "incomplete_value": true,
      "site": "00798514",
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
      "definition_site": "00798128",
      "incomplete_value": true,
      "site": "00798138",
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
      "007984f8",
      "READ",
      [
        "storage",
        "002c32e0",
        null,
        null
      ]
    ],
    [
      "00798504",
      "READ",
      [
        "storage",
        "002aebc2",
        null,
        "string"
      ]
    ],
    [
      "00798504",
      "READ",
      [
        "storage",
        "002aebd2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "007984f8",
      "READ",
      [
        "storage",
        "002c3330",
        null,
        null
      ]
    ],
    [
      "00798504",
      "READ",
      [
        "storage",
        "002aec99",
        null,
        "string"
      ]
    ],
    [
      "00798504",
      "READ",
      [
        "storage",
        "002aeca9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007980e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md#insn-007980e4) · [`007980f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md#insn-007980f4) · [`00798104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/007980b8.md#insn-00798104)
- 新版 [`007984c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798494.md#insn-007984c0) · [`007984d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798494.md#insn-007984d0) · [`007984e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798494.md#insn-007984e0)

~~~diff
- 007980e4 ["INT_ADD", "register:40f0:8", ["const:7980e4:8", "const:4:8"]]
- 007980e4 ["CALL", null, ["callee:007a0b80:8"]]
+ 007984c0 ["INT_ADD", "register:40f0:8", ["const:7984c0:8", "const:4:8"]]
+ 007984c0 ["CALL", null, ["callee:007a0b80:8"]]
- 007980e4 bytes b0210094
+ 007984c0 bytes b0210094
- 007980f4 ["INT_ADD", "register:40f0:8", ["const:7980f4:8", "const:4:8"]]
- 007980f4 ["CALL", null, ["callee:007a0bb8:8"]]
+ 007984d0 ["INT_ADD", "register:40f0:8", ["const:7984d0:8", "const:4:8"]]
+ 007984d0 ["CALL", null, ["callee:007a0bb8:8"]]
- 007980f4 bytes ba210094
+ 007984d0 bytes ba210094
- 00798104 ["INT_ADD", "register:40f0:8", ["const:798104:8", "const:4:8"]]
- 00798104 ["CALL", null, ["callee:00c58f50:8"]]
+ 007984e0 ["INT_ADD", "register:40f0:8", ["const:7984e0:8", "const:4:8"]]
+ 007984e0 ["CALL", null, ["callee:00c58f50:8"]]
- 00798104 bytes 9fff1294
+ 007984e0 bytes 9c021394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d42db1f76ec3cdde518da4e933335f6"></a>

### [`0079826c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md) → [`00798648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798648.md) FUN_00798648

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008978e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0048ce94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0048c/0048ce94.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`007a07a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07a4.md) [`007a07dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/007a0/007a07dc.md)
- 新版 呼出元 1件 [`00898890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/00898890.md) · 呼出先 10件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0048d1b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0048d/0048d1b4.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`007a0b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0b80.md) [`007a0bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/007a0/007a0bb8.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 94.84% / 新版 94.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007986bc",
      "incomplete_value": true,
      "site": "007986cc",
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
                "const:17c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007982e0",
      "incomplete_value": true,
      "site": "007982f0",
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
                "const:9e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007986d0",
      "incomplete_value": true,
      "site": "007986d0",
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
      "definition_site": "007982f4",
      "incomplete_value": true,
      "site": "007982f4",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "007986c4",
      "incomplete_value": true,
      "site": "007986d4",
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007982e8",
      "incomplete_value": true,
      "site": "007982f8",
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
                "const:490:8"
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
      "007986bc",
      "READ",
      [
        "storage",
        "002b409e",
        null,
        "string"
      ]
    ],
    [
      "007986c0",
      "READ",
      [
        "storage",
        "002b40ad",
        null,
        "string"
      ]
    ],
    [
      "007986c4",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "007986bc",
      "READ",
      [
        "storage",
        "002b417c",
        null,
        "string"
      ]
    ],
    [
      "007986c0",
      "READ",
      [
        "storage",
        "002b418b",
        null,
        "string"
      ]
    ],
    [
      "007986c4",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079834c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md#insn-0079834c) · [`007986d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md#insn-007986d0) · [`0079871c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/0079826c.md#insn-0079871c)
- 新版 [`00798728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798648.md#insn-00798728) · [`00798aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00798/00798648.md#insn-00798aac)

~~~diff
- 0079834c ["INT_ADD", "register:40f0:8", ["const:79834c:8", "const:4:8"]]
- 0079834c ["CALL", null, ["callee:00c58f50:8"]]
+ 00798728 ["INT_ADD", "register:40f0:8", ["const:798728:8", "const:4:8"]]
+ 00798728 ["CALL", null, ["callee:00c58f50:8"]]
- 0079834c bytes 0dff1294
+ 00798728 bytes 0a021394
- 007986d0 ["INT_ADD", "register:40f0:8", ["const:7986d0:8", "const:4:8"]]
- 007986d0 ["CALL", null, ["callee:0043be80:8"]]
+ 00798aac ["INT_ADD", "register:40f0:8", ["const:798aac:8", "const:4:8"]]
+ 00798aac ["CALL", null, ["callee:0043be80:8"]]
- 007986d0 bytes 248df297
+ 00798aac bytes f58cf297
- 0079871c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079871c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 0079871c bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f747e65ee1ae3bc2450da4bbaa43ed41"></a>

### [`00798ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md) → [`007992d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00799/007992d4.md) FUN_007992d4

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008978e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00897/008978e4.md) · 呼出先 31件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004517dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004517dc.md) [`00451a18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/00451a18.md) [`00459430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459430.md) [`0045986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/0045986c.md)
- 新版 呼出元 1件 [`00898890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00898/00898890.md) · 呼出先 31件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00451afc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451afc.md) [`00451d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451d38.md) [`00459750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459750.md) [`00459b8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459b8c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.55% / 新版 80.55%

CFGの説明率　旧版 41.35% / 新版 41.98%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 6件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 9件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 31件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00798f40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00798f48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00798f80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00798f48",
      "DATA",
      [
        "storage",
        "00c63bb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00798f74",
      "READ",
      [
        "storage",
        "002a6a54",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00798f74",
      "READ",
      [
        "storage",
        "002a6a64",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00799324",
      "DATA",
      [
        "storage",
        "00c64b80",
        null,
        "pointer"
      ]
    ],
    [
      "00799350",
      "READ",
      [
        "storage",
        "002a6bac",
        null,
        "string"
      ]
    ],
    [
      "00799350",
      "READ",
      [
        "storage",
        "002a6bbc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00798f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md#insn-00798f40) · [`00798f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md#insn-00798f48) · [`00798f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00798/00798ef8.md#insn-00798f80)

~~~diff
- 00798f40 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00798f40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00798f40 bytes 080800b9
- 00798f48 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00798f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00798f48 bytes 090000f9
- 00798f80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00798f80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00798f80 bytes e04b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3712150faca2521958bf74c5a276e8d"></a>

### [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) → [`0079a0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a0c8.md) FUN_0079a0c8

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md) · 呼出先 15件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043bbe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bbe4.md) [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md)
- 新版 呼出元 1件 [`0079bdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079bdf8.md) · 呼出先 15件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043bf04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bf04.md) [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`005a4600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4600.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.35% / 新版 79.35%

CFGの説明率　旧版 43.21% / 新版 43.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 12件, `call_target` 1件, `store_condition` 5件, `unresolved_branch_alignment` 19件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00799d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00799d1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00799d20"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00799d14",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ],
    [
      "unmatched:00799d1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00799d20",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0079a0f0",
      "WRITE",
      [
        "storage",
        "Stack[-0xe8]",
        null,
        null
      ]
    ],
    [
      "0079a0f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "0079a0fc",
      "WRITE",
      [
        "storage",
        "Stack[-0xe0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00799d14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md#insn-00799d14) · [`00799d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md#insn-00799d1c) · [`00799d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md#insn-00799d20)

~~~diff
- 00799d14 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00799d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00799d14 bytes e90700f9
- 00799d1c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00799d1c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00799d1c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00799d1c bytes a9831ff8
- 00799d20 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00799d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00799d20 bytes e00b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-825ab9cf2eeba10039f9973010eebcd8"></a>

### [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) → [`0079aa3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079aa3c.md) FUN_0079aa3c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) · 呼出先 6件 [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`0079d624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md) · 呼出先 6件 [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) [`005a4444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4444.md) [`005a4600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4600.md) [`0079da00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079da00.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 83.06% / 新版 83.06%

CFGの説明率　旧版 79.31% / 新版 79.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a664"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a668"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079a664",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079a668",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079a66c",
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
      "0079aa40",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0079aa44",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0079aa48",
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

- 旧版 [`0079a664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a664) · [`0079a668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a668) · [`0079a66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md#insn-0079a66c)

~~~diff
- 0079a664 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079a664 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079a664 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0079a664 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079a664 bytes fd7b0aa9
- 0079a668 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:b0:8"]]
- 0079a668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 0079a668 bytes f95b00f9
- 0079a66c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0079a66c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0079a66c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 0079a66c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079a66c bytes f85f0ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-358866637c16e52331d96b532e67c96b"></a>

### [`0079a9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md) → [`0079adc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079adc4.md) FUN_0079adc4

採用 · 移動量 `+0x3dc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079a898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a898.md) · 呼出先 14件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)
- 新版 呼出元 1件 [`0079ac74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079ac74.md) · 呼出先 14件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`0059bc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059bc68.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.94% / 新版 83.94%

CFGの説明率　旧版 53.45% / 新版 53.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a9ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079a9f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079a9ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079a9f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079a9f4",
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
      "0079adc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0079adcc",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0079add0",
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

- 旧版 [`0079a9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md#insn-0079a9ec) · [`0079a9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md#insn-0079a9f0) · [`0079a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a9e8.md#insn-0079a9f4)

~~~diff
- 0079a9ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079a9ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079a9ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 0079a9ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079a9ec bytes fd7b10a9
- 0079a9f0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:110:8"]]
- 0079a9f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0079a9f0 bytes fc8b00f9
- 0079a9f4 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0079a9f4 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0079a9f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:120:8"]]
- 0079a9f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079a9f4 bytes f85f12a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f99099b13b217c516c7769c91d4a0b14"></a>

### [`0079b168`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md) → [`0079b544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b544.md) FUN_0079b544

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079afe0.md) · 呼出先 9件 [`0044f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044f920.md) [`00452c94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00452/00452c94.md) [`007643dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00764/007643dc.md) [`007685fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/007685fc.md) [`0079da34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da34.md)
- 新版 呼出元 1件 [`0079b3bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b3bc.md) · 呼出先 9件 [`0044fc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0044f/0044fc40.md) [`00452fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00452/00452fb4.md) [`007647b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00764/007647b8.md) [`007689d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00768/007689d8.md) [`0079de10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079de10.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 90.38% / 新版 90.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b588",
      "incomplete_value": false,
      "site": "0079b588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b1ac",
      "incomplete_value": false,
      "site": "0079b1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079b56c",
      "value": [
        "leaf",
        "ram:7647b8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079b190",
      "value": [
        "leaf",
        "ram:7643dc:8"
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
      "site": "0079b194"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079b56c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007643dc"
      ]
    ],
    [
      "unmatched:0079b194",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "0079b578",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007685fc"
      ]
    ]
  ],
  "added": [
    [
      "0079b56c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007647b8"
      ]
    ],
    [
      "0079b570",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008524fc"
      ]
    ],
    [
      "0079b578",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md#insn-0079b190) · [`0079b194`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md#insn-0079b194) · [`0079b19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b168.md#insn-0079b19c)
- 新版 [`0079b56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b544.md#insn-0079b56c) · [`0079b578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b544.md#insn-0079b578)

~~~diff
- 0079b190 ["INT_ADD", "register:40f0:8", ["const:79b190:8", "const:4:8"]]
- 0079b190 ["CALL", null, ["ram:7643dc:8"]]
+ 0079b56c ["INT_ADD", "register:40f0:8", ["const:79b56c:8", "const:4:8"]]
+ 0079b56c ["CALL", null, ["ram:7647b8:8"]]
- 0079b190 bytes 9324ff97
+ 0079b56c bytes 9324ff97
- 0079b194 ["INT_ADD", "register:40f0:8", ["const:79b194:8", "const:4:8"]]
- 0079b194 ["CALL", null, ["callee:008524fc:8"]]
- 0079b194 bytes efd80294
- 0079b19c ["INT_ADD", "register:40f0:8", ["const:79b19c:8", "const:4:8"]]
- 0079b19c ["CALL", null, ["ram:7685fc:8"]]
+ 0079b578 ["INT_ADD", "register:40f0:8", ["const:79b578:8", "const:4:8"]]
+ 0079b578 ["CALL", null, ["ram:7689d8:8"]]
- 0079b19c bytes 1835ff97
+ 0079b578 bytes 1835ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d664738bc0792d468fe22352c482abc1"></a>

### [`0079b2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md) → [`0079b6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md) FUN_0079b6b4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0079da3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md) · 呼出先 6件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) [`0079db64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db64.md) [`0079db68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db68.md) [`0079dbe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbe8.md) [`0079dbec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbec.md)
- 新版 呼出元 1件 [`0079de18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079de18.md) · 呼出先 6件 [`0079b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md) [`0079df40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df40.md) [`0079df44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df44.md) [`0079dfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfc4.md) [`0079dfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfc8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079b6dc",
      "incomplete_value": false,
      "site": "0079b6dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b300",
      "incomplete_value": false,
      "site": "0079b300",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "definition_site": "0079b6f0",
      "incomplete_value": false,
      "site": "0079b6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079b314",
      "incomplete_value": false,
      "site": "0079b314",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:48:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079b6dc",
      "DATA",
      [
        "storage",
        "00c79fb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b6f0",
      "DATA",
      [
        "storage",
        "00c7a048",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b728",
      "READ",
      [
        "storage",
        "00c7a068",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0079b6dc",
      "DATA",
      [
        "storage",
        "00c7af88",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b6f0",
      "DATA",
      [
        "storage",
        "00c7b018",
        null,
        "undefined *"
      ]
    ],
    [
      "0079b728",
      "READ",
      [
        "storage",
        "00c7b038",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md#insn-0079b2f8) · [`0079b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md#insn-0079b2fc) · [`0079b30c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md#insn-0079b30c)
- 新版 [`0079b6d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md#insn-0079b6d4) · [`0079b6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md#insn-0079b6d8) · [`0079b6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md#insn-0079b6e8)

~~~diff
- 0079b2f8 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079b6d4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079b2f8 bytes e82600d0
+ 0079b6d4 bytes e82600f0
- 0079b2fc ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0079b2fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079b2fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079b2fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079b6d8 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0079b6d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b6d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079b6d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079b2fc bytes 08e13e91
+ 0079b6d8 bytes 08213e91
- 0079b30c ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 0079b6e8 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 0079b30c bytes e82600f0
+ 0079b6e8 bytes 08270090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00f32c6bc2fdfdd88e5a56f949d619b3"></a>

### [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) → [`0079b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md) FUN_0079b800

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079b2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md) · 呼出先 14件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`0059b948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0059b/0059b948.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)
- 新版 呼出元 1件 [`0079b6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md) · 呼出先 14件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`0059bc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0059b/0059bc68.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.50% / 新版 86.50%

CFGの説明率　旧版 37.50% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079b454"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079b47c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079b484"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079b454",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079b47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079b484",
      "DATA",
      [
        "storage",
        "00c6e900",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079b830",
      "WRITE",
      [
        "storage",
        "Stack[-0x58]",
        null,
        null
      ]
    ],
    [
      "0079b858",
      "WRITE",
      [
        "storage",
        "Stack[-0x90]",
        null,
        null
      ]
    ],
    [
      "0079b860",
      "DATA",
      [
        "storage",
        "00c6f8d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079b454`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md#insn-0079b454) · [`0079b458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md#insn-0079b458) · [`0079b47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md#insn-0079b47c)
- 新版 [`0079b834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md#insn-0079b834)

~~~diff
- 0079b454 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079b454 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0079b454 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079b454 bytes a8831ff8
- 0079b458 ["INT_ADD", "register:40f0:8", ["const:79b458:8", "const:4:8"]]
- 0079b458 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079b834 ["INT_ADD", "register:40f0:8", ["const:79b834:8", "const:4:8"]]
+ 0079b834 ["CALL", null, ["callee:00c58f30:8"]]
- 0079b458 bytes c2f21294
+ 0079b834 bytes bff51294
- 0079b47c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079b47c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 0079b47c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079b47c bytes b4031cf8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1236f33e7181a04bc4398b576c746c0"></a>

### [`0079ba1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md) → [`0079bdf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079bdf8.md) FUN_0079bdf8

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079db6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db6c.md) · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) [`0079bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`0079df48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df48.md) · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`0079a0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a0c8.md) [`0079c0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c0f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.06% / 新版 86.06%

CFGの説明率　旧版 56.98% / 新版 56.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ba20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ba20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ba24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079ba20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ba24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ba28",
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
      "0079bdfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079be00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079be04",
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

- 旧版 [`0079ba20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079ba20) · [`0079ba24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079ba24) · [`0079ba28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079ba1c.md#insn-0079ba28)

~~~diff
- 0079ba20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079ba20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079ba20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0079ba20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ba20 bytes fd7b05a9
- 0079ba24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 0079ba24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0079ba24 bytes f53300f9
- 0079ba28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079ba28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079ba28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 0079ba28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ba28 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db674d3321c22731202465f2ae59e6f4"></a>

### [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) → [`0079c23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c23c.md) FUN_0079c23c

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079bd14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079bd14.md) · 呼出先 15件 [`00598b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598b74.md) [`00598d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00598/00598d34.md) [`005a1768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1768.md) [`00795e7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795e7c.md) [`00795eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00795/00795eb4.md)
- 新版 呼出元 1件 [`0079c0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c0f0.md) · 呼出先 15件 [`00598e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598e94.md) [`00599054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00599/00599054.md) [`005a1a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a1/005a1a88.md) [`00796258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796258.md) [`00796290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00796/00796290.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.34% / 新版 91.34%

CFGの説明率　旧版 60.00% / 新版 61.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079bf70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079c0f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079c34c"
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
      "unmatched:0079bf70",
      "DATA",
      [
        "storage",
        "00c7a1d8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079bf74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079c36c"
      ]
    ],
    [
      "unmatched:0079bf80",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079c374"
      ]
    ]
  ],
  "added": [
    [
      "0079c34c",
      "DATA",
      [
        "storage",
        "00c7b1a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0079c350",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079c36c"
      ]
    ],
    [
      "0079c35c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079c374"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079bee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md#insn-0079bee4) · [`0079bf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md#insn-0079bf08) · [`0079bf2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md#insn-0079bf2c)

~~~diff
- 0079bee4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079bee4 ["INT_ADD", "register:40f0:8", ["const:79bee4:8", "const:4:8"]]
- 0079bee4 ["CALLIND", null, ["register:0:8"]]
- 0079bee4 bytes 00013fd6
- 0079bf08 ["COPY", "register:0:8", ["register:4040:8"]]
- 0079bf08 ["INT_ADD", "register:40f0:8", ["const:79bf08:8", "const:4:8"]]
- 0079bf08 ["CALLIND", null, ["register:0:8"]]
- 0079bf08 bytes 00013fd6
- 0079bf2c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079bf2c ["INT_ADD", "register:40f0:8", ["const:79bf2c:8", "const:4:8"]]
- 0079bf2c ["CALLIND", null, ["register:0:8"]]
- 0079bf2c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4737b1845393da9ce15a2cf922574f32"></a>

### [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md) → [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md) FUN_0079c7d4

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079dce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dce8.md) · 呼出先 11件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`004939d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00493/004939d8.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`005a4124`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4124.md)
- 新版 呼出元 1件 [`0079e0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0c4.md) · 呼出先 11件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00493cf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00493/00493cf8.md) [`005410dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00541/005410dc.md) [`005a4444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4444.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 93.31% / 新版 93.31%

CFGの説明率　旧版 73.33% / 新版 74.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079c674"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079c688"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079c690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079c674",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cb9c"
      ]
    ],
    [
      "unmatched:0079c690",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0079c67c"
      ]
    ],
    [
      "unmatched:0079c698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cb9c"
      ]
    ]
  ],
  "added": [
    [
      "0079ca50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cb9c"
      ]
    ],
    [
      "0079ca6c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079ca58"
      ]
    ],
    [
      "0079ca74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cb9c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079c648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c648) · [`0079c674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c674) · [`0079c688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md#insn-0079c688)
- 新版 [`0079ca24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md#insn-0079ca24)

~~~diff
- 0079c648 ["INT_ADD", "register:40f0:8", ["const:79c648:8", "const:4:8"]]
- 0079c648 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079ca24 ["INT_ADD", "register:40f0:8", ["const:79ca24:8", "const:4:8"]]
+ 0079ca24 ["CALL", null, ["callee:00c58f50:8"]]
- 0079c648 bytes 4eee1294
+ 0079ca24 bytes 4bf11294
- 0079c674 ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 0079c674 ["CBRANCH", null, ["local:b80:8", "tmp:0:1"]]
- 0079c674 bytes 6a0a00b4
- 0079c688 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0079c688 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0079c688 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0079c688 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0079c688 bytes 29b18a9a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf592d1f1da68dfd1b825ed331ef15da"></a>

### [`0079c9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md) → [`0079cdb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cdb4.md) FUN_0079cdb4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`005a1768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a1/005a1768.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`005a1a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a1/005a1a88.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079c9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md#insn-0079c9ec) · [`0079c9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c9d8.md#insn-0079c9f4)
- 新版 [`0079cdc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cdb4.md#insn-0079cdc8) · [`0079cdd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cdb4.md#insn-0079cdd0)

~~~diff
- 0079c9ec ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0079c9ec ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0079cdc8 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0079cdc8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0079c9ec bytes f30000b4
+ 0079cdc8 bytes f30000b4
- 0079c9f4 ["INT_ADD", "register:40f0:8", ["const:79c9f4:8", "const:4:8"]]
- 0079c9f4 ["CALL", null, ["callee:005a1a88:8"]]
+ 0079cdd0 ["INT_ADD", "register:40f0:8", ["const:79cdd0:8", "const:4:8"]]
+ 0079cdd0 ["CALL", null, ["callee:005a1a88:8"]]
- 0079c9f4 bytes 5d13f897
+ 0079cdd0 bytes 2e13f897
~~~


<a id="compare-e87fc9b900d58f428e5e272a9c475fa9"></a>

### [`0079ca98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079ca98.md) → [`0079ce74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079ce74.md) FUN_0079ce74

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079ce98",
      "incomplete_value": false,
      "site": "0079ce9c",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
              ]
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
      "definition_site": "0079cabc",
      "incomplete_value": false,
      "site": "0079cac0",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
              ]
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079caac"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079ce88"
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
      "unmatched:0079caac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cecc"
      ]
    ],
    [
      "0079ce9c",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ce88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079cecc"
      ]
    ],
    [
      "0079ce9c",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079caac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079ca98.md#insn-0079caac) · [`0079cab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079ca98.md#insn-0079cab0)
- 新版 [`0079ce88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079ce74.md#insn-0079ce88) · [`0079ce8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079ce74.md#insn-0079ce8c)

~~~diff
- 0079caac ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0079caac ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0079caac bytes 330200b4
+ 0079ce88 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0079ce88 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 0079ce88 bytes 330200b4
- 0079cab0 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0079ce8c ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0079cab0 bytes 882600b0
+ 0079ce8c bytes 882600d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdb55d23d3f309dcd5ee285899f9d20f"></a>

### [`0079cb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cb80.md) → [`0079cf5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cf5c.md) FUN_0079cf5c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079cf80",
      "incomplete_value": false,
      "site": "0079cf84",
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
                "const:c6e000:8"
              ],
              [
                "leaf",
                "const:ab0:8"
              ]
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
      "definition_site": "0079cba4",
      "incomplete_value": false,
      "site": "0079cba8",
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
                "const:c6d000:8"
              ],
              [
                "leaf",
                "const:ae0:8"
              ]
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0079cf84",
      "DATA",
      [
        "storage",
        "00c6daf0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079cf84",
      "DATA",
      [
        "storage",
        "00c6eac0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079cb98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cb80.md#insn-0079cb98) · [`0079cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cb80.md#insn-0079cb9c) · [`0079cbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cb80.md#insn-0079cbb4)
- 新版 [`0079cf74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cf5c.md#insn-0079cf74) · [`0079cf78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cf5c.md#insn-0079cf78) · [`0079cf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079cf5c.md#insn-0079cf90)

~~~diff
- 0079cb98 ["COPY", "register:4040:8", ["const:c6d000:8"]]
+ 0079cf74 ["COPY", "register:4040:8", ["const:c6e000:8"]]
- 0079cb98 bytes 882600b0
+ 0079cf74 bytes 882600d0
- 0079cb9c ["COPY", "tmp:0:8", ["const:ae0:8"]]
- 0079cb9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079cb9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079cb9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079cf78 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0079cf78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079cf78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079cf78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079cb9c bytes 08812b91
+ 0079cf78 bytes 08c12a91
- 0079cbb4 ["INT_ADD", "register:40f0:8", ["const:79cbb4:8", "const:4:8"]]
- 0079cbb4 ["CALL", null, ["callee:00c58f50:8"]]
+ 0079cf90 ["INT_ADD", "register:40f0:8", ["const:79cf90:8", "const:4:8"]]
+ 0079cf90 ["CALL", null, ["callee:00c58f50:8"]]
- 0079cbb4 bytes f3ec1294
+ 0079cf90 bytes f0ef1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a905230b0e2da999faffa51256811bf9"></a>

### [`0079cc68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md) → [`0079d044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d044.md) FUN_0079d044

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00799cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00799/00799cec.md) · 呼出先 10件 [`005a42ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42ac.md) [`005a42c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42c0.md) [`005a42e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a42e0.md) [`005a4548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4548.md) [`0079cfcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cfcc.md)
- 新版 呼出元 1件 [`0079a0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079a0c8.md) · 呼出先 10件 [`005a45cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a45cc.md) [`005a45e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a45e0.md) [`005a4600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4600.md) [`005a4868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a4868.md) [`0079d3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d3a8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 92.31% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0079cea8",
      "incomplete_value": true,
      "site": "0079ceb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0079cea4",
      "incomplete_value": true,
      "site": "0079ceb8",
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
                "const:60:8"
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
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0079cea4",
      "incomplete_value": true,
      "site": "0079ceb8",
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
    "ordinal": 11,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0079ceb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079ceb8) · [`0079ccd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079ccd4) · [`0079ccdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079cc68.md#insn-0079ccdc)
- 新版 [`0079d294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d044.md#insn-0079d294) · [`0079d0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d044.md#insn-0079d0b0) · [`0079d0b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d044.md#insn-0079d0b8)

~~~diff
- 0079ceb8 ["INT_ADD", "register:40f0:8", ["const:79ceb8:8", "const:4:8"]]
- 0079ceb8 ["CALL", null, ["callee:0079d3a8:8"]]
+ 0079d294 ["INT_ADD", "register:40f0:8", ["const:79d294:8", "const:4:8"]]
+ 0079d294 ["CALL", null, ["callee:0079d3a8:8"]]
- 0079ceb8 bytes 45000094
+ 0079d294 bytes 45000094
- 0079ccd4 ["INT_ADD", "register:40f0:8", ["const:79ccd4:8", "const:4:8"]]
- 0079ccd4 ["CALL", null, ["callee:005a4868:8"]]
+ 0079d0b0 ["INT_ADD", "register:40f0:8", ["const:79d0b0:8", "const:4:8"]]
+ 0079d0b0 ["CALL", null, ["callee:005a4868:8"]]
- 0079ccd4 bytes 1d1ef897
+ 0079d0b0 bytes ee1df897
- 0079ccdc ["INT_ADD", "register:40f0:8", ["const:79ccdc:8", "const:4:8"]]
- 0079ccdc ["CALL", null, ["callee:00c58f50:8"]]
+ 0079d0b8 ["INT_ADD", "register:40f0:8", ["const:79d0b8:8", "const:4:8"]]
+ 0079d0b8 ["CALL", null, ["callee:00c58f50:8"]]
- 0079ccdc bytes a9ec1294
+ 0079d0b8 bytes a6ef1294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a1d51096e69fdc590432a44175f2bd"></a>

### [`0079d41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d41c.md) → [`0079d7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d7f8.md) FUN_0079d7f8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079d80c",
      "incomplete_value": false,
      "site": "0079d810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d430",
      "incomplete_value": false,
      "site": "0079d434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0079d810",
      "DATA",
      [
        "storage",
        "00c79db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d810",
      "DATA",
      [
        "storage",
        "00c7ad88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d428`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d41c.md#insn-0079d428) · [`0079d42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d41c.md#insn-0079d42c) · [`0079d430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d41c.md#insn-0079d430)
- 新版 [`0079d804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d7f8.md#insn-0079d804) · [`0079d808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d7f8.md#insn-0079d808) · [`0079d80c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d7f8.md#insn-0079d80c)

~~~diff
- 0079d428 ["INT_ADD", "register:40f0:8", ["const:79d428:8", "const:4:8"]]
- 0079d428 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079d804 ["INT_ADD", "register:40f0:8", ["const:79d804:8", "const:4:8"]]
+ 0079d804 ["CALL", null, ["callee:00c58f30:8"]]
- 0079d428 bytes ceea1294
+ 0079d804 bytes cbed1294
- 0079d42c ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079d808 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079d42c bytes e8260090
+ 0079d808 bytes e82600b0
- 0079d430 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0079d430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d80c ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0079d80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d430 bytes 08e13691
+ 0079d80c bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09693bb8da8e66a83e97c676a12f9c76"></a>

### [`0079d440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d440.md) → [`0079d81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d81c.md) FUN_0079d81c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079d820",
      "incomplete_value": false,
      "site": "0079d824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d444",
      "incomplete_value": false,
      "site": "0079d448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "0079d824",
      "DATA",
      [
        "storage",
        "00c79db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079d824",
      "DATA",
      [
        "storage",
        "00c7ad88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d440.md#insn-0079d440) · [`0079d444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d440.md#insn-0079d444)
- 新版 [`0079d81c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d81c.md#insn-0079d81c) · [`0079d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d81c.md#insn-0079d820)

~~~diff
- 0079d440 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079d81c ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079d440 bytes e8260090
+ 0079d81c bytes e82600b0
- 0079d444 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0079d444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079d820 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 0079d820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079d820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d444 bytes 08e13691
+ 0079d820 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-904123b4b62ce48e71bd9039487c3bfd"></a>

### [`0079d458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d458.md) → [`0079d834`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d834.md) FUN_0079d834

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047ad34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047a/0047ad34.md) [`0047ce14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0047c/0047ce14.md) [`008b91d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008b9/008b91d0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047b054`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047b/0047b054.md) [`0047d134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0047d/0047d134.md) [`008ba17c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008ba/008ba17c.md)

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
      "site": "0079d858",
      "value": [
        "leaf",
        "ram:47b054:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0079d47c",
      "value": [
        "leaf",
        "ram:47ad34:8"
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
      "0079d858",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047ad34"
      ]
    ]
  ],
  "added": [
    [
      "0079d858",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d458.md#insn-0079d47c) · [`0079d488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d458.md#insn-0079d488)
- 新版 [`0079d858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d834.md#insn-0079d858) · [`0079d864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d834.md#insn-0079d864)

~~~diff
- 0079d47c ["INT_ADD", "register:40f0:8", ["const:79d47c:8", "const:4:8"]]
- 0079d47c ["CALL", null, ["ram:47ad34:8"]]
+ 0079d858 ["INT_ADD", "register:40f0:8", ["const:79d858:8", "const:4:8"]]
+ 0079d858 ["CALL", null, ["ram:47b054:8"]]
- 0079d47c bytes 2e76f397
+ 0079d858 bytes ff75f397
- 0079d488 ["INT_ADD", "register:40f0:8", ["const:79d488:8", "const:4:8"]]
- 0079d488 ["CALL", null, ["callee:0047d134:8"]]
+ 0079d864 ["INT_ADD", "register:40f0:8", ["const:79d864:8", "const:4:8"]]
+ 0079d864 ["CALL", null, ["callee:0047d134:8"]]
- 0079d488 bytes 637ef397
+ 0079d864 bytes 347ef397
~~~


<a id="compare-440170eaec4110d19a5099375f6c9bbe"></a>

### [`0079d610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md) → [`0079d9ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d9ec.md) FUN_0079d9ec

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0079d4c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d4c8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)
- 新版 呼出元 1件 [`0079d8a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d8a4.md) · 呼出先 1件 [`0043bad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bad8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079d9f8",
      "incomplete_value": false,
      "site": "0079d9fc",
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
            "const:5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d61c",
      "incomplete_value": false,
      "site": "0079d620",
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
            "const:f8c:8"
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
      "0079d9f8",
      "PARAM",
      [
        "storage",
        "002b7f8c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0079d9f8",
      "PARAM",
      [
        "storage",
        "002b805b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md#insn-0079d620) · [`0079d618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md#insn-0079d618) · [`0079d61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d610.md#insn-0079d61c)
- 新版 [`0079d9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d9ec.md#insn-0079d9fc) · [`0079d9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d9ec.md#insn-0079d9f4) · [`0079d9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079d9ec.md#insn-0079d9f8)

~~~diff
- 0079d620 ["INT_ADD", "register:40f0:8", ["const:79d620:8", "const:4:8"]]
- 0079d620 ["CALL", null, ["callee:0043bad8:8"]]
+ 0079d9fc ["INT_ADD", "register:40f0:8", ["const:79d9fc:8", "const:4:8"]]
+ 0079d9fc ["CALL", null, ["callee:0043bad8:8"]]
- 0079d620 bytes 6678f297
+ 0079d9fc bytes 3778f297
- 0079d618 ["COPY", "register:4000:8", ["const:2b7000:8"]]
+ 0079d9f4 ["COPY", "register:4000:8", ["const:2b8000:8"]]
- 0079d618 bytes c0d8ffd0
+ 0079d9f4 bytes c0d8fff0
- 0079d61c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0079d61c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0079d61c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0079d61c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0079d9f8 ["COPY", "tmp:0:8", ["const:5b:8"]]
+ 0079d9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0079d9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0079d9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0079d61c bytes 00303e91
+ 0079d9f8 bytes 006c0191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49dbdf373e82cc49962907f3f51dc13a"></a>

### [`0079d624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md) → [`0079da00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079da00.md) FUN_0079da00

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079a/0079a660.md) · 呼出先 6件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005a4498`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005a4/005a4498.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`0079aa3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079a/0079aa3c.md) · 呼出先 6件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`005a47b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005a4/005a47b8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 84.14% / 新版 84.14%

CFGの説明率　旧版 43.18% / 新版 43.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d66c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d6b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d6bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079d66c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dac0"
      ]
    ],
    [
      "unmatched:0079d6c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079db84"
      ]
    ],
    [
      "unmatched:0079d6f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079db0c"
      ]
    ]
  ],
  "added": [
    [
      "0079da48",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dac0"
      ]
    ],
    [
      "0079da9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079db84"
      ]
    ],
    [
      "0079dad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079db0c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d66c) · [`0079d6b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d6b4) · [`0079d6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d624.md#insn-0079d6bc)

~~~diff
- 0079d66c ["INT_EQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0079d66c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0079d66c bytes ca030054
- 0079d6b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0079d6b4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 0079d6b4 ["COPY", "tmp:2:8", ["register:4058:8"]]
- 0079d6b4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 0079d6b4 bytes 6a818a9a
- 0079d6bc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0079d6bc ["COPY", "tmp:1:8", ["register:4050:8"]]
- 0079d6bc ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0079d6bc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0079d6bc bytes 5931899a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f38bad622d7e1cfcde617e9d343b787e"></a>

### [`0079d86c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d86c.md) → [`0079dc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc48.md) FUN_0079dc48

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079dc6c",
      "incomplete_value": false,
      "site": "0079dc6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d890",
      "incomplete_value": false,
      "site": "0079d890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:e38:8"
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
      "0079dc6c",
      "DATA",
      [
        "storage",
        "00c79e38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dc6c",
      "DATA",
      [
        "storage",
        "00c7ae08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d86c.md#insn-0079d880) · [`0079d888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d86c.md#insn-0079d888) · [`0079d88c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d86c.md#insn-0079d88c)
- 新版 [`0079dc5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc48.md#insn-0079dc5c) · [`0079dc64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc48.md#insn-0079dc64) · [`0079dc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dc48.md#insn-0079dc68)

~~~diff
- 0079d880 ["INT_ADD", "register:40f0:8", ["const:79d880:8", "const:4:8"]]
- 0079d880 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079dc5c ["INT_ADD", "register:40f0:8", ["const:79dc5c:8", "const:4:8"]]
+ 0079dc5c ["CALL", null, ["callee:00c58f30:8"]]
- 0079d880 bytes b8e91294
+ 0079dc5c bytes b5ec1294
- 0079d888 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079dc64 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079d888 bytes e8260090
+ 0079dc64 bytes e82600b0
- 0079d88c ["COPY", "tmp:0:8", ["const:e38:8"]]
- 0079d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dc68 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 0079dc68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dc68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dc68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079d88c bytes 08e13891
+ 0079dc68 bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c41052d08759bbc92fef6c4087d3557"></a>

### [`0079d8f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8f4.md) → [`0079dcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dcd0.md) FUN_0079dcd0

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d918"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079d918"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079dcf4"
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
      "unmatched:0079d918",
      "DATA",
      [
        "storage",
        "00c79eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079d91c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079d920",
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
      "0079dcf4",
      "DATA",
      [
        "storage",
        "00c7ae88",
        null,
        "undefined *"
      ]
    ],
    [
      "0079dcf8",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079dcfc",
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

- 旧版 [`0079d908`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8f4.md#insn-0079d908) · [`0079d918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8f4.md#insn-0079d918) · [`0079d924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d8f4.md#insn-0079d924)
- 新版 [`0079dce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dcd0.md#insn-0079dce4)

~~~diff
- 0079d908 ["INT_ADD", "register:40f0:8", ["const:79d908:8", "const:4:8"]]
- 0079d908 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079dce4 ["INT_ADD", "register:40f0:8", ["const:79dce4:8", "const:4:8"]]
+ 0079dce4 ["CALL", null, ["callee:00c58f30:8"]]
- 0079d908 bytes 96e91294
+ 0079dce4 bytes 93ec1294
- 0079d918 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079d918 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 0079d918 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 0079d918 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079d918 bytes 082400a9
- 0079d924 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079d924 ["RETURN", null, ["register:0:8"]]
- 0079d924 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97a46e4de9aa03426b39c84d5dee0c89"></a>

### [`0079d928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d928.md) → [`0079dd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd04.md) FUN_0079dd04

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079dd10",
      "incomplete_value": false,
      "site": "0079dd10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079d934",
      "incomplete_value": false,
      "site": "0079d934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "0079dd10",
      "DATA",
      [
        "storage",
        "00c79eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dd10",
      "DATA",
      [
        "storage",
        "00c7ae88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079d92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d928.md#insn-0079d92c) · [`0079d930`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d928.md#insn-0079d930)
- 新版 [`0079dd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd04.md#insn-0079dd08) · [`0079dd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dd04.md#insn-0079dd0c)

~~~diff
- 0079d92c ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079dd08 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079d92c bytes e9260090
+ 0079dd08 bytes e92600b0
- 0079d930 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 0079d930 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079d930 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079d930 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079dd0c ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 0079dd0c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd0c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079dd0c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079d930 bytes 29e13a91
+ 0079dd0c bytes 29213a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a138aa2501c3bca23013662d26e9de"></a>

### [`0079d9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md) → [`0079ddc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddc8.md) FUN_0079ddc8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079ddec",
      "incomplete_value": false,
      "site": "0079ddec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079da10",
      "incomplete_value": false,
      "site": "0079da10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "0079ddec",
      "DATA",
      [
        "storage",
        "00c79f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079ddec",
      "DATA",
      [
        "storage",
        "00c7af08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079da00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md#insn-0079da00) · [`0079da08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md#insn-0079da08) · [`0079da0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079d9ec.md#insn-0079da0c)
- 新版 [`0079dddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddc8.md#insn-0079dddc) · [`0079dde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddc8.md#insn-0079dde4) · [`0079dde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddc8.md#insn-0079dde8)

~~~diff
- 0079da00 ["INT_ADD", "register:40f0:8", ["const:79da00:8", "const:4:8"]]
- 0079da00 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079dddc ["INT_ADD", "register:40f0:8", ["const:79dddc:8", "const:4:8"]]
+ 0079dddc ["CALL", null, ["callee:00c58f30:8"]]
- 0079da00 bytes 58e91294
+ 0079dddc bytes 55ec1294
- 0079da08 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079dde4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079da08 bytes e8260090
+ 0079dde4 bytes e82600b0
- 0079da0c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0079da0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079da0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079da0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079dde8 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0079dde8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dde8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079dde8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079da0c bytes 08e13c91
+ 0079dde8 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35557d440d6c2f2574123ce17af7c949"></a>

### [`0079da20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da20.md) → [`0079ddfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddfc.md) FUN_0079ddfc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079de08",
      "incomplete_value": false,
      "site": "0079de08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079da2c",
      "incomplete_value": false,
      "site": "0079da2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "0079de08",
      "DATA",
      [
        "storage",
        "00c79f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079de08",
      "DATA",
      [
        "storage",
        "00c7af08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079da24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da20.md#insn-0079da24) · [`0079da28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da20.md#insn-0079da28)
- 新版 [`0079de00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddfc.md#insn-0079de00) · [`0079de04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079ddfc.md#insn-0079de04)

~~~diff
- 0079da24 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079de00 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079da24 bytes e9260090
+ 0079de00 bytes e92600b0
- 0079da28 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0079da28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079da28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079da28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079de04 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 0079de04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079de04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079de04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079da28 bytes 29e13c91
+ 0079de04 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1c6b8daf488ed59ea8f36f3e4d53153"></a>

### [`0079da3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md) → [`0079de18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079de18.md) FUN_0079de18

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00768ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00768/00768ee8.md) [`0079b2d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b2d8.md) [`00851550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00851/00851550.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`007692c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00769/007692c4.md) [`0079b6b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b6b4.md) [`008524fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00852/008524fc.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.18% / 新版 93.18%

CFGの説明率　旧版 50.00% / 新版 52.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079da8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079dabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079de68"
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
      "0079de40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768ee8"
      ]
    ],
    [
      "unmatched:0079da8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079de9c"
      ]
    ],
    [
      "unmatched:0079dabc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dea8"
      ]
    ]
  ],
  "added": [
    [
      "0079de40",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007692c4"
      ]
    ],
    [
      "0079de68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079de9c"
      ]
    ],
    [
      "0079de98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dea8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079da64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079da64) · [`0079da8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079da8c) · [`0079dabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079da3c.md#insn-0079dabc)
- 新版 [`0079de40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079de18.md#insn-0079de40)

~~~diff
- 0079da64 ["INT_ADD", "register:40f0:8", ["const:79da64:8", "const:4:8"]]
- 0079da64 ["CALL", null, ["ram:768ee8:8"]]
+ 0079de40 ["INT_ADD", "register:40f0:8", ["const:79de40:8", "const:4:8"]]
+ 0079de40 ["CALL", null, ["ram:7692c4:8"]]
- 0079da64 bytes 212dff97
+ 0079de40 bytes 212dff97
- 0079da8c ["INT_EQUAL", "tmp:0:1", ["register:4050:8", "const:0:8"]]
- 0079da8c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0079da8c bytes aa0100b4
- 0079dabc ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 0079dabc ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 0079dabc ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 0079dabc bytes 8d000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e36ce2512615cf8c41b3137ddb4b132"></a>

### [`0079db1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md) → [`0079def8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079def8.md) FUN_0079def8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079df1c",
      "incomplete_value": false,
      "site": "0079df1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db40",
      "incomplete_value": false,
      "site": "0079db40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "0079df1c",
      "DATA",
      [
        "storage",
        "00c79fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079df1c",
      "DATA",
      [
        "storage",
        "00c7af88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md#insn-0079db30) · [`0079db38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md#insn-0079db38) · [`0079db3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db1c.md#insn-0079db3c)
- 新版 [`0079df0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079def8.md#insn-0079df0c) · [`0079df14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079def8.md#insn-0079df14) · [`0079df18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079def8.md#insn-0079df18)

~~~diff
- 0079db30 ["INT_ADD", "register:40f0:8", ["const:79db30:8", "const:4:8"]]
- 0079db30 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079df0c ["INT_ADD", "register:40f0:8", ["const:79df0c:8", "const:4:8"]]
+ 0079df0c ["CALL", null, ["callee:00c58f30:8"]]
- 0079db30 bytes 0ce91294
+ 0079df0c bytes 09ec1294
- 0079db38 ["COPY", "register:4040:8", ["const:c79000:8"]]
+ 0079df14 ["COPY", "register:4040:8", ["const:c7a000:8"]]
- 0079db38 bytes e8260090
+ 0079df14 bytes e82600b0
- 0079db3c ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0079db3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079db3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079db3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079df18 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0079df18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079db3c bytes 08e13e91
+ 0079df18 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96995180b648e8c3b2c3601aab1eec85"></a>

### [`0079db50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db50.md) → [`0079df2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df2c.md) FUN_0079df2c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079df38",
      "incomplete_value": false,
      "site": "0079df38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079db5c",
      "incomplete_value": false,
      "site": "0079db5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c79000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "0079df38",
      "DATA",
      [
        "storage",
        "00c79fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079df38",
      "DATA",
      [
        "storage",
        "00c7af88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079db54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db50.md#insn-0079db54) · [`0079db58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079db50.md#insn-0079db58)
- 新版 [`0079df30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df2c.md#insn-0079df30) · [`0079df34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df2c.md#insn-0079df34)

~~~diff
- 0079db54 ["COPY", "register:4048:8", ["const:c79000:8"]]
+ 0079df30 ["COPY", "register:4048:8", ["const:c7a000:8"]]
- 0079db54 bytes e9260090
+ 0079df30 bytes e92600b0
- 0079db58 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 0079db58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079db58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079db58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079df34 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 0079df34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079df34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079df34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079db58 bytes 29e13e91
+ 0079df34 bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-648f199b9fe25f0ec39a021c2895a5e8"></a>

### [`0079dba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md) → [`0079df7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df7c.md) FUN_0079df7c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079dfa0",
      "incomplete_value": false,
      "site": "0079dfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dbc4",
      "incomplete_value": false,
      "site": "0079dbc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:48:8"
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
      "0079dfa0",
      "DATA",
      [
        "storage",
        "00c7a048",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079dfa0",
      "DATA",
      [
        "storage",
        "00c7b018",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dbb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbb4) · [`0079dbbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbbc) · [`0079dbc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dba0.md#insn-0079dbc0)
- 新版 [`0079df90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df7c.md#insn-0079df90) · [`0079df98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df7c.md#insn-0079df98) · [`0079df9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079df7c.md#insn-0079df9c)

~~~diff
- 0079dbb4 ["INT_ADD", "register:40f0:8", ["const:79dbb4:8", "const:4:8"]]
- 0079dbb4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079df90 ["INT_ADD", "register:40f0:8", ["const:79df90:8", "const:4:8"]]
+ 0079df90 ["CALL", null, ["callee:00c58f30:8"]]
- 0079dbb4 bytes ebe81294
+ 0079df90 bytes e8eb1294
- 0079dbbc ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 0079df98 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 0079dbbc bytes e82600b0
+ 0079df98 bytes e82600d0
- 0079dbc0 ["COPY", "tmp:0:8", ["const:48:8"]]
- 0079dbc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dbc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dbc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["COPY", "tmp:0:8", ["const:18:8"]]
+ 0079df9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079df9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dbc0 bytes 08210191
+ 0079df9c bytes 08610091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7685147f632271dd12fbe8e72520bcee"></a>

### [`0079dbf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbf0.md) → [`0079dfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfcc.md) FUN_0079dfcc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 80.00% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079dc04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079dfe0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "0079dc04"
      ],
      [
        "FALL_THROUGH",
        "0079dfe0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "0079dfe0",
      "incomplete_value": true,
      "site": "0079dfe4",
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
      "definition_site": "0079dc04",
      "incomplete_value": true,
      "site": "0079dc08",
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
      "unmatched:0079dc04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dfe8"
      ]
    ]
  ],
  "added": [
    [
      "0079dfe0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079dfe8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dc04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbf0.md#insn-0079dc04) · [`0079dc10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dbf0.md#insn-0079dc10)
- 新版 [`0079dfe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfcc.md#insn-0079dfe0) · [`0079dfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079d/0079dfcc.md#insn-0079dfec)

~~~diff
- 0079dc04 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0079dc04 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0079dc04 bytes 41000054
+ 0079dfe0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 0079dfe0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 0079dfe0 bytes 41000054
- 0079dc10 ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
- 0079dc10 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 0079dfec ["INT_EQUAL", "tmp:0:1", ["register:4058:8", "const:0:8"]]
+ 0079dfec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 0079dc10 bytes ab0100b4
+ 0079dfec bytes ab0100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a36b0e888e57a33b051563d2945d4cd"></a>

### [`0079dccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md) → [`0079e0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0a8.md) FUN_0079e0a8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079e0b4",
      "incomplete_value": false,
      "site": "0079e0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dcd8",
      "incomplete_value": false,
      "site": "0079dcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:c8:8"
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
      "0079e0b4",
      "DATA",
      [
        "storage",
        "00c7a0c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e0b4",
      "DATA",
      [
        "storage",
        "00c7b098",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dcd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md#insn-0079dcd0) · [`0079dcd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dccc.md#insn-0079dcd4)
- 新版 [`0079e0ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0a8.md#insn-0079e0ac) · [`0079e0b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0a8.md#insn-0079e0b0)

~~~diff
- 0079dcd0 ["COPY", "register:4048:8", ["const:c7a000:8"]]
+ 0079e0ac ["COPY", "register:4048:8", ["const:c7b000:8"]]
- 0079dcd0 bytes e92600b0
+ 0079e0ac bytes e92600b0
- 0079dcd4 ["COPY", "tmp:0:8", ["const:c8:8"]]
- 0079dcd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dcd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dcd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079e0b0 ["COPY", "tmp:0:8", ["const:98:8"]]
+ 0079e0b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e0b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e0b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dcd4 bytes 29210391
+ 0079e0b0 bytes 29610291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-000ea5aad621b92ecde5a4b96c9ac096"></a>

### [`0079dce8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dce8.md) → [`0079e0c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0c4.md) FUN_0079e0c4

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`0079c3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079c/0079c3f8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0079c7d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c7d4.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079dcec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0079c7d4"
      ]
    ]
  ],
  "added": [
    [
      "0079e0c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0079c7d4"
      ]
    ]
  ]
}
~~~


<a id="compare-3355daf8d509f4d77df3f5ef70cd9f8d"></a>

### [`0079dd1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md) → [`0079e0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0f8.md) FUN_0079e0f8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

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
      "definition_site": "0079e11c",
      "incomplete_value": false,
      "site": "0079e11c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dd40",
      "incomplete_value": false,
      "site": "0079dd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "0079e11c",
      "DATA",
      [
        "storage",
        "00c7a158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e11c",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dd30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md#insn-0079dd30) · [`0079dd38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md#insn-0079dd38) · [`0079dd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd1c.md#insn-0079dd3c)
- 新版 [`0079e10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0f8.md#insn-0079e10c) · [`0079e114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0f8.md#insn-0079e114) · [`0079e118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e0f8.md#insn-0079e118)

~~~diff
- 0079dd30 ["INT_ADD", "register:40f0:8", ["const:79dd30:8", "const:4:8"]]
- 0079dd30 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079e10c ["INT_ADD", "register:40f0:8", ["const:79e10c:8", "const:4:8"]]
+ 0079e10c ["CALL", null, ["callee:00c58f30:8"]]
- 0079dd30 bytes 8ce81294
+ 0079e10c bytes 89eb1294
- 0079dd38 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 0079e114 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 0079dd38 bytes e82600b0
+ 0079e114 bytes e82600b0
- 0079dd3c ["COPY", "tmp:0:8", ["const:158:8"]]
- 0079dd3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079dd3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079dd3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079e118 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 0079e118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079e118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079dd3c bytes 08610591
+ 0079e118 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49d693a0c26626174ae8c3b13f3fea57"></a>

### [`0079dd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd50.md) → [`0079e12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e12c.md) FUN_0079e12c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0079e138",
      "incomplete_value": false,
      "site": "0079e138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:128:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079dd5c",
      "incomplete_value": false,
      "site": "0079dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "0079e138",
      "DATA",
      [
        "storage",
        "00c7a158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e138",
      "DATA",
      [
        "storage",
        "00c7b128",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079dd54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd50.md#insn-0079dd54) · [`0079dd58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079dd50.md#insn-0079dd58)
- 新版 [`0079e130`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e12c.md#insn-0079e130) · [`0079e134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e12c.md#insn-0079e134)

~~~diff
- 0079dd54 ["COPY", "register:4048:8", ["const:c7a000:8"]]
+ 0079e130 ["COPY", "register:4048:8", ["const:c7b000:8"]]
- 0079dd54 bytes e92600b0
+ 0079e130 bytes e92600b0
- 0079dd58 ["COPY", "tmp:0:8", ["const:158:8"]]
- 0079dd58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0079dd58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0079dd58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0079e134 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 0079e134 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e134 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0079e134 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0079dd58 bytes 29610591
+ 0079e134 bytes 29a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a2fea28935af3994e99d14c97df1c16"></a>

### [`0079de0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md) → [`0079e1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e1e8.md) FUN_0079e1e8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0079be60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079be60.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0079c23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079c/0079c23c.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 96.10% / 新版 96.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079de4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079e228"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079e24c",
      "incomplete_value": true,
      "site": "0079e250",
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
            "const:20:8"
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
      "unmatched:0079de4c",
      "DATA",
      [
        "storage",
        "00c70690",
        null,
        "pointer"
      ]
    ],
    [
      "0079e2e0",
      "READ",
      [
        "storage",
        "00c706a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e228",
      "DATA",
      [
        "storage",
        "00c71660",
        null,
        "pointer"
      ]
    ],
    [
      "0079e2e0",
      "READ",
      [
        "storage",
        "00c71670",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079de4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md#insn-0079de4c) · [`0079de74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079d/0079de0c.md#insn-0079de74)
- 新版 [`0079e250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e1e8.md#insn-0079e250) · [`0079e228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e1e8.md#insn-0079e228)

~~~diff
- 0079de4c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0079de4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 0079de4c bytes 080000f9
- 0079de74 ["INT_ADD", "register:40f0:8", ["const:79de74:8", "const:4:8"]]
- 0079de74 ["CALL", null, ["callee:00598230:8"]]
+ 0079e250 ["INT_ADD", "register:40f0:8", ["const:79e250:8", "const:4:8"]]
+ 0079e250 ["CALL", null, ["callee:00598230:8"]]
- 0079de74 bytes 27e8f797
+ 0079e250 bytes f8e7f797
+ 0079e228 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 0079e228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 0079e228 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e10cfa66c827b6e000ffb9a4b6ec0f8"></a>

### [`0079e0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md) → [`0079e47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e47c.md) FUN_0079e47c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.34% / 新版 72.34%

CFGの説明率　旧版 11.11% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e0a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079e0a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e0a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e0a8",
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
      "0079e47c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079e480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079e484",
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

- 旧版 [`0079e0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e0a0) · [`0079e0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e0a4) · [`0079e0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e0a0.md#insn-0079e0a8)

~~~diff
- 0079e0a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079e0a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079e0a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0079e0a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079e0a0 bytes fd7bbda9
- 0079e0a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079e0a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0079e0a4 bytes f50b00f9
- 0079e0a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079e0a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079e0a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079e0a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079e0a8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f43092741f8098bc97d8b9a74056a32e"></a>

### [`0079e3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md) → [`0079e794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e794.md) FUN_0079e794

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 80.65% / 新版 80.65%

CFGの説明率　旧版 41.51% / 新版 43.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e418"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e4a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0079e7f4"
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
      "0079e7d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0079e498"
      ]
    ],
    [
      "unmatched:0079e418",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0079e498"
      ]
    ],
    [
      "0079e804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079e84c"
      ]
    ]
  ],
  "added": [
    [
      "0079e7d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079e874"
      ]
    ],
    [
      "0079e7f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079e874"
      ]
    ],
    [
      "0079e804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079e818"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e418) · [`0079e434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e434) · [`0079e45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e3b8.md#insn-0079e45c)
- 新版 [`0079e810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e794.md#insn-0079e810)

~~~diff
- 0079e418 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079e418 ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
- 0079e418 bytes 000400b4
- 0079e434 ["INT_ADD", "register:40f0:8", ["const:79e434:8", "const:4:8"]]
- 0079e434 ["CALL", null, ["callee:00c54d90:8"]]
+ 0079e810 ["INT_ADD", "register:40f0:8", ["const:79e810:8", "const:4:8"]]
+ 0079e810 ["CALL", null, ["callee:00c54d90:8"]]
- 0079e434 bytes 5bd61294
+ 0079e810 bytes 60d91294
- 0079e45c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0079e45c ["RETURN", null, ["register:0:8"]]
- 0079e45c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f871cd0510daf8bdec6fe1046edcda93"></a>

### [`0079e4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md) → [`0079e8d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e8d8.md) FUN_0079e8d8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 21.43% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e4fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e500"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079e4fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e500",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079e538",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0079e8d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079e8dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079e914",
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

- 旧版 [`0079e4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md#insn-0079e4fc) · [`0079e500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md#insn-0079e500) · [`0079e518`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e4fc.md#insn-0079e518)
- 新版 [`0079e8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e8d8.md#insn-0079e8f4)

~~~diff
- 0079e4fc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079e4fc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079e4fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079e4fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079e4fc bytes fd7bbea9
- 0079e500 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079e500 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0079e500 bytes f30b00f9
- 0079e518 ["INT_ADD", "register:40f0:8", ["const:79e518:8", "const:4:8"]]
- 0079e518 ["CALL", null, ["callee:00c54d90:8"]]
+ 0079e8f4 ["INT_ADD", "register:40f0:8", ["const:79e8f4:8", "const:4:8"]]
+ 0079e8f4 ["CALL", null, ["callee:00c54d90:8"]]
- 0079e518 bytes 22d61294
+ 0079e8f4 bytes 27d91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0751c53f7f2613ba7df71fe3b3f6961e"></a>

### [`0079e54c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md) → [`0079e928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e928.md) FUN_0079e928

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 80.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0079e934",
      "incomplete_value": false,
      "site": "0079e940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e558",
      "incomplete_value": false,
      "site": "0079e564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
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
      "0079e940",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e940",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md#insn-0079e554) · [`0079e558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md#insn-0079e558) · [`0079e56c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e54c.md#insn-0079e56c)
- 新版 [`0079e930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e928.md#insn-0079e930) · [`0079e934`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e928.md#insn-0079e934) · [`0079e948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e928.md#insn-0079e948)

~~~diff
- 0079e554 ["COPY", "register:4050:8", ["const:c7a000:8"]]
+ 0079e930 ["COPY", "register:4050:8", ["const:c7b000:8"]]
- 0079e554 bytes ea260090
+ 0079e930 bytes ea2600b0
- 0079e558 ["COPY", "tmp:0:8", ["const:258:8"]]
- 0079e558 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0079e558 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0079e558 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0079e934 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0079e934 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e934 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0079e934 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0079e558 bytes 4a610991
+ 0079e934 bytes 4aa10891
- 0079e56c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079e56c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 0079e948 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0079e948 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 0079e56c bytes 000100b4
+ 0079e948 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00a8f681191fef01bfcd7e26f9ca6161"></a>

### [`0079e5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md) → [`0079e9c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e9c8.md) FUN_0079e9c8

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e618"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079e9f4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0079ea2c",
      "incomplete_value": true,
      "site": "0079ea38",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "unmatched:0079e618",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079e9f4",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md#insn-0079e618) · [`0079e600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e5ec.md#insn-0079e600)
- 新版 [`0079e9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e9c8.md#insn-0079e9f4) · [`0079e9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079e9c8.md#insn-0079e9dc)

~~~diff
- 0079e618 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079e618 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0079e618 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0079e618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079e618 bytes 280401f8
+ 0079e9f4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 0079e9f4 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 0079e9f4 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 0079e9f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0079e9f4 bytes 280401f8
- 0079e600 ["INT_ADD", "register:40f0:8", ["const:79e600:8", "const:4:8"]]
- 0079e600 ["CALL", null, ["callee:00c58f30:8"]]
+ 0079e9dc ["INT_ADD", "register:40f0:8", ["const:79e9dc:8", "const:4:8"]]
+ 0079e9dc ["CALL", null, ["callee:00c58f30:8"]]
- 0079e600 bytes 58e61294
+ 0079e9dc bytes 55e91294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e1e89f4f269a3c3ae5e47a9cc854fa"></a>

### [`0079e674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md) → [`0079ea50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ea50.md) FUN_0079ea50

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e690"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0079ea6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0079e694"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079e690",
      "DATA",
      [
        "storage",
        "00c7a258",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0079e694",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079ea98"
      ]
    ]
  ],
  "added": [
    [
      "0079ea6c",
      "DATA",
      [
        "storage",
        "00c7b228",
        null,
        "undefined *"
      ]
    ],
    [
      "0079ea70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0079ea98"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md#insn-0079e690) · [`0079e694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e674.md#insn-0079e694)
- 新版 [`0079ea6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ea50.md#insn-0079ea6c)

~~~diff
- 0079e690 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0079e690 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0079e690 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0079e690 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079e690 bytes 290401f8
- 0079e694 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0079e694 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0079e694 bytes 480100b4
+ 0079ea6c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 0079ea6c ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 0079ea6c ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 0079ea6c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 0079ea6c bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6339a6878e1027445c5a579e2713676a"></a>

### [`0079e9c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md) → [`0079ed9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed9c.md) FUN_0079ed9c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

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
      "definition_site": "0079edb4",
      "incomplete_value": false,
      "site": "0079edc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7b000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0079e9d8",
      "incomplete_value": false,
      "site": "0079e9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7a000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
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
      "0079edc4",
      "DATA",
      [
        "storage",
        "00c7a2d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079edc4",
      "DATA",
      [
        "storage",
        "00c7b2a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079e9d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079e9d4) · [`0079e9d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079e9d8) · [`0079ea0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079e9c0.md#insn-0079ea0c)
- 新版 [`0079edb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed9c.md#insn-0079edb0) · [`0079edb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed9c.md#insn-0079edb4) · [`0079ede8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ed9c.md#insn-0079ede8)

~~~diff
- 0079e9d4 ["COPY", "register:4040:8", ["const:c7a000:8"]]
+ 0079edb0 ["COPY", "register:4040:8", ["const:c7b000:8"]]
- 0079e9d4 bytes e8260090
+ 0079edb0 bytes e82600b0
- 0079e9d8 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0079e9d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0079e9d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0079e9d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0079edb4 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 0079edb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0079edb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0079edb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0079e9d8 bytes 08610b91
+ 0079edb4 bytes 08a10a91
- 0079ea0c ["COPY", "register:0:8", ["register:4040:8"]]
- 0079ea0c ["INT_ADD", "register:40f0:8", ["const:79ea0c:8", "const:4:8"]]
- 0079ea0c ["CALLIND", null, ["register:0:8"]]
+ 0079ede8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0079ede8 ["INT_ADD", "register:40f0:8", ["const:79ede8:8", "const:4:8"]]
+ 0079ede8 ["CALLIND", null, ["register:0:8"]]
- 0079ea0c bytes 00013fd6
+ 0079ede8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe0682efb9f6e38f5ff2a95c05c1a2b"></a>

### [`0079eb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md) → [`0079ef30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079e/0079ef30.md) FUN_0079ef30

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.92% / 新版 76.92%

CFGの説明率　旧版 50.00% / 新版 52.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079eb54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079eb54"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079eb58"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079eb54",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079eb58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079eb5c",
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
      "0079ef30",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079ef34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079ef38",
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

- 旧版 [`0079eb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md#insn-0079eb54) · [`0079eb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md#insn-0079eb58) · [`0079eb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079eb54.md#insn-0079eb5c)

~~~diff
- 0079eb54 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079eb54 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079eb54 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0079eb54 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079eb54 bytes fd7bbda9
- 0079eb58 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079eb58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0079eb58 bytes f50b00f9
- 0079eb5c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079eb5c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079eb5c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079eb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079eb5c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4890ae2622e813b97d5070c25e80bb10"></a>

### [`0079ed64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md) → [`0079f140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f140.md) FUN_0079f140

採用 · 移動量 `+0x3dc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 60.87% / 新版 60.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ed68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ed68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ed6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079ed68",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ed6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079edfc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0079f144",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079f148",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079f1d8",
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

- 旧版 [`0079ed68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079ed68) · [`0079ed6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079ed6c) · [`0079ed9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ed64.md#insn-0079ed9c)
- 新版 [`0079f178`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f140.md#insn-0079f178)

~~~diff
- 0079ed68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079ed68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079ed68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079ed68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ed68 bytes fd7b02a9
- 0079ed6c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0079ed6c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0079ed6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0079ed6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ed6c bytes f65703a9
- 0079ed9c ["INT_ADD", "register:40f0:8", ["const:79ed9c:8", "const:4:8"]]
- 0079ed9c ["CALL", null, ["callee:00c54d60:8"]]
+ 0079f178 ["INT_ADD", "register:40f0:8", ["const:79f178:8", "const:4:8"]]
+ 0079f178 ["CALL", null, ["callee:00c54d60:8"]]
- 0079ed9c bytes f5d31294
+ 0079f178 bytes fad61294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cffa7b6b7701c93569bc91d9e7db0788"></a>

### [`0079ee90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md) → [`0079f26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f26c.md) FUN_0079f26c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0079eea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md#insn-0079eea0) · [`0079eeac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md#insn-0079eeac) · [`0079eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ee90.md#insn-0079eeb0)
- 新版 [`0079f27c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f26c.md#insn-0079f27c) · [`0079f288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f26c.md#insn-0079f288) · [`0079f28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f26c.md#insn-0079f28c)

~~~diff
- 0079eea0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0079eea0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 0079f27c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0079f27c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0079eea0 bytes b30000b4
+ 0079f27c bytes b30000b4
- 0079eeac ["INT_ADD", "register:40f0:8", ["const:79eeac:8", "const:4:8"]]
- 0079eeac ["CALL", null, ["callee:00c54d90:8"]]
+ 0079f288 ["INT_ADD", "register:40f0:8", ["const:79f288:8", "const:4:8"]]
+ 0079f288 ["CALL", null, ["callee:00c54d90:8"]]
- 0079eeac bytes bdd31294
+ 0079f288 bytes c2d61294
- 0079eeb0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079eeb0 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0079f28c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0079f28c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0079eeb0 bytes 800000b4
+ 0079f28c bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc4cd13b1da831884dae5d8d8a7abdcf"></a>

### [`0079ef80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md) → [`0079f35c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f35c.md) FUN_0079f35c

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 79.31% / 新版 79.31%

CFGの説明率　旧版 42.86% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ef80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ef80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079ef84"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079ef80",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079ef84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079efac",
      "DATA",
      [
        "storage",
        "00c7a358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0079f35c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079f360",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0079f388",
      "DATA",
      [
        "storage",
        "00c7b328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0079ef80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079ef80) · [`0079ef84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079ef84) · [`0079efac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079e/0079ef80.md#insn-0079efac)

~~~diff
- 0079ef80 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079ef80 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079ef80 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0079ef80 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079ef80 bytes fd7bbea9
- 0079ef84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079ef84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079ef84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0079ef84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079ef84 bytes f44f01a9
- 0079efac ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0079efac ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0079efac ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0079efac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0079efac bytes 280401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4010830fb325af9e7fe004b6a4392aa8"></a>

### [`0079f14c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f14c.md) → [`0079f528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f528.md) FUN_0079f528

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0079b424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079b/0079b424.md) · 呼出先 7件 [`00597f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00597/00597f10.md) [`005b737c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005b7/005b737c.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 1件 [`0079b800`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079b/0079b800.md) · 呼出先 7件 [`00598230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00598/00598230.md) [`005b772c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/005b7/005b772c.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.01% / 新版 87.01%

CFGの説明率　旧版 44.44% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f150"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f150"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f154"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f150",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f154",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f158",
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
      "0079f52c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0079f530",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079f534",
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

- 旧版 [`0079f150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f14c.md#insn-0079f150) · [`0079f154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f14c.md#insn-0079f154) · [`0079f158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f14c.md#insn-0079f158)

~~~diff
- 0079f150 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079f150 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079f150 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0079f150 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079f150 bytes fd7b01a9
- 0079f154 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0079f154 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0079f154 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079f154 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079f154 bytes f85f02a9
- 0079f158 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0079f158 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0079f158 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0079f158 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079f158 bytes f65703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-046febbe2c9e5672e7ccc3431ebac4dd"></a>

### [`0079f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md) → [`0079f7bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079f7bc.md) FUN_0079f7bc

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 47.06% / 新版 53.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f3e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f3e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0079f3e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0079f3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f3e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0079f3e8",
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
      "0079f7bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0079f7c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0079f7c4",
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

- 旧版 [`0079f3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f3e0) · [`0079f3e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f3e4) · [`0079f3e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f3e0.md#insn-0079f3e8)

~~~diff
- 0079f3e0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0079f3e0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0079f3e0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 0079f3e0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0079f3e0 bytes fd7bbda9
- 0079f3e4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 0079f3e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0079f3e4 bytes f50b00f9
- 0079f3e8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0079f3e8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0079f3e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 0079f3e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0079f3e8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed2958139e5d208d4d5e2679ab4477a"></a>

### [`0079f83c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md) → [`0079fc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc18.md) FUN_0079fc18

採用 · 移動量 `+0x3dc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0079fc30",
      "incomplete_value": false,
      "site": "0079fc34",
      "value": [
        "leaf",
        "const:ffffffffffffffff:8"
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
      "definition_site": "0079fc2c",
      "incomplete_value": true,
      "site": "0079fc34",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0079f858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md#insn-0079f858) · [`0079f84c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md#insn-0079f84c) · [`0079f85c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0079f/0079f83c.md#insn-0079f85c)
- 新版 [`0079fc34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc18.md#insn-0079fc34) · [`0079fc28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc18.md#insn-0079fc28) · [`0079fc38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0079f/0079fc18.md#insn-0079fc38)

~~~diff
- 0079f858 ["INT_ADD", "register:40f0:8", ["const:79f858:8", "const:4:8"]]
- 0079f858 ["CALL", null, ["callee:00c54d90:8"]]
+ 0079fc34 ["INT_ADD", "register:40f0:8", ["const:79fc34:8", "const:4:8"]]
+ 0079fc34 ["CALL", null, ["callee:00c54d90:8"]]
- 0079f858 bytes 52d11294
+ 0079fc34 bytes 57d41294
- 0079f84c ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0079f84c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 0079fc28 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 0079fc28 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 0079f84c bytes b30000b4
+ 0079fc28 bytes b30000b4
- 0079f85c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0079f85c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 0079fc38 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 0079fc38 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 0079f85c bytes 800000b4
+ 0079fc38 bytes 800000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

