# v15.7.4 → v16.0.0 · 最優先の変更候補 (78)

[一覧の目次](README.md)

<a id="compare-86ef22eee6a6c33c6782366fc5cb4361"></a>

### [`00bc8808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md) → [`00c45250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45250.md) FUN_00c45250

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 31.36% / 新版 31.36%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 6件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc880c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc880c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bc8810"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bc880c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc8810",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bc8814",
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
      "00c45254",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c45258",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4525c",
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

- 旧版 [`00bc880c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md#insn-00bc880c) · [`00bc8810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md#insn-00bc8810) · [`00bc8814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc8808.md#insn-00bc8814)

~~~diff
- 00bc880c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bc880c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bc880c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bc880c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bc880c bytes fd7bbda9
- 00bc8810 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bc8810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bc8810 bytes f50b00f9
- 00bc8814 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bc8814 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bc8814 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bc8814 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bc8814 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06bab3f516a6ed8c8e1b1a4725534088"></a>

### [`00bc93c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md) → [`00c45e10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md) FUN_00c45e10

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 3件 [`00bbdd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbdd1c.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 3件 [`00c3a764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a764.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c45eb8",
      "incomplete_value": false,
      "site": "00c45eb8",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9470",
      "incomplete_value": false,
      "site": "00bc9470",
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
            "const:308:8"
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
      "00c45eb8",
      "DATA",
      [
        "storage",
        "00c18308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c45eb8",
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc93f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc93f0) · [`00bc9438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc9438) · [`00bc9468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc93c8.md#insn-00bc9468)
- 新版 [`00c45e38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45e38) · [`00c45e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45e80) · [`00c45eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45e10.md#insn-00c45eb0)

~~~diff
- 00bc93f0 ["INT_ADD", "register:40f0:8", ["const:bc93f0:8", "const:4:8"]]
- 00bc93f0 ["CALL", null, ["callee:00c3a764:8"]]
+ 00c45e38 ["INT_ADD", "register:40f0:8", ["const:c45e38:8", "const:4:8"]]
+ 00c45e38 ["CALL", null, ["callee:00c3a764:8"]]
- 00bc93f0 bytes 4bd2ff97
+ 00c45e38 bytes 4bd2ff97
- 00bc9438 ["INT_ADD", "register:40f0:8", ["const:bc9438:8", "const:4:8"]]
- 00bc9438 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c45e80 ["INT_ADD", "register:40f0:8", ["const:c45e80:8", "const:4:8"]]
+ 00c45e80 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9438 bytes 664f0094
+ 00c45e80 bytes 684f0094
- 00bc9468 ["COPY", "register:4048:8", ["const:c18000:8"]]
+ 00c45eb0 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00bc9468 bytes 690200f0
+ 00c45eb0 bytes 890200d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98f4b2a59dfa30718452d1aedabf628e"></a>

### [`00bc94bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md) → [`00c45f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md) FUN_00c45f04

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

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
      "definition_site": "00c45f74",
      "incomplete_value": false,
      "site": "00c45f80",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc952c",
      "incomplete_value": false,
      "site": "00bc9538",
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
            "const:378:8"
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
      "00c45f80",
      "DATA",
      [
        "storage",
        "00c18378",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c45f80",
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc94f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc94f0) · [`00bc9528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc9528) · [`00bc952c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc94bc.md#insn-00bc952c)
- 新版 [`00c45f38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f38) · [`00c45f70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f70) · [`00c45f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45f04.md#insn-00c45f74)

~~~diff
- 00bc94f0 ["INT_ADD", "register:40f0:8", ["const:bc94f0:8", "const:4:8"]]
- 00bc94f0 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c45f38 ["INT_ADD", "register:40f0:8", ["const:c45f38:8", "const:4:8"]]
+ 00c45f38 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc94f0 bytes 384f0094
+ 00c45f38 bytes 3a4f0094
- 00bc9528 ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00c45f70 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc9528 bytes 680200f0
+ 00c45f70 bytes 880200d0
- 00bc952c ["COPY", "tmp:0:8", ["const:378:8"]]
- 00bc952c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc952c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc952c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c45f74 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00c45f74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c45f74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c45f74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc952c bytes 08e10d91
+ 00c45f74 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3958662cc510a2400b09cd434fc661a"></a>

### [`00bc9564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md) → [`00c45fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md) FUN_00c45fac

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

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
      "definition_site": "00c46010",
      "incomplete_value": false,
      "site": "00c46010",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc95c8",
      "incomplete_value": false,
      "site": "00bc95c8",
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
            "const:538:8"
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
      "00c46010",
      "DATA",
      [
        "storage",
        "00c18538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46010",
      "DATA",
      [
        "storage",
        "00c97ee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc9598) · [`00bc95b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc95b8) · [`00bc95bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9564.md#insn-00bc95bc)
- 新版 [`00c45fe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c45fe0) · [`00c46000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c46000) · [`00c46004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c45/00c45fac.md#insn-00c46004)

~~~diff
- 00bc9598 ["INT_ADD", "register:40f0:8", ["const:bc9598:8", "const:4:8"]]
- 00bc9598 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c45fe0 ["INT_ADD", "register:40f0:8", ["const:c45fe0:8", "const:4:8"]]
+ 00c45fe0 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9598 bytes 0e4f0094
+ 00c45fe0 bytes 104f0094
- 00bc95b8 ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00c46000 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00bc95b8 bytes 680200f0
+ 00c46000 bytes 880200b0
- 00bc95bc ["COPY", "tmp:0:8", ["const:538:8"]]
- 00bc95bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc95bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc95bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46004 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00c46004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc95bc bytes 08e11491
+ 00c46004 bytes 08813b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9d98a22906e3c41d32cb76473a2fc5"></a>

### [`00bc9604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md) → [`00c4604c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md) FUN_00c4604c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c460b8",
      "incomplete_value": false,
      "site": "00c460b8",
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
      "definition_site": "00bc9670",
      "incomplete_value": false,
      "site": "00bc9670",
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
      "00c460b8",
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
      "00c460b8",
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

- 旧版 [`00bc9638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9638) · [`00bc9660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9660) · [`00bc9664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9604.md#insn-00bc9664)
- 新版 [`00c46080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c46080) · [`00c460a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c460a8) · [`00c460ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c4604c.md#insn-00c460ac)

~~~diff
- 00bc9638 ["INT_ADD", "register:40f0:8", ["const:bc9638:8", "const:4:8"]]
- 00bc9638 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c46080 ["INT_ADD", "register:40f0:8", ["const:c46080:8", "const:4:8"]]
+ 00c46080 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9638 bytes e64e0094
+ 00c46080 bytes e84e0094
- 00bc9660 ["INT_ADD", "register:40f0:8", ["const:bc9660:8", "const:4:8"]]
- 00bc9660 ["CALL", null, ["callee:00c57be0:8"]]
+ 00c460a8 ["INT_ADD", "register:40f0:8", ["const:c460a8:8", "const:4:8"]]
+ 00c460a8 ["CALL", null, ["callee:00c57be0:8"]]
- 00bc9660 bytes cc460094
+ 00c460a8 bytes ce460094
- 00bc9664 ["COPY", "register:4048:8", ["const:c17000:8"]]
+ 00c460ac ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00bc9664 bytes 690200d0
+ 00c460ac bytes 890200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4ed735cc35c80343e1be8a961b64d76"></a>

### [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) → [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) FUN_00c460f8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 14件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md)
- 新版 呼出元 2件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 14件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.05% / 新版 95.05%

CFGの説明率　旧版 88.33% / 新版 91.91%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `store_value` 3件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46218",
      "incomplete_value": false,
      "site": "00c46218",
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
      "definition_site": "00bc97d0",
      "incomplete_value": false,
      "site": "00bc97d0",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46240",
      "incomplete_value": false,
      "site": "00c46240",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc97f8",
      "incomplete_value": false,
      "site": "00bc97f8",
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
            "const:a6:8"
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
      "site": "00bc993c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c46218",
      "DATA",
      [
        "storage",
        "00c17898",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46240",
      "DATA",
      [
        "storage",
        "002a80a6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bc994c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c463b4"
      ]
    ]
  ],
  "added": [
    [
      "00c46218",
      "DATA",
      [
        "storage",
        "00c97240",
        null,
        "undefined *"
      ]
    ],
    [
      "00c46240",
      "DATA",
      [
        "storage",
        "002b8d48",
        null,
        "string"
      ]
    ],
    [
      "00c46394",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c463b4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc993c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc993c) · [`00bc994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc994c) · [`00bc9954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md#insn-00bc9954)
- 新版 [`00c4639c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md#insn-00c4639c)

~~~diff
- 00bc993c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bc993c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bc993c bytes 690200f9
- 00bc994c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bc994c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bc994c ["CBRANCH", null, ["local:b38:8", "tmp:1:1"]]
- 00bc994c bytes 08010054
- 00bc9954 ["INT_ADD", "register:40f0:8", ["const:bc9954:8", "const:4:8"]]
- 00bc9954 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c4639c ["INT_ADD", "register:40f0:8", ["const:c4639c:8", "const:4:8"]]
+ 00c4639c ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9954 bytes 1f4e0094
+ 00c4639c bytes 214e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec5a96b49683ebebc536f406c6acab9c"></a>

### [`00bc9e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md) → [`00c46878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md) FUN_00c46878

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

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
      "definition_site": "00c468dc",
      "incomplete_value": false,
      "site": "00c468dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9e94",
      "incomplete_value": false,
      "site": "00bc9e94",
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
            "const:928:8"
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
      "00c468dc",
      "DATA",
      [
        "storage",
        "00c18928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c468dc",
      "DATA",
      [
        "storage",
        "00c982d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9e64) · [`00bc9e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9e84) · [`00bc9e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9e30.md#insn-00bc9e88)
- 新版 [`00c468ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c468ac) · [`00c468cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c468cc) · [`00c468d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46878.md#insn-00c468d0)

~~~diff
- 00bc9e64 ["INT_ADD", "register:40f0:8", ["const:bc9e64:8", "const:4:8"]]
- 00bc9e64 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c468ac ["INT_ADD", "register:40f0:8", ["const:c468ac:8", "const:4:8"]]
+ 00c468ac ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9e64 bytes db4c0094
+ 00c468ac bytes dd4c0094
- 00bc9e84 ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00c468cc ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00bc9e84 bytes 680200f0
+ 00c468cc bytes 880200d0
- 00bc9e88 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00bc9e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c468d0 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 00c468d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c468d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c468d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9e88 bytes 08a12491
+ 00c468d0 bytes 08410b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac211c0083dfcd25301a8cc2f3d415c"></a>

### [`00bc9ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md) → [`00c46918`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md) FUN_00c46918

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bc48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc4/00bc48e0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41328.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46980",
      "incomplete_value": false,
      "site": "00c46980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc9f38",
      "incomplete_value": false,
      "site": "00bc9f38",
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
            "const:998:8"
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
      "00c46980",
      "DATA",
      [
        "storage",
        "00c18998",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c46980",
      "DATA",
      [
        "storage",
        "00c98340",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc9f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f08) · [`00bc9f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f28) · [`00bc9f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc9ed0.md#insn-00bc9f2c)
- 新版 [`00c46950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c46950) · [`00c46970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c46970) · [`00c46974`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46918.md#insn-00c46974)

~~~diff
- 00bc9f08 ["INT_ADD", "register:40f0:8", ["const:bc9f08:8", "const:4:8"]]
- 00bc9f08 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c46950 ["INT_ADD", "register:40f0:8", ["const:c46950:8", "const:4:8"]]
+ 00c46950 ["CALL", null, ["callee:00c59c20:8"]]
- 00bc9f08 bytes b24c0094
+ 00c46950 bytes b44c0094
- 00bc9f28 ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00c46970 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00bc9f28 bytes 680200f0
+ 00c46970 bytes 880200d0
- 00bc9f2c ["COPY", "tmp:0:8", ["const:998:8"]]
- 00bc9f2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9f2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc9f2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c46974 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00c46974 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46974 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c46974 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc9f2c bytes 08612691
+ 00c46974 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-584e0e7162aee397c7b6b65c8da9ac7f"></a>

### [`00bca320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md) → [`00c46d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md) FUN_00c46d68

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)

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
      "definition_site": "00c46e8c",
      "incomplete_value": false,
      "site": "00c46ea4",
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
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca444",
      "incomplete_value": false,
      "site": "00bca45c",
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
            "const:9e:8"
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
      "00c46e8c",
      "PARAM",
      [
        "storage",
        "002a809e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c46e8c",
      "PARAM",
      [
        "storage",
        "002b8d40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca45c) · [`00bca440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca440) · [`00bca444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca320.md#insn-00bca444)
- 新版 [`00c46ea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46ea4) · [`00c46e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46e88) · [`00c46e8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46d68.md#insn-00c46e8c)

~~~diff
- 00bca45c ["INT_ADD", "register:40f0:8", ["const:bca45c:8", "const:4:8"]]
- 00bca45c ["CALL", null, ["callee:00c5dd00:8"]]
+ 00c46ea4 ["INT_ADD", "register:40f0:8", ["const:c46ea4:8", "const:4:8"]]
+ 00c46ea4 ["CALL", null, ["callee:00c5dd00:8"]]
- 00bca45c bytes 295b0094
+ 00c46ea4 bytes 975b0094
- 00bca440 ["COPY", "register:4010:8", ["const:2a8000:8"]]
+ 00c46e88 ["COPY", "register:4010:8", ["const:2b8000:8"]]
- 00bca440 bytes e2b6ffd0
+ 00c46e88 bytes 82b3ffd0
- 00bca444 ["COPY", "tmp:0:8", ["const:9e:8"]]
- 00bca444 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca444 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca444 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c46e8c ["COPY", "tmp:0:8", ["const:d40:8"]]
+ 00c46e8c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c46e8c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c46e8c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca444 bytes 42780291
+ 00c46e8c bytes 42003591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbadc6d38fb77345c3029fd061edb087"></a>

### [`00bca4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md) → [`00c46f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md) FUN_00c46f24

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47060",
      "incomplete_value": false,
      "site": "00c47070",
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
            "const:4dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca618",
      "incomplete_value": false,
      "site": "00bca628",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:2b7:8"
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
      "00c47060",
      "PARAM",
      [
        "storage",
        "0029c2b7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47060",
      "PARAM",
      [
        "storage",
        "002ac4dd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca628) · [`00bca614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca614) · [`00bca618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca4dc.md#insn-00bca618)
- 新版 [`00c47070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c47070) · [`00c4705c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c4705c) · [`00c47060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c46f24.md#insn-00c47060)

~~~diff
- 00bca628 ["INT_ADD", "register:40f0:8", ["const:bca628:8", "const:4:8"]]
- 00bca628 ["CALL", null, ["callee:00c5dd00:8"]]
+ 00c47070 ["INT_ADD", "register:40f0:8", ["const:c47070:8", "const:4:8"]]
+ 00c47070 ["CALL", null, ["callee:00c5dd00:8"]]
- 00bca628 bytes b65a0094
+ 00c47070 bytes 245b0094
- 00bca614 ["COPY", "register:4010:8", ["const:29c000:8"]]
+ 00c4705c ["COPY", "register:4010:8", ["const:2ac000:8"]]
- 00bca614 bytes 82b6ffd0
+ 00c4705c bytes 22b3ffb0
- 00bca618 ["COPY", "tmp:0:8", ["const:2b7:8"]]
- 00bca618 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca618 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca618 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47060 ["COPY", "tmp:0:8", ["const:4dd:8"]]
+ 00c47060 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47060 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47060 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca618 bytes 42dc0a91
+ 00c47060 bytes 42741391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d01ea6314c5f42e75d672212526d294"></a>

### [`00bca6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md) → [`00c470f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md) FUN_00c470f0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5dd00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd00.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47264",
      "incomplete_value": false,
      "site": "00c47278",
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
            "const:e0e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bca81c",
      "incomplete_value": false,
      "site": "00bca830",
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
            "const:177:8"
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
      "00c47264",
      "PARAM",
      [
        "storage",
        "002a9177",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c47264",
      "PARAM",
      [
        "storage",
        "002b9e0e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bca830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca830) · [`00bca818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca818) · [`00bca81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca6a8.md#insn-00bca81c)
- 新版 [`00c47278`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c47278) · [`00c47260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c47260) · [`00c47264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c470f0.md#insn-00c47264)

~~~diff
- 00bca830 ["INT_ADD", "register:40f0:8", ["const:bca830:8", "const:4:8"]]
- 00bca830 ["CALL", null, ["callee:00c5dd00:8"]]
+ 00c47278 ["INT_ADD", "register:40f0:8", ["const:c47278:8", "const:4:8"]]
+ 00c47278 ["CALL", null, ["callee:00c5dd00:8"]]
- 00bca830 bytes 345a0094
+ 00c47278 bytes a25a0094
- 00bca818 ["COPY", "register:4010:8", ["const:2a9000:8"]]
+ 00c47260 ["COPY", "register:4010:8", ["const:2b9000:8"]]
- 00bca818 bytes e2b6fff0
+ 00c47260 bytes 82b3ffd0
- 00bca81c ["COPY", "tmp:0:8", ["const:177:8"]]
- 00bca81c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00bca81c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00bca81c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00c47264 ["COPY", "tmp:0:8", ["const:e0e:8"]]
+ 00c47264 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47264 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00c47264 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00bca81c bytes 42dc0591
+ 00c47264 bytes 42383891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96bca1fabbf98b45e1fd5520b0016151"></a>

### [`00bca8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca8b0.md) → [`00c472f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md) FUN_00c472f8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bca8f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca8b0.md#insn-00bca8f4) · [`00bca8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca8b0.md#insn-00bca8fc) · [`00bca930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca8b0.md#insn-00bca930)
- 新版 [`00c4733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c4733c) · [`00c47344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c47344) · [`00c47378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c472f8.md#insn-00c47378)

~~~diff
- 00bca8f4 ["INT_ADD", "register:40f0:8", ["const:bca8f4:8", "const:4:8"]]
- 00bca8f4 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4733c ["INT_ADD", "register:40f0:8", ["const:c4733c:8", "const:4:8"]]
+ 00c4733c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bca8f4 bytes 574a0094
+ 00c4733c bytes 594a0094
- 00bca8fc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bca8fc ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00c47344 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c47344 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bca8fc bytes c00500b4
+ 00c47344 bytes c00500b4
- 00bca930 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bca930 ["INT_ADD", "register:40f0:8", ["const:bca930:8", "const:4:8"]]
- 00bca930 ["CALLIND", null, ["register:0:8"]]
+ 00c47378 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c47378 ["INT_ADD", "register:40f0:8", ["const:c47378:8", "const:4:8"]]
+ 00c47378 ["CALLIND", null, ["register:0:8"]]
- 00bca930 bytes 00013fd6
+ 00c47378 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb7fa17674114c2b5e0758286a4b5e64"></a>

### [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) → [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) FUN_00c4740c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bbfad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbfad0.md) [`00bc96b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc9/00bc96b0.md) [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) · 呼出先 14件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md)
- 新版 呼出元 3件 [`00c3c518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) [`00c460f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c46/00c460f8.md) [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) · 呼出先 14件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.00% / 新版 86.00%

CFGの説明率　旧版 48.47% / 新版 52.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件, `store_value` 4件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 23件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaab8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcaac4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcaaac",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ],
    [
      "unmatched:00bcaab0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c47d10"
      ]
    ],
    [
      "00c47528",
      "DATA",
      [
        "storage",
        "00c18618",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c474f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ],
    [
      "00c474f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c47d10"
      ]
    ],
    [
      "00c47528",
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcaab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcaab8) · [`00bcaac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcaac4) · [`00bcae30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md#insn-00bcae30)

~~~diff
- 00bcaab8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00bcaab8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcaab8 ["COPY", "tmp:2:8", ["tmp:0:8"]]
- 00bcaab8 ["COPY", "tmp:3:8", ["register:4000:8"]]
- 00bcaab8 bytes 157c00a9
- 00bcaac4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1330:8"]]
- 00bcaac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcaac4 bytes 609a09f9
- 00bcae30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8:8"]]
- 00bcae30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bcae30 bytes 890600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93b248ff9175e72bd99b1c59252b0c0a"></a>

### [`00bcb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md) → [`00c47e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md) FUN_00c47e58

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47eb4",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:e15:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb46c",
      "incomplete_value": false,
      "site": "00bcb484",
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
            "const:7fc:8"
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
      "definition_site": "00c47ebc",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:856:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb474",
      "incomplete_value": false,
      "site": "00bcb484",
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
            "const:195:8"
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
      "definition_site": "00c47ec4",
      "incomplete_value": false,
      "site": "00c47ecc",
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
            "const:30e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb47c",
      "incomplete_value": false,
      "site": "00bcb484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7d9:8"
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
      "00c47eb4",
      "PARAM",
      [
        "storage",
        "002917fc",
        null,
        "string"
      ]
    ],
    [
      "00c47ebc",
      "PARAM",
      [
        "storage",
        "002a2195",
        null,
        "string"
      ]
    ],
    [
      "00c47ec4",
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
      "00c47eb4",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ],
    [
      "00c47ebc",
      "PARAM",
      [
        "storage",
        "002b2856",
        null,
        "string"
      ]
    ],
    [
      "00c47ec4",
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

- 旧版 [`00bcb484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb484) · [`00bcb468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb468) · [`00bcb46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb410.md#insn-00bcb46c)
- 新版 [`00c47ecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47ecc) · [`00c47eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47eb0) · [`00c47eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c47e58.md#insn-00c47eb4)

~~~diff
- 00bcb484 ["INT_ADD", "register:40f0:8", ["const:bcb484:8", "const:4:8"]]
- 00bcb484 ["CALL", null, ["callee:00c37be4:8"]]
+ 00c47ecc ["INT_ADD", "register:40f0:8", ["const:c47ecc:8", "const:4:8"]]
+ 00c47ecc ["CALL", null, ["callee:00c37be4:8"]]
- 00bcb484 bytes 46bfff97
+ 00c47ecc bytes 46bfff97
- 00bcb468 ["COPY", "register:4000:8", ["const:291000:8"]]
+ 00c47eb0 ["COPY", "register:4000:8", ["const:2a0000:8"]]
- 00bcb468 bytes 20b6ffd0
+ 00c47eb0 bytes c0b2ffb0
- 00bcb46c ["COPY", "tmp:0:8", ["const:7fc:8"]]
- 00bcb46c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bcb46c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bcb46c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00c47eb4 ["COPY", "tmp:0:8", ["const:e15:8"]]
+ 00c47eb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00c47eb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00c47eb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bcb46c bytes 00f01f91
+ 00c47eb4 bytes 00543891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60933f8eb3ed4d20ce6a7ca78b19f361"></a>

### [`00bcb5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md) → [`00c48024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md) FUN_00c48024

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bca9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bca/00bca9c4.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c4740c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c47/00c4740c.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

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
      "definition_site": "00c48088",
      "incomplete_value": false,
      "site": "00c48088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb640",
      "incomplete_value": false,
      "site": "00bcb640",
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
            "const:848:8"
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
      "00c48088",
      "DATA",
      [
        "storage",
        "00c18848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c48088",
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb610) · [`00bcb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb630) · [`00bcb634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb5dc.md#insn-00bcb634)
- 新版 [`00c48058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c48058) · [`00c48078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c48078) · [`00c4807c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48024.md#insn-00c4807c)

~~~diff
- 00bcb610 ["INT_ADD", "register:40f0:8", ["const:bcb610:8", "const:4:8"]]
- 00bcb610 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c48058 ["INT_ADD", "register:40f0:8", ["const:c48058:8", "const:4:8"]]
+ 00c48058 ["CALL", null, ["callee:00c59c20:8"]]
- 00bcb610 bytes f0460094
+ 00c48058 bytes f2460094
- 00bcb630 ["COPY", "register:4040:8", ["const:c18000:8"]]
+ 00c48078 ["COPY", "register:4040:8", ["const:c98000:8"]]
- 00bcb630 bytes 680200b0
+ 00c48078 bytes 88020090
- 00bcb634 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00bcb634 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb634 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bcb634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c4807c ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 00c4807c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4807c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c4807c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bcb634 bytes 08212191
+ 00c4807c bytes 08c10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddaf65fd34bcc773b4521c12d0744230"></a>

### [`00bcb67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb67c.md) → [`00c480c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md) FUN_00c480c4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.96% / 新版 94.96%

CFGの説明率　旧版 71.79% / 新版 75.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb81c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c48264"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcb780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcb780",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48200"
      ]
    ],
    [
      "unmatched:00bcb81c",
      "WRITE",
      [
        "storage",
        "Stack[-0x31]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c481c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48200"
      ]
    ],
    [
      "00c48264",
      "WRITE",
      [
        "storage",
        "Stack[-0x31]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb67c.md#insn-00bcb780) · [`00bcb81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb67c.md#insn-00bcb81c)
- 新版 [`00c481c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c480c4.md#insn-00c481c8)

~~~diff
- 00bcb780 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcb780 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcb780 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 00bcb780 bytes c9010054
- 00bcb81c ["COPY", "tmp:0:4", ["register:4068:4"]]
- 00bcb81c ["INT_ADD", "tmp:1:8", ["register:4070:8", "const:14:8"]]
- 00bcb81c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcb81c bytes cd510039
+ 00c481c8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c481c8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c481c8 ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
+ 00c481c8 bytes c9010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebed3d0debd983f68224a769772e1c8b"></a>

### [`00bcb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md) → [`00c482f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md) FUN_00c482f8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48350",
      "incomplete_value": true,
      "site": "00c4835c",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:cd1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcb908",
      "incomplete_value": true,
      "site": "00bcb914",
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
                "const:292000:8"
              ],
              [
                "leaf",
                "const:5c1:8"
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
      "00c48350",
      "READ",
      [
        "storage",
        "002925c1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48350",
      "READ",
      [
        "storage",
        "002a1cd1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcb8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb8ec) · [`00bcb8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb8fc) · [`00bcb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb8b0.md#insn-00bcb900)
- 新版 [`00c48334`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c48334) · [`00c48344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c48344) · [`00c48348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c482f8.md#insn-00c48348)

~~~diff
- 00bcb8ec ["INT_ADD", "register:40f0:8", ["const:bcb8ec:8", "const:4:8"]]
- 00bcb8ec ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c48334 ["INT_ADD", "register:40f0:8", ["const:c48334:8", "const:4:8"]]
+ 00c48334 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcb8ec bytes 59460094
+ 00c48334 bytes 5b460094
- 00bcb8fc ["COPY", "register:4048:8", ["const:292000:8"]]
+ 00c48344 ["COPY", "register:4048:8", ["const:2a1000:8"]]
- 00bcb8fc bytes 29b6fff0
+ 00c48344 bytes c9b2ffb0
- 00bcb900 ["COPY", "tmp:0:8", ["const:5c1:8"]]
- 00bcb900 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb900 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcb900 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c48348 ["COPY", "tmp:0:8", ["const:cd1:8"]]
+ 00c48348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c48348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcb900 bytes 29051791
+ 00c48348 bytes 29453391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43aec923d4b833ec4ffa0e0638cacc0b"></a>

### [`00bcb938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb938.md) → [`00c48380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md) FUN_00c48380

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bcb95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb938.md#insn-00bcb95c) · [`00bcb96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcb938.md#insn-00bcb96c)
- 新版 [`00c483a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md#insn-00c483a4) · [`00c483b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48380.md#insn-00c483b4)

~~~diff
- 00bcb95c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcb95c ["INT_ADD", "register:40f0:8", ["const:bcb95c:8", "const:4:8"]]
- 00bcb95c ["CALLIND", null, ["register:0:8"]]
+ 00c483a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c483a4 ["INT_ADD", "register:40f0:8", ["const:c483a4:8", "const:4:8"]]
+ 00c483a4 ["CALLIND", null, ["register:0:8"]]
- 00bcb95c bytes 00013fd6
+ 00c483a4 bytes 00013fd6
- 00bcb96c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcb96c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c483b4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c483b4 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bcb96c bytes a1000054
+ 00c483b4 bytes a1000054
~~~


<a id="compare-463541c92b5186430cbbbaffb53c64c8"></a>

### [`00bcbd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md) → [`00c48764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md) FUN_00c48764

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48804",
      "incomplete_value": true,
      "site": "00c48814",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:e10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcbdbc",
      "incomplete_value": true,
      "site": "00bcbdcc",
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
                "const:7ec:8"
              ]
            ]
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
      "00c48804",
      "READ",
      [
        "storage",
        "002af7ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c48804",
      "READ",
      [
        "storage",
        "002c0e10",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbd48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbd48) · [`00bcbd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbd6c) · [`00bcbd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbd1c.md#insn-00bcbd74)
- 新版 [`00c48790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c48790) · [`00c487b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c487b4) · [`00c487bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48764.md#insn-00c487bc)

~~~diff
- 00bcbd48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbd48 ["INT_ADD", "register:40f0:8", ["const:bcbd48:8", "const:4:8"]]
- 00bcbd48 ["CALLIND", null, ["register:0:8"]]
+ 00c48790 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c48790 ["INT_ADD", "register:40f0:8", ["const:c48790:8", "const:4:8"]]
+ 00c48790 ["CALLIND", null, ["register:0:8"]]
- 00bcbd48 bytes 00013fd6
+ 00c48790 bytes 00013fd6
- 00bcbd6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcbd6c ["INT_ADD", "register:40f0:8", ["const:bcbd6c:8", "const:4:8"]]
- 00bcbd6c ["CALLIND", null, ["register:0:8"]]
+ 00c487b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c487b4 ["INT_ADD", "register:40f0:8", ["const:c487b4:8", "const:4:8"]]
+ 00c487b4 ["CALLIND", null, ["register:0:8"]]
- 00bcbd6c bytes 00013fd6
+ 00c487b4 bytes 00013fd6
- 00bcbd74 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00bcbd74 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00c487bc ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00c487bc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bcbd74 bytes 680400b4
+ 00c487bc bytes 680400b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef6155cf819c6dc54dbae01ebbe06334"></a>

### [`00bcbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md) → [`00c48938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md) FUN_00c48938

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 38.10% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcbf90"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c48964"
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
      "unmatched:00bcbf1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48994"
      ]
    ],
    [
      "unmatched:00bcbf90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48a00"
      ]
    ]
  ],
  "added": [
    [
      "00c48964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48994"
      ]
    ],
    [
      "00c489d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48a00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcbf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md#insn-00bcbf1c) · [`00bcbf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md#insn-00bcbf90)
- 新版 [`00c48964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md#insn-00c48964)

~~~diff
- 00bcbf1c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcbf1c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcbf1c ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bcbf1c bytes 89010054
- 00bcbf90 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcbf90 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcbf90 ["CBRANCH", null, ["local:b10:8", "tmp:1:1"]]
- 00bcbf90 bytes 49010054
+ 00c48964 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c48964 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c48964 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c48964 bytes 89010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4537eb5fbb8730fcf7da965a28b56612"></a>

### [`00bcc050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md) → [`00c48a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48a98.md) FUN_00c48a98

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bcbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbef0.md) [`00bcc3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc3b0.md) · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 2件 [`00c48938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48938.md) [`00c48df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48df8.md) · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.83% / 新版 73.83%

CFGの説明率　旧版 30.36% / 新版 35.42%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc0a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc0f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc15c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc08c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48afc"
      ]
    ],
    [
      "unmatched:00bcc0a4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcc0e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48b54"
      ]
    ]
  ],
  "added": [
    [
      "00c48ad4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48afc"
      ]
    ],
    [
      "00c48aec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c48b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c48b54"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md#insn-00bcc08c) · [`00bcc09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md#insn-00bcc09c) · [`00bcc0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc050.md#insn-00bcc0a0)

~~~diff
- 00bcc08c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcc08c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcc08c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bcc08c bytes 49010054
- 00bcc09c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcc09c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcc09c ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bcc09c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcc09c bytes 2181889a
- 00bcc0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcc0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcc0a0 bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa1526443e0cdc5b2adecc77e122215"></a>

### [`00bcc4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc4b4.md) → [`00c48efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c48/00c48efc.md) FUN_00c48efc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 34.69% / 新版 45.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc4bc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc4b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc4bc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc4c0",
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
      "00c48f00",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c48f04",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c48f08",
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

- 旧版 [`00bcc4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc4b4.md#insn-00bcc4b8) · [`00bcc4bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc4b4.md#insn-00bcc4bc) · [`00bcc4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc4b4.md#insn-00bcc4c0)

~~~diff
- 00bcc4b8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc4b8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc4b8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcc4b8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc4b8 bytes fd7bbda9
- 00bcc4bc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bcc4bc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bcc4bc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcc4bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc4bc bytes f65701a9
- 00bcc4c0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc4c0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc4c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcc4c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc4c0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df6fce6240cee34661682f714ebbf897"></a>

### [`00bcc6e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6e4.md) → [`00c4912c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c4912c.md) _ZdlPv

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc6e8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ],
  "added": [
    [
      "00c49130",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ]
}
~~~


<a id="compare-ccc6f8d97e3803b05b1a5d2430e107ff"></a>

### [`00bcc6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md) → [`00c49134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49134.md) FUN_00c49134

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc5260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc5/00bc5260.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c41ca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c41/00c41ca8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc6f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc6f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc6f4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc6f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc6f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc6f8",
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
      "00c49138",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4913c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c49140",
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

- 旧版 [`00bcc6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc6f0) · [`00bcc6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc6f4) · [`00bcc6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc6ec.md#insn-00bcc6f8)

~~~diff
- 00bcc6f0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcc6f0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcc6f0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcc6f0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcc6f0 bytes fd7bbda9
- 00bcc6f4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bcc6f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bcc6f4 bytes f50b00f9
- 00bcc6f8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc6f8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc6f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcc6f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc6f8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5fb0770363baf14607684a09cfe860"></a>

### [`00bcc78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc78c.md) → [`00c491d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md) FUN_00c491d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 50.00% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc7b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c49200"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bcc7b8"
      ],
      [
        "FALL_THROUGH",
        "00c49200"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c49200",
      "incomplete_value": true,
      "site": "00c49218",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcc7b8",
      "incomplete_value": true,
      "site": "00bcc7d0",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
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
      "unmatched:00bcc7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49230"
      ]
    ]
  ],
  "added": [
    [
      "00c49200",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49230"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc78c.md#insn-00bcc7b8) · [`00bcc7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc78c.md#insn-00bcc7b4)
- 新版 [`00c49200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c491d4.md#insn-00c49200)

~~~diff
- 00bcc7b8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcc7b8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcc7b8 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bcc7b8 bytes 89010054
+ 00c49200 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c49200 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c49200 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c49200 bytes 89010054
- 00bcc7b4 ["INT_LESSEQUAL", "register:105:1", ["register:4050:8", "register:4058:8"]]
- 00bcc7b4 ["INT_SBORROW", "register:106:1", ["register:4058:8", "register:4050:8"]]
- 00bcc7b4 ["INT_SUB", "tmp:0:8", ["register:4058:8", "register:4050:8"]]
- 00bcc7b4 ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
- 00bcc7b4 bytes 7f010aeb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-465e0e2825a70b2e046185b5d6ac986b"></a>

### [`00bcc880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md) → [`00c492c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c492c8.md) FUN_00c492c8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 38.20% / 新版 38.20%

CFGの説明率　旧版 11.39% / 新版 14.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 45件, `unresolved_call_alignment` 33件, `unresolved_store_alignment` 60件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc890"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc890"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcc8d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcc890",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcc8d4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcc8dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49a08"
      ]
    ]
  ],
  "added": [
    [
      "00c492d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c4931c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c49324",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49a08"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcc890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bcc890) · [`00bcc8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bcc8d0) · [`00bcc8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcc/00bcc880.md#insn-00bcc8d8)

~~~diff
- 00bcc890 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcc890 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcc890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bcc890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcc890 bytes f44f04a9
- 00bcc8d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcc8d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcc8d0 bytes 610a00f9
- 00bcc8d8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bcc8d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bcc8d8 bytes 600200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-691c50427857bdfc6b48f6bb71f6f4cc"></a>

### [`00bcd1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd1c4.md) → [`00c49c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49c0c.md) FUN_00c49c0c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 90.34% / 新版 90.34%

CFGの説明率　旧版 54.29% / 新版 55.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd20c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd214"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd2cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd210",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcd218",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49e40"
      ]
    ],
    [
      "unmatched:00bcd2d0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c49c58",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c49c60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c49e40"
      ]
    ],
    [
      "00c49d18",
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

- 旧版 [`00bcd208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd1c4.md#insn-00bcd208) · [`00bcd20c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd1c4.md#insn-00bcd20c) · [`00bcd210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd1c4.md#insn-00bcd210)

~~~diff
- 00bcd208 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcd208 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcd208 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bcd208 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcd208 bytes 2181889a
- 00bcd20c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcd20c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcd20c bytes 610a00f9
- 00bcd210 ["INT_ADD", "register:40f0:8", ["const:bcd210:8", "const:4:8"]]
- 00bcd210 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcd210 bytes 10400094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eddcc29d5a694b0b883f2a7b9ac396d"></a>

### [`00bcd9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md) → [`00c4a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a3f0.md) FUN_00c4a3f0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.35% / 新版 91.35%

CFGの説明率　旧版 86.54% / 新版 90.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd9ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcd9b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcd9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd9b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcd9b4",
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
      "00c4a3f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4a3f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4a3fc",
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

- 旧版 [`00bcd9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcd9ac) · [`00bcd9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcd9b0) · [`00bcd9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd9a8.md#insn-00bcd9b4)

~~~diff
- 00bcd9ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcd9ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcd9ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bcd9ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcd9ac bytes fd7bbda9
- 00bcd9b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bcd9b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bcd9b0 bytes f50b00f9
- 00bcd9b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcd9b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcd9b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bcd9b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcd9b4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a85712ee61b90bd41191d869231c6c3e"></a>

### [`00bcdc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdc94.md) → [`00c4a6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md) FUN_00c4a6dc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a740",
      "incomplete_value": true,
      "site": "00c4a750",
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
                "const:2bc000:8"
              ],
              [
                "leaf",
                "const:2c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcdcf8",
      "incomplete_value": true,
      "site": "00bcdd08",
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
                "const:39f:8"
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
      "00c4a740",
      "READ",
      [
        "storage",
        "002ab39f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4a740",
      "READ",
      [
        "storage",
        "002bc2c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdc94.md#insn-00bcdcd8) · [`00bcdcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdc94.md#insn-00bcdcec) · [`00bcdcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcdc94.md#insn-00bcdcf0)
- 新版 [`00c4a720`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a720) · [`00c4a734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a734) · [`00c4a738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a6dc.md#insn-00c4a738)

~~~diff
- 00bcdcd8 ["INT_ADD", "register:40f0:8", ["const:bcdcd8:8", "const:4:8"]]
- 00bcdcd8 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4a720 ["INT_ADD", "register:40f0:8", ["const:c4a720:8", "const:4:8"]]
+ 00c4a720 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcdcd8 bytes 5e3d0094
+ 00c4a720 bytes 603d0094
- 00bcdcec ["COPY", "register:4050:8", ["const:2ab000:8"]]
+ 00c4a734 ["COPY", "register:4050:8", ["const:2bc000:8"]]
- 00bcdcec bytes eab6ffd0
+ 00c4a734 bytes 8ab3ffd0
- 00bcdcf0 ["COPY", "tmp:0:8", ["const:39f:8"]]
- 00bcdcf0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bcdcf0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bcdcf0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4a738 ["COPY", "tmp:0:8", ["const:2c2:8"]]
+ 00c4a738 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4a738 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4a738 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bcdcf0 bytes 4a7d0e91
+ 00c4a738 bytes 4a090b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5ed7c4c5459d077cb874c1748ca4859"></a>

### [`00bcddb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md) → [`00c4a800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md) FUN_00c4a800

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4a864",
      "incomplete_value": true,
      "site": "00c4a874",
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
                "const:2c0000:8"
              ],
              [
                "leaf",
                "const:e10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcde1c",
      "incomplete_value": true,
      "site": "00bcde2c",
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
                "const:7ec:8"
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
      "00c4a864",
      "READ",
      [
        "storage",
        "002af7ec",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4a864",
      "READ",
      [
        "storage",
        "002c0e10",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcdde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcdde0) · [`00bcddfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcddfc) · [`00bcde04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcddb8.md#insn-00bcde04)
- 新版 [`00c4a828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a828) · [`00c4a844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a844) · [`00c4a84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4a800.md#insn-00c4a84c)

~~~diff
- 00bcdde0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcdde0 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcdde0 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00c4a828 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4a828 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4a828 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00bcdde0 bytes 89010054
+ 00c4a828 bytes 89010054
- 00bcddfc ["INT_ADD", "register:40f0:8", ["const:bcddfc:8", "const:4:8"]]
- 00bcddfc ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4a844 ["INT_ADD", "register:40f0:8", ["const:c4a844:8", "const:4:8"]]
+ 00c4a844 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcddfc bytes 153d0094
+ 00c4a844 bytes 173d0094
- 00bcde04 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcde04 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
+ 00c4a84c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c4a84c ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00bcde04 bytes 400600b4
+ 00c4a84c bytes 400600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eddf9dd4731a1a24387da5708ad81d14"></a>

### [`00bce234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md) → [`00c4ac7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md) FUN_00c4ac7c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 92.27% / 新版 92.27%

CFGの説明率　旧版 90.74% / 新版 94.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ad9c",
      "incomplete_value": true,
      "site": "00c4ada8",
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
                "const:2b7000:8"
              ],
              [
                "leaf",
                "const:e64:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bce354",
      "incomplete_value": true,
      "site": "00bce360",
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
                "const:2f5:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce270"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4acb8"
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
      "unmatched:00bce270",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4acd0"
      ]
    ],
    [
      "00c4ad9c",
      "READ",
      [
        "storage",
        "002a72f5",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bce260",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4acb8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4acd0"
      ]
    ],
    [
      "00c4ad9c",
      "READ",
      [
        "storage",
        "002b7e64",
        null,
        "string"
      ]
    ],
    [
      "00c4aca8",
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

- 旧版 [`00bce260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md#insn-00bce260) · [`00bce270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce234.md#insn-00bce270)
- 新版 [`00c4aca8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4ac7c.md#insn-00c4aca8)

~~~diff
- 00bce260 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bce260 ["INT_ADD", "register:40f0:8", ["const:bce260:8", "const:4:8"]]
- 00bce260 ["CALLIND", null, ["register:0:8"]]
- 00bce260 bytes 00013fd6
- 00bce270 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bce270 bytes c0000054
+ 00c4aca8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4aca8 ["INT_ADD", "register:40f0:8", ["const:c4aca8:8", "const:4:8"]]
+ 00c4aca8 ["CALLIND", null, ["register:0:8"]]
+ 00c4aca8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0b62f7bec1ea0f6e5a0f0cd063b402f"></a>

### [`00bce544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md) → [`00c4af8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4a/00c4af8c.md) FUN_00c4af8c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bcd004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c49a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c49/00c49a4c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.04% / 新版 84.04%

CFGの説明率　旧版 4.35% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce5b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce5b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce58c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bce5ac",
      "READ",
      [
        "storage",
        "0029c31a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bce5e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b054"
      ]
    ]
  ],
  "added": [
    [
      "00c4afd4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4aff4",
      "READ",
      [
        "storage",
        "002ac540",
        null,
        "string"
      ]
    ],
    [
      "00c4b028",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b054"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bce584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce584) · [`00bce588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce588) · [`00bce58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce544.md#insn-00bce58c)

~~~diff
- 00bce584 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bce584 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bce584 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00bce584 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bce584 bytes 4181899a
- 00bce588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bce588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bce588 bytes 610a00f9
- 00bce58c ["INT_ADD", "register:40f0:8", ["const:bce58c:8", "const:4:8"]]
- 00bce58c ["CALL", null, ["callee:00c59ca0:8"]]
- 00bce58c bytes 313b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e22f6e12a3379deb9ee5042e40d004c8"></a>

### [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) → [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) FUN_00c4b200

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) · 呼出先 8件 [`00bc1ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1ccc.md) [`00bc2090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2090.md) [`00bc21c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc21c4.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) · 呼出先 8件 [`00c3e714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) [`00c3ead8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ead8.md) [`00c3ec0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3ec0c.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.66% / 新版 88.66%

CFGの説明率　旧版 67.50% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce808"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bce824"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4b250"
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
      "unmatched:00bce808",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b358"
      ]
    ],
    [
      "unmatched:00bce824",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b2ec"
      ]
    ],
    [
      "unmatched:00bce828",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ]
  ],
  "added": [
    [
      "00c4b250",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b358"
      ]
    ],
    [
      "00c4b26c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b2ec"
      ]
    ],
    [
      "00c4b270",
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

- 旧版 [`00bce808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md#insn-00bce808) · [`00bce824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md#insn-00bce824) · [`00bce828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md#insn-00bce828)

~~~diff
- 00bce808 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bce808 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
- 00bce808 bytes 41080054
- 00bce824 ["CBRANCH", null, ["local:b18:8", "register:101:1"]]
- 00bce824 bytes 00040054
- 00bce828 ["INT_ADD", "register:40f0:8", ["const:bce828:8", "const:4:8"]]
- 00bce828 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bce828 bytes 8a3a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d035408c2d226b42761f2a9411c8b99"></a>

### [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) → [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) FUN_00c4b384

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc67fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc67fc.md) · 呼出先 6件 [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bce7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce7b8.md) [`00bcecec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c43244`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c43/00c43244.md) · 呼出先 6件 [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c4b200`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b200.md) [`00c4b734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.32% / 新版 82.32%

CFGの説明率　旧版 73.68% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `store_value` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcea14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcea14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcea1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bce994",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b3e8"
      ]
    ],
    [
      "00c4b444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcea24"
      ]
    ],
    [
      "unmatched:00bcea08",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59c20"
      ]
    ]
  ],
  "added": [
    [
      "00c4b3dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b3e8"
      ]
    ],
    [
      "00c4b444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4b46c"
      ]
    ],
    [
      "00c4b450",
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

- 旧版 [`00bce994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bce994) · [`00bcea08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bcea08) · [`00bcea0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md#insn-00bcea0c)

~~~diff
- 00bce994 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bce994 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bce994 bytes 61000054
- 00bcea08 ["INT_ADD", "register:40f0:8", ["const:bcea08:8", "const:4:8"]]
- 00bcea08 ["CALL", null, ["callee:00c59c20:8"]]
- 00bcea08 bytes f2390094
- 00bcea0c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bcea0c ["CBRANCH", null, ["local:b35:8", "tmp:0:1"]]
- 00bcea0c bytes e00d00b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca124e7530871503da5e19d49b4e112b"></a>

### [`00bcecec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md) → [`00c4b734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b734.md) FUN_00c4b734

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) [`00bce93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bce93c.md) · 呼出先 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1140.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) [`00c4b384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4b384.md) · 呼出先 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3db88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3d/00c3db88.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.40% / 新版 72.40%

CFGの説明率　旧版 37.21% / 新版 45.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bceda4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcedc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcee30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4b78c",
      "READ",
      [
        "storage",
        "00c17bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4b79c",
      "READ",
      [
        "storage",
        "00c17bb9",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4b7c8",
      "READ",
      [
        "storage",
        "00c17bc8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c4b78c",
      "READ",
      [
        "storage",
        "00c97560",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4b79c",
      "READ",
      [
        "storage",
        "00c97561",
        null,
        "undefined1"
      ]
    ],
    [
      "00c4b7c8",
      "READ",
      [
        "storage",
        "00c97570",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bceda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bceda4) · [`00bcedc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bcedc8) · [`00bcee30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bce/00bcecec.md#insn-00bcee30)

~~~diff
- 00bceda4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bceda4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bceda4 bytes 080000f9
- 00bcedc8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00bcedc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:309:8"]]
- 00bcedc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bcedc8 bytes 08240c39
- 00bcee30 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:8:8"]]
- 00bcee30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bcee30 bytes ea0600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a64d8c0d2518e97efb8ca55a5be1a23"></a>

### [`00bcf108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf108.md) → [`00c4bb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md) FUN_00c4bb50

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bbb4",
      "incomplete_value": true,
      "site": "00c4bbc4",
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
                "const:655:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf16c",
      "incomplete_value": true,
      "site": "00bcf17c",
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
                "const:5dd:8"
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
      "00c4bbb4",
      "READ",
      [
        "storage",
        "002ac5dd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4bbb4",
      "READ",
      [
        "storage",
        "002bd655",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf108.md#insn-00bcf14c) · [`00bcf160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf108.md#insn-00bcf160) · [`00bcf164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf108.md#insn-00bcf164)
- 新版 [`00c4bb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bb94) · [`00c4bba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bba8) · [`00c4bbac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bb50.md#insn-00c4bbac)

~~~diff
- 00bcf14c ["INT_ADD", "register:40f0:8", ["const:bcf14c:8", "const:4:8"]]
- 00bcf14c ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4bb94 ["INT_ADD", "register:40f0:8", ["const:c4bb94:8", "const:4:8"]]
+ 00c4bb94 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bcf14c bytes 41380094
+ 00c4bb94 bytes 43380094
- 00bcf160 ["COPY", "register:4050:8", ["const:2ac000:8"]]
+ 00c4bba8 ["COPY", "register:4050:8", ["const:2bd000:8"]]
- 00bcf160 bytes eab6ffb0
+ 00c4bba8 bytes 8ab3ffd0
- 00bcf164 ["COPY", "tmp:0:8", ["const:5dd:8"]]
- 00bcf164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bcf164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bcf164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbac ["COPY", "tmp:0:8", ["const:655:8"]]
+ 00c4bbac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4bbac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bcf164 bytes 4a751791
+ 00c4bbac bytes 4a551991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40ddaa75732618933109d0a43e73d9e1"></a>

### [`00bcf4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md) → [`00c4bf10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md) FUN_00c4bf10

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.18% / 新版 88.18%

CFGの説明率　旧版 67.74% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4c070",
      "incomplete_value": true,
      "site": "00c4c07c",
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
            "register:4040:8"
          ]
        ]
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
      "definition_site": "00c4c0a4",
      "incomplete_value": false,
      "site": "00c4c0bc",
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
            "const:e15:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf65c",
      "incomplete_value": false,
      "site": "00bcf674",
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
            "const:7fc:8"
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
      "definition_site": "00c4c0ac",
      "incomplete_value": false,
      "site": "00c4c0bc",
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
            "const:856:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf664",
      "incomplete_value": false,
      "site": "00bcf674",
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
            "const:195:8"
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
      "00c4bfc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bcf5c0"
      ]
    ],
    [
      "unmatched:00bcf58c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c014"
      ]
    ],
    [
      "00c4c014",
      "READ",
      [
        "storage",
        "002a924c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4bfc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c008"
      ]
    ],
    [
      "00c4bfd4",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c014"
      ]
    ],
    [
      "00c4c014",
      "READ",
      [
        "storage",
        "002b9ee3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf634) · [`00bcf674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf674) · [`00bcf4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf4c8.md#insn-00bcf4d8)
- 新版 [`00c4c07c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md#insn-00c4c07c) · [`00c4c0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4b/00c4bf10.md#insn-00c4c0bc)

~~~diff
- 00bcf634 ["INT_ADD", "register:40f0:8", ["const:bcf634:8", "const:4:8"]]
- 00bcf634 ["CALL", null, ["callee:00c57c00:8"]]
+ 00c4c07c ["INT_ADD", "register:40f0:8", ["const:c4c07c:8", "const:4:8"]]
+ 00c4c07c ["CALL", null, ["callee:00c57c00:8"]]
- 00bcf634 bytes df2e0094
+ 00c4c07c bytes e12e0094
- 00bcf674 ["INT_ADD", "register:40f0:8", ["const:bcf674:8", "const:4:8"]]
- 00bcf674 ["CALL", null, ["callee:00c37be4:8"]]
+ 00c4c0bc ["INT_ADD", "register:40f0:8", ["const:c4c0bc:8", "const:4:8"]]
+ 00c4c0bc ["CALL", null, ["callee:00c37be4:8"]]
- 00bcf674 bytes caaeff97
+ 00c4c0bc bytes caaeff97
- 00bcf4d8 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00bcf4d8 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d46dbc91ed795275daf71c4b5ac58ca"></a>

### [`00bcf764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md) → [`00c4c1ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md) FUN_00c4c1ac

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 91.61% / 新版 91.61%

CFGの説明率　旧版 88.57% / 新版 91.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c2ec",
      "incomplete_value": true,
      "site": "00c4c2f4",
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
                "const:a70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf8a4",
      "incomplete_value": true,
      "site": "00bcf8ac",
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
                "const:203:8"
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
      "definition_site": "00c4c2f0",
      "incomplete_value": true,
      "site": "00c4c2f8",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf8a8",
      "incomplete_value": true,
      "site": "00bcf8b0",
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
                "const:d:8"
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
      "definition_site": "00c4c358",
      "incomplete_value": true,
      "site": "00c4c360",
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
                "const:2bb000:8"
              ],
              [
                "leaf",
                "const:156:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf910",
      "incomplete_value": true,
      "site": "00bcf918",
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
                "const:2aa000:8"
              ],
              [
                "leaf",
                "const:3da:8"
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
      "00c4c2ec",
      "READ",
      [
        "storage",
        "002a4203",
        null,
        "string"
      ]
    ],
    [
      "00c4c2f0",
      "READ",
      [
        "storage",
        "002a4210",
        null,
        "string"
      ]
    ],
    [
      "00c4c358",
      "READ",
      [
        "storage",
        "002aa3da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4c2ec",
      "READ",
      [
        "storage",
        "002b4a70",
        null,
        "string"
      ]
    ],
    [
      "00c4c2f0",
      "READ",
      [
        "storage",
        "002b4a7d",
        null,
        "string"
      ]
    ],
    [
      "00c4c358",
      "READ",
      [
        "storage",
        "002bb156",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md#insn-00bcf7a4) · [`00bcf790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf764.md#insn-00bcf790)
- 新版 [`00c4c1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md#insn-00c4c1ec) · [`00c4c1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c1ac.md#insn-00c4c1d8)

~~~diff
- 00bcf7a4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcf7a4 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcf7a4 ["COPY", "tmp:2:8", ["register:4050:8"]]
- 00bcf7a4 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcf7a4 bytes 4181899a
+ 00c4c1ec ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c4c1ec ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c4c1ec ["COPY", "tmp:2:8", ["register:4050:8"]]
+ 00c4c1ec ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
+ 00c4c1ec bytes 4181899a
- 00bcf790 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcf790 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcf790 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
+ 00c4c1d8 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4c1d8 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4c1d8 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
- 00bcf790 bytes 89010054
+ 00c4c1d8 bytes 89010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a67a59eb38d3b77bc44ef3f751f3de2"></a>

### [`00bcf9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9a0.md) → [`00c4c3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md) FUN_00c4c3e8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00c4c408",
      "incomplete_value": true,
      "site": "00c4c40c",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:d48:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bcf9c0",
      "incomplete_value": true,
      "site": "00bcf9c4",
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
                "const:2fd000:8"
              ],
              [
                "leaf",
                "const:f10:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
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
      "00c4c3f8",
      "DATA",
      [
        "storage",
        "002fdee0",
        null,
        null
      ]
    ],
    [
      "00c4c404",
      "DATA",
      [
        "storage",
        "002fdf10",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4c3f8",
      "DATA",
      [
        "storage",
        "00313d18",
        null,
        null
      ]
    ],
    [
      "00c4c404",
      "DATA",
      [
        "storage",
        "00313d48",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcf9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9a0.md#insn-00bcf9a8) · [`00bcf9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9a0.md#insn-00bcf9ac) · [`00bcf9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcf9a0.md#insn-00bcf9b4)
- 新版 [`00c4c3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md#insn-00c4c3f0) · [`00c4c3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c3e8.md#insn-00c4c3f4)

~~~diff
- 00bcf9a8 ["COPY", "register:4048:8", ["const:2fd000:8"]]
+ 00c4c3f0 ["COPY", "register:4048:8", ["const:313000:8"]]
- 00bcf9a8 bytes 69b9ffd0
+ 00c4c3f0 bytes 29b6fff0
- 00bcf9ac ["COPY", "tmp:0:8", ["const:ee0:8"]]
- 00bcf9ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bcf9ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bcf9ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00c4c3f4 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00c4c3f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c3f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00c4c3f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bcf9ac bytes 29813b91
+ 00c4c3f4 bytes 29613491
- 00bcf9b4 ["COPY", "register:4048:8", ["const:2fd000:8"]]
- 00bcf9b4 bytes 69b9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1712aadf3ae9fef12b1eed2971c2a26"></a>

### [`00bcfa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfa38.md) → [`00c4c480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md) FUN_00c4c480

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 52.38% / 新版 61.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfb30"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4c578"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bcfb30"
      ],
      [
        "FALL_THROUGH",
        "00c4c578"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c4c578",
      "incomplete_value": true,
      "site": "00c4c58c",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
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
      "definition_site": "00bcfb30",
      "incomplete_value": true,
      "site": "00bcfb44",
      "value": [
        "BOOL_OR",
        "1",
        [
          [
            "BOOL_NEGATE",
            "1",
            [
              "INT_LESSEQUAL"
            ]
          ],
          [
            "INT_EQUAL",
            "1",
            [
              "INT_SUB",
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ]
        ]
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
      "unmatched:00bcfb30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c5a0"
      ]
    ]
  ],
  "added": [
    [
      "00c4c578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c5a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfa38.md#insn-00bcfb30) · [`00bcfa60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfa38.md#insn-00bcfa60)
- 新版 [`00c4c578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md#insn-00c4c578) · [`00c4c4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c480.md#insn-00c4c4a8)

~~~diff
- 00bcfb30 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcfb30 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcfb30 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00bcfb30 bytes 49010054
+ 00c4c578 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4c578 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4c578 ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
+ 00c4c578 bytes 49010054
- 00bcfa60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcfa60 ["INT_ADD", "register:40f0:8", ["const:bcfa60:8", "const:4:8"]]
- 00bcfa60 ["CALLIND", null, ["register:0:8"]]
+ 00c4c4a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4c4a8 ["INT_ADD", "register:40f0:8", ["const:c4c4a8:8", "const:4:8"]]
+ 00c4c4a8 ["CALLIND", null, ["register:0:8"]]
- 00bcfa60 bytes 00013fd6
+ 00c4c4a8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b50ad4c28e4de6a87b423c3ab1d315a"></a>

### [`00bcfba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfba8.md) → [`00c4c5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c5f0.md) FUN_00c4c5f0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 68.42% / 新版 68.42%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfbac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfbac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfbb0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcfbac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcfbb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bcfbdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c650"
      ]
    ]
  ],
  "added": [
    [
      "00c4c5f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4c5f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c4c624",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c650"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfbac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfba8.md#insn-00bcfbac) · [`00bcfbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfba8.md#insn-00bcfbb0) · [`00bcfbdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfba8.md#insn-00bcfbdc)

~~~diff
- 00bcfbac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bcfbac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bcfbac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bcfbac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bcfbac bytes fd7bbea9
- 00bcfbb0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bcfbb0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bcfbb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bcfbb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bcfbb0 bytes f44f01a9
- 00bcfbdc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcfbdc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcfbdc ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bcfbdc bytes 69010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7332cbf2b6c5c48cb5341ae05e77bb2"></a>

### [`00bcfc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc8c.md) → [`00c4c6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6d4.md) _ZdlPv

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcfc90",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ],
  "added": [
    [
      "00c4c6d8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ]
}
~~~


<a id="compare-1a127cdd31d6525d0880a32990c80265"></a>

### [`00bcfc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md) → [`00c4c6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c6dc.md) FUN_00c4c6dc

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bc24a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc24a0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3eee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3eee8.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 22.22% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfd04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfd14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfd18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcfcc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c734"
      ]
    ],
    [
      "unmatched:00bcfd04",
      "DATA",
      [
        "storage",
        "00c19488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4c710",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c734"
      ]
    ],
    [
      "00c4c74c",
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfcc8) · [`00bcfd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfd04) · [`00bcfd14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfc94.md#insn-00bcfd14)

~~~diff
- 00bcfcc8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcfcc8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcfcc8 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bcfcc8 bytes 28010054
- 00bcfd04 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bcfd04 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bcfd04 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bcfd04 bytes 090c01f8
- 00bcfd14 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00bcfd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bcfd14 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-483e5fb0cf84b8a1f2f9d528bbce083d"></a>

### [`00bcfd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfd54.md) → [`00c4c79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c79c.md) FUN_00c4c79c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.77% / 新版 70.77%

CFGの説明率　旧版 15.38% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfda0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfe0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4c7e8"
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
      "unmatched:00bcfd88",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c800"
      ]
    ],
    [
      "unmatched:00bcfda4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bcfdf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c868"
      ]
    ]
  ],
  "added": [
    [
      "00c4c7d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c800"
      ]
    ],
    [
      "00c4c7ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4c840",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c868"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bcfd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfd54.md#insn-00bcfd88) · [`00bcfd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfd54.md#insn-00bcfd9c) · [`00bcfda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfd54.md#insn-00bcfda0)

~~~diff
- 00bcfd88 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcfd88 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcfd88 ["CBRANCH", null, ["local:b9:8", "tmp:1:1"]]
- 00bcfd88 bytes 89010054
- 00bcfd9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bcfd9c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bcfd9c ["COPY", "tmp:2:8", ["register:4040:8"]]
- 00bcfd9c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bcfd9c bytes 0181899a
- 00bcfda0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bcfda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bcfda0 bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fea3cda5dac1b2292fa9aa38ace662a"></a>

### [`00bcfe60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfe60.md) → [`00c4c8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md) FUN_00c4c8a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 12.50% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcfec4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c4c90c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bcff10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bcfec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c938"
      ]
    ],
    [
      "unmatched:00bcff10",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4c90c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4c938"
      ]
    ],
    [
      "00c4c958",
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

- 旧版 [`00bcfec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfe60.md#insn-00bcfec4) · [`00bcff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcf/00bcfe60.md#insn-00bcff10)
- 新版 [`00c4c90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4c8a8.md#insn-00c4c90c)

~~~diff
- 00bcfec4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bcfec4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bcfec4 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00bcfec4 bytes 69010054
- 00bcff10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bcff10 ["INT_ADD", "register:40f0:8", ["const:bcff10:8", "const:4:8"]]
- 00bcff10 ["CALLIND", null, ["register:0:8"]]
- 00bcff10 bytes 00013fd6
+ 00c4c90c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c4c90c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c4c90c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00c4c90c bytes 69010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6647cf0bac709edcd77f5c80eaaacf6f"></a>

### [`00bd0280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md) → [`00c4ccc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4c/00c4ccc8.md) FUN_00c4ccc8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbf39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbf39c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3bde4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3b/00c3bde4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd02ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd030c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd030c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd02ec",
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
      "00c4cd34",
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

- 旧版 [`00bd02ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd02ec) · [`00bd030c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd030c) · [`00bd0310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0280.md#insn-00bd0310)

~~~diff
- 00bd02ec ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bd02ec ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00bd02ec ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00bd02ec bytes 890e01f8
- 00bd030c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd030c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bd030c ["INT_ADD", "tmp:2:8", ["register:40a0:8", "const:10:8"]]
- 00bd030c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd030c bytes 932201a9
- 00bd0310 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd0310 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:9:8"]]
- 00bd0310 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00bd0310 bytes 89920078
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72a441e05e5d6673be8a5e2d4481af1e"></a>

### [`00bd0800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0800.md) → [`00c4d248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d248.md) _ZdlPv

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0804",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ],
  "added": [
    [
      "00c4d24c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ]
}
~~~


<a id="compare-086bd567ec12e2ea62213c6ade043b25"></a>

### [`00bd095c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md) → [`00c4d3a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md) FUN_00c4d3a4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

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
      "definition_site": "00c4d408",
      "incomplete_value": true,
      "site": "00c4d41c",
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
                "const:daf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd09c0",
      "incomplete_value": true,
      "site": "00bd09d4",
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
                "const:294000:8"
              ],
              [
                "leaf",
                "const:499:8"
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
      "00c4d408",
      "READ",
      [
        "storage",
        "00294499",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4d408",
      "READ",
      [
        "storage",
        "002a3daf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd09a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09a0) · [`00bd09b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09b4) · [`00bd09b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd095c.md#insn-00bd09b8)
- 新版 [`00c4d3e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d3e8) · [`00c4d3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d3fc) · [`00c4d400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d3a4.md#insn-00c4d400)

~~~diff
- 00bd09a0 ["INT_ADD", "register:40f0:8", ["const:bd09a0:8", "const:4:8"]]
- 00bd09a0 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c4d3e8 ["INT_ADD", "register:40f0:8", ["const:c4d3e8:8", "const:4:8"]]
+ 00c4d3e8 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd09a0 bytes 2c320094
+ 00c4d3e8 bytes 2e320094
- 00bd09b4 ["COPY", "register:4050:8", ["const:294000:8"]]
+ 00c4d3fc ["COPY", "register:4050:8", ["const:2a3000:8"]]
- 00bd09b4 bytes 2ab6ff90
+ 00c4d3fc bytes aab2ffd0
- 00bd09b8 ["COPY", "tmp:0:8", ["const:499:8"]]
- 00bd09b8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00bd09b8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00bd09b8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00c4d400 ["COPY", "tmp:0:8", ["const:daf:8"]]
+ 00c4d400 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d400 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00c4d400 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00bd09b8 bytes 4a651291
+ 00c4d400 bytes 4abd3691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f41d74f678f81c27c82459a8d12994cc"></a>

### [`00bd0c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0c58.md) → [`00c4d6a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4d6a0.md) FUN_00c4d6a0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.78% / 新版 60.78%

CFGの説明率　旧版 20.22% / 新版 26.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 4件, `store_value` 2件, `unresolved_branch_alignment` 16件, `unresolved_call_alignment` 15件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0ca4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd0cac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd0c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d704"
      ]
    ],
    [
      "unmatched:00bd0ca8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd0cb0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd1034"
      ]
    ]
  ],
  "added": [
    [
      "00c4d6d8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4d704"
      ]
    ],
    [
      "00c4d6f0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4d6f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4da7c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd0c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0c58.md#insn-00bd0c8c) · [`00bd0ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0c58.md#insn-00bd0ca4) · [`00bd0cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd0/00bd0c58.md#insn-00bd0cac)

~~~diff
- 00bd0c8c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:20:8"]]
- 00bd0c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 00bd0c8c bytes 2b2000b9
- 00bd0ca4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd0ca4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd0ca4 bytes 610a00f9
- 00bd0cac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd0cac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bd0cac bytes 600200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0fee6425b391310418e91e05828701a"></a>

### [`00bd105c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd105c.md) → [`00c4daa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4daa4.md) FUN_00c4daa4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.33% / 新版 70.33%

CFGの説明率　旧版 2.44% / 新版 4.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 3件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1060",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1064",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1068",
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
      "00c4daa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4daac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4dab0",
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

- 旧版 [`00bd1060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd105c.md#insn-00bd1060) · [`00bd1064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd105c.md#insn-00bd1064) · [`00bd1068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd105c.md#insn-00bd1068)

~~~diff
- 00bd1060 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd1060 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd1060 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd1060 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd1060 bytes fd7bbda9
- 00bd1064 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd1064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bd1064 bytes f50b00f9
- 00bd1068 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd1068 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd1068 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd1068 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1068 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-126386f1d8ecc2cd664d99c5d931aa44"></a>

### [`00bd11c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11c8.md) → [`00c4dc10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc10.md) _ZdlPv

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd11cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ],
  "added": [
    [
      "00c4dc14",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ]
}
~~~


<a id="compare-3443f08118e5bc912930d3e94cb85b91"></a>

### [`00bd11d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md) → [`00c4dc18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4d/00c4dc18.md) FUN_00c4dc18

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 8件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bbff70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbf/00bbff70.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 8件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3c9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c9b8.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.85% / 新版 87.85%

CFGの説明率　旧版 59.86% / 新版 67.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_value` 4件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd11dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd11d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd11dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd11e0",
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
      "00c4dc20",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c4dc24",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c4dc28",
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

- 旧版 [`00bd11d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd11d8) · [`00bd11dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd11dc) · [`00bd11e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd11d0.md#insn-00bd11e0)

~~~diff
- 00bd11d8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd11d8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd11d8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd11d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd11d8 bytes fd7b01a9
- 00bd11dc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bd11dc ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bd11dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd11dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd11dc bytes fc6f02a9
- 00bd11e0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bd11e0 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bd11e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00bd11e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd11e0 bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6994ce4d321389d587f07a9d3d9eb89c"></a>

### [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) → [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) FUN_00c4e1c0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) · 呼出先 5件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc1754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc1/00bc1754.md) [`00bd1778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 2件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) · 呼出先 5件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3e19c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e19c.md) [`00c4e1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e1c0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.61% / 新版 75.61%

CFGの説明率　旧版 34.21% / 新版 45.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 5件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 29件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd177c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd177c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1780"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd177c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1780",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1784",
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
      "00c4e1c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c4e1c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4e1cc",
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

- 旧版 [`00bd177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd177c) · [`00bd1780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd1780) · [`00bd1784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1778.md#insn-00bd1784)

~~~diff
- 00bd177c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd177c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd177c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00bd177c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd177c bytes fd7bbca9
- 00bd1780 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00bd1780 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00bd1780 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd1780 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1780 bytes f85f01a9
- 00bd1784 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd1784 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd1784 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd1784 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1784 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-585acd20652379fee0a4f2dd8dcd0496"></a>

### [`00bd1b50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md) → [`00c4e598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e598.md) FUN_00c4e598

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 72.09% / 新版 72.09%

CFGの説明率　旧版 37.50% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1bbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1bd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1bdc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1bbc",
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
      "00c4e604",
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

- 旧版 [`00bd1bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1bbc) · [`00bd1bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1bd4) · [`00bd1bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1b50.md#insn-00bd1bdc)

~~~diff
- 00bd1bbc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bd1bbc ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00bd1bbc ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00bd1bbc bytes 890e01f8
- 00bd1bd4 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd1bd4 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:8:8"]]
- 00bd1bd4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1bd4 bytes 8a220039
- 00bd1bdc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd1bdc ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bd1bdc ["INT_ADD", "tmp:2:8", ["register:40a0:8", "const:10:8"]]
- 00bd1bdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1bdc bytes 932201a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af61bd2ffa83b2283789eac0a2d8d210"></a>

### [`00bd1bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md) → [`00c4e644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e644.md) FUN_00c4e644

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 72.09% / 新版 72.09%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1c68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1c80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1c88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1c68",
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
      "00c4e6b0",
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

- 旧版 [`00bd1c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c68) · [`00bd1c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c80) · [`00bd1c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1bfc.md#insn-00bd1c88)

~~~diff
- 00bd1c68 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bd1c68 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00bd1c68 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00bd1c68 bytes 890e01f8
- 00bd1c80 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd1c80 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:8:8"]]
- 00bd1c80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1c80 bytes 8a220039
- 00bd1c88 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bd1c88 ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bd1c88 ["INT_ADD", "tmp:2:8", ["register:40a0:8", "const:10:8"]]
- 00bd1c88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1c88 bytes 932201a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afa910789fd4dcc051bb3aff86149b4"></a>

### [`00bd1ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md) → [`00c4e6f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md) FUN_00c4e6f0

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 3件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 3件 [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e75c",
      "incomplete_value": false,
      "site": "00c4e75c",
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
      "definition_site": "00bd1d14",
      "incomplete_value": false,
      "site": "00bd1d14",
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
      "00c4e75c",
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
      "00c4e75c",
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

- 旧版 [`00bd1cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1cdc) · [`00bd1d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1d04) · [`00bd1d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ca8.md#insn-00bd1d08)
- 新版 [`00c4e724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e724) · [`00c4e74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e74c) · [`00c4e750`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e6f0.md#insn-00c4e750)

~~~diff
- 00bd1cdc ["INT_ADD", "register:40f0:8", ["const:bd1cdc:8", "const:4:8"]]
- 00bd1cdc ["CALL", null, ["callee:00c59c20:8"]]
+ 00c4e724 ["INT_ADD", "register:40f0:8", ["const:c4e724:8", "const:4:8"]]
+ 00c4e724 ["CALL", null, ["callee:00c59c20:8"]]
- 00bd1cdc bytes 3d2d0094
+ 00c4e724 bytes 3f2d0094
- 00bd1d04 ["INT_ADD", "register:40f0:8", ["const:bd1d04:8", "const:4:8"]]
- 00bd1d04 ["CALL", null, ["callee:00c57be0:8"]]
+ 00c4e74c ["INT_ADD", "register:40f0:8", ["const:c4e74c:8", "const:4:8"]]
+ 00c4e74c ["CALL", null, ["callee:00c57be0:8"]]
- 00bd1d04 bytes 23250094
+ 00c4e74c bytes 25250094
- 00bd1d08 ["COPY", "register:4048:8", ["const:c17000:8"]]
+ 00c4e750 ["COPY", "register:4048:8", ["const:c97000:8"]]
- 00bd1d08 bytes 290200d0
+ 00c4e750 bytes 490200b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fd296d2dee04954e610f86f1d91e397"></a>

### [`00bd1d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md) → [`00c4e79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md) FUN_00c4e79c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4e7fc"
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
      "unmatched:00bd1dbc",
      "DATA",
      [
        "storage",
        "00c19d48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e804",
      "DATA",
      [
        "storage",
        "00c996f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md#insn-00bd1db4) · [`00bd1dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1d54.md#insn-00bd1dbc)
- 新版 [`00c4e7fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e79c.md#insn-00c4e7fc)

~~~diff
- 00bd1db4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bd1db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd1db4 bytes c90600f9
- 00bd1dbc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd1dbc ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd1dbc ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd1dbc bytes 080c01f8
+ 00c4e7fc ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
+ 00c4e7fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c4e7fc bytes c90600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ade49c498722e2f2dd10888aab42ece"></a>

### [`00bd1e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md) → [`00c4e848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e848.md) FUN_00c4e848

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1e70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1e64",
      "DATA",
      [
        "storage",
        "00c19db8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e8ac",
      "DATA",
      [
        "storage",
        "00c99760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e5c) · [`00bd1e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e64) · [`00bd1e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1e00.md#insn-00bd1e70)

~~~diff
- 00bd1e5c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bd1e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd1e5c bytes a90600f9
- 00bd1e64 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd1e64 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd1e64 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd1e64 bytes 080c01f8
- 00bd1e70 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd1e70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bd1e70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1e70 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32534a64e514681e321462693f737a9d"></a>

### [`00bd1ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md) → [`00c4e8e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e8e8.md) FUN_00c4e8e8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 83.72% / 新版 83.72%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1ea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1ea4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1ea8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1ea4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1ea8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd1eac",
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
      "00c4e8ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4e8f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4e8f4",
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

- 旧版 [`00bd1ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1ea4) · [`00bd1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1ea8) · [`00bd1eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ea0.md#insn-00bd1eac)

~~~diff
- 00bd1ea4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd1ea4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd1ea4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd1ea4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd1ea4 bytes fd7bbda9
- 00bd1ea8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd1ea8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd1ea8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd1ea8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1ea8 bytes f65701a9
- 00bd1eac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd1eac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd1eac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd1eac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd1eac bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f2a9a2911751d7080fcc4fa066bf9ba"></a>

### [`00bd1f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md) → [`00c4e994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4e994.md) FUN_00c4e994

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 79.07% / 新版 79.07%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1fac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1fb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd1fbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd1fb4",
      "DATA",
      [
        "storage",
        "00c19e98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4e9fc",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd1fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1fac) · [`00bd1fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1fb4) · [`00bd1fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1f4c.md#insn-00bd1fbc)

~~~diff
- 00bd1fac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00bd1fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd1fac bytes c90600f9
- 00bd1fb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd1fb4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd1fb4 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd1fb4 bytes 080c01f8
- 00bd1fbc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00bd1fbc ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bd1fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd1fbc bytes 0a200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1cf581b8a41d908511fdd5695efcc03"></a>

### [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) → [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) FUN_00c4ea40

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 6件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) [`00bc2f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc2/00bc2f0c.md) [`00bd39c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md) [`00bd3a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 6件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) [`00c3f954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3f/00c3f954.md) [`00c50408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md) [`00c504a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.71% / 新版 81.71%

CFGの説明率　旧版 50.00% / 新版 55.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件, `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2098"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd20f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2114"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd202c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ea94"
      ]
    ],
    [
      "unmatched:00bd209c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4eac4"
      ]
    ],
    [
      "unmatched:00bd20f4",
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
      "00c4ea74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ea94"
      ]
    ],
    [
      "00c4eae4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4eac4"
      ]
    ],
    [
      "00c4eb3c",
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

- 旧版 [`00bd202c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd202c) · [`00bd2098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd2098) · [`00bd209c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md#insn-00bd209c)

~~~diff
- 00bd202c ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00bd202c bytes 00010054
- 00bd2098 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bd2098 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd2098 bytes 090000f9
- 00bd209c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd209c ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bd209c bytes 01ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3a338651510850259517832aa696ba3"></a>

### [`00bd2404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md) → [`00c4ee4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md) FUN_00c4ee4c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd246c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c4eeb4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c4eeb4",
      "incomplete_value": true,
      "site": "00c4eef0",
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
                "register:40a8:8"
              ],
              [
                "live",
                "register:4040:8"
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
      "unmatched:00bd246c",
      "DATA",
      [
        "storage",
        "00c1a138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4eeb4",
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md#insn-00bd246c) · [`00bd2438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2404.md#insn-00bd2438)
- 新版 [`00c4eeb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md#insn-00c4eeb4) · [`00c4ee80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ee4c.md#insn-00c4ee80)

~~~diff
- 00bd246c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd246c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd246c ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd246c bytes 080c01f8
+ 00c4eeb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c4eeb4 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
+ 00c4eeb4 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
+ 00c4eeb4 bytes 080c01f8
- 00bd2438 ["INT_ADD", "register:40f0:8", ["const:bd2438:8", "const:4:8"]]
- 00bd2438 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c4ee80 ["INT_ADD", "register:40f0:8", ["const:c4ee80:8", "const:4:8"]]
+ 00c4ee80 ["CALL", null, ["callee:00c59c20:8"]]
- 00bd2438 bytes 662b0094
+ 00c4ee80 bytes 682b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5ff756059e61ee05a73de5c1266c711"></a>

### [`00bd24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md) → [`00c4eef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4eef8.md) FUN_00c4eef8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 70.21% / 新版 70.21%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2548"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd24dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ef48"
      ]
    ],
    [
      "unmatched:00bd2524",
      "DATA",
      [
        "storage",
        "00c1a1a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c4ef24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ef48"
      ]
    ],
    [
      "00c4ef6c",
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd24dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd24dc) · [`00bd2524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd2524) · [`00bd2538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd24b0.md#insn-00bd2538)

~~~diff
- 00bd24dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd24dc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd24dc ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00bd24dc bytes 28010054
- 00bd2524 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bd2524 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd2524 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd2524 bytes 0a0c01f8
- 00bd2538 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00bd2538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd2538 bytes 080800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6901a8eac81a2377f765fe794e121734"></a>

### [`00bd256c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md) → [`00c4efb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4efb4.md) FUN_00c4efb4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

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
      "site": "00bd25c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd25d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd25e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd25d0",
      "DATA",
      [
        "storage",
        "00c19e98",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bd25f0",
      "DATA",
      [
        "storage",
        "00297854",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c4f018",
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ],
    [
      "00c4f038",
      "DATA",
      [
        "storage",
        "002a748f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd25c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25c8) · [`00bd25d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25d0) · [`00bd25e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd256c.md#insn-00bd25e0)

~~~diff
- 00bd25c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8:8"]]
- 00bd25c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd25c8 bytes a90600f9
- 00bd25d0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd25d0 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:10:8"]]
- 00bd25d0 ["STORE", null, ["const:1b1:8", "register:4000:8", "tmp:0:8"]]
- 00bd25d0 bytes 080c01f8
- 00bd25e0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd25e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "const:8:8"]]
- 00bd25e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd25e0 bytes 09200039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02890e8be9f9d4a4442790d4170495b"></a>

### [`00bd261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md) → [`00c4f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f064.md) FUN_00c4f064

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 25.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2620"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2624"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2620",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd2624",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd2628",
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
      "00c4f068",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4f06c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4f070",
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

- 旧版 [`00bd2620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd2620) · [`00bd2624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd2624) · [`00bd2628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd261c.md#insn-00bd2628)

~~~diff
- 00bd2620 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd2620 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd2620 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd2620 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd2620 bytes fd7bbda9
- 00bd2624 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd2624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bd2624 bytes f50b00f9
- 00bd2628 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd2628 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd2628 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd2628 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd2628 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb4498d67bfafe2605f4d43611a50a5"></a>

### [`00bd26cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md) → [`00c4f114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f114.md) FUN_00c4f114

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 66.03% / 新版 66.03%

CFGの説明率　旧版 12.50% / 新版 17.65%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 10件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd270c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2758"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2710",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4f160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd2928"
      ]
    ],
    [
      "unmatched:00bd275c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f1d0"
      ]
    ]
  ],
  "added": [
    [
      "00c4f158",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4f160",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f370"
      ]
    ],
    [
      "00c4f1a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f1d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd270c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd270c) · [`00bd2750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd2750) · [`00bd2758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd26cc.md#insn-00bd2758)

~~~diff
- 00bd270c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd270c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd270c bytes 610a00f9
- 00bd2750 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:20:8"]]
- 00bd2750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4060:4"]]
- 00bd2750 bytes 6c2200b9
- 00bd2758 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bd2758 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd2758 bytes 680600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00198aebf8268e571a70771047e88f88"></a>

### [`00bd2944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md) → [`00c4f38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f38c.md) FUN_00c4f38c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.41% / 新版 63.41%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2948"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd294c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2948",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd294c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd296c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f3e4"
      ]
    ]
  ],
  "added": [
    [
      "00c4f390",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4f394",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c4f3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f3e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd2948) · [`00bd294c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd294c) · [`00bd296c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2944.md#insn-00bd296c)

~~~diff
- 00bd2948 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd2948 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd2948 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd2948 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd2948 bytes fd7bbea9
- 00bd294c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd294c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd294c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd294c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd294c bytes f44f01a9
- 00bd296c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd296c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd296c ["CBRANCH", null, ["local:b11:8", "tmp:1:1"]]
- 00bd296c bytes 89010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b185f232faad2ae0cb92b40cd8643aa"></a>

### [`00bd2b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md) → [`00c4f578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f578.md) FUN_00c4f578

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bc82d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc8/00bc82d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c44d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c44/00c44d1c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.29% / 新版 77.29%

CFGの説明率　旧版 62.50% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd2b80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd2b64",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f5d8"
      ]
    ],
    [
      "unmatched:00bd2b7c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd2b84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f8ec"
      ]
    ]
  ],
  "added": [
    [
      "00c4f5ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f5d8"
      ]
    ],
    [
      "00c4f5c4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4f5cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4f8ec"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd2b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2b60) · [`00bd2b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2b64) · [`00bd2b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2b30.md#insn-00bd2b74)

~~~diff
- 00bd2b60 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:20:8"]]
- 00bd2b60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 00bd2b60 bytes 2b2000b9
- 00bd2b64 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd2b64 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd2b64 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bd2b64 bytes 69010054
- 00bd2b74 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd2b74 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd2b74 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd2b74 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd2b74 bytes 2181889a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bcdf055f5f72e7c77298582f3b4b216"></a>

### [`00bd2ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md) → [`00c4f914`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md) FUN_00c4f914

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 86.36% / 新版 90.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd2ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2ef8) · [`00bd2f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2f08) · [`00bd2f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd2/00bd2ecc.md#insn-00bd2f1c)
- 新版 [`00c4f940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f940) · [`00c4f950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f950) · [`00c4f964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4f914.md#insn-00c4f964)

~~~diff
- 00bd2ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2ef8 ["INT_ADD", "register:40f0:8", ["const:bd2ef8:8", "const:4:8"]]
- 00bd2ef8 ["CALLIND", null, ["register:0:8"]]
+ 00c4f940 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f940 ["INT_ADD", "register:40f0:8", ["const:c4f940:8", "const:4:8"]]
+ 00c4f940 ["CALLIND", null, ["register:0:8"]]
- 00bd2ef8 bytes 00013fd6
+ 00c4f940 bytes 00013fd6
- 00bd2f08 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
+ 00c4f950 ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00bd2f08 bytes c0000054
+ 00c4f950 bytes c0000054
- 00bd2f1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd2f1c ["INT_ADD", "register:40f0:8", ["const:bd2f1c:8", "const:4:8"]]
- 00bd2f1c ["CALLIND", null, ["register:0:8"]]
+ 00c4f964 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c4f964 ["INT_ADD", "register:40f0:8", ["const:c4f964:8", "const:4:8"]]
+ 00c4f964 ["CALLIND", null, ["register:0:8"]]
- 00bd2f1c bytes 00013fd6
+ 00c4f964 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72828a6cd492fa2dc141d47b41ddb696"></a>

### [`00bd3244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md) → [`00c4fc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fc8c.md) FUN_00c4fc8c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.21% / 新版 70.21%

CFGの説明率　旧版 35.71% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd32d0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd32fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3304"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c4fd30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd3310"
      ]
    ],
    [
      "unmatched:00bd3300",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd3308",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4fdfc"
      ]
    ]
  ],
  "added": [
    [
      "00c4fd30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4fd58"
      ]
    ],
    [
      "00c4fd48",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c4fd50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4fdfc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd32d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd32d0) · [`00bd32f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd32f8) · [`00bd32fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3244.md#insn-00bd32fc)

~~~diff
- 00bd32d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bd32d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bd32d0 bytes 690600f9
- 00bd32f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd32f8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd32f8 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd32f8 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd32f8 bytes 2181889a
- 00bd32fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd32fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd32fc bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae23c4ab8b44c1b4cd3554dc19ef77a2"></a>

### [`00bd33d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md) → [`00c4fe20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4fe20.md) FUN_00c4fe20

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 7.14% / 新版 9.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd33dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd33dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd33e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd33dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd33e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd33e4",
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
      "00c4fe24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c4fe28",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c4fe2c",
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

- 旧版 [`00bd33dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd33dc) · [`00bd33e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd33e0) · [`00bd33e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd33d8.md#insn-00bd33e4)

~~~diff
- 00bd33dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd33dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd33dc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd33dc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd33dc bytes fd7bbda9
- 00bd33e0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd33e0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd33e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd33e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd33e0 bytes f65701a9
- 00bd33e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd33e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd33e4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd33e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd33e4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7794c93730fb054dc7834239300fac5a"></a>

### [`00bd354c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md) → [`00c4ff94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4f/00c4ff94.md) FUN_00c4ff94

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 18.18% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd35d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c5001c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3574"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ffec"
      ]
    ],
    [
      "unmatched:00bd35dc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c4ffbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c4ffec"
      ]
    ],
    [
      "00c50024",
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

- 旧版 [`00bd3574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd3574) · [`00bd35d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd35d4) · [`00bd35dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd354c.md#insn-00bd35dc)

~~~diff
- 00bd3574 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd3574 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd3574 ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
- 00bd3574 bytes 89010054
- 00bd35d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bd35d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd35d4 bytes 680600f9
- 00bd35dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd35dc ["INT_ADD", "register:40f0:8", ["const:bd35dc:8", "const:4:8"]]
- 00bd35dc ["CALLIND", null, ["register:0:8"]]
- 00bd35dc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93ecb26c881caa5df97a9f5e4c3db06c"></a>

### [`00bd3914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md) → [`00c5035c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md) FUN_00c5035c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd393c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd393c) · [`00bd3944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd3944) · [`00bd395c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3914.md#insn-00bd395c)
- 新版 [`00c50384`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c50384) · [`00c5038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c5038c) · [`00c503a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c5035c.md#insn-00c503a4)

~~~diff
- 00bd393c ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd393c ["INT_ADD", "register:40f0:8", ["const:bd393c:8", "const:4:8"]]
- 00bd393c ["CALLIND", null, ["register:0:8"]]
+ 00c50384 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c50384 ["INT_ADD", "register:40f0:8", ["const:c50384:8", "const:4:8"]]
+ 00c50384 ["CALLIND", null, ["register:0:8"]]
- 00bd393c bytes 00013fd6
+ 00c50384 bytes 00013fd6
- 00bd3944 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00bd3944 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00c5038c ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00c5038c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00bd3944 bytes f40200b4
+ 00c5038c bytes f40200b4
- 00bd395c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd395c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd395c ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00c503a4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c503a4 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c503a4 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bd395c bytes 49010054
+ 00c503a4 bytes 49010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024eb1aa25c120a59f5155576d7bc763"></a>

### [`00bd39c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md) → [`00c50408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50408.md) FUN_00c50408

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 50.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd39c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd39c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd39c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd39c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd39c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd39cc",
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
      "00c5040c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c50410",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c50414",
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

- 旧版 [`00bd39c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd39c4) · [`00bd39c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd39c8) · [`00bd39cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd39c0.md#insn-00bd39cc)

~~~diff
- 00bd39c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd39c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd39c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd39c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd39c4 bytes fd7bbda9
- 00bd39c8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd39c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bd39c8 bytes f50b00f9
- 00bd39cc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd39cc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd39cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd39cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd39cc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055ea358e24cc3c1eea640f0d2c184a9"></a>

### [`00bd3a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md) → [`00c504a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md) FUN_00c504a8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd1ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd1/00bd1ff8.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c4ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c4e/00c4ea40.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

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
      "definition_site": "00c50510",
      "incomplete_value": false,
      "site": "00c50510",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3ac8",
      "incomplete_value": false,
      "site": "00bd3ac8",
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
            "const:f78:8"
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
      "00c50510",
      "DATA",
      [
        "storage",
        "00c19f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50510",
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3a98) · [`00bd3ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3ab8) · [`00bd3abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3a60.md#insn-00bd3abc)
- 新版 [`00c504e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c504e0) · [`00c50500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c50500) · [`00c50504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c504a8.md#insn-00c50504)

~~~diff
- 00bd3a98 ["INT_ADD", "register:40f0:8", ["const:bd3a98:8", "const:4:8"]]
- 00bd3a98 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c504e0 ["INT_ADD", "register:40f0:8", ["const:c504e0:8", "const:4:8"]]
+ 00c504e0 ["CALL", null, ["callee:00c59c20:8"]]
- 00bd3a98 bytes ce250094
+ 00c504e0 bytes d0250094
- 00bd3ab8 ["COPY", "register:4040:8", ["const:c19000:8"]]
+ 00c50500 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00bd3ab8 bytes 280200d0
+ 00c50500 bytes 480200b0
- 00bd3abc ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00bd3abc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3abc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd3abc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50504 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00c50504 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50504 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50504 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd3abc bytes 08e13d91
+ 00c50504 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a413cd94688cff7e02744712fdad7b6e"></a>

### [`00bd3b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md) → [`00c50550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md) FUN_00c50550

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 78.57% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `store_value` 2件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c505b4",
      "incomplete_value": true,
      "site": "00c505c0",
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
                "const:2bf000:8"
              ],
              [
                "leaf",
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd3b6c",
      "incomplete_value": true,
      "site": "00bd3b78",
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
                "const:2ae000:8"
              ],
              [
                "leaf",
                "const:644:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c505c4",
      "incomplete_value": true,
      "site": "00c505c4",
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
      "definition_site": "00bd3b7c",
      "incomplete_value": true,
      "site": "00bd3b7c",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3b30",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c505a8"
      ]
    ],
    [
      "00c505b4",
      "READ",
      [
        "storage",
        "002ae644",
        null,
        "string"
      ]
    ],
    [
      "00c505b8",
      "READ",
      [
        "storage",
        "002ae649",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c50578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c505a8"
      ]
    ],
    [
      "00c505b4",
      "READ",
      [
        "storage",
        "002bfb28",
        null,
        "string"
      ]
    ],
    [
      "00c505b8",
      "READ",
      [
        "storage",
        "002bfb2d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md#insn-00bd3b30) · [`00bd3b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3b08.md#insn-00bd3b28)
- 新版 [`00c50578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50550.md#insn-00c50578)

~~~diff
- 00bd3b30 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd3b30 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd3b30 ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bd3b30 bytes 89010054
+ 00c50578 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c50578 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c50578 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c50578 bytes 89010054
- 00bd3b28 ["COPY", "tmp:0:8", ["const:d:8"]]
- 00bd3b28 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3b28 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bd3b28 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bd3b28 bytes 2b350091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1635293f57bba7a783c184a3f79052bf"></a>

### [`00bd3c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md) → [`00c50678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md) FUN_00c50678

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 95.29% / 新版 95.29%

CFGの説明率　旧版 23.81% / 新版 27.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3d64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c507ac"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3c94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3c94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c50704"
      ]
    ]
  ],
  "added": [
    [
      "00c506dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c50704"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd3c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md#insn-00bd3c94) · [`00bd3d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3c30.md#insn-00bd3d64)
- 新版 [`00c506dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50678.md#insn-00c506dc)

~~~diff
- 00bd3c94 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd3c94 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd3c94 ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
- 00bd3c94 bytes 49010054
- 00bd3d64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8:8"]]
- 00bd3d64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd3d64 bytes 680600f9
+ 00c506dc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c506dc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c506dc ["CBRANCH", null, ["local:b5:8", "tmp:1:1"]]
+ 00c506dc bytes 49010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ef727ed8bcbe71676375176f1482223"></a>

### [`00bd3d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md) → [`00c507d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c507d4.md) FUN_00c507d4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 65.85% / 新版 65.85%

CFGの説明率　旧版 42.86% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3d90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3d94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3d90",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3d94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3d98",
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
      "00c507d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c507dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c507e0",
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

- 旧版 [`00bd3d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3d90) · [`00bd3d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3d94) · [`00bd3d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3d8c.md#insn-00bd3d98)

~~~diff
- 00bd3d90 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd3d90 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd3d90 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd3d90 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd3d90 bytes fd7bbda9
- 00bd3d94 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00bd3d94 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00bd3d94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd3d94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3d94 bytes f65701a9
- 00bd3d98 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd3d98 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd3d98 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd3d98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3d98 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cffe460fcd16cf19b00b9cdfd4665e0"></a>

### [`00bd3e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md) → [`00c508a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c508a4.md) FUN_00c508a4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 64.76% / 新版 64.76%

CFGの説明率　旧版 18.75% / 新版 24.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_condition` 2件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3e60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd3e64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd3e60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3e64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd3e68",
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
      "00c508a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c508ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c508b0",
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

- 旧版 [`00bd3e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3e60) · [`00bd3e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3e64) · [`00bd3e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd3/00bd3e5c.md#insn-00bd3e68)

~~~diff
- 00bd3e60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd3e60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd3e60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00bd3e60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd3e60 bytes fd7bbda9
- 00bd3e64 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd3e64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00bd3e64 bytes f50b00f9
- 00bd3e68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd3e68 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd3e68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd3e68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd3e68 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04916d253dc754d1f640fdc1cc49bda5"></a>

### [`00bd4008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md) → [`00c50a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md) FUN_00c50a50

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbde5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbd/00bbde5c.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c3a8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3a/00c3a8a4.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c50abc",
      "incomplete_value": false,
      "site": "00c50abc",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd4074",
      "incomplete_value": false,
      "site": "00bd4074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c1a000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00c50abc",
      "DATA",
      [
        "storage",
        "00c1a058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00c50abc",
      "DATA",
      [
        "storage",
        "00c99a00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd4040) · [`00bd4068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd4068) · [`00bd406c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4008.md#insn-00bd406c)
- 新版 [`00c50a88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50a88) · [`00c50ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50ab0) · [`00c50ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50a50.md#insn-00c50ab4)

~~~diff
- 00bd4040 ["INT_ADD", "register:40f0:8", ["const:bd4040:8", "const:4:8"]]
- 00bd4040 ["CALL", null, ["callee:00c59c20:8"]]
+ 00c50a88 ["INT_ADD", "register:40f0:8", ["const:c50a88:8", "const:4:8"]]
+ 00c50a88 ["CALL", null, ["callee:00c59c20:8"]]
- 00bd4040 bytes 64240094
+ 00c50a88 bytes 66240094
- 00bd4068 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00c50ab0 ["COPY", "register:4040:8", ["const:c99000:8"]]
- 00bd4068 bytes 280200d0
+ 00c50ab0 bytes 480200b0
- 00bd406c ["COPY", "tmp:0:8", ["const:58:8"]]
- 00bd406c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bd406c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bd406c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00c50ab4 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00c50ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00c50ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bd406c bytes 08610191
+ 00c50ab4 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-579b80c57ee4fc568acbbc10140aa03a"></a>

### [`00bd4500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md) → [`00c50f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c50/00c50f48.md) FUN_00c50f48

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.02% / 新版 87.02%

CFGの説明率　旧版 45.21% / 新版 51.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd45e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4688"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd480c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd45e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "unmatched:00bd464c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c510f8"
      ]
    ],
    [
      "unmatched:00bd4660",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c510f8"
      ]
    ]
  ],
  "added": [
    [
      "00c5102c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c51094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c510f8"
      ]
    ],
    [
      "00c510a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c510f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd45dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd45dc) · [`00bd45e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd45e0) · [`00bd45e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4500.md#insn-00bd45e4)

~~~diff
- 00bd45dc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd45dc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd45dc ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd45dc ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd45dc bytes 2181889a
- 00bd45e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd45e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd45e0 bytes 610a00f9
- 00bd45e4 ["INT_ADD", "register:40f0:8", ["const:bd45e4:8", "const:4:8"]]
- 00bd45e4 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd45e4 bytes 1b230094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6cba494049539a7e54780e1e5e506e28"></a>

### [`00bd49cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md) → [`00c51414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md) FUN_00c51414

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.85% / 新版 73.85%

CFGの説明率　旧版 20.75% / 新版 26.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 4件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4a6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4a90"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4b14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4a58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c514c8"
      ]
    ],
    [
      "unmatched:00bd4a70",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c5151c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd4b3c"
      ]
    ]
  ],
  "added": [
    [
      "00c514a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c514c8"
      ]
    ],
    [
      "00c514b8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c59ca0"
      ]
    ],
    [
      "00c5151c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51584"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md#insn-00bd4a58) · [`00bd4a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md#insn-00bd4a68) · [`00bd4a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md#insn-00bd4a6c)

~~~diff
- 00bd4a58 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd4a58 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bd4a58 ["CBRANCH", null, ["local:b12:8", "tmp:1:1"]]
- 00bd4a58 bytes 49010054
- 00bd4a68 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd4a68 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd4a68 ["COPY", "tmp:2:8", ["register:4048:8"]]
- 00bd4a68 ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd4a68 bytes 2181889a
- 00bd4a6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00bd4a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00bd4a6c bytes 610a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7af9423babf68be3202f120887c2d9"></a>

### [`00bd4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md) → [`00c51624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md) FUN_00c51624

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 84.62% / 新版 88.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4bf4) · [`00bd4c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4c08) · [`00bd4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md#insn-00bd4c10)
- 新版 [`00c5163c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c5163c) · [`00c51650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c51650) · [`00c51658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md#insn-00c51658)

~~~diff
- 00bd4bf4 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bd4bf4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bd4bf4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bd4bf4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c5163c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00c5163c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c5163c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c5163c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00bd4bf4 bytes 08070037
+ 00c5163c bytes 08070037
- 00bd4c08 ["INT_ADD", "register:40f0:8", ["const:bd4c08:8", "const:4:8"]]
- 00bd4c08 ["CALL", null, ["callee:00c5174c:8"]]
+ 00c51650 ["INT_ADD", "register:40f0:8", ["const:c51650:8", "const:4:8"]]
+ 00c51650 ["CALL", null, ["callee:00c5174c:8"]]
- 00bd4c08 bytes 3f000094
+ 00c51650 bytes 3f000094
- 00bd4c10 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00bd4c10 ["CBRANCH", null, ["local:b15:8", "tmp:0:1"]]
+ 00c51658 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00c51658 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00bd4c10 bytes 010600b4
+ 00c51658 bytes 010600b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e7f49b36a469aaf8c10cacc6eb36464"></a>

### [`00bd4cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4cfc.md) → [`00c51744`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51744.md) _ZdlPv

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4d00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ],
  "added": [
    [
      "00c51748",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57ab0"
      ]
    ]
  ]
}
~~~


<a id="compare-2300fb1ce80dd07cd9d5f76d2d1a6b56"></a>

### [`00bd4d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md) → [`00c5174c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md) FUN_00c5174c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd49cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd49cc.md) [`00bd4bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4bdc.md) · 呼出先 6件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 2件 [`00c51414`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51414.md) [`00c51624`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md) · 呼出先 6件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 52.94% / 新版 62.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4dbc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd4e04"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c51804"
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
      "unmatched:00bd4dbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c5181c"
      ]
    ],
    [
      "unmatched:00bd4e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51794"
      ]
    ],
    [
      "00c518b4",
      "PARAM",
      [
        "storage",
        "002917fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c51804",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c5181c"
      ]
    ],
    [
      "00c5184c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51794"
      ]
    ],
    [
      "00c518b4",
      "PARAM",
      [
        "storage",
        "002a0e15",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd4dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4dbc) · [`00bd4e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4e04) · [`00bd4e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4d04.md#insn-00bd4e84)
- 新版 [`00c518cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c5174c.md#insn-00c518cc)

~~~diff
- 00bd4dbc ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bd4dbc bytes c0000054
- 00bd4e04 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd4e04 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd4e04 bytes 43faff54
- 00bd4e84 ["INT_ADD", "register:40f0:8", ["const:bd4e84:8", "const:4:8"]]
- 00bd4e84 ["CALL", null, ["callee:00c37be4:8"]]
+ 00c518cc ["INT_ADD", "register:40f0:8", ["const:c518cc:8", "const:4:8"]]
+ 00c518cc ["CALL", null, ["callee:00c37be4:8"]]
- 00bd4e84 bytes c698ff97
+ 00c518cc bytes c698ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ab7a545ba2832830b3a4394d86129b6"></a>

### [`00bd4ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4ee0.md) → [`00c51928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51928.md) _ZnamRKSt9nothrow_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5ba50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba50.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd4eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4ee0.md#insn-00bd4eec)
- 新版 [`00c51934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51928.md#insn-00c51934)

~~~diff
- 00bd4eec ["INT_ADD", "register:40f0:8", ["const:bd4eec:8", "const:4:8"]]
- 00bd4eec ["CALL", null, ["callee:00c5ba50:8"]]
+ 00c51934 ["INT_ADD", "register:40f0:8", ["const:c51934:8", "const:4:8"]]
+ 00c51934 ["CALL", null, ["callee:00c5ba50:8"]]
- 00bd4eec bytes 2d280094
+ 00c51934 bytes 47280094
~~~


<a id="compare-01952fe3e59b3920ca907086524dec37"></a>

### [`00bd4fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fb0.md) → [`00c519f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c519f8.md) _ZdlPvmSt11align_val_t

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5eaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eaf0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd4fb8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5eaf0"
      ]
    ]
  ],
  "added": [
    [
      "00c51a00",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c5eaf0"
      ]
    ]
  ]
}
~~~


<a id="compare-cd9669c6a330784d84d5ca671995f214"></a>

### [`00bd5008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md) → [`00c51a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md) __cxa_allocate_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) · 呼出先 3件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) · 呼出先 3件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51a78",
      "incomplete_value": true,
      "site": "00c51a80",
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
      "definition_site": "00c51a7c",
      "incomplete_value": false,
      "site": "00c51a80",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51a74",
      "incomplete_value": true,
      "site": "00c51a80",
      "value": [
        "INT_AND",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:fffffffffffffff0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 1,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5038) · [`00bd5020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5020) · [`00bd5028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5008.md#insn-00bd5028)
- 新版 [`00c51a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a80) · [`00c51a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a68) · [`00c51a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a50.md#insn-00c51a70)

~~~diff
- 00bd5038 ["INT_ADD", "register:40f0:8", ["const:bd5038:8", "const:4:8"]]
- 00bd5038 ["CALL", null, ["callee:00c57c90:8"]]
+ 00c51a80 ["INT_ADD", "register:40f0:8", ["const:c51a80:8", "const:4:8"]]
+ 00c51a80 ["CALL", null, ["callee:00c57c90:8"]]
- 00bd5038 bytes 82180094
+ 00c51a80 bytes 84180094
- 00bd5020 ["INT_ADD", "register:40f0:8", ["const:bd5020:8", "const:4:8"]]
- 00bd5020 ["CALL", null, ["callee:00c5221c:8"]]
+ 00c51a68 ["INT_ADD", "register:40f0:8", ["const:c51a68:8", "const:4:8"]]
+ 00c51a68 ["CALL", null, ["callee:00c5221c:8"]]
- 00bd5020 bytes ed010094
+ 00c51a68 bytes ed010094
- 00bd5028 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bd5028 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c51a70 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c51a70 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5028 bytes 400100b4
+ 00c51a70 bytes 400100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66d0bb58cc14f33a6ddf583963ff2903"></a>

### [`00bd5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md) → [`00c51aa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md) __cxa_begin_catch

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md) · 呼出先 2件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)
- 新版 呼出元 1件 [`00c57c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c10.md) · 呼出先 2件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 41.67% / 新版 55.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5088"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c51ad0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00bd5088"
      ],
      [
        "FALL_THROUGH",
        "00c51ad0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00c51ad0",
      "incomplete_value": true,
      "site": "00c51aec",
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
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd5088",
      "incomplete_value": true,
      "site": "00bd50a4",
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
      "unmatched:00bd5088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51b10"
      ]
    ]
  ],
  "added": [
    [
      "00c51ad0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51b10"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md#insn-00bd5088) · [`00bd506c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5058.md#insn-00bd506c)
- 新版 [`00c51ad0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md#insn-00c51ad0) · [`00c51ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51aa0.md#insn-00c51ab4)

~~~diff
- 00bd5088 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd5088 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bd5088 bytes 01020054
+ 00c51ad0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c51ad0 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00c51ad0 bytes 01020054
- 00bd506c ["INT_ADD", "register:40f0:8", ["const:bd506c:8", "const:4:8"]]
- 00bd506c ["CALL", null, ["callee:00c5e990:8"]]
+ 00c51ab4 ["INT_ADD", "register:40f0:8", ["const:c51ab4:8", "const:4:8"]]
+ 00c51ab4 ["CALL", null, ["callee:00c5e990:8"]]
- 00bd506c bytes 59330094
+ 00c51ab4 bytes b7330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-286f59b468e297fd8eca3726d861efeb"></a>

### [`00bd5118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5118.md) → [`00c51b60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b60.md) __cxa_init_primary_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4e0.md) · 呼出先 3件 [`00bd5188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5188.md) [`00be1e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e00.md) [`00be1e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e10.md)
- 新版 呼出元 1件 [`00c57f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f30.md) · 呼出先 3件 [`00c51bd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51bd0.md) [`00c5e9c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9c0.md) [`00c5e9d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9d0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd516c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd516c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c51bb4"
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
      "unmatched:00bd516c",
      "DATA",
      [
        "storage",
        "00bd5188",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c51bb4",
      "DATA",
      [
        "storage",
        "00c51bd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd516c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5118.md#insn-00bd516c) · [`00bd5140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5118.md#insn-00bd5140)
- 新版 [`00c51bb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b60.md#insn-00c51bb4) · [`00c51b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51b60.md#insn-00c51b88)

~~~diff
- 00bd516c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd516c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bd516c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ffffffffffffffe0:8"]]
- 00bd516c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd516c bytes a8263ea9
+ 00c51bb4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c51bb4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00c51bb4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ffffffffffffffe0:8"]]
+ 00c51bb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c51bb4 bytes a8263ea9
- 00bd5140 ["INT_ADD", "register:40f0:8", ["const:bd5140:8", "const:4:8"]]
- 00bd5140 ["CALL", null, ["callee:00c5e9c0:8"]]
+ 00c51b88 ["INT_ADD", "register:40f0:8", ["const:c51b88:8", "const:4:8"]]
+ 00c51b88 ["CALL", null, ["callee:00c5e9c0:8"]]
- 00bd5140 bytes 30330094
+ 00c51b88 bytes 8e330094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99b72d93948d982b69077aa38d81ebb3"></a>

### [`00bd51f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md) → [`00c51c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md) __cxa_allocate_dependent_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd5200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md#insn-00bd5200) · [`00bd5204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md#insn-00bd5204) · [`00bd5228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd51f0.md#insn-00bd5228)
- 新版 [`00c51c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md#insn-00c51c48) · [`00c51c4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md#insn-00c51c4c) · [`00c51c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c38.md#insn-00c51c70)

~~~diff
- 00bd5200 ["INT_ADD", "register:40f0:8", ["const:bd5200:8", "const:4:8"]]
- 00bd5200 ["CALL", null, ["callee:00c5221c:8"]]
+ 00c51c48 ["INT_ADD", "register:40f0:8", ["const:c51c48:8", "const:4:8"]]
+ 00c51c48 ["CALL", null, ["callee:00c5221c:8"]]
- 00bd5200 bytes 75010094
+ 00c51c48 bytes 75010094
- 00bd5204 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bd5204 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
+ 00c51c4c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c51c4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd5204 bytes 200100b4
+ 00c51c4c bytes 200100b4
- 00bd5228 ["INT_ADD", "register:40f0:8", ["const:bd5228:8", "const:4:8"]]
- 00bd5228 ["CALL", null, ["callee:00c57c20:8"]]
+ 00c51c70 ["INT_ADD", "register:40f0:8", ["const:c51c70:8", "const:4:8"]]
+ 00c51c70 ["CALL", null, ["callee:00c57c20:8"]]
- 00bd5228 bytes ea170094
+ 00c51c70 bytes ec170094
~~~


<a id="compare-480dbf5d3e0f9d0816b4d580c9d94fbf"></a>

### [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) → [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) __cxa_throw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) · 呼出先 4件 [`00bd5290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5290.md) [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bdb4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4e0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)
- 新版 呼出元 1件 [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) · 呼出先 4件 [`00c51cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51cd8.md) [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c57f30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f30.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd527c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c51cc4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c51cc8",
      "incomplete_value": true,
      "site": "00c51ccc",
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
            "const:60:8"
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


#### 変更候補の命令位置

- 旧版 [`00bd527c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md#insn-00bd527c) · [`00bd5284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md#insn-00bd5284)
- 新版 [`00c51ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md#insn-00c51ccc) · [`00c51cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md#insn-00c51cc4)

~~~diff
- 00bd527c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00bd527c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd527c bytes 080400f9
- 00bd5284 ["INT_ADD", "register:40f0:8", ["const:bd5284:8", "const:4:8"]]
- 00bd5284 ["CALL", null, ["callee:00c53910:8"]]
+ 00c51ccc ["INT_ADD", "register:40f0:8", ["const:c51ccc:8", "const:4:8"]]
+ 00c51ccc ["CALL", null, ["callee:00c53910:8"]]
- 00bd5284 bytes 0f070094
+ 00c51ccc bytes 11070094
+ 00c51cc4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
+ 00c51cc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c51cc4 bytes 080400f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9cb947b91a005a64b82b9cb235ed313"></a>

### [`00bd52c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md) → [`00c51d08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51d08.md) __cxa_end_catch

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb480.md) · 呼出先 4件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bd72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd72cc.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 1件 [`00c57ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ed0.md) · 呼出先 4件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c53d1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d1c.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 52.00% / 新版 59.09%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd52c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd52c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd52c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd52c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd52c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd52f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51db0"
      ]
    ]
  ],
  "added": [
    [
      "00c51d0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c51d10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c51d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51db0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd52c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd52c4) · [`00bd52c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd52c8) · [`00bd52f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd52c0.md#insn-00bd52f8)

~~~diff
- 00bd52c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd52c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd52c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bd52c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd52c4 bytes fd7bbea9
- 00bd52c8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd52c8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd52c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bd52c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd52c8 bytes f44f01a9
- 00bd52f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd52f8 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 00bd52f8 bytes 81030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc19899015022b0662c37bcbc26f8987"></a>

### [`00bd53ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md) → [`00c51df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md) __cxa_decrement_exception_refcount

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f10.md) · 呼出先 2件 [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c5db10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db10.md) · 呼出先 2件 [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 55.56% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c51e34",
      "value": [
        "leaf",
        "ram:c523f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bd53ec",
      "value": [
        "leaf",
        "ram:bd59a8:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd53fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c51e44"
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
      "00c51e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd53f0"
      ]
    ],
    [
      "00c51e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd53f0"
      ]
    ],
    [
      "00c51e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bd59a8"
      ]
    ]
  ],
  "added": [
    [
      "00c51e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51e38"
      ]
    ],
    [
      "00c51e1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51e38"
      ]
    ],
    [
      "00c51e34",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd53ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md#insn-00bd53ec) · [`00bd53fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd53ac.md#insn-00bd53fc)
- 新版 [`00c51e34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md#insn-00c51e34) · [`00c51e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51df4.md#insn-00c51e44)

~~~diff
- 00bd53ec ["INT_ADD", "register:40f0:8", ["const:bd53ec:8", "const:4:8"]]
- 00bd53ec ["CALL", null, ["ram:bd59a8:8"]]
+ 00c51e34 ["INT_ADD", "register:40f0:8", ["const:c51e34:8", "const:4:8"]]
+ 00c51e34 ["CALL", null, ["ram:c523f0:8"]]
- 00bd53ec bytes 6f010094
+ 00c51e34 bytes 6f010094
- 00bd53fc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd53fc ["RETURN", null, ["register:0:8"]]
- 00bd53fc bytes c0035fd6
+ 00c51e44 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c51e44 ["RETURN", null, ["register:0:8"]]
+ 00c51e44 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1db968d8fe52de720db8e33d5666e7df"></a>

### [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) → [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) __cxa_rethrow

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6b0.md) · 呼出先 5件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md) [`00be1dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dd0.md)
- 新版 呼出元 1件 [`00c58100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58100.md) · 呼出先 5件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md) [`00c5e990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e990.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.23% / 新版 91.23%

CFGの説明率　旧版 27.59% / 新版 44.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd54f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c51f3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd54f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd54f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51f4c"
      ]
    ],
    [
      "unmatched:00bd5514",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51ec0"
      ]
    ]
  ],
  "added": [
    [
      "00c51f40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51f4c"
      ]
    ],
    [
      "00c51f5c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c51ec0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd54f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd54f4) · [`00bd54f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd54f8) · [`00bd5514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md#insn-00bd5514)

~~~diff
- 00bd54f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00bd54f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00bd54f4 bytes 893a00b9
- 00bd54f8 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 00bd54f8 bytes 60000054
- 00bd5514 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd5514 ["CBRANCH", null, ["local:b1:8", "tmp:0:1"]]
- 00bd5514 bytes 21fbff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07e52736eb2d0cf16772263bc95ee753"></a>

### [`00bd5568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md) → [`00c51fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md) __cxa_current_primary_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f40.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be1de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1de0.md)
- 新版 呼出元 1件 [`00c5db40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db40.md) · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c5e9a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9a0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52000",
      "incomplete_value": true,
      "site": "00c5200c",
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
            "const:8:8"
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

- 旧版 [`00bd55c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md#insn-00bd55c4) · [`00bd5578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md#insn-00bd5578) · [`00bd557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5568.md#insn-00bd557c)
- 新版 [`00c5200c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md#insn-00c5200c) · [`00c51fc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md#insn-00c51fc0) · [`00c51fc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51fb0.md#insn-00c51fc4)

~~~diff
- 00bd55c4 ["INT_ADD", "register:40f0:8", ["const:bd55c4:8", "const:4:8"]]
- 00bd55c4 ["CALL", null, ["callee:00c538e0:8"]]
+ 00c5200c ["INT_ADD", "register:40f0:8", ["const:c5200c:8", "const:4:8"]]
+ 00c5200c ["CALL", null, ["callee:00c538e0:8"]]
- 00bd55c4 bytes 33060094
+ 00c5200c bytes 35060094
- 00bd5578 ["INT_ADD", "register:40f0:8", ["const:bd5578:8", "const:4:8"]]
- 00bd5578 ["CALL", null, ["callee:00c5e9a0:8"]]
+ 00c51fc0 ["INT_ADD", "register:40f0:8", ["const:c51fc0:8", "const:4:8"]]
+ 00c51fc0 ["CALL", null, ["callee:00c5e9a0:8"]]
- 00bd5578 bytes 1a320094
+ 00c51fc0 bytes 78320094
- 00bd557c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bd557c ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00c51fc4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c51fc4 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bd557c bytes c00200b4
+ 00c51fc4 bytes c00200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ab181f43e978385d3c02133f2323adf"></a>

### [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) → [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) __cxa_rethrow_primary_exception

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f60.md) · 呼出先 8件 [`00bd5708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md) [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 1件 [`00c5db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db60.md) · 呼出先 8件 [`00c52150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md) [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment

命令の説明率　旧版 91.55% / 新版 91.55%

CFGの説明率　旧版 29.41% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 2件, `unresolved_branch_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c520c4",
      "incomplete_value": false,
      "site": "00c520c8",
      "value": [
        "leaf",
        "const:c52150:8"
      ]
    },
    "old": {
      "definition_site": "00bd567c",
      "incomplete_value": false,
      "site": "00bd5680",
      "value": [
        "leaf",
        "const:bd5708:8"
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd56c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c5210c"
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
      "00c520c8",
      "DATA",
      [
        "storage",
        "00bd5708",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd56c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52118"
      ]
    ]
  ],
  "added": [
    [
      "00c520c8",
      "DATA",
      [
        "storage",
        "00c52150",
        null,
        null
      ]
    ],
    [
      "00c5210c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52118"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd56c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md#insn-00bd56c4) · [`00bd55fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md#insn-00bd55fc)
- 新版 [`00c5210c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md#insn-00c5210c) · [`00c52044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md#insn-00c52044)

~~~diff
- 00bd56c4 ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
- 00bd56c4 bytes 60000054
+ 00c5210c ["CBRANCH", null, ["local:b5:8", "register:101:1"]]
+ 00c5210c bytes 60000054
- 00bd55fc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bd55fc ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
+ 00c52044 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c52044 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00bd55fc bytes 800700b4
+ 00c52044 bytes 800700b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c6a6e38baa98e6ba35b2f206d9a89d"></a>

### [`00bd5708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md) → [`00c52150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md) FUN_00c52150

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 4件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd59a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd59a8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 4件 [`00440bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440bfc.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c523f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c523f0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 40.00% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c5219c",
      "value": [
        "leaf",
        "ram:c523f0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bd5754",
      "value": [
        "leaf",
        "ram:bd59a8:8"
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
      "site": "00bd5770"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5774"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c52168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd576c"
      ]
    ],
    [
      "00c5219c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bd59a8"
      ]
    ],
    [
      "unmatched:00bd5768",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bd59a8"
      ]
    ]
  ],
  "added": [
    [
      "00c52168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c521b4"
      ]
    ],
    [
      "00c5219c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ],
    [
      "00c521b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c523f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd5754) · [`00bd5770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd5770) · [`00bd5774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5708.md#insn-00bd5774)
- 新版 [`00c5219c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52150.md#insn-00c5219c)

~~~diff
- 00bd5754 ["INT_ADD", "register:40f0:8", ["const:bd5754:8", "const:4:8"]]
- 00bd5754 ["CALL", null, ["ram:bd59a8:8"]]
+ 00c5219c ["INT_ADD", "register:40f0:8", ["const:c5219c:8", "const:4:8"]]
+ 00c5219c ["CALL", null, ["ram:c523f0:8"]]
- 00bd5754 bytes 95000094
+ 00c5219c bytes 95000094
- 00bd5770 ["INT_ADD", "register:40f0:8", ["const:bd5770:8", "const:4:8"]]
- 00bd5770 ["CALL", null, ["callee:00c374b8:8"]]
- 00bd5770 bytes c094ff97
- 00bd5774 ["INT_ADD", "register:40f0:8", ["const:bd5774:8", "const:4:8"]]
- 00bd5774 ["CALL", null, ["callee:00440bfc:8"]]
- 00bd5774 bytes 6222e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea9eb3656e56413f223373d2b783df18"></a>

### [`00bd5820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md) → [`00c52268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md) FUN_00c52268

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd57d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd57d4.md) · 呼出先 3件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 1件 [`00c5221c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c5221c.md) · 呼出先 3件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 62.92% / 新版 62.92%

CFGの説明率　旧版 23.08% / 新版 27.27%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd58fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5838",
      "PARAM",
      [
        "storage",
        "010a3760",
        null,
        null
      ]
    ],
    [
      "00c5228c",
      "READ",
      [
        "storage",
        "010a3788",
        null,
        "undefined8"
      ]
    ],
    [
      "00c52290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd5860"
      ]
    ]
  ],
  "added": [
    [
      "00c52280",
      "PARAM",
      [
        "storage",
        "01128668",
        null,
        null
      ]
    ],
    [
      "00c5228c",
      "READ",
      [
        "storage",
        "01128690",
        null,
        "undefined8"
      ]
    ],
    [
      "00c52290",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c522a8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd583c) · [`00bd5858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd5858) · [`00bd5870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5820.md#insn-00bd5870)
- 新版 [`00c52284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52268.md#insn-00c52284)

~~~diff
- 00bd583c ["INT_ADD", "register:40f0:8", ["const:bd583c:8", "const:4:8"]]
- 00bd583c ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00c52284 ["INT_ADD", "register:40f0:8", ["const:c52284:8", "const:4:8"]]
+ 00c52284 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00bd583c bytes f9230094
+ 00c52284 bytes 07240094
- 00bd5858 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd5858 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00bd5858 bytes 01010054
- 00bd5870 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:788:8"]]
- 00bd5870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4070:8"]]
- 00bd5870 bytes 0ec503f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c6adfc8ab7c7b797aafe6bb15b3cca8"></a>

### [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) → [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) __gxx_personality_v0

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) [`00bd7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7264.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c52cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md) [`00c52e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52e80.md) [`00c53cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53cb4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.43% / 新版 94.43%

CFGの説明率　旧版 83.33% / 新版 87.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5af4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd5cc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd5af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5cc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd5d50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52718"
      ]
    ]
  ],
  "added": [
    [
      "00c5253c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c52710",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00c52798",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c52718"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd5af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5af4) · [`00bd5b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5b74) · [`00bd5cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md#insn-00bd5cc8)
- 新版 [`00c525bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md#insn-00c525bc)

~~~diff
- 00bd5af4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bd5af4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bd5af4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00bd5af4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd5af4 bytes f44f0ba9
- 00bd5b74 ["INT_ADD", "register:40f0:8", ["const:bd5b74:8", "const:4:8"]]
- 00bd5b74 ["CALL", null, ["callee:00c53d70:8"]]
+ 00c525bc ["INT_ADD", "register:40f0:8", ["const:c525bc:8", "const:4:8"]]
+ 00c525bc ["CALL", null, ["callee:00c53d70:8"]]
- 00bd5b74 bytes eb050094
+ 00c525bc bytes ed050094
- 00bd5cc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00bd5cc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd5cc8 bytes e81700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

