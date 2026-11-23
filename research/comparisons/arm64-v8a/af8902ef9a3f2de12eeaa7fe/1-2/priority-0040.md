# v15.7.4 → v16.0.0 · 最優先の変更候補 (40)

[一覧の目次](README.md)

<a id="compare-2108712e9f97751d2eba7ed589e597e0"></a>

### [`00843b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b9c.md) → [`00875e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875e88.md) FUN_00875e88

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 20.00% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843ba0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00843b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00843ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00843bb8",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875e88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00875e8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00875ea4",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b9c.md#insn-00843b9c) · [`00843ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b9c.md#insn-00843ba0) · [`00843bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843b9c.md#insn-00843bb8)

~~~diff
- 00843b9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00843b9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00843b9c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00843b9c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00843b9c bytes fd7bbea9
- 00843ba0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00843ba0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00843ba0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00843ba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00843ba0 bytes f44f01a9
- 00843bb8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00843bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00843bb8 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61738d4259efb92af28d0038ab6b7ffd"></a>

### [`00843bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843bf8.md) → [`00875ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md) FUN_00875ee4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00875f08",
      "incomplete_value": false,
      "site": "00875f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00843c1c",
      "incomplete_value": false,
      "site": "00843c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c01000:8"
          ],
          [
            "leaf",
            "const:f78:8"
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
      "00875f0c",
      "DATA",
      [
        "storage",
        "00c01f78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00875f0c",
      "DATA",
      [
        "storage",
        "00c7fbb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00843c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843bf8.md#insn-00843c0c) · [`00843c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843bf8.md#insn-00843c18) · [`00843c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843bf8.md#insn-00843c1c)
- 新版 [`00875ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875ef8) · [`00875f04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875f04) · [`00875f08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875ee4.md#insn-00875f08)

~~~diff
- 00843c0c ["INT_ADD", "register:40f0:8", ["const:843c0c:8", "const:4:8"]]
- 00843c0c ["CALL", null, ["callee:00c57a90:8"]]
+ 00875ef8 ["INT_ADD", "register:40f0:8", ["const:875ef8:8", "const:4:8"]]
+ 00875ef8 ["CALL", null, ["callee:00c57a90:8"]]
- 00843c0c bytes 0d5d0e94
+ 00875ef8 bytes e6860f94
- 00843c18 ["COPY", "register:4048:8", ["const:c01000:8"]]
+ 00875f04 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 00843c18 bytes e91d00d0
+ 00875f04 bytes 492000d0
- 00843c1c ["COPY", "tmp:0:8", ["const:f78:8"]]
- 00843c1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00843c1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00843c1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00875f08 ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 00875f08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00875f08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00843c1c bytes 29e13d91
+ 00875f08 bytes 29c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be0010647c5ad8062e020e32caf7b0f5"></a>

### [`00843cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md) → [`00875fc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md) FUN_00875fc8

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`0084394c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/0084394c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00875c38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875c38.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 42.86% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00843cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md#insn-00843cfc) · [`00843d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md#insn-00843d10) · [`00843d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843cdc.md#insn-00843d18)
- 新版 [`00875fe8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00875fe8) · [`00875ffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00875ffc) · [`00876004`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00875/00875fc8.md#insn-00876004)

~~~diff
- 00843cfc ["INT_ADD", "register:40f0:8", ["const:843cfc:8", "const:4:8"]]
- 00843cfc ["CALL", null, ["callee:00c538e0:8"]]
+ 00875fe8 ["INT_ADD", "register:40f0:8", ["const:875fe8:8", "const:4:8"]]
+ 00875fe8 ["CALL", null, ["callee:00c538e0:8"]]
- 00843cfc bytes 654c0e94
+ 00875fe8 bytes 3e760f94
- 00843d10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00843d10 ["INT_ADD", "register:40f0:8", ["const:843d10:8", "const:4:8"]]
- 00843d10 ["CALLIND", null, ["register:0:8"]]
+ 00875ffc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00875ffc ["INT_ADD", "register:40f0:8", ["const:875ffc:8", "const:4:8"]]
+ 00875ffc ["CALLIND", null, ["register:0:8"]]
- 00843d10 bytes 00013fd6
+ 00875ffc bytes 00013fd6
- 00843d18 ["INT_ADD", "register:40f0:8", ["const:843d18:8", "const:4:8"]]
- 00843d18 ["CALL", null, ["callee:00c57a80:8"]]
+ 00876004 ["INT_ADD", "register:40f0:8", ["const:876004:8", "const:4:8"]]
+ 00876004 ["CALL", null, ["callee:00c57a80:8"]]
- 00843d18 bytes c65c0e94
+ 00876004 bytes 9f860f94
~~~


<a id="compare-137bd9420844fc99a805e5e35f9f5785"></a>

### [`00843d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md) → [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) FUN_00876050

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00841c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841c14.md) [`00843d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md) · 呼出先 2件 [`00843d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 2件 [`00873f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873f00.md) [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) · 呼出先 2件 [`00876050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 28.57% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843d68"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843d6c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00843d68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00843d6c",
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
      "00876054",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00876058",
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

- 旧版 [`00843d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md#insn-00843d68) · [`00843d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md#insn-00843d6c) · [`00843d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843d64.md#insn-00843d80)
- 新版 [`0087606c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876050.md#insn-0087606c)

~~~diff
- 00843d68 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00843d68 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00843d68 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00843d68 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00843d68 bytes fd7bbea9
- 00843d6c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00843d6c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00843d6c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00843d6c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00843d6c bytes f44f01a9
- 00843d80 ["INT_ADD", "register:40f0:8", ["const:843d80:8", "const:4:8"]]
- 00843d80 ["CALL", null, ["local:b0:8"]]
+ 0087606c ["INT_ADD", "register:40f0:8", ["const:87606c:8", "const:4:8"]]
+ 0087606c ["CALL", null, ["local:b0:8"]]
- 00843d80 bytes f9ffff97
+ 0087606c bytes f9ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d47a8334ab998ca359d94ec1822f5c9"></a>

### [`00843df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843df4.md) → [`008760e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760e0.md) FUN_008760e0

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 0件 
- 新版 呼出元 2件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-dbd9963f5c55638fe7a60d1c5f506225"></a>

### [`00843e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md) → [`008760f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md) FUN_008760f0

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00574ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 2件 [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00597e88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.86% / 新版 69.86%

CFGの説明率　旧版 60.78% / 新版 53.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 25件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843e08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00843e0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00843e08",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00843e0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00843e10",
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
      "008760f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "008760f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "008760fc",
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

- 旧版 [`00843e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md#insn-00843e08) · [`00843e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md#insn-00843e0c) · [`00843e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md#insn-00843e10)

~~~diff
- 00843e08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00843e08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00843e08 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00843e08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00843e08 bytes fd7b05a9
- 00843e0c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00843e0c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00843e0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00843e0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00843e0c bytes fa6706a9
- 00843e10 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00843e10 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00843e10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00843e10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00843e10 bytes f85f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87c8129b67869ded39fbd0e89b806b88"></a>

### [`00844200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844200.md) → [`008764ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md) FUN_008764ec

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00876504",
      "incomplete_value": false,
      "site": "00876508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00844218",
      "incomplete_value": false,
      "site": "0084421c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "definition_site": "00876520",
      "incomplete_value": true,
      "site": "00876528",
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
            "const:8:8"
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
      "definition_site": "00876538",
      "incomplete_value": true,
      "site": "00876540",
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
      "00876508",
      "DATA",
      [
        "storage",
        "00c02058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876508",
      "DATA",
      [
        "storage",
        "00c7fc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084423c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844200.md#insn-0084423c) · [`00844254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844200.md#insn-00844254) · [`0084427c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844200.md#insn-0084427c)
- 新版 [`00876528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876528) · [`00876540`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876540) · [`00876568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008764ec.md#insn-00876568)

~~~diff
- 0084423c ["INT_ADD", "register:40f0:8", ["const:84423c:8", "const:4:8"]]
- 0084423c ["CALL", null, ["callee:00c538e0:8"]]
+ 00876528 ["INT_ADD", "register:40f0:8", ["const:876528:8", "const:4:8"]]
+ 00876528 ["CALL", null, ["callee:00c538e0:8"]]
- 0084423c bytes 154b0e94
+ 00876528 bytes ee740f94
- 00844254 ["INT_ADD", "register:40f0:8", ["const:844254:8", "const:4:8"]]
- 00844254 ["CALL", null, ["callee:00c538e0:8"]]
+ 00876540 ["INT_ADD", "register:40f0:8", ["const:876540:8", "const:4:8"]]
+ 00876540 ["CALL", null, ["callee:00c538e0:8"]]
- 00844254 bytes 0f4b0e94
+ 00876540 bytes e8740f94
- 0084427c ["INT_ADD", "register:40f0:8", ["const:84427c:8", "const:4:8"]]
- 0084427c ["CALL", null, ["callee:00c57a80:8"]]
+ 00876568 ["INT_ADD", "register:40f0:8", ["const:876568:8", "const:4:8"]]
+ 00876568 ["CALL", null, ["callee:00c57a80:8"]]
- 0084427c bytes 6d5b0e94
+ 00876568 bytes 46850f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e8a0e2a08478f3b144e3ad162bea062"></a>

### [`008442ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008442ac.md) → [`00876598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md) FUN_00876598

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "008765b0",
      "incomplete_value": false,
      "site": "008765b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:c90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008442c4",
      "incomplete_value": false,
      "site": "008442c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "008765b4",
      "DATA",
      [
        "storage",
        "00c02058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008765b4",
      "DATA",
      [
        "storage",
        "00c7fc90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008442c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008442ac.md#insn-008442c0) · [`008442c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008442ac.md#insn-008442c4) · [`008442d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008442ac.md#insn-008442d4)
- 新版 [`008765ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765ac) · [`008765b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765b0) · [`008765c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876598.md#insn-008765c0)

~~~diff
- 008442c0 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 008765ac ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008442c0 bytes e91d00d0
+ 008765ac bytes 492000b0
- 008442c4 ["COPY", "tmp:0:8", ["const:58:8"]]
- 008442c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008442c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008442c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008765b0 ["COPY", "tmp:0:8", ["const:c90:8"]]
+ 008765b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008765b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008765b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008442c4 bytes 29610191
+ 008765b0 bytes 29413291
- 008442d4 ["INT_ADD", "register:40f0:8", ["const:8442d4:8", "const:4:8"]]
- 008442d4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 008765c0 ["INT_ADD", "register:40f0:8", ["const:8765c0:8", "const:4:8"]]
+ 008765c0 ["CALL", null, ["callee:00c57ab0:8"]]
- 008442d4 bytes 635b0e94
+ 008765c0 bytes 3c850f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ef06ec4296a8c29f640251b7ffc1443"></a>

### [`00844378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844378.md) → [`00876664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md) FUN_00876664

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00876688",
      "incomplete_value": false,
      "site": "00876688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084439c",
      "incomplete_value": false,
      "site": "0084439c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "00876688",
      "DATA",
      [
        "storage",
        "00c020b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00876688",
      "DATA",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084438c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844378.md#insn-0084438c) · [`00844394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844378.md#insn-00844394) · [`00844398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844378.md#insn-00844398)
- 新版 [`00876678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876678) · [`00876680`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876680) · [`00876684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876664.md#insn-00876684)

~~~diff
- 0084438c ["INT_ADD", "register:40f0:8", ["const:84438c:8", "const:4:8"]]
- 0084438c ["CALL", null, ["callee:00c57a90:8"]]
+ 00876678 ["INT_ADD", "register:40f0:8", ["const:876678:8", "const:4:8"]]
+ 00876678 ["CALL", null, ["callee:00c57a90:8"]]
- 0084438c bytes 2d5b0e94
+ 00876678 bytes 06850f94
- 00844394 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00876680 ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 00844394 bytes e81d00d0
+ 00876680 bytes 482000b0
- 00844398 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00844398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00844398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00844398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00876684 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 00876684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00876684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00876684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00844398 bytes 08e10291
+ 00876684 bytes 08c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae905f068cd60d1f7e26aeaaf0aa9cd"></a>

### [`008443ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443ac.md) → [`00876698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md) FUN_00876698

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008766a4",
      "incomplete_value": false,
      "site": "008766a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008443b8",
      "incomplete_value": false,
      "site": "008443b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b8:8"
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
      "008766a4",
      "DATA",
      [
        "storage",
        "00c020b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008766a4",
      "DATA",
      [
        "storage",
        "00c7fcf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008443b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443ac.md#insn-008443b0) · [`008443b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443ac.md#insn-008443b4)
- 新版 [`0087669c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md#insn-0087669c) · [`008766a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876698.md#insn-008766a0)

~~~diff
- 008443b0 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 0087669c ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008443b0 bytes e91d00d0
+ 0087669c bytes 492000b0
- 008443b4 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 008443b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008443b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008443b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008766a0 ["COPY", "tmp:0:8", ["const:cf0:8"]]
+ 008766a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008766a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008766a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008443b4 bytes 29e10291
+ 008766a0 bytes 29c13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36222a6218a256188ad4077f8960b4f3"></a>

### [`008443c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md) → [`008766b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008766b4.md) FUN_008766b4

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`004724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00472/004724fc.md) [`00840d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d5c.md) [`00840d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00840/00840d6c.md) [`00843df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843df4.md) [`00843e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00843/00843e04.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00495394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00495/00495394.md) [`00873048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873048.md) [`00873058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873058.md) [`008760e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760e0.md) [`008760f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008760f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.41% / 新版 65.41%

CFGの説明率　旧版 42.11% / 新版 47.06%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00844410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00844418"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084447c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00844408",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b9134"
      ]
    ],
    [
      "unmatched:0084440c",
      "DATA",
      [
        "storage",
        "00334658",
        null,
        "byte[51]"
      ]
    ],
    [
      "unmatched:00844410",
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
      "008766f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b9134"
      ]
    ],
    [
      "008766f8",
      "DATA",
      [
        "storage",
        "003386f8",
        null,
        "fde_table_entry"
      ]
    ],
    [
      "008766fc",
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

- 旧版 [`00844408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md#insn-00844408) · [`00844410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md#insn-00844410) · [`00844418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008443c8.md#insn-00844418)

~~~diff
- 00844408 ["INT_ADD", "register:40f0:8", ["const:844408:8", "const:4:8"]]
- 00844408 ["CALL", null, ["callee:008b9134:8"]]
- 00844408 bytes de060194
- 00844410 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00844410 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00844410 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00844410 bytes a8831ef8
- 00844418 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00844418 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00844418 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00844418 bytes a8031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecab4cf2c69a8c8c54862eebb545fae4"></a>

### [`00844694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844694.md) → [`00876980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md) FUN_00876980

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008769a4",
      "incomplete_value": false,
      "site": "008769a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008446b8",
      "incomplete_value": false,
      "site": "008446b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "008769a4",
      "DATA",
      [
        "storage",
        "00c02138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008769a4",
      "DATA",
      [
        "storage",
        "00c7fd70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008446a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844694.md#insn-008446a8) · [`008446b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844694.md#insn-008446b0) · [`008446b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844694.md#insn-008446b4)
- 新版 [`00876994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-00876994) · [`0087699c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-0087699c) · [`008769a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876980.md#insn-008769a0)

~~~diff
- 008446a8 ["INT_ADD", "register:40f0:8", ["const:8446a8:8", "const:4:8"]]
- 008446a8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00876994 ["INT_ADD", "register:40f0:8", ["const:876994:8", "const:4:8"]]
+ 00876994 ["CALL", null, ["callee:00c57a90:8"]]
- 008446a8 bytes 665a0e94
+ 00876994 bytes 3f840f94
- 008446b0 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0087699c ["COPY", "register:4040:8", ["const:c7f000:8"]]
- 008446b0 bytes e81d00d0
+ 0087699c bytes 482000b0
- 008446b4 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008446b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008446b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008446b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008769a0 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 008769a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008769a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008769a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008446b4 bytes 08e10491
+ 008769a0 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d684a29ba7452aacb00db309a9e8abd"></a>

### [`008446c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446c8.md) → [`008769b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md) FUN_008769b4

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008769c0",
      "incomplete_value": false,
      "site": "008769c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c7f000:8"
          ],
          [
            "leaf",
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008446d4",
      "incomplete_value": false,
      "site": "008446d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "008769c0",
      "DATA",
      [
        "storage",
        "00c02138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008769c0",
      "DATA",
      [
        "storage",
        "00c7fd70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008446cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446c8.md#insn-008446cc) · [`008446d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446c8.md#insn-008446d0)
- 新版 [`008769b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md#insn-008769b8) · [`008769bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769b4.md#insn-008769bc)

~~~diff
- 008446cc ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 008769b8 ["COPY", "register:4048:8", ["const:c7f000:8"]]
- 008446cc bytes e91d00d0
+ 008769b8 bytes 492000b0
- 008446d0 ["COPY", "tmp:0:8", ["const:138:8"]]
- 008446d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008446d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008446d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008769bc ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 008769bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008769bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008769bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008446d0 bytes 29e10491
+ 008769bc bytes 29c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb7dc6a7fee088721fea774d6e79f02b"></a>

### [`008446e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md) → [`008769d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md) FUN_008769d0

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0042c4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c4b8.md) [`0042c564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042c564.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0044f350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f350.md) [`0044f3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f3fc.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

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
      "site": "00876a18",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0084472c",
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
      "site": "00876a8c",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008447a0",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "00876a18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00457e1c"
      ]
    ],
    [
      "00876a8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "00876a18",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00876a8c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084472c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md#insn-0084472c) · [`008447a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md#insn-008447a0) · [`00844728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/008446e4.md#insn-00844728)
- 新版 [`00876a18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876a18) · [`00876a8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876a8c) · [`00876a14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/008769d0.md#insn-00876a14)

~~~diff
- 0084472c ["INT_ADD", "register:40f0:8", ["const:84472c:8", "const:4:8"]]
- 0084472c ["CALL", null, ["ram:457e1c:8"]]
+ 00876a18 ["INT_ADD", "register:40f0:8", ["const:876a18:8", "const:4:8"]]
+ 00876a18 ["CALL", null, ["ram:47acb4:8"]]
- 0084472c bytes bc4df097
+ 00876a18 bytes a710f097
- 008447a0 ["INT_ADD", "register:40f0:8", ["const:8447a0:8", "const:4:8"]]
- 008447a0 ["CALL", null, ["ram:469e20:8"]]
+ 00876a8c ["INT_ADD", "register:40f0:8", ["const:876a8c:8", "const:4:8"]]
+ 00876a8c ["CALL", null, ["ram:48ccb8:8"]]
- 008447a0 bytes a095f097
+ 00876a8c bytes 8b58f097
- 00844728 ["INT_ADD", "register:40f0:8", ["const:844728:8", "const:4:8"]]
- 00844728 ["CALL", null, ["callee:008b9134:8"]]
+ 00876a14 ["INT_ADD", "register:40f0:8", ["const:876a14:8", "const:4:8"]]
+ 00876a14 ["CALL", null, ["callee:008b9134:8"]]
- 00844728 bytes 16060194
+ 00876a14 bytes c8090194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74acd8d77c888b4609773e53a9d003dc"></a>

### [`00844848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844848.md) → [`00876b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md) _INIT_157

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00876b70",
      "incomplete_value": true,
      "site": "00876b8c",
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
      "definition_site": "00844884",
      "incomplete_value": true,
      "site": "008448a0",
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
      "definition_site": "00876b94",
      "incomplete_value": true,
      "site": "00876bb0",
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
      "definition_site": "008448a8",
      "incomplete_value": true,
      "site": "008448c4",
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
      "definition_site": "00876bb4",
      "incomplete_value": true,
      "site": "00876bd0",
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
      "definition_site": "008448c8",
      "incomplete_value": true,
      "site": "008448e4",
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
      "00876b70",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00876b94",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00876bb4",
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
      "00876b70",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00876b94",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00876bb4",
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

- 旧版 [`008449a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844848.md#insn-008449a8) · [`00844a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844848.md#insn-00844a7c) · [`00844870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844848.md#insn-00844870)
- 新版 [`00876c94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876c94) · [`00876d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876d68) · [`00876b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876b34.md#insn-00876b5c)

~~~diff
- 008449a8 ["INT_ADD", "register:40f0:8", ["const:8449a8:8", "const:4:8"]]
- 008449a8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 00876c94 ["INT_ADD", "register:40f0:8", ["const:876c94:8", "const:4:8"]]
+ 00876c94 ["CALL", null, ["callee:0043b7b8:8"]]
- 008449a8 bytes c450ef97
+ 00876c94 bytes c912ef97
- 00844a7c ["INT_ADD", "register:40f0:8", ["const:844a7c:8", "const:4:8"]]
- 00844a7c ["CALL", null, ["callee:00c57a30:8"]]
+ 00876d68 ["INT_ADD", "register:40f0:8", ["const:876d68:8", "const:4:8"]]
+ 00876d68 ["CALL", null, ["callee:00c57a30:8"]]
- 00844a7c bytes 59590e94
+ 00876d68 bytes 32830f94
- 00844870 ["COPY", "register:4098:8", ["const:109e000:8"]]
+ 00876b5c ["COPY", "register:4098:8", ["const:1123000:8"]]
- 00844870 bytes d34200d0
+ 00876b5c bytes 734500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60bc11b371c5091b7e4264cb30e5d938"></a>

### [`008456e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008456e4.md) → [`008779d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md) FUN_008779d0

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00844bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00844/00844bd8.md) · 呼出先 6件 [`00423f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00423/00423f08.md) [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb320.md)
- 新版 呼出元 1件 [`00876ec4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00876/00876ec4.md) · 呼出先 6件 [`00446a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00446/00446a08.md) [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "site": "00877a04",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00845718",
      "value": [
        "leaf",
        "ram:bdb280:8"
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
      "00877a04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ]
  ],
  "added": [
    [
      "00877a04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00845718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008456e4.md#insn-00845718) · [`00845700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008456e4.md#insn-00845700) · [`00845708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/008456e4.md#insn-00845708)
- 新版 [`00877a04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-00877a04) · [`008779ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-008779ec) · [`008779f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/008779d0.md#insn-008779f4)

~~~diff
- 00845718 ["INT_ADD", "register:40f0:8", ["const:845718:8", "const:4:8"]]
- 00845718 ["CALL", null, ["ram:bdb280:8"]]
+ 00877a04 ["INT_ADD", "register:40f0:8", ["const:877a04:8", "const:4:8"]]
+ 00877a04 ["CALL", null, ["ram:c57cd0:8"]]
- 00845718 bytes da560e94
+ 00877a04 bytes b3800f94
- 00845700 ["INT_ADD", "register:40f0:8", ["const:845700:8", "const:4:8"]]
- 00845700 ["CALL", null, ["callee:00446a08:8"]]
+ 008779ec ["INT_ADD", "register:40f0:8", ["const:8779ec:8", "const:4:8"]]
+ 008779ec ["CALL", null, ["callee:00446a08:8"]]
- 00845700 bytes 027aef97
+ 008779ec bytes 073cef97
- 00845708 ["INT_ADD", "register:40f0:8", ["const:845708:8", "const:4:8"]]
- 00845708 ["CALL", null, ["callee:00c57d70:8"]]
+ 008779f4 ["INT_ADD", "register:40f0:8", ["const:8779f4:8", "const:4:8"]]
+ 008779f4 ["CALL", null, ["callee:00c57d70:8"]]
- 00845708 bytes 06570e94
+ 008779f4 bytes df800f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebc094176d834383d74058ecd6d056b0"></a>

### [`00845744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md) → [`00877a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md) FUN_00877a30

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`00574f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`00845a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md)
- 新版 呼出元 0件  · 呼出先 13件 [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`00877d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 95.60% / 新版 95.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00877b44",
      "incomplete_value": true,
      "site": "00877b44",
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
            "const:357c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845858",
      "incomplete_value": true,
      "site": "00845858",
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
            "const:3484:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00877b4c",
      "incomplete_value": true,
      "site": "00877b4c",
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
            "const:3578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845860",
      "incomplete_value": true,
      "site": "00845860",
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
            "const:3480:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00877ae8",
      "incomplete_value": false,
      "site": "00877af4",
      "value": [
        "leaf",
        "const:877d10:8"
      ]
    },
    "old": {
      "definition_site": "008457fc",
      "incomplete_value": false,
      "site": "00845808",
      "value": [
        "leaf",
        "const:845a24:8"
      ]
    },
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
      "00877ae8",
      "PARAM",
      [
        "storage",
        "00845a24",
        null,
        null
      ]
    ],
    [
      "unmatched:0084585c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00877b8c",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00877ae8",
      "PARAM",
      [
        "storage",
        "00877d10",
        null,
        null
      ]
    ],
    [
      "00877b48",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00877b8c",
      "PARAM",
      [
        "storage",
        "002a3e5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00845808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md#insn-00845808) · [`00845858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md#insn-00845858) · [`0084585c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md#insn-0084585c)
- 新版 [`00877af4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md#insn-00877af4) · [`00877b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md#insn-00877b44)

~~~diff
- 00845808 ["INT_ADD", "register:40f0:8", ["const:845808:8", "const:4:8"]]
- 00845808 ["CALL", null, ["callee:00c57d10:8"]]
+ 00877af4 ["INT_ADD", "register:40f0:8", ["const:877af4:8", "const:4:8"]]
+ 00877af4 ["CALL", null, ["callee:00c57d10:8"]]
- 00845808 bytes ae560e94
+ 00877af4 bytes 87800f94
- 00845858 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3484:8"]]
- 00845858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:4"]]
+ 00877b44 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:357c:8"]]
+ 00877b44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:4"]]
- 00845858 bytes 138434b9
+ 00877b44 bytes 137c35b9
- 0084585c ["INT_ADD", "register:40f0:8", ["const:84585c:8", "const:4:8"]]
- 0084585c ["CALL", null, ["callee:008514b8:8"]]
- 0084585c bytes 4967ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0696f4d5ff28577eb40fd3fea8d1dfb5"></a>

### [`00845a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md) → [`00877d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md) FUN_00877d10

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00845744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845744.md) · 呼出先 9件 [`00574bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574bb4.md) [`00574f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574f70.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`00877a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877a30.md) · 呼出先 9件 [`00597a4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597a4c.md) [`00597e08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/00597e08.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085b3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b3f0.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_count, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_destination` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00877d7c",
      "incomplete_value": true,
      "site": "00877d7c",
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
            "const:357c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845a90",
      "incomplete_value": true,
      "site": "00845a90",
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
            "const:3484:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00877d84",
      "incomplete_value": true,
      "site": "00877d84",
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
            "const:3578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00845a98",
      "incomplete_value": true,
      "site": "00845a98",
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
            "const:3480:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00845a94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00845a94",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00877da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb300"
      ]
    ]
  ],
  "added": [
    [
      "00877d80",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "00877da0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57d50"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00845a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md#insn-00845a90) · [`00845a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md#insn-00845a94) · [`00845a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845a24.md#insn-00845a98)
- 新版 [`00877d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md#insn-00877d7c) · [`00877d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877d10.md#insn-00877d84)

~~~diff
- 00845a90 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3484:8"]]
- 00845a90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 00877d7c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:357c:8"]]
+ 00877d7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00845a90 bytes 148434b9
+ 00877d7c bytes 147c35b9
- 00845a94 ["INT_ADD", "register:40f0:8", ["const:845a94:8", "const:4:8"]]
- 00845a94 ["CALL", null, ["callee:008514b8:8"]]
- 00845a94 bytes bb66ff97
- 00845a98 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3480:8"]]
- 00845a98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
+ 00877d84 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3578:8"]]
+ 00877d84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00845a98 bytes 148034b9
+ 00877d84 bytes 147835b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0e7fc99183fef6a15c6dcdba55e3619"></a>

### [`00845b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845b6c.md) → [`00877e58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00877/00877e58.md) _INIT_158

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.71% / 新版 75.71%

CFGの説明率　旧版 93.33% / 新版 87.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_store_alignment` 20件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00845b9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00845bc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00845be8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00845b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00845ba8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00845bc4",
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
      "00877e88",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00877e94",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00877eb0",
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

- 旧版 [`00845b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845b6c.md#insn-00845b9c) · [`00845bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845b6c.md#insn-00845bc4) · [`00845be8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845b6c.md#insn-00845be8)

~~~diff
- 00845b9c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00845b9c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00845b9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00845b9c bytes a9831ff8
- 00845bc4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 00845bc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00845bc4 bytes e013813c
- 00845be8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00845be8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00845be8 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80d23749ce2722cab11bdaaf3305fcf4"></a>

### [`008460c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md) → [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) FUN_008783b0

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 19件 [`005d996c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d9/005d996c.md) [`006c4ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006c4/006c4ea8.md) [`006d584c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d5/006d584c.md) [`006e34b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e3/006e34b0.md) [`007317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00731/007317b0.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 19件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`006eec6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ee/006eec6c.md) [`006ff600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006ff600.md) [`0070d378`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0070d/0070d378.md) [`0075b984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075b/0075b984.md) · 呼出先 6件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.58% / 新版 67.58%

CFGの説明率　旧版 40.00% / 新版 29.63%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846108"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846184"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846188"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00846108",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "unmatched:00846184",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "unmatched:00846184",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008783f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x68]",
        null,
        null
      ]
    ],
    [
      "00878470",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "00878470",
      "WRITE",
      [
        "storage",
        "Stack[-0xa0]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md#insn-00846108) · [`00846184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md#insn-00846184) · [`00846188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md#insn-00846188)

~~~diff
- 00846108 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00846108 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00846108 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00846108 bytes a8831ff8
- 00846184 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00846184 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00846184 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00846184 bytes a8031cf8
- 00846188 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00846188 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00846188 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00846188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00846188 bytes bf831cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da354bcd936b67e955b6a8cc90016a6c"></a>

### [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) → [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) FUN_00878718

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`008460c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008460c4.md) [`008468c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md) [`00846bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bac.md) [`00846bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bc4.md) [`00846f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f70.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md)
- 新版 呼出元 5件 [`008783b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/008783b0.md) [`00878bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md) [`00878e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878e98.md) [`00878eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878eb0.md) [`0087925c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/0087925c.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md)

変更の種類 call, call_target, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 6件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008787b0",
      "incomplete_value": false,
      "site": "008787b0",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008464c4",
      "incomplete_value": false,
      "site": "008464c4",
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
            "const:962:8"
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
      "definition_site": "00878818",
      "incomplete_value": false,
      "site": "00878818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:6e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084652c",
      "incomplete_value": false,
      "site": "0084652c",
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
            "const:66b:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084658c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008787b0",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "008787d4",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "00878804",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "008787b0",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "008787d4",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878804",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md#insn-00846518) · [`0084658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md#insn-0084658c) · [`00846608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md#insn-00846608)
- 新版 [`00878804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md#insn-00878804)

~~~diff
- 00846518 ["INT_ADD", "register:40f0:8", ["const:846518:8", "const:4:8"]]
- 00846518 ["CALL", null, ["ram:469e20:8"]]
+ 00878804 ["INT_ADD", "register:40f0:8", ["const:878804:8", "const:4:8"]]
+ 00878804 ["CALL", null, ["ram:48ccb8:8"]]
- 00846518 bytes 428ef097
+ 00878804 bytes 2d51f097
- 0084658c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0084658c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0084658c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 0084658c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 0084658c bytes bf031cb8
- 00846608 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00846608 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00846608 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 00846608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00846608 bytes bf031cb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ba36204beba17dae78b98121d2dd0b1"></a>

### [`008468c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md) → [`00878bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md) FUN_00878bac

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`005ec96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ec/005ec96c.md) [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) [`006f5fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f5/006f5fe8.md) [`008d9aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d9/008d9aa4.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) · 呼出先 6件 [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0084642c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/0084642c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md)
- 新版 呼出元 5件 [`00611e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00611/00611e20.md) [`00696de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00696/00696de4.md) [`00720050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00720/00720050.md) [`0090db60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0090d/0090db60.md) [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) · 呼出先 6件 [`0071be98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0071b/0071be98.md) [`00878718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878718.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md) [`00c5a440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a440.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.20% / 新版 90.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878c5c",
      "incomplete_value": false,
      "site": "00878c5c",
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
            "const:fe7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846970",
      "incomplete_value": false,
      "site": "00846970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29f000:8"
          ],
          [
            "leaf",
            "const:bc9:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878cd0",
      "incomplete_value": false,
      "site": "00878cd0",
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
            "const:156:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008469e4",
      "incomplete_value": false,
      "site": "008469e4",
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
            "const:37d:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878d40",
      "incomplete_value": false,
      "site": "00878d40",
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
            "const:16a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846a54",
      "incomplete_value": false,
      "site": "00846a54",
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
            "const:b6f:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878c5c",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "00878ca4",
      "DATA",
      [
        "storage",
        "0029fbc9",
        null,
        null
      ]
    ],
    [
      "00878cbc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "006f1e2c"
      ]
    ]
  ],
  "added": [
    [
      "00878c5c",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "00878ca4",
      "DATA",
      [
        "storage",
        "002affe7",
        null,
        null
      ]
    ],
    [
      "00878cbc",
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

- 旧版 [`008469d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md#insn-008469d0) · [`00846a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md#insn-00846a44) · [`00846acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/008468c0.md#insn-00846acc)
- 新版 [`00878cbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878cbc) · [`00878d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878d30) · [`00878db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878bac.md#insn-00878db8)

~~~diff
- 008469d0 ["INT_ADD", "register:40f0:8", ["const:8469d0:8", "const:4:8"]]
- 008469d0 ["CALL", null, ["ram:6f1e2c:8"]]
+ 00878cbc ["INT_ADD", "register:40f0:8", ["const:878cbc:8", "const:4:8"]]
+ 00878cbc ["CALL", null, ["ram:71be98:8"]]
- 008469d0 bytes 17adfa97
+ 00878cbc bytes 778cfa97
- 00846a44 ["INT_ADD", "register:40f0:8", ["const:846a44:8", "const:4:8"]]
- 00846a44 ["CALL", null, ["ram:6f1e2c:8"]]
+ 00878d30 ["INT_ADD", "register:40f0:8", ["const:878d30:8", "const:4:8"]]
+ 00878d30 ["CALL", null, ["ram:71be98:8"]]
- 00846a44 bytes faacfa97
+ 00878d30 bytes 5a8cfa97
- 00846acc ["INT_ADD", "register:40f0:8", ["const:846acc:8", "const:4:8"]]
- 00846acc ["CALL", null, ["callee:00878718:8"]]
+ 00878db8 ["INT_ADD", "register:40f0:8", ["const:878db8:8", "const:4:8"]]
+ 00878db8 ["CALL", null, ["callee:00878718:8"]]
- 00846acc bytes 58feff97
+ 00878db8 bytes 58feff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc5bfa97d0235ecf95071427cc860fc"></a>

### [`00846bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bdc.md) → [`00878ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00878/00878ec8.md) FUN_00878ec8

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00733548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00733/00733548.md) · 呼出先 11件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00759ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759ddc.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md)
- 新版 呼出元 1件 [`0075d71c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0075d/0075d71c.md) · 呼出先 11件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce44.md) [`00752240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00752/00752240.md) [`00784240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00784/00784240.md) [`00b3c4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3c/00b3c4b4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 64.00% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00878f50",
      "incomplete_value": false,
      "site": "00878f50",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00846c64",
      "incomplete_value": false,
      "site": "00846c64",
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
            "const:962:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846ccc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846d2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00878f50",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "00878f74",
      "DATA",
      [
        "storage",
        "002a2962",
        null,
        null
      ]
    ],
    [
      "00878f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00846cb8"
      ]
    ]
  ],
  "added": [
    [
      "00878f50",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878f74",
      "DATA",
      [
        "storage",
        "002b2fc0",
        null,
        null
      ]
    ],
    [
      "00878f98",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00878fa4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00846cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bdc.md#insn-00846cb4) · [`00846cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bdc.md#insn-00846cb8) · [`00846cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846bdc.md#insn-00846cbc)

~~~diff
- 00846cb4 ["INT_ADD", "register:40f0:8", ["const:846cb4:8", "const:4:8"]]
- 00846cb4 ["CALL", null, ["callee:00c57ab0:8"]]
- 00846cb4 bytes eb500e94
- 00846cb8 ["INT_ADD", "register:40f0:8", ["const:846cb8:8", "const:4:8"]]
- 00846cb8 ["CALL", null, ["ram:469e20:8"]]
- 00846cb8 bytes 5a8cf097
- 00846cbc ["INT_ADD", "register:40f0:8", ["const:846cbc:8", "const:4:8"]]
- 00846cbc ["CALL", null, ["callee:0048ce44:8"]]
- 00846cbc bytes bc8cf097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-99de1100ff618309d214f55d27c0a82a"></a>

### [`00846f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f88.md) → [`00879274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879274.md) _INIT_159

採用 · 移動量 `+0x322ec` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 48.02% / 新版 48.02%

CFGの説明率　旧版 70.00% / 新版 56.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00846f90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00846f8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00846f90",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00846f94",
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
      "00879278",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087927c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00879280",
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

- 旧版 [`00846f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f88.md#insn-00846f8c) · [`00846f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f88.md#insn-00846f90) · [`00846f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00846/00846f88.md#insn-00846f94)

~~~diff
- 00846f8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00846f8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00846f8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00846f8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00846f8c bytes fd7b0fa9
- 00846f90 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00846f90 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00846f90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00846f90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00846f90 bytes fc5710a9
- 00846f94 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00846f94 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00846f94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00846f94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00846f94 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d56768c60b5cf5b9e2207c56165aeb67"></a>

### [`00847318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847318.md) → [`00879604`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md) FUN_00879604

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084914c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/0084914c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00470ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470ac0.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0087bc04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087bc04.md) · 呼出先 6件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00493958`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493958.md) [`005626b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00562/005626b4.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.31% / 新版 88.31%

CFGの説明率　旧版 43.75% / 新版 45.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00847348"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084734c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "008473ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084734c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00879710"
      ]
    ],
    [
      "unmatched:00847354",
      "PARAM",
      [
        "storage",
        "0109e3c8",
        null,
        "undefined2"
      ]
    ],
    [
      "00879690",
      "PARAM",
      [
        "storage",
        "0109e3b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879638",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00879710"
      ]
    ],
    [
      "00879640",
      "PARAM",
      [
        "storage",
        "011231f8",
        null,
        "undefined2"
      ]
    ],
    [
      "00879690",
      "PARAM",
      [
        "storage",
        "011231e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00847348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847318.md#insn-00847348) · [`0084734c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847318.md#insn-0084734c) · [`00847360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847318.md#insn-00847360)
- 新版 [`0087964c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879604.md#insn-0087964c)

~~~diff
- 00847348 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00847348 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00847348 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00847348 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00847348 bytes 4801899a
- 0084734c ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0084734c ["CBRANCH", null, ["local:b20:8", "tmp:0:1"]]
- 0084734c bytes c80600b4
- 00847360 ["INT_ADD", "register:40f0:8", ["const:847360:8", "const:4:8"]]
- 00847360 ["CALL", null, ["callee:005626b4:8"]]
+ 0087964c ["INT_ADD", "register:40f0:8", ["const:87964c:8", "const:4:8"]]
+ 0087964c ["CALL", null, ["callee:005626b4:8"]]
- 00847360 bytes 2fe1f397
+ 0087964c bytes 1aa4f397
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4e38421d1fff71302b04b7aea6aef80"></a>

### [`00847488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847488.md) → [`00879774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879774.md) _INIT_160

採用 · 移動量 `+0x322ec` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 50.97% / 新版 50.97%

CFGの説明率　旧版 57.50% / 新版 76.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 15件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 44件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008474b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008474e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008474ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008474b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008474c4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:008474e0",
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
      "008797a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "008797b0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "008797cc",
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

- 旧版 [`008474b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847488.md#insn-008474b8) · [`008474e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847488.md#insn-008474e0) · [`008474ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847488.md#insn-008474ec)

~~~diff
- 008474b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 008474b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008474b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008474b8 bytes a9831ff8
- 008474e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:11:8"]]
- 008474e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008474e0 bytes e013813c
- 008474ec ["COPY", "tmp:0:4", ["register:4048:4"]]
- 008474ec ["INT_ADD", "tmp:1:8", ["register:8:8", "const:41:8"]]
- 008474ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 008474ec bytes e9130478
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c07e954f52ded1687602f38bad864fb"></a>

### [`0084788c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084788c.md) → [`00879b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md) FUN_00879b78

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0058ccc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0058c/0058ccc8.md) · 呼出先 7件 [`00565f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00565/00565f94.md) [`00566284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566284.md) [`00566978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/00566978.md) [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`005b12f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005b1/005b12f8.md) · 呼出先 7件 [`00588e2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00588/00588e2c.md) [`0058911c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/0058911c.md) [`00589810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00589/00589810.md) [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.09% / 新版 72.09%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008478b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008478b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008478b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008478b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:008478b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:008478b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00879b9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00879ba0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00879ba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x100]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008478b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084788c.md#insn-008478b0) · [`008478b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084788c.md#insn-008478b4) · [`008478b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084788c.md#insn-008478b8)

~~~diff
- 008478b0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 008478b0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 008478b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 008478b0 bytes a8831ff8
- 008478b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:d0:8"]]
- 008478b4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 008478b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 008478b4 bytes ff6b00f9
- 008478b8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 008478b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008478b8 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 008478b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 008478b8 bytes e08300ad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b803dfd56c3d0dd99871c8a00f65049d"></a>

### [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) → [`00879c48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md) FUN_00879c48

採用 · 移動量 `+0x322ec` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 7件 [`0084788c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084788c.md) [`0084b5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b5fc.md) [`00b06b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md) [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 7件 [`00879b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879b78.md) [`0087e594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e594.md) [`00b667d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b667d0.md) [`00b66884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b66884.md) [`00b6697c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b66/00b6697c.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 63.16% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00879cdc",
      "incomplete_value": true,
      "site": "00879ce0",
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
                "const:88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`008479f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md#insn-008479f4) · [`00847970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md#insn-00847970) · [`00847978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md#insn-00847978)
- 新版 [`00879ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879ce0) · [`00879c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879c5c) · [`00879c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00879/00879c48.md#insn-00879c64)

~~~diff
- 008479f4 ["INT_ADD", "register:40f0:8", ["const:8479f4:8", "const:4:8"]]
- 008479f4 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00879ce0 ["INT_ADD", "register:40f0:8", ["const:879ce0:8", "const:4:8"]]
+ 00879ce0 ["CALL", null, ["callee:00c57ab0:8"]]
- 008479f4 bytes 9b4d0e94
+ 00879ce0 bytes 74770f94
- 00847970 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00847970 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00847970 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00847970 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00879c5c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00879c5c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00879c5c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00879c5c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00847970 bytes 88020037
+ 00879c5c bytes 88020037
- 00847978 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00847978 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00847978 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00847978 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00879c64 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00879c64 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00879c64 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00879c64 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00847978 bytes c8020037
+ 00879c64 bytes c8020037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd648a8932a0928c0bdb8672e314d14b"></a>

### [`00848e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md) → [`0087b8ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md) FUN_0087b8ec

採用 · 移動量 `+0x32ab8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00847a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/00847a5c.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.59% / 新版 79.59%

CFGの説明率　旧版 25.00% / 新版 29.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848e64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848ed8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0087b91c"
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
      "unmatched:00848e64",
      "DATA",
      [
        "storage",
        "00c02230",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00848e9c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "unmatched:00848ee0",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "0087b91c",
      "DATA",
      [
        "storage",
        "00c7fef8",
        null,
        "undefined *"
      ]
    ],
    [
      "0087b954",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ],
    [
      "0087b998",
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

- 旧版 [`00848e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md#insn-00848e4c) · [`00848e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md#insn-00848e64) · [`00848e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848e34.md#insn-00848e9c)
- 新版 [`0087b904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b8ec.md#insn-0087b904)

~~~diff
- 00848e4c ["INT_ADD", "register:40f0:8", ["const:848e4c:8", "const:4:8"]]
- 00848e4c ["CALL", null, ["callee:00c57a90:8"]]
+ 0087b904 ["INT_ADD", "register:40f0:8", ["const:87b904:8", "const:4:8"]]
+ 0087b904 ["CALL", null, ["callee:00c57a90:8"]]
- 00848e4c bytes 7d480e94
+ 0087b904 bytes 63700f94
- 00848e64 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00848e64 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00848e64 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00848e64 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00848e64 bytes 880601f8
- 00848e9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00848e9c ["INT_ADD", "register:40f0:8", ["const:848e9c:8", "const:4:8"]]
- 00848e9c ["CALLIND", null, ["register:0:8"]]
- 00848e9c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d18e1340b284916c8b28b6b0256e51"></a>

### [`00848f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848f44.md) → [`0087b9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087b/0087b9fc.md) FUN_0087b9fc

採用 · 移動量 `+0x32ab8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 78.00% / 新版 78.00%

CFGの説明率　旧版 23.81% / 新版 22.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848f44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00848f48"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00848f44",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00848f48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00848f4c",
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
      "0087b9fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087ba00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087ba04",
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

- 旧版 [`00848f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848f44.md#insn-00848f44) · [`00848f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848f44.md#insn-00848f48) · [`00848f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848f44.md#insn-00848f4c)

~~~diff
- 00848f44 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00848f44 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00848f44 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00848f44 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00848f44 bytes fd7bbda9
- 00848f48 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00848f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00848f48 bytes f50b00f9
- 00848f4c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00848f4c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00848f4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00848f4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00848f4c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d98f2ab4a3fd2b454799047ffa09b7"></a>

### [`00849e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849e98.md) → [`0087ce30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087c/0087ce30.md) _INIT_161

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00bc43c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc4/00bc43c8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 40.58% / 新版 40.58%

CFGの説明率　旧版 30.00% / 新版 19.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 52件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849e9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849e9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00849ea0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00849e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00849ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00849ea4",
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
      "0087ce34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087ce38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087ce3c",
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

- 旧版 [`00849e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849e98.md#insn-00849e9c) · [`00849ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849e98.md#insn-00849ea0) · [`00849ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00849/00849e98.md#insn-00849ea4)

~~~diff
- 00849e9c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00849e9c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00849e9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00849e9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00849e9c bytes fd7b0fa9
- 00849ea0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00849ea0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00849ea0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00849ea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00849ea0 bytes fc5710a9
- 00849ea4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00849ea4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00849ea4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00849ea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00849ea4 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6119170a517242314638d811487821a"></a>

### [`0084a3a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a3a8.md) → [`0087d340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d340.md) FUN_0087d340

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00552dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00552/00552dcc.md) [`00567ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00567/00567ef0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00575c64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00575/00575c64.md) [`0058ad88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058a/0058ad88.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 26.09% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a3ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a3ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a3b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084a3ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084a3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084a3b4",
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
      "0087d344",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0087d348",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "0087d34c",
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

- 旧版 [`0084a3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a3a8.md#insn-0084a3ac) · [`0084a3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a3a8.md#insn-0084a3b0) · [`0084a3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a3a8.md#insn-0084a3b4)

~~~diff
- 0084a3ac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084a3ac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084a3ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 0084a3ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084a3ac bytes fd7b03a9
- 0084a3b0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 0084a3b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0084a3b0 bytes f72300f9
- 0084a3b4 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0084a3b4 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0084a3b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0084a3b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084a3b4 bytes f65705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16333f1baa30f0d61634889ea636a4e3"></a>

### [`0084a588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a588.md) → [`0087d520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d520.md) _INIT_162

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 52.54% / 新版 52.54%

CFGの説明率　旧版 80.00% / 新版 70.59%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_store_alignment` 39件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a5b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a5cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084a5d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084a5b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084a5c4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "unmatched:0084a5cc",
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
      "0087d550",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "0087d55c",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "0087d564",
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

- 旧版 [`0084a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a588.md#insn-0084a5b8) · [`0084a5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a588.md#insn-0084a5cc) · [`0084a5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a588.md#insn-0084a5d0)

~~~diff
- 0084a5b8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0084a5b8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084a5b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084a5b8 bytes a9831ff8
- 0084a5cc ["COPY", "tmp:0:4", ["register:4050:4"]]
- 0084a5cc ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 0084a5cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0084a5cc bytes ea130278
- 0084a5d0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 0084a5d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 0084a5d0 bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70976afb69513dd8a689e1fff66a4d5d"></a>

### [`0084a9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a9ec.md) → [`0087d984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087d984.md) FUN_0087d984

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084bb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bb48.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00574730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574730.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 1件 [`0087eae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eae0.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00596cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00596/00596cd0.md) [`005975c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005975c8.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 62.16% / 新版 54.76%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084aa14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084aa1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084aa1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084aa14",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084aa1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084aa20",
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
      "0087d9ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "0087d9b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0087d9b8",
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

- 旧版 [`0084aa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a9ec.md#insn-0084aa14) · [`0084aa1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a9ec.md#insn-0084aa1c) · [`0084aa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084a9ec.md#insn-0084aa20)

~~~diff
- 0084aa14 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084aa14 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084aa14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084aa14 bytes a8831ff8
- 0084aa1c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0084aa1c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0084aa1c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0084aa1c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0084aa1c bytes bf7f3ea9
- 0084aa20 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0084aa20 ["COPY", "tmp:1:8", ["tmp:0:8"]]
- 0084aa20 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 0084aa20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:8"]]
- 0084aa20 bytes bf031ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75fafd74a5100c501bc3cb87629daac8"></a>

### [`0084ac4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ac4c.md) → [`0087dbe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dbe4.md) FUN_0087dbe4

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084ad38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ad38.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0087dcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087d/0087dcd0.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 25.42% / 新版 25.42%

CFGの説明率　旧版 7.69% / 新版 6.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084ac74"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084ac8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084aca4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0087dbf0",
      "READ",
      [
        "storage",
        "0109e5f8",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dbf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0084ac6c"
      ]
    ],
    [
      "unmatched:0084ac64",
      "READ",
      [
        "storage",
        "0109e608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0087dbf0",
      "READ",
      [
        "storage",
        "01123428",
        null,
        "undefined1"
      ]
    ],
    [
      "0087dbf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087dc04"
      ]
    ],
    [
      "0087dbfc",
      "READ",
      [
        "storage",
        "01123438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084ac68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ac4c.md#insn-0084ac68) · [`0084ac74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ac4c.md#insn-0084ac74) · [`0084ac80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084a/0084ac4c.md#insn-0084ac80)

~~~diff
- 0084ac68 ["INT_ADD", "register:40f0:8", ["const:84ac68:8", "const:4:8"]]
- 0084ac68 ["CALL", null, ["callee:00c57ab0:8"]]
- 0084ac68 bytes fe400e94
- 0084ac74 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0084ac74 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0084ac74 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0084ac74 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0084ac74 bytes 88000036
- 0084ac80 ["INT_ADD", "register:40f0:8", ["const:84ac80:8", "const:4:8"]]
- 0084ac80 ["CALL", null, ["callee:00c57ab0:8"]]
- 0084ac80 bytes f8400e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdbf5c72552945e1626188f5581ec0e"></a>

### [`0084b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md) → [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) FUN_0087e6d0

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b734.md) · 呼出先 15件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0084bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md) [`0084c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md)
- 新版 呼出元 1件 [`0087e6cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6cc.md) · 呼出先 15件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0044104c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00441/0044104c.md) [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) [`0087eff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.74% / 新版 75.74%

CFGの説明率　旧版 17.24% / 新版 12.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 27件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084b73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084b73c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084b740"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084b73c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084b740",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084b744",
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
      "0087e6d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "0087e6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0087e6dc",
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

- 旧版 [`0084b73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md#insn-0084b73c) · [`0084b740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md#insn-0084b740) · [`0084b744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md#insn-0084b744)

~~~diff
- 0084b73c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084b73c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084b73c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:90:8"]]
- 0084b73c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084b73c bytes fd7b09a9
- 0084b740 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0084b740 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 0084b740 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0084b740 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084b740 bytes fc6f0aa9
- 0084b744 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 0084b744 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0084b744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 0084b744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084b744 bytes fa670ba9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ec840e7902282be61d6ac2a57234947"></a>

### [`0084bbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md) → [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) FUN_0087eb7c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 3件 [`0084b6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b6f8.md) [`0084b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b704.md) [`0084bbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md) · 呼出先 4件 [`0084bbe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 3件 [`0087e690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e690.md) [`0087e69c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e69c.md) [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) · 呼出先 4件 [`0087eb7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`0084bc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md#insn-0084bc00) · [`0084bc0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md#insn-0084bc0c) · [`0084bc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bbe4.md#insn-0084bc20)
- 新版 [`0087eb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087eb98) · [`0087eba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087eba4) · [`0087ebb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eb7c.md#insn-0087ebb8)

~~~diff
- 0084bc00 ["INT_ADD", "register:40f0:8", ["const:84bc00:8", "const:4:8"]]
- 0084bc00 ["CALL", null, ["local:b0:8"]]
+ 0087eb98 ["INT_ADD", "register:40f0:8", ["const:87eb98:8", "const:4:8"]]
+ 0087eb98 ["CALL", null, ["local:b0:8"]]
- 0084bc00 bytes f9ffff97
+ 0087eb98 bytes f9ffff97
- 0084bc0c ["INT_ADD", "register:40f0:8", ["const:84bc0c:8", "const:4:8"]]
- 0084bc0c ["CALL", null, ["local:b0:8"]]
+ 0087eba4 ["INT_ADD", "register:40f0:8", ["const:87eba4:8", "const:4:8"]]
+ 0087eba4 ["CALL", null, ["local:b0:8"]]
- 0084bc0c bytes f6ffff97
+ 0087eba4 bytes f6ffff97
- 0084bc20 ["INT_ADD", "register:40f0:8", ["const:84bc20:8", "const:4:8"]]
- 0084bc20 ["CALL", null, ["callee:00c538e0:8"]]
+ 0087ebb8 ["INT_ADD", "register:40f0:8", ["const:87ebb8:8", "const:4:8"]]
+ 0087ebb8 ["CALL", null, ["callee:00c538e0:8"]]
- 0084bc20 bytes 9c2c0e94
+ 0087ebb8 bytes 4a530f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f81df844c4d4b2cecee4f9d60833c7"></a>

### [`0084bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md) → [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) FUN_0087ed0c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0084bea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bea0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) · 呼出先 5件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`0087ee38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 50.00% / 新版 43.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bd84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bd84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bda4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084bd84",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084bda4",
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
      "0087ed1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087ed3c",
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

- 旧版 [`0084bd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md#insn-0084bd84) · [`0084bda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md#insn-0084bda4) · [`0084bda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md#insn-0084bda8)
- 新版 [`0087ed40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md#insn-0087ed40)

~~~diff
- 0084bd84 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084bd84 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084bd84 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0084bd84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084bd84 bytes f44f06a9
- 0084bda4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084bda4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084bda4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084bda4 bytes a8831ff8
- 0084bda8 ["INT_ADD", "register:40f0:8", ["const:84bda8:8", "const:4:8"]]
- 0084bda8 ["CALL", null, ["callee:0087ee38:8"]]
+ 0087ed40 ["INT_ADD", "register:40f0:8", ["const:87ed40:8", "const:4:8"]]
+ 0087ed40 ["CALL", null, ["callee:0087ee38:8"]]
- 0084bda8 bytes 3e000094
+ 0087ed40 bytes 3e000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ce165716c419fda9f77e8ddd69393f3"></a>

### [`0084bea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bea0.md) → [`0087ee38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ee38.md) FUN_0087ee38

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084bd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bd74.md) · 呼出先 1件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 1件 [`0087ed0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087ed0c.md) · 呼出先 1件 [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.54% / 新版 81.54%

CFGの説明率　旧版 12.50% / 新版 13.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bf0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bf10"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084bf1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084bf24",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ],
    [
      "unmatched:0084bf78",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087ee88"
      ]
    ]
  ],
  "added": [
    [
      "0087eebc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c50"
      ]
    ],
    [
      "0087ef10",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087ee88"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084bf0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bea0.md#insn-0084bf0c) · [`0084bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bea0.md#insn-0084bf10) · [`0084bf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084bea0.md#insn-0084bf1c)

~~~diff
- 0084bf0c ["COPY", "tmp:0:8", ["register:4050:8"]]
- 0084bf0c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0084bf0c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0084bf0c ["COPY", "register:40d0:8", ["tmp:0:8"]]
- 0084bf0c bytes 5a01899a
- 0084bf10 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084bf10 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 0084bf10 ["COPY", "tmp:0:8", ["register:4058:8"]]
- 0084bf10 ["COPY", "register:40b0:8", ["tmp:0:8"]]
- 0084bf10 bytes 16018b9a
- 0084bf1c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 0084bf1c ["COPY", "tmp:1:8", ["register:40d0:8"]]
- 0084bf1c ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 0084bf1c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0084bf1c bytes 5733999a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-364c9fe36956403b86be43fde6e9f1ba"></a>

### [`0084c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md) → [`0087eff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087eff8.md) FUN_0087eff8

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084b738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084b/0084b738.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md)
- 新版 呼出元 1件 [`0087e6d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087e/0087e6d0.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a430`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a430.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 22.22% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c060"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c064"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084c060",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c064",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c088",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087f038"
      ]
    ]
  ],
  "added": [
    [
      "0087eff8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087effc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087f020",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0087f038"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md#insn-0084c060) · [`0084c064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md#insn-0084c064) · [`0084c088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c060.md#insn-0084c088)

~~~diff
- 0084c060 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084c060 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084c060 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 0084c060 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 0084c060 bytes fd7bbea9
- 0084c064 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084c064 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084c064 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 0084c064 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c064 bytes f44f01a9
- 0084c088 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 0084c088 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0084c088 bytes d40000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-acd30e96810b77095c4620af30982688"></a>

### [`0084c290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md) → [`0087f228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f228.md) FUN_0087f228

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 46.81% / 新版 46.81%

CFGの説明率　旧版 12.50% / 新版 7.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c294"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c298"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084c294",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c298",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c2a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0087f22c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "0087f230",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "0087f240",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084c294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md#insn-0084c294) · [`0084c298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md#insn-0084c298) · [`0084c2a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c290.md#insn-0084c2a8)

~~~diff
- 0084c294 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084c294 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084c294 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0084c294 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c294 bytes fd7b04a9
- 0084c298 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084c298 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084c298 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0084c298 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c298 bytes f44f05a9
- 0084c2a8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084c2a8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084c2a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084c2a8 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8270b4dfd2cfc5bd3d1747db4920a9aa"></a>

### [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) → [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) FUN_0087f328

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 55件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c120.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md)
- 新版 呼出元 0件  · 呼出先 55件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043ec20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043ec20.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.71% / 新版 60.71%

CFGの説明率　旧版 25.97% / 新版 19.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `call_target` 3件, `return_value_candidate` 1件, `store_condition` 1件, `store_destination` 1件, `store_value` 1件, `unresolved_branch_alignment` 14件, `unresolved_call_alignment` 72件, `unresolved_store_alignment` 51件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084c398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084c394",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c398",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084c39c",
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
      "0087f32c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "0087f330",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "0087f334",
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

- 旧版 [`0084c394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md#insn-0084c394) · [`0084c398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md#insn-0084c398) · [`0084c39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md#insn-0084c39c)

~~~diff
- 0084c394 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084c394 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084c394 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 0084c394 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c394 bytes fd7b18a9
- 0084c398 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 0084c398 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 0084c398 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 0084c398 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c398 bytes fc6719a9
- 0084c39c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0084c39c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0084c39c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 0084c39c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084c39c bytes f85f1aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3932742903c4e7d7efb5a7fc5398d931"></a>

### [`0084d1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md) → [`0088014c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md) FUN_0088014c

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) · 呼出先 9件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046fd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fd28.md) [`004709fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/004709fc.md)
- 新版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 9件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`00492bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492bc0.md) [`00493894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/00493894.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 60.00% / 新版 51.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00880184",
      "incomplete_value": true,
      "site": "00880184",
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
      "definition_site": "0084d1ec",
      "incomplete_value": true,
      "site": "0084d1ec",
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
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d274"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "0088020c"
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
      "00880180",
      "DATA",
      [
        "storage",
        "00397077",
        null,
        "qword"
      ]
    ],
    [
      "00880188",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "00880198",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ]
  ],
  "added": [
    [
      "00880180",
      "DATA",
      [
        "storage",
        "0039b1d7",
        null,
        "byte[11]"
      ]
    ],
    [
      "00880188",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00880198",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d1ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md#insn-0084d1ec) · [`0084d1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md#insn-0084d1f0) · [`0084d200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d1b4.md#insn-0084d200)
- 新版 [`00880184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-00880184) · [`00880188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-00880188) · [`00880198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/0088014c.md#insn-00880198)

~~~diff
- 0084d1ec ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3388:8"]]
- 0084d1ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
+ 00880184 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:3478:8"]]
+ 00880184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:8"]]
- 0084d1ec bytes 00c419fd
+ 00880184 bytes 003c1afd
- 0084d1f0 ["INT_ADD", "register:40f0:8", ["const:84d1f0:8", "const:4:8"]]
- 0084d1f0 ["CALL", null, ["ram:469e20:8"]]
+ 00880188 ["INT_ADD", "register:40f0:8", ["const:880188:8", "const:4:8"]]
+ 00880188 ["CALL", null, ["ram:48ccb8:8"]]
- 0084d1f0 bytes 0c73f097
+ 00880188 bytes cc32f097
- 0084d200 ["INT_ADD", "register:40f0:8", ["const:84d200:8", "const:4:8"]]
- 0084d200 ["CALL", null, ["ram:469e20:8"]]
+ 00880198 ["INT_ADD", "register:40f0:8", ["const:880198:8", "const:4:8"]]
+ 00880198 ["CALL", null, ["ram:48ccb8:8"]]
- 0084d200 bytes 0873f097
+ 00880198 bytes c832f097
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd56a6f5e94c7871227108c62bf3b273"></a>

### [`0084d3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d3e8.md) → [`00880380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md) FUN_00880380

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0088039c",
      "incomplete_value": true,
      "site": "008803a0",
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
      "definition_site": "0084d404",
      "incomplete_value": true,
      "site": "0084d408",
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
      "00880394",
      "READ",
      [
        "storage",
        "00c1aea8",
        null,
        "pointer"
      ]
    ],
    [
      "008803a0",
      "DATA",
      [
        "storage",
        "00be85d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00880394",
      "READ",
      [
        "storage",
        "00c9a898",
        null,
        "pointer"
      ]
    ],
    [
      "008803a0",
      "DATA",
      [
        "storage",
        "00c65198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d3e8.md#insn-0084d3f4) · [`0084d3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d3e8.md#insn-0084d3fc) · [`0084d418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d3e8.md#insn-0084d418)
- 新版 [`0088038c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-0088038c) · [`00880394`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-00880394) · [`008803b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880380.md#insn-008803b0)

~~~diff
- 0084d3f4 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 0088038c ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 0084d3f4 bytes 681e00b0
+ 0088038c bytes c82000d0
- 0084d3fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 0084d3fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00880394 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
+ 00880394 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0084d3fc bytes 085547f9
+ 00880394 bytes 084d44f9
- 0084d418 ["INT_ADD", "register:40f0:8", ["const:84d418:8", "const:4:8"]]
- 0084d418 ["CALL", null, ["callee:00c538e0:8"]]
+ 008803b0 ["INT_ADD", "register:40f0:8", ["const:8803b0:8", "const:4:8"]]
+ 008803b0 ["CALL", null, ["callee:00c538e0:8"]]
- 0084d418 bytes 9e260e94
+ 008803b0 bytes 4c4d0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ac17b83f472698ef91439d200292686"></a>

### [`0084d464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md) → [`008803fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/008803fc.md) FUN_008803fc

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 15件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041cc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041cc4c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`0045a0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0c0.md) [`0045a0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045a/0045a0e0.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f74c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f74c.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cf58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf58.md) [`0047cf78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cf78.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 37.88% / 新版 37.88%

CFGの説明率　旧版 5.00% / 新版 2.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 16件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d468"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d468"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d46c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084d468",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084d46c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084d470",
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
      "00880400",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00880404",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00880408",
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

- 旧版 [`0084d468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md#insn-0084d468) · [`0084d46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md#insn-0084d46c) · [`0084d470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d464.md#insn-0084d470)

~~~diff
- 0084d468 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084d468 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084d468 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0084d468 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084d468 bytes fd7b04a9
- 0084d46c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:50:8"]]
- 0084d46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 0084d46c bytes f52b00f9
- 0084d470 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084d470 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084d470 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 0084d470 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084d470 bytes f44f06a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-744bddcf750a4eb0d4cf36cd9af21c84"></a>

### [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md) → [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md) FUN_00880668

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 13件 [`00841924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841924.md) [`00851444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851444.md) [`008517f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008517f0.md) [`00852390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852390.md) [`0085274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md) · 呼出先 15件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042f000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`00574810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574810.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md)
- 新版 呼出元 13件 [`00873c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873c10.md) [`008843dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008843dc.md) [`00884788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884788.md) [`00885328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885328.md) [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) · 呼出先 15件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00451e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00451/00451e98.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`005976a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00597/005976a8.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 79.69% / 新版 79.69%

CFGの説明率　旧版 46.94% / 新版 41.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件, `unresolved_branch_alignment` 7件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d6d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d6d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084d6d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084d6d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084d6d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084d6dc",
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
      "0088066c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00880670",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00880674",
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

- 旧版 [`0084d6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md#insn-0084d6d4) · [`0084d6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md#insn-0084d6d8) · [`0084d6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md#insn-0084d6dc)

~~~diff
- 0084d6d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084d6d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084d6d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:140:8"]]
- 0084d6d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084d6d4 bytes fd7b14a9
- 0084d6d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:150:8"]]
- 0084d6d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0084d6d8 bytes fcab00f9
- 0084d6dc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 0084d6dc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 0084d6dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:160:8"]]
- 0084d6dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084d6dc bytes f85f16a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70b81caee263eda660cd0e7f37cd0f66"></a>

### [`0084dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dc14.md) → [`00880bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md) FUN_00880bac

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 72.73% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "0084dc60",
      "incomplete_value": false,
      "site": "0084dc64",
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
      "definition_site": "0084dc5c",
      "incomplete_value": true,
      "site": "0084dc64",
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
    "ordinal": 1,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`0084dc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dc14.md#insn-0084dc64) · [`0084dc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dc14.md#insn-0084dc50) · [`0084dc58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dc14.md#insn-0084dc58)
- 新版 [`00880bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880bfc) · [`00880be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880be8) · [`00880bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880bac.md#insn-00880bf0)

~~~diff
- 0084dc64 ["INT_ADD", "register:40f0:8", ["const:84dc64:8", "const:4:8"]]
- 0084dc64 ["CALL", null, ["callee:00c538e0:8"]]
+ 00880bfc ["INT_ADD", "register:40f0:8", ["const:880bfc:8", "const:4:8"]]
+ 00880bfc ["CALL", null, ["callee:00c538e0:8"]]
- 0084dc64 bytes 8b240e94
+ 00880bfc bytes 394b0f94
- 0084dc50 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084dc50 ["INT_ADD", "register:40f0:8", ["const:84dc50:8", "const:4:8"]]
- 0084dc50 ["CALLIND", null, ["register:0:8"]]
+ 00880be8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00880be8 ["INT_ADD", "register:40f0:8", ["const:880be8:8", "const:4:8"]]
+ 00880be8 ["CALLIND", null, ["register:0:8"]]
- 0084dc50 bytes 00013fd6
+ 00880be8 bytes 00013fd6
- 0084dc58 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
- 0084dc58 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00880bf0 ["INT_EQUAL", "tmp:0:1", ["register:4098:8", "const:0:8"]]
+ 00880bf0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 0084dc58 bytes b30000b4
+ 00880bf0 bytes b30000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e12528489c5f3f975ea5862f2f72e6dc"></a>

### [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) → [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) FUN_00880cb4

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00841a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00841/00841a9c.md) [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) [`00850afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md) · 呼出先 14件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073e07c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e07c.md)
- 新版 呼出元 16件 [`0047373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/0047373c.md) [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) [`00873d88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00873/00873d88.md) [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) · 呼出先 14件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764344.md) [`00768388`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768388.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 74.53% / 新版 74.53%

CFGの説明率　旧版 20.00% / 新版 17.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 8件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084dd20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084dd20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084dd24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084dd20",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084dd24",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084dd28",
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
      "00880cb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00880cbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00880cc0",
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

- 旧版 [`0084dd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md#insn-0084dd20) · [`0084dd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md#insn-0084dd24) · [`0084dd28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md#insn-0084dd28)

~~~diff
- 0084dd20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084dd20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084dd20 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 0084dd20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084dd20 bytes fd7b0ca9
- 0084dd24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:d0:8"]]
- 0084dd24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 0084dd24 bytes f76b00f9
- 0084dd28 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 0084dd28 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 0084dd28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 0084dd28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084dd28 bytes f6570ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6ea46eaaf30dd0ff2d041b9cb7dc201"></a>

### [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) → [`00881058`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881058.md) FUN_00881058

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`008629ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00862/008629ec.md) · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0053d984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md) [`008531c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/008531c8.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`0089598c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00895/0089598c.md) · 呼出先 9件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`0056081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00560/0056081c.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md) [`00886160`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886160.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 88.97% / 新版 88.97%

CFGの説明率　旧版 54.17% / 新版 55.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00881128",
      "incomplete_value": false,
      "site": "00881128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084e190",
      "incomplete_value": false,
      "site": "0084e190",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e1c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "0088115c"
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
      "00881128",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0084e1c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881174"
      ]
    ],
    [
      "008811a8",
      "READ",
      [
        "storage",
        "00c02c78",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00881128",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ],
    [
      "0088115c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00881174"
      ]
    ],
    [
      "008811a8",
      "READ",
      [
        "storage",
        "00c80a50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md#insn-0084e14c) · [`0084e1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md#insn-0084e1c4) · [`0084e244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md#insn-0084e244)

~~~diff
- 0084e14c ["COPY", "register:0:8", ["register:4040:8"]]
- 0084e14c ["INT_ADD", "register:40f0:8", ["const:84e14c:8", "const:4:8"]]
- 0084e14c ["CALLIND", null, ["register:0:8"]]
- 0084e14c bytes 00013fd6
- 0084e1c4 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
- 0084e1c4 bytes c0000054
- 0084e244 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084e244 ["INT_ADD", "register:40f0:8", ["const:84e244:8", "const:4:8"]]
- 0084e244 ["CALLIND", null, ["register:0:8"]]
- 0084e244 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f69c3bccbbc05cc73f6cda617f8f47fb"></a>

### [`0084e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e3d8.md) → [`00881370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881370.md) FUN_00881370

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.76% / 新版 53.76%

CFGの説明率　旧版 17.65% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e3dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e3e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084e3dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084e3e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084e3f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00881374",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00881378",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00881388",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e3d8.md#insn-0084e3dc) · [`0084e3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e3d8.md#insn-0084e3e0) · [`0084e3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e3d8.md#insn-0084e3f0)

~~~diff
- 0084e3dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084e3dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084e3dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 0084e3dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084e3dc bytes fd7b04a9
- 0084e3e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084e3e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084e3e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 0084e3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084e3e0 bytes f44f05a9
- 0084e3f0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084e3f0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084e3f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084e3f0 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e20526d3804572f963ef6387859b31f9"></a>

### [`0084e5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e5ac.md) → [`00881544`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881544.md) FUN_00881544

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`00461338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00461/00461338.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004841d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00484/004841d0.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 61.29% / 新版 61.29%

CFGの説明率　旧版 47.06% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e5c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e5d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e5d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084e5c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084e5c8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "unmatched:0084e5d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x35]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0088155c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ],
    [
      "00881560",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008514b8"
      ]
    ],
    [
      "0088156c",
      "WRITE",
      [
        "storage",
        "Stack[-0x35]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e5ac.md#insn-0084e5c4) · [`0084e5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e5ac.md#insn-0084e5c8) · [`0084e5d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e5ac.md#insn-0084e5d4)

~~~diff
- 0084e5c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084e5c4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084e5c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084e5c4 bytes a8831ff8
- 0084e5c8 ["INT_ADD", "register:40f0:8", ["const:84e5c8:8", "const:4:8"]]
- 0084e5c8 ["CALL", null, ["callee:008514b8:8"]]
- 0084e5c8 bytes ee43ff97
- 0084e5d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0084e5d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0084e5d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 0084e5d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0084e5d4 bytes ffaf0039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32faf1407e1760a860587e05cdf388a1"></a>

### [`0084e780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md) → [`00881718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881718.md) FUN_00881718

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 28件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`0043344c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/0043344c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043e90c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043e/0043e90c.md) [`0043f3f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043f/0043f3f8.md) [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`004543cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00454/004543cc.md) [`004562e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00456/004562e4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.33% / 新版 80.33%

CFGの説明率　旧版 65.28% / 新版 47.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 12件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e7bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e7e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084e7e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084e7bc",
      "DATA",
      [
        "storage",
        "00397078",
        null,
        "qword"
      ]
    ],
    [
      "unmatched:0084e7c0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "unmatched:0084e7dc",
      "READ",
      [
        "storage",
        "00291f08",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00881754",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881758",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00881774",
      "READ",
      [
        "storage",
        "002a1500",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084e7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md#insn-0084e7bc) · [`0084e7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md#insn-0084e7e0) · [`0084e7e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e780.md#insn-0084e7e8)

~~~diff
- 0084e7bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 0084e7bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0084e7bc ["COPY", "tmp:2:8", ["register:4040:8"]]
- 0084e7bc ["COPY", "tmp:3:8", ["tmp:2:8"]]
- 0084e7bc bytes 1f682838
- 0084e7e0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0084e7e0 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffc0:8"]]
- 0084e7e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0084e7e0 bytes a8031c38
- 0084e7e8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 0084e7e8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "const:9:8"]]
- 0084e7e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 0084e7e8 bytes 88920078
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f464ee2c55dd876a0a507d51ddc78aef"></a>

### [`0084eca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eca4.md) → [`00881c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md) FUN_00881c3c

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`0046b908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046b/0046b908.md) [`0046f9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046f9d4.md) [`0046fe2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fe2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048e7a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048e/0048e7a0.md) [`0049286c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/0049286c.md) [`00492cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492cc4.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00881c78",
      "incomplete_value": true,
      "site": "00881c8c",
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
                "const:487:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084ece0",
      "incomplete_value": true,
      "site": "0084ecf4",
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
                "const:d56:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00881c68",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0084ecd0",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "site": "00881ccc",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "0084ed34",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "00881c64",
      "DATA",
      [
        "storage",
        "00397078",
        null,
        "qword"
      ]
    ],
    [
      "00881c68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "00881c78",
      "READ",
      [
        "storage",
        "00292d56",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00881c64",
      "DATA",
      [
        "storage",
        "0039b1d8",
        "fde_0039b1d8",
        "dword"
      ]
    ],
    [
      "00881c68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00881c78",
      "READ",
      [
        "storage",
        "002a2487",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084ecd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eca4.md#insn-0084ecd0) · [`0084ed34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eca4.md#insn-0084ed34) · [`0084ecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084eca4.md#insn-0084ecc0)
- 新版 [`00881c68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881c68) · [`00881ccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881ccc) · [`00881c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00881/00881c3c.md#insn-00881c58)

~~~diff
- 0084ecd0 ["INT_ADD", "register:40f0:8", ["const:84ecd0:8", "const:4:8"]]
- 0084ecd0 ["CALL", null, ["ram:469e20:8"]]
+ 00881c68 ["INT_ADD", "register:40f0:8", ["const:881c68:8", "const:4:8"]]
+ 00881c68 ["CALL", null, ["ram:48ccb8:8"]]
- 0084ecd0 bytes 546cf097
+ 00881c68 bytes 142cf097
- 0084ed34 ["INT_ADD", "register:40f0:8", ["const:84ed34:8", "const:4:8"]]
- 0084ed34 ["CALL", null, ["ram:469e20:8"]]
+ 00881ccc ["INT_ADD", "register:40f0:8", ["const:881ccc:8", "const:4:8"]]
+ 00881ccc ["CALL", null, ["ram:48ccb8:8"]]
- 0084ed34 bytes 3b6cf097
+ 00881ccc bytes fb2bf097
- 0084ecc0 ["INT_ADD", "register:40f0:8", ["const:84ecc0:8", "const:4:8"]]
- 0084ecc0 ["CALL", null, ["callee:008514b8:8"]]
+ 00881c58 ["INT_ADD", "register:40f0:8", ["const:881c58:8", "const:4:8"]]
+ 00881c58 ["CALL", null, ["callee:008514b8:8"]]
- 0084ecc0 bytes 3042ff97
+ 00881c58 bytes 183eff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a79eb74048a527d12b0bc1765e569dc"></a>

### [`0084f198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f198.md) → [`00882130`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md) FUN_00882130

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0083b350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0083b/0083b350.md) · 呼出先 5件 [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`0086d63c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0086d/0086d63c.md) · 呼出先 5件 [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00a1a508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a1a/00a1a508.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 75.93% / 新版 75.93%

CFGの説明率　旧版 31.25% / 新版 35.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084f258"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008821f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0084f204"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00882170",
      "DATA",
      [
        "storage",
        "003c34a8",
        "fde_003c34a8",
        "dword"
      ]
    ],
    [
      "00882190",
      "DATA",
      [
        "storage",
        "003c34a8",
        "fde_003c34a8",
        "dword"
      ]
    ],
    [
      "008821a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ]
  ],
  "added": [
    [
      "00882170",
      "DATA",
      [
        "storage",
        "003c7788",
        "fde_003c7788",
        "dword"
      ]
    ],
    [
      "00882190",
      "DATA",
      [
        "storage",
        "003c7788",
        "fde_003c7788",
        "dword"
      ]
    ],
    [
      "008821a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f198.md#insn-0084f204) · [`0084f210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f198.md#insn-0084f210) · [`0084f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f198.md#insn-0084f258)
- 新版 [`008821a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882130.md#insn-008821a8)

~~~diff
- 0084f204 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084f204 ["INT_ADD", "register:40f0:8", ["const:84f204:8", "const:4:8"]]
- 0084f204 ["CALLIND", null, ["register:0:8"]]
- 0084f204 bytes 00013fd6
- 0084f210 ["INT_ADD", "register:40f0:8", ["const:84f210:8", "const:4:8"]]
- 0084f210 ["CALL", null, ["ram:73ab94:8"]]
+ 008821a8 ["INT_ADD", "register:40f0:8", ["const:8821a8:8", "const:4:8"]]
+ 008821a8 ["CALL", null, ["ram:764ea0:8"]]
- 0084f210 bytes 61aefb97
+ 008821a8 bytes 3e8bfb97
- 0084f258 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 0084f258 ["CBRANCH", null, ["local:b13:8", "tmp:0:1"]]
- 0084f258 bytes a1000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eed2cfa4519a330e2ebf4f9895fe5714"></a>

### [`0084f468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f468.md) → [`00882400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882400.md) FUN_00882400

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088240c",
      "incomplete_value": false,
      "site": "00882418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f474",
      "incomplete_value": false,
      "site": "0084f480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00882418",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882418",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f468.md#insn-0084f470) · [`0084f474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f468.md#insn-0084f474)
- 新版 [`00882408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882400.md#insn-00882408) · [`0088240c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882400.md#insn-0088240c)

~~~diff
- 0084f470 ["COPY", "register:4050:8", ["const:c02000:8"]]
+ 00882408 ["COPY", "register:4050:8", ["const:c80000:8"]]
- 0084f470 bytes 8a1d00f0
+ 00882408 bytes ea1f00d0
- 0084f474 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0084f474 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0084f474 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0084f474 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0088240c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0088240c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0088240c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0088240c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0084f474 bytes 4a011591
+ 0088240c bytes 4a610c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ff7647c6313225852274ea40bb11638"></a>

### [`0084f4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f4ac.md) → [`00882444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md) FUN_00882444

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0088245c",
      "incomplete_value": false,
      "site": "00882468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f4c4",
      "incomplete_value": false,
      "site": "0084f4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "00882468",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882468",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f4ac.md#insn-0084f4c0) · [`0084f4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f4ac.md#insn-0084f4c4) · [`0084f4f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f4ac.md#insn-0084f4f4)
- 新版 [`00882458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md#insn-00882458) · [`0088245c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md#insn-0088245c) · [`0088248c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882444.md#insn-0088248c)

~~~diff
- 0084f4c0 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00882458 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0084f4c0 bytes 881d00f0
+ 00882458 bytes e81f00d0
- 0084f4c4 ["COPY", "tmp:0:8", ["const:540:8"]]
- 0084f4c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088245c ["COPY", "tmp:0:8", ["const:318:8"]]
+ 0088245c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088245c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088245c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f4c4 bytes 08011591
+ 0088245c bytes 08610c91
- 0084f4f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 0084f4f4 ["INT_ADD", "register:40f0:8", ["const:84f4f4:8", "const:4:8"]]
- 0084f4f4 ["CALLIND", null, ["register:0:8"]]
+ 0088248c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088248c ["INT_ADD", "register:40f0:8", ["const:88248c:8", "const:4:8"]]
+ 0088248c ["CALLIND", null, ["register:0:8"]]
- 0084f4f4 bytes 00013fd6
+ 0088248c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1de9cef2c7a80ac1041a186cd8053df9"></a>

### [`0084f590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f590.md) → [`00882528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882528.md) FUN_00882528

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084f5ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00882544"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "0084f5b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084f5ac",
      "DATA",
      [
        "storage",
        "00c02540",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0084f5b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00882570"
      ]
    ],
    [
      "unmatched:0084f5cc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00882544",
      "DATA",
      [
        "storage",
        "00c80318",
        null,
        "undefined *"
      ]
    ],
    [
      "00882548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00882570"
      ]
    ],
    [
      "00882564",
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

- 旧版 [`0084f5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f590.md#insn-0084f5ac) · [`0084f5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f590.md#insn-0084f5b0) · [`0084f5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f590.md#insn-0084f5cc)

~~~diff
- 0084f5ac ["COPY", "tmp:0:8", ["register:4048:8"]]
- 0084f5ac ["COPY", "tmp:1:8", ["register:4008:8"]]
- 0084f5ac ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 0084f5ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084f5ac bytes 290401f8
- 0084f5b0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 0084f5b0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 0084f5b0 bytes 480100b4
- 0084f5cc ["COPY", "register:0:8", ["register:4048:8"]]
- 0084f5cc ["INT_ADD", "register:40f0:8", ["const:84f5cc:8", "const:4:8"]]
- 0084f5cc ["CALLIND", null, ["register:0:8"]]
- 0084f5cc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17a9802ad87595833d3b8f323c337b86"></a>

### [`0084f6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f6f4.md) → [`0088268c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/0088268c.md) FUN_0088268c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00882690",
      "incomplete_value": false,
      "site": "00882694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f6f8",
      "incomplete_value": false,
      "site": "0084f6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:5c0:8"
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
      "00882694",
      "DATA",
      [
        "storage",
        "00c025c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882694",
      "DATA",
      [
        "storage",
        "00c80398",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f6f4.md#insn-0084f6f4) · [`0084f6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f6f4.md#insn-0084f6f8)
- 新版 [`0088268c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/0088268c.md#insn-0088268c) · [`00882690`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/0088268c.md#insn-00882690)

~~~diff
- 0084f6f4 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0088268c ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0084f6f4 bytes 881d00f0
+ 0088268c bytes e81f00d0
- 0084f6f8 ["COPY", "tmp:0:8", ["const:5c0:8"]]
- 0084f6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882690 ["COPY", "tmp:0:8", ["const:398:8"]]
+ 00882690 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882690 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882690 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f6f8 bytes 08011791
+ 00882690 bytes 08610e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71c37ebf99ff41234a5cb84c336563eb"></a>

### [`0084f98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f98c.md) → [`00882924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md) FUN_00882924

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00882938",
      "incomplete_value": false,
      "site": "0088293c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f9a0",
      "incomplete_value": false,
      "site": "0084f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "0088293c",
      "DATA",
      [
        "storage",
        "00c02640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088293c",
      "DATA",
      [
        "storage",
        "00c80418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f98c.md#insn-0084f998) · [`0084f99c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f98c.md#insn-0084f99c) · [`0084f9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f98c.md#insn-0084f9a0)
- 新版 [`00882930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md#insn-00882930) · [`00882934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md#insn-00882934) · [`00882938`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882924.md#insn-00882938)

~~~diff
- 0084f998 ["INT_ADD", "register:40f0:8", ["const:84f998:8", "const:4:8"]]
- 0084f998 ["CALL", null, ["callee:00c57a90:8"]]
+ 00882930 ["INT_ADD", "register:40f0:8", ["const:882930:8", "const:4:8"]]
+ 00882930 ["CALL", null, ["callee:00c57a90:8"]]
- 0084f998 bytes aa2d0e94
+ 00882930 bytes 58540f94
- 0084f99c ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00882934 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0084f99c bytes 881d00f0
+ 00882934 bytes e81f00d0
- 0084f9a0 ["COPY", "tmp:0:8", ["const:640:8"]]
- 0084f9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00882938 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 00882938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00882938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00882938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f9a0 bytes 08011991
+ 00882938 bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6960a76f7f7d9a16676d04e22dd410db"></a>

### [`0084f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f9b0.md) → [`00882948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882948.md) FUN_00882948

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0088294c",
      "incomplete_value": false,
      "site": "00882950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084f9b4",
      "incomplete_value": false,
      "site": "0084f9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "00882950",
      "DATA",
      [
        "storage",
        "00c02640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882950",
      "DATA",
      [
        "storage",
        "00c80418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084f9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f9b0.md#insn-0084f9b0) · [`0084f9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f9b0.md#insn-0084f9b4)
- 新版 [`00882948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882948.md#insn-00882948) · [`0088294c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882948.md#insn-0088294c)

~~~diff
- 0084f9b0 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00882948 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 0084f9b0 bytes 881d00f0
+ 00882948 bytes e81f00d0
- 0084f9b4 ["COPY", "tmp:0:8", ["const:640:8"]]
- 0084f9b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088294c ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0088294c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088294c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088294c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0084f9b4 bytes 08011991
+ 0088294c bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25076221c468b50eaf48cb85bd2e4bef"></a>

### [`0084fc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc44.md) → [`00882bdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bdc.md) FUN_00882bdc

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00882be4",
      "incomplete_value": false,
      "site": "00882be8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fc4c",
      "incomplete_value": false,
      "site": "0084fc50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "00882be8",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882be8",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc44.md#insn-0084fc48) · [`0084fc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc44.md#insn-0084fc4c)
- 新版 [`00882be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bdc.md#insn-00882be0) · [`00882be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bdc.md#insn-00882be4)

~~~diff
- 0084fc48 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 00882be0 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0084fc48 bytes 891d00f0
+ 00882be0 bytes e91f00d0
- 0084fc4c ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 0084fc4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882be4 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00882be4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882be4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882be4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084fc4c bytes 29011b91
+ 00882be4 bytes 29611291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-044f6a77904c0429e839f552dec372d6"></a>

### [`0084fc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc64.md) → [`00882bfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md) FUN_00882bfc

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00882c04",
      "incomplete_value": false,
      "site": "00882c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fc6c",
      "incomplete_value": false,
      "site": "0084fc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "00882c08",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882c08",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fc68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc64.md#insn-0084fc68) · [`0084fc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc64.md#insn-0084fc6c) · [`0084fc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fc64.md#insn-0084fc90)
- 新版 [`00882c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md#insn-00882c00) · [`00882c04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md#insn-00882c04) · [`00882c28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882bfc.md#insn-00882c28)

~~~diff
- 0084fc68 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 00882c00 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0084fc68 bytes 891d00f0
+ 00882c00 bytes e91f00d0
- 0084fc6c ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 0084fc6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00882c04 ["COPY", "tmp:0:8", ["const:498:8"]]
+ 00882c04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00882c04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0084fc6c bytes 29011b91
+ 00882c04 bytes 29611291
- 0084fc90 ["INT_ADD", "register:40f0:8", ["const:84fc90:8", "const:4:8"]]
- 0084fc90 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00882c28 ["INT_ADD", "register:40f0:8", ["const:882c28:8", "const:4:8"]]
+ 00882c28 ["CALL", null, ["callee:00c57ab0:8"]]
- 0084fc90 bytes f42c0e94
+ 00882c28 bytes a2530f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a43938040d2e6b7d6ff833153896a128"></a>

### [`0084fca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fca4.md) → [`00882c3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md) FUN_00882c3c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00882c68",
      "incomplete_value": false,
      "site": "00882c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fcd0",
      "incomplete_value": false,
      "site": "0084fcd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0084fd00"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00882c98"
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
      "00882c68",
      "DATA",
      [
        "storage",
        "00c026c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00882c68",
      "DATA",
      [
        "storage",
        "00c80498",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084fd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fca4.md#insn-0084fd00) · [`0084fcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fca4.md#insn-0084fcb8)
- 新版 [`00882c98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md#insn-00882c98) · [`00882c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882c3c.md#insn-00882c50)

~~~diff
- 0084fd00 ["COPY", "register:0:8", ["register:40f0:8"]]
- 0084fd00 ["RETURN", null, ["register:0:8"]]
- 0084fd00 bytes c0035fd6
+ 00882c98 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00882c98 ["RETURN", null, ["register:0:8"]]
+ 00882c98 bytes c0035fd6
- 0084fcb8 ["INT_ADD", "register:40f0:8", ["const:84fcb8:8", "const:4:8"]]
- 0084fcb8 ["CALL", null, ["callee:00c57a90:8"]]
+ 00882c50 ["INT_ADD", "register:40f0:8", ["const:882c50:8", "const:4:8"]]
+ 00882c50 ["CALL", null, ["callee:00c57a90:8"]]
- 0084fcb8 bytes e22c0e94
+ 00882c50 bytes 90530f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73306b36045477a99def939b3a694eaa"></a>

### [`0084fd68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fd68.md) → [`00882d00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d00.md) FUN_00882d00

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0084c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c390.md) · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0087f328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0087f/0087f328.md) · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00882d1c",
      "incomplete_value": true,
      "site": "00882d20",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0084fd84",
      "incomplete_value": true,
      "site": "0084fd88",
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


#### 変更候補の命令位置

- 旧版 [`0084fd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fd68.md#insn-0084fd88) · [`0084fd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fd68.md#insn-0084fd6c) · [`0084fd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084fd68.md#insn-0084fd84)
- 新版 [`00882d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d00.md#insn-00882d20) · [`00882d04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882d00.md#insn-00882d04)

~~~diff
- 0084fd88 ["INT_ADD", "register:40f0:8", ["const:84fd88:8", "const:4:8"]]
- 0084fd88 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00882d20 ["INT_ADD", "register:40f0:8", ["const:882d20:8", "const:4:8"]]
+ 00882d20 ["CALL", null, ["callee:00c57ab0:8"]]
- 0084fd88 bytes b62c0e94
+ 00882d20 bytes 64530f94
- 0084fd6c ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 0084fd6c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0084fd6c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0084fd6c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00882d04 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00882d04 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00882d04 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00882d04 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0084fd6c bytes 68010036
+ 00882d04 bytes 68010036
- 0084fd84 ["COPY", "register:4000:8", ["register:4040:8"]]
- 0084fd84 bytes e00308aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1461e06cc78a848391d32b0867a51b6a"></a>

### [`0084feac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084feac.md) → [`00882e44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00882/00882e44.md) FUN_00882e44

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470050.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00492ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00492/00492ee8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 85.44% / 新版 85.44%

CFGの説明率　旧版 53.45% / 新版 93.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084feb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084feb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0084feb4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0084feb0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084feb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:0084fec4",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00882e48",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00882e4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00882e5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x28]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0084feb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084feac.md#insn-0084feb0) · [`0084feb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084feac.md#insn-0084feb4) · [`0084fec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084feac.md#insn-0084fec4)

~~~diff
- 0084feb0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 0084feb0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 0084feb0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 0084feb0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084feb0 bytes fd7b0aa9
- 0084feb4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 0084feb4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 0084feb4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 0084feb4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 0084feb4 bytes f44f0ba9
- 0084fec4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 0084fec4 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 0084fec4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 0084fec4 bytes a8831ff8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a43b4762d1c6f37eefd2502d7ef5427e"></a>

### [`00850128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850128.md) → [`008830c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md) FUN_008830c0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008830e0",
      "incomplete_value": false,
      "site": "008830e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850148",
      "incomplete_value": false,
      "site": "0085014c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:7c0:8"
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
      "008830e4",
      "DATA",
      [
        "storage",
        "00c027c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008830e4",
      "DATA",
      [
        "storage",
        "00c80598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085013c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850128.md#insn-0085013c) · [`00850144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850128.md#insn-00850144) · [`00850148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850128.md#insn-00850148)
- 新版 [`008830d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md#insn-008830d4) · [`008830dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md#insn-008830dc) · [`008830e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830c0.md#insn-008830e0)

~~~diff
- 0085013c ["INT_ADD", "register:40f0:8", ["const:85013c:8", "const:4:8"]]
- 0085013c ["CALL", null, ["callee:00c57a90:8"]]
+ 008830d4 ["INT_ADD", "register:40f0:8", ["const:8830d4:8", "const:4:8"]]
+ 008830d4 ["CALL", null, ["callee:00c57a90:8"]]
- 0085013c bytes c12b0e94
+ 008830d4 bytes 6f520f94
- 00850144 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008830dc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00850144 bytes 881d00d0
+ 008830dc bytes e81f00b0
- 00850148 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00850148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008830e0 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 008830e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008830e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008830e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850148 bytes 08011f91
+ 008830e0 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0d2c77d272c0cdbfee2138e210cac70"></a>

### [`00850160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850160.md) → [`008830f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830f8.md) FUN_008830f8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883100",
      "incomplete_value": false,
      "site": "00883104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:598:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850168",
      "incomplete_value": false,
      "site": "0085016c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
      "00883104",
      "DATA",
      [
        "storage",
        "00c027c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883104",
      "DATA",
      [
        "storage",
        "00c80598",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850160.md#insn-00850164) · [`00850168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850160.md#insn-00850168)
- 新版 [`008830fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830f8.md#insn-008830fc) · [`00883100`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008830f8.md#insn-00883100)

~~~diff
- 00850164 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 008830fc ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00850164 bytes 891d00d0
+ 008830fc bytes e91f00b0
- 00850168 ["COPY", "tmp:0:8", ["const:7c0:8"]]
- 00850168 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00850168 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00850168 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00883100 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00883100 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00883100 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00883100 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00850168 bytes 29011f91
+ 00883100 bytes 29611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a5831f0cb5d27f77f4cd4678ead3acf"></a>

### [`00850180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md) → [`00883118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md) FUN_00883118

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 12件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fff8.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00470404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00470/00470404.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00442af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/00442af8.md) [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0049329c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00493/0049329c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.24% / 新版 87.24%

CFGの説明率　旧版 67.69% / 新版 59.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883178",
      "incomplete_value": true,
      "site": "00883178",
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
                "const:4f6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008501e0",
      "incomplete_value": true,
      "site": "008501e0",
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
                "const:efe:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00883180",
      "incomplete_value": true,
      "site": "00883180",
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
                "const:f82:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008501e8",
      "incomplete_value": true,
      "site": "008501e8",
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
                "const:29f000:8"
              ],
              [
                "leaf",
                "const:b64:8"
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
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850314"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0088316c",
      "READ",
      [
        "storage",
        "00291efe",
        null,
        "string"
      ]
    ],
    [
      "00883170",
      "READ",
      [
        "storage",
        "0029fb64",
        null,
        "string"
      ]
    ],
    [
      "00883284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008502f8"
      ]
    ]
  ],
  "added": [
    [
      "0088316c",
      "READ",
      [
        "storage",
        "002a14f6",
        null,
        "string"
      ]
    ],
    [
      "00883170",
      "READ",
      [
        "storage",
        "002aff82",
        null,
        "string"
      ]
    ],
    [
      "00883284",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883290"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008502a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md#insn-008502a8) · [`008502f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md#insn-008502f8) · [`00850314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850180.md#insn-00850314)
- 新版 [`00883240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883118.md#insn-00883240)

~~~diff
- 008502a8 ["INT_ADD", "register:40f0:8", ["const:8502a8:8", "const:4:8"]]
- 008502a8 ["CALL", null, ["callee:005dbcd4:8"]]
+ 00883240 ["INT_ADD", "register:40f0:8", ["const:883240:8", "const:4:8"]]
+ 00883240 ["CALL", null, ["callee:005dbcd4:8"]]
- 008502a8 bytes 579bf597
+ 00883240 bytes a562f597
- 008502f8 ["INT_ADD", "register:40f0:8", ["const:8502f8:8", "const:4:8"]]
- 008502f8 ["CALL", null, ["ram:469e20:8"]]
- 008502f8 bytes ca66f097
- 00850314 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00850314 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:80:8"]]
- 00850314 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00850314 bytes e8030239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3112b3b46915aaff6f29220c16f6d09"></a>

### [`00850640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850640.md) → [`008835d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md) FUN_008835d8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "008835ec",
      "incomplete_value": false,
      "site": "008835f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850654",
      "incomplete_value": false,
      "site": "00850658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:830:8"
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
      "008835f0",
      "DATA",
      [
        "storage",
        "00c02830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008835f0",
      "DATA",
      [
        "storage",
        "00c80608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085064c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850640.md#insn-0085064c) · [`00850650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850640.md#insn-00850650) · [`00850654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850640.md#insn-00850654)
- 新版 [`008835e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md#insn-008835e4) · [`008835e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md#insn-008835e8) · [`008835ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835d8.md#insn-008835ec)

~~~diff
- 0085064c ["INT_ADD", "register:40f0:8", ["const:85064c:8", "const:4:8"]]
- 0085064c ["CALL", null, ["callee:00c57a90:8"]]
+ 008835e4 ["INT_ADD", "register:40f0:8", ["const:8835e4:8", "const:4:8"]]
+ 008835e4 ["CALL", null, ["callee:00c57a90:8"]]
- 0085064c bytes 7d2a0e94
+ 008835e4 bytes 2b510f94
- 00850650 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008835e8 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00850650 bytes 881d00d0
+ 008835e8 bytes e81f00b0
- 00850654 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00850654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008835ec ["COPY", "tmp:0:8", ["const:608:8"]]
+ 008835ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008835ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008835ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850654 bytes 08c12091
+ 008835ec bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e630b9e51f5e3706ec35444962ed2e7"></a>

### [`00850664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850664.md) → [`008835fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835fc.md) FUN_008835fc

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00883600",
      "incomplete_value": false,
      "site": "00883604",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:608:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850668",
      "incomplete_value": false,
      "site": "0085066c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
      "00883604",
      "DATA",
      [
        "storage",
        "00c02830",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883604",
      "DATA",
      [
        "storage",
        "00c80608",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850664.md#insn-00850664) · [`00850668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850664.md#insn-00850668)
- 新版 [`008835fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835fc.md#insn-008835fc) · [`00883600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008835fc.md#insn-00883600)

~~~diff
- 00850664 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008835fc ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00850664 bytes 881d00d0
+ 008835fc bytes e81f00b0
- 00850668 ["COPY", "tmp:0:8", ["const:830:8"]]
- 00850668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00883600 ["COPY", "tmp:0:8", ["const:608:8"]]
+ 00883600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00883600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00883600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850668 bytes 08c12091
+ 00883600 bytes 08211891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8476d5db9bd97cb221b0922bcb6c8330"></a>

### [`0085067c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085067c.md) → [`00883614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md) FUN_00883614

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ad88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046ad88.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0048ccb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ccb8.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`0048dc20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048d/0048dc20.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00883658",
      "incomplete_value": true,
      "site": "00883658",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:e12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008506c0",
      "incomplete_value": true,
      "site": "008506c0",
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
                "const:f2f:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00883630",
      "value": [
        "leaf",
        "ram:48ccb8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00850698",
      "value": [
        "leaf",
        "ram:469e20:8"
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
      "00883630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00469e20"
      ]
    ],
    [
      "00883644",
      "READ",
      [
        "storage",
        "00299f2f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00883630",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0048ccb8"
      ]
    ],
    [
      "00883644",
      "READ",
      [
        "storage",
        "002a9e12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085067c.md#insn-00850698) · [`008506a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085067c.md#insn-008506a0) · [`008506a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085067c.md#insn-008506a4)
- 新版 [`00883630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-00883630) · [`00883638`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-00883638) · [`0088363c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883614.md#insn-0088363c)

~~~diff
- 00850698 ["INT_ADD", "register:40f0:8", ["const:850698:8", "const:4:8"]]
- 00850698 ["CALL", null, ["ram:469e20:8"]]
+ 00883630 ["INT_ADD", "register:40f0:8", ["const:883630:8", "const:4:8"]]
+ 00883630 ["CALL", null, ["ram:48ccb8:8"]]
- 00850698 bytes e265f097
+ 00883630 bytes a225f097
- 008506a0 ["COPY", "register:4048:8", ["const:299000:8"]]
+ 00883638 ["COPY", "register:4048:8", ["const:2a9000:8"]]
- 008506a0 bytes 49d2ffb0
+ 00883638 bytes 29d1ffd0
- 008506a4 ["COPY", "tmp:0:8", ["const:f2f:8"]]
- 008506a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008506a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008506a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0088363c ["COPY", "tmp:0:8", ["const:e12:8"]]
+ 0088363c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0088363c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0088363c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008506a4 bytes 29bd3c91
+ 0088363c bytes 29493891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49b9ad85fdbeda9641a46618efb06b37"></a>

### [`0085078c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085078c.md) → [`00883724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md) FUN_00883724

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0088373c",
      "incomplete_value": false,
      "site": "00883748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008507a4",
      "incomplete_value": false,
      "site": "008507b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
      "00883748",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00883748",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008507a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085078c.md#insn-008507a0) · [`008507a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085078c.md#insn-008507a4) · [`008507d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085078c.md#insn-008507d4)
- 新版 [`00883738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-00883738) · [`0088373c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-0088373c) · [`0088376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883724.md#insn-0088376c)

~~~diff
- 008507a0 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00883738 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008507a0 bytes 881d00d0
+ 00883738 bytes e81f00b0
- 008507a4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 008507a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008507a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008507a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0088373c ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0088373c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0088373c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0088373c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008507a4 bytes 08012391
+ 0088373c bytes 08611a91
- 008507d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 008507d4 ["INT_ADD", "register:40f0:8", ["const:8507d4:8", "const:4:8"]]
- 008507d4 ["CALLIND", null, ["register:0:8"]]
+ 0088376c ["COPY", "register:0:8", ["register:4040:8"]]
+ 0088376c ["INT_ADD", "register:40f0:8", ["const:88376c:8", "const:4:8"]]
+ 0088376c ["CALLIND", null, ["register:0:8"]]
- 008507d4 bytes 00013fd6
+ 0088376c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d422ec04f7f714498d74aef8060559e2"></a>

### [`0085081c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085081c.md) → [`008837b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md) FUN_008837b4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008837cc",
      "incomplete_value": false,
      "site": "008837d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00850834",
      "incomplete_value": false,
      "site": "00850840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:8c0:8"
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
    "new": null,
    "old": {
      "definition_site": "00850890",
      "incomplete_value": true,
      "site": "00850894",
      "value": [
        "live",
        "register:40a0:8"
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
      "008837d8",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008837d8",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085081c.md#insn-00850894) · [`00850830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085081c.md#insn-00850830) · [`00850834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/0085081c.md#insn-00850834)
- 新版 [`0088382c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-0088382c) · [`008837c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-008837c8) · [`008837cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008837b4.md#insn-008837cc)

~~~diff
- 00850894 ["INT_ADD", "register:40f0:8", ["const:850894:8", "const:4:8"]]
- 00850894 ["CALL", null, ["callee:00c57a80:8"]]
+ 0088382c ["INT_ADD", "register:40f0:8", ["const:88382c:8", "const:4:8"]]
+ 0088382c ["CALL", null, ["callee:00c57a80:8"]]
- 00850894 bytes e7290e94
+ 0088382c bytes 95500f94
- 00850830 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008837c8 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00850830 bytes 881d00d0
+ 008837c8 bytes e81f00b0
- 00850834 ["COPY", "tmp:0:8", ["const:8c0:8"]]
- 00850834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00850834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00850834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008837cc ["COPY", "tmp:0:8", ["const:698:8"]]
+ 008837cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008837cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008837cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00850834 bytes 08012391
+ 008837cc bytes 08611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644b0a2fc96802fb64320ce7146e844b"></a>

### [`008508a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/008508a8.md) → [`00883840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883840.md) FUN_00883840

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 50.00% / 新版 38.46%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008508d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008508d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008508dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008508d4",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008508e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883888"
      ]
    ],
    [
      "unmatched:00850900",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008838b0"
      ]
    ]
  ],
  "added": [
    [
      "0088386c",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ],
    [
      "00883878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883888"
      ]
    ],
    [
      "00883898",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008838b0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008508d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/008508a8.md#insn-008508d4) · [`008508d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/008508a8.md#insn-008508d8) · [`008508dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/008508a8.md#insn-008508dc)

~~~diff
- 008508d4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008508d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008508d4 bytes 090000f9
- 008508d8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 008508d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008508d8 bytes 0004803d
- 008508dc ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 008508dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008508dc bytes 081000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0caaf257360416e9e125796e71dd0d53"></a>

### [`00850958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850958.md) → [`008838f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/008838f0.md) FUN_008838f0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.14% / 新版 77.14%

CFGの説明率　旧版 30.00% / 新版 21.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850978"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850980"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00883910"
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
      "unmatched:00850980",
      "DATA",
      [
        "storage",
        "00c028c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:0085099c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883950"
      ]
    ],
    [
      "unmatched:008509a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883958"
      ]
    ]
  ],
  "added": [
    [
      "00883918",
      "DATA",
      [
        "storage",
        "00c80698",
        null,
        "undefined *"
      ]
    ],
    [
      "00883934",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883950"
      ]
    ],
    [
      "00883940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883958"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850958.md#insn-00850978) · [`00850980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850958.md#insn-00850980) · [`0085099c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850958.md#insn-0085099c)

~~~diff
- 00850978 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00850978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00850978 bytes 2004803d
- 00850980 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00850980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00850980 bytes 290000f9
- 0085099c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 0085099c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 0085099c bytes e00000b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fa7ebc860b7c43ba247f35604348e1"></a>

### [`00850afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md) → [`00883a94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883a94.md) FUN_00883a94

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e4a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e4a4.md) [`0073e89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e89c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0084dd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084dd1c.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007687b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007687b0.md) [`00768ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768ba8.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00880cb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880cb4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 57.50% / 新版 57.50%

CFGの説明率　旧版 25.53% / 新版 25.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `store_value` 1件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850b20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00850c0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00850b20",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00883df4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883b28"
      ]
    ],
    [
      "unmatched:00850b74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883f38"
      ]
    ]
  ],
  "added": [
    [
      "00883ab8",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00883ae0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883b28"
      ]
    ],
    [
      "00883b0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00883f38"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00850b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md#insn-00850b20) · [`00850c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md#insn-00850c0c) · [`00850c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850afc.md#insn-00850c10)

~~~diff
- 00850b20 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00850b20 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00850b20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00850b20 bytes a8831ff8
- 00850c0c ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00850c0c ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00850c0c ["COPY", "tmp:2:8", ["register:8:8"]]
- 00850c0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00850c0c bytes f35300a9
- 00850c10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00850c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00850c10 bytes e80b00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5faeb324501a65a817de51ee04287363"></a>

### [`00850fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850fcc.md) → [`00883f64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md) FUN_00883f64

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 61.54% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00850fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850fcc.md#insn-00850fe8) · [`00850fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850fcc.md#insn-00850fec) · [`00850ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00850/00850fcc.md#insn-00850ff4)
- 新版 [`00883f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883f80) · [`00883f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883f84) · [`00883f8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00883/00883f64.md#insn-00883f8c)

~~~diff
- 00850fe8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00883f80 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00850fe8 bytes 80000054
+ 00883f80 bytes 80000054
- 00850fec ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00850fec ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00883f84 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00883f84 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00850fec bytes 000100b4
+ 00883f84 bytes 000100b4
- 00850ff4 ["BRANCH", null, ["local:b5:8"]]
+ 00883f8c ["BRANCH", null, ["local:b4:8"]]
- 00850ff4 bytes 03000014
+ 00883f8c bytes 03000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-192c06ec53456523fd6ba5ad7967e1d2"></a>

### [`008510d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008510d4.md) → [`0088406c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md) FUN_0088406c

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 90.91% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884084",
      "incomplete_value": false,
      "site": "00884090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:718:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008510ec",
      "incomplete_value": false,
      "site": "008510f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00851150"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "008840e8"
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
      "00884090",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00851150",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00884090",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ],
    [
      "008840e8",
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

- 旧版 [`00851150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008510d4.md#insn-00851150) · [`008510e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008510d4.md#insn-008510e8)
- 新版 [`008840e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md#insn-008840e8) · [`00884080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/0088406c.md#insn-00884080)

~~~diff
- 00851150 ["COPY", "register:0:8", ["register:4040:8"]]
- 00851150 ["INT_ADD", "register:40f0:8", ["const:851150:8", "const:4:8"]]
- 00851150 ["CALLIND", null, ["register:0:8"]]
- 00851150 bytes 00013fd6
+ 008840e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 008840e8 ["INT_ADD", "register:40f0:8", ["const:8840e8:8", "const:4:8"]]
+ 008840e8 ["CALLIND", null, ["register:0:8"]]
+ 008840e8 bytes 00013fd6
- 008510e8 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00884080 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008510e8 bytes 881d00b0
+ 00884080 bytes e81f0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5baaf25b14efd074a763afe9c39be8b"></a>

### [`008511f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008511f0.md) → [`00884188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md) FUN_00884188

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085121c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008841b4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00851248"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:0085121c",
      "DATA",
      [
        "storage",
        "00c02940",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00851248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008841f8"
      ]
    ]
  ],
  "added": [
    [
      "008841b4",
      "DATA",
      [
        "storage",
        "00c80718",
        null,
        "undefined *"
      ]
    ],
    [
      "008841e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008841f8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085121c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008511f0.md#insn-0085121c) · [`00851234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008511f0.md#insn-00851234) · [`00851248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008511f0.md#insn-00851248)
- 新版 [`008841cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884188.md#insn-008841cc)

~~~diff
- 0085121c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 0085121c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 0085121c bytes 090000f9
- 00851234 ["INT_ADD", "register:40f0:8", ["const:851234:8", "const:4:8"]]
- 00851234 ["CALL", null, ["callee:00c538b0:8"]]
+ 008841cc ["INT_ADD", "register:40f0:8", ["const:8841cc:8", "const:4:8"]]
+ 008841cc ["CALL", null, ["callee:00c538b0:8"]]
- 00851234 bytes 0b170e94
+ 008841cc bytes b93d0f94
- 00851248 ["CBRANCH", null, ["local:b6:8", "register:101:1"]]
- 00851248 bytes c0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97c9e9871f0b47e167e9e8b227e16233"></a>

### [`0085164c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085164c.md) → [`008845e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008845e4.md) FUN_008845e4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 70.00% / 新版 58.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0085166c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00851674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00884604"
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
      "unmatched:00851674",
      "DATA",
      [
        "storage",
        "00c029c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088460c",
      "DATA",
      [
        "storage",
        "00c80798",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085166c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085164c.md#insn-0085166c) · [`00851674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085164c.md#insn-00851674) · [`00851688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085164c.md#insn-00851688)
- 新版 [`00884620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008845e4.md#insn-00884620)

~~~diff
- 0085166c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 0085166c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 0085166c bytes 2004803d
- 00851674 ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00851674 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00851674 bytes 290000f9
- 00851688 ["INT_ADD", "register:40f0:8", ["const:851688:8", "const:4:8"]]
- 00851688 ["CALL", null, ["callee:00c538b0:8"]]
+ 00884620 ["INT_ADD", "register:40f0:8", ["const:884620:8", "const:4:8"]]
+ 00884620 ["CALL", null, ["callee:00c538b0:8"]]
- 00851688 bytes f6150e94
+ 00884620 bytes a43c0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efb718d8be2ef93fad1e541a55aff952"></a>

### [`0085182c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085182c.md) → [`008847c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md) FUN_008847c4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 72.73% / 新版 61.54%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008847dc",
      "incomplete_value": false,
      "site": "008847e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851844",
      "incomplete_value": false,
      "site": "00851850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008847e8",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008847e8",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085182c.md#insn-00851840) · [`00851844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085182c.md#insn-00851844) · [`00851858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/0085182c.md#insn-00851858)
- 新版 [`008847d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-008847d8) · [`008847dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-008847dc) · [`008847f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008847c4.md#insn-008847f0)

~~~diff
- 00851840 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008847d8 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00851840 bytes 881d00b0
+ 008847d8 bytes e81f0090
- 00851844 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00851844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00851844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008847dc ["COPY", "tmp:0:8", ["const:828:8"]]
+ 008847dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008847dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008847dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00851844 bytes 08412991
+ 008847dc bytes 08a12091
- 00851858 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00851858 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 008847f0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 008847f0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00851858 bytes 000100b4
+ 008847f0 bytes 000100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa3d04f6f5c7ba72f2774c12b68c09f8"></a>

### [`00851948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851948.md) → [`008848e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md) FUN_008848e0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884908",
      "incomplete_value": false,
      "site": "0088490c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851970",
      "incomplete_value": false,
      "site": "00851974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "0088490c",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088490c",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085195c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851948.md#insn-0085195c) · [`0085196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851948.md#insn-0085196c) · [`00851970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851948.md#insn-00851970)
- 新版 [`008848f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-008848f4) · [`00884904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-00884904) · [`00884908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/008848e0.md#insn-00884908)

~~~diff
- 0085195c ["INT_ADD", "register:40f0:8", ["const:85195c:8", "const:4:8"]]
- 0085195c ["CALL", null, ["callee:00c57a90:8"]]
+ 008848f4 ["INT_ADD", "register:40f0:8", ["const:8848f4:8", "const:4:8"]]
+ 008848f4 ["CALL", null, ["callee:00c57a90:8"]]
- 0085195c bytes b9250e94
+ 008848f4 bytes 674c0f94
- 0085196c ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 00884904 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 0085196c bytes 891d00b0
+ 00884904 bytes e91f0090
- 00851970 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00851970 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851970 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00884908 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 00884908 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00884908 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00884908 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851970 bytes 29412991
+ 00884908 bytes 29a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0540c4ec190dfeffc4cecae6f99705d"></a>

### [`008519f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008519f8.md) → [`00884990`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md) FUN_00884990

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "008849ac",
      "incomplete_value": false,
      "site": "008849b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00851a14",
      "incomplete_value": false,
      "site": "00851a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:a50:8"
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
      "008849b8",
      "DATA",
      [
        "storage",
        "00c02a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008849b8",
      "DATA",
      [
        "storage",
        "00c80828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00851a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008519f8.md#insn-00851a10) · [`00851a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008519f8.md#insn-00851a14) · [`00851a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/008519f8.md#insn-00851a34)
- 新版 [`008849a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849a8) · [`008849ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849ac) · [`008849cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884990.md#insn-008849cc)

~~~diff
- 00851a10 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 008849a8 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00851a10 bytes 891d00b0
+ 008849a8 bytes e91f0090
- 00851a14 ["COPY", "tmp:0:8", ["const:a50:8"]]
- 00851a14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00851a14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008849ac ["COPY", "tmp:0:8", ["const:828:8"]]
+ 008849ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008849ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008849ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00851a14 bytes 29412991
+ 008849ac bytes 29a12091
- 00851a34 ["INT_ADD", "register:40f0:8", ["const:851a34:8", "const:4:8"]]
- 00851a34 ["CALL", null, ["callee:00c538b0:8"]]
+ 008849cc ["INT_ADD", "register:40f0:8", ["const:8849cc:8", "const:4:8"]]
+ 008849cc ["CALL", null, ["callee:00c538b0:8"]]
- 00851a34 bytes 0b150e94
+ 008849cc bytes b93b0f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a524f5d57387debd0746a875ccddf0"></a>

### [`00851f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851f9c.md) → [`00884f34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md) FUN_00884f34

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 53.85% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00851fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851f9c.md#insn-00851fb8) · [`00851fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851f9c.md#insn-00851fbc) · [`00851fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851f9c.md#insn-00851fc4)
- 新版 [`00884f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884f50) · [`00884f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884f54) · [`00884f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884f34.md#insn-00884f5c)

~~~diff
- 00851fb8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00884f50 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00851fb8 bytes 80000054
+ 00884f50 bytes 80000054
- 00851fbc ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00851fbc ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00884f54 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00884f54 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00851fbc bytes 000100b4
+ 00884f54 bytes 000100b4
- 00851fc4 ["BRANCH", null, ["local:b6:8"]]
+ 00884f5c ["BRANCH", null, ["local:b4:8"]]
- 00851fc4 bytes 03000014
+ 00884f5c bytes 03000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8b4dedfda55fa2790cffb4921ee396a"></a>

### [`00852020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852020.md) → [`00884fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md) FUN_00884fb8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_return_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 53.85% / 新版 63.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00884fd0",
      "incomplete_value": false,
      "site": "00884fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852038",
      "incomplete_value": false,
      "site": "00852044",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "definition_site": "0088500c",
      "incomplete_value": true,
      "site": "00885014",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "0085208c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00884fdc",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00884fdc",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0085207c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852020.md#insn-0085207c) · [`0085208c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852020.md#insn-0085208c)
- 新版 [`00885014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md#insn-00885014) · [`00885024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00884/00884fb8.md#insn-00885024)

~~~diff
- 0085207c ["INT_ADD", "register:40f0:8", ["const:85207c:8", "const:4:8"]]
- 0085207c ["CALL", null, ["callee:00c538e0:8"]]
+ 00885014 ["INT_ADD", "register:40f0:8", ["const:885014:8", "const:4:8"]]
+ 00885014 ["CALL", null, ["callee:00c538e0:8"]]
- 0085207c bytes 85130e94
+ 00885014 bytes 333a0f94
- 0085208c ["COPY", "register:0:8", ["register:40f0:8"]]
- 0085208c ["RETURN", null, ["register:0:8"]]
- 0085208c bytes c0035fd6
+ 00885024 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00885024 ["RETURN", null, ["register:0:8"]]
+ 00885024 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4120de099867ffe7c2874deb213a00"></a>

### [`008520b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008520b0.md) → [`00885048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md) FUN_00885048

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00885060",
      "incomplete_value": false,
      "site": "0088506c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008520c8",
      "incomplete_value": false,
      "site": "008520d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "0088506c",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0088506c",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008520c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008520b0.md#insn-008520c4) · [`008520c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008520b0.md#insn-008520c8) · [`008520f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008520b0.md#insn-008520f8)
- 新版 [`0088505c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-0088505c) · [`00885060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-00885060) · [`00885090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885048.md#insn-00885090)

~~~diff
- 008520c4 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0088505c ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008520c4 bytes 881d0090
+ 0088505c bytes c81f00f0
- 008520c8 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 008520c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008520c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885060 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00885060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008520c8 bytes 08012b91
+ 00885060 bytes 08612291
- 008520f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008520f8 ["INT_ADD", "register:40f0:8", ["const:8520f8:8", "const:4:8"]]
- 008520f8 ["CALLIND", null, ["register:0:8"]]
+ 00885090 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885090 ["INT_ADD", "register:40f0:8", ["const:885090:8", "const:4:8"]]
+ 00885090 ["CALLIND", null, ["register:0:8"]]
- 008520f8 bytes 00013fd6
+ 00885090 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c969b21b18f257b469d1ade7acb4d1cc"></a>

### [`0085213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085213c.md) → [`008850d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md) FUN_008850d4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008850fc",
      "incomplete_value": false,
      "site": "00885100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852164",
      "incomplete_value": false,
      "site": "00852168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "00885100",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885100",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085213c.md#insn-00852150) · [`00852160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085213c.md#insn-00852160) · [`00852164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085213c.md#insn-00852164)
- 新版 [`008850e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-008850e8) · [`008850f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-008850f8) · [`008850fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008850d4.md#insn-008850fc)

~~~diff
- 00852150 ["INT_ADD", "register:40f0:8", ["const:852150:8", "const:4:8"]]
- 00852150 ["CALL", null, ["callee:00c57a90:8"]]
+ 008850e8 ["INT_ADD", "register:40f0:8", ["const:8850e8:8", "const:4:8"]]
+ 008850e8 ["CALL", null, ["callee:00c57a90:8"]]
- 00852150 bytes bc230e94
+ 008850e8 bytes 6a4a0f94
- 00852160 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 008850f8 ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00852160 bytes 891d0090
+ 008850f8 bytes c91f00f0
- 00852164 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00852164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008850fc ["COPY", "tmp:0:8", ["const:898:8"]]
+ 008850fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008850fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008850fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852164 bytes 29012b91
+ 008850fc bytes 29612291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af1de6ac58e2424f2ea12fc479f77fd8"></a>

### [`008521ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008521ec.md) → [`00885184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md) FUN_00885184

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md)

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
      "definition_site": "008851a0",
      "incomplete_value": false,
      "site": "008851ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852208",
      "incomplete_value": false,
      "site": "00852214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
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
      "008851ac",
      "DATA",
      [
        "storage",
        "00c02ac0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008851ac",
      "DATA",
      [
        "storage",
        "00c80898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008521ec.md#insn-00852204) · [`00852208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008521ec.md#insn-00852208) · [`00852228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008521ec.md#insn-00852228)
- 新版 [`0088519c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-0088519c) · [`008851a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-008851a0) · [`008851c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885184.md#insn-008851c0)

~~~diff
- 00852204 ["COPY", "register:4048:8", ["const:c02000:8"]]
+ 0088519c ["COPY", "register:4048:8", ["const:c80000:8"]]
- 00852204 bytes 891d0090
+ 0088519c bytes c91f00f0
- 00852208 ["COPY", "tmp:0:8", ["const:ac0:8"]]
- 00852208 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00852208 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008851a0 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 008851a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008851a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008851a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00852208 bytes 29012b91
+ 008851a0 bytes 29612291
- 00852228 ["INT_ADD", "register:40f0:8", ["const:852228:8", "const:4:8"]]
- 00852228 ["CALL", null, ["callee:00c538b0:8"]]
+ 008851c0 ["INT_ADD", "register:40f0:8", ["const:8851c0:8", "const:4:8"]]
+ 008851c0 ["CALL", null, ["callee:00c538b0:8"]]
- 00852228 bytes 0e130e94
+ 008851c0 bytes bc390f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-899b1f9c6dd2c64ae1e52a9f5b1fabff"></a>

### [`008523cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008523cc.md) → [`00885364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md) FUN_00885364

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00885380",
      "incomplete_value": false,
      "site": "00885388",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008523e8",
      "incomplete_value": false,
      "site": "008523f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "00885388",
      "DATA",
      [
        "storage",
        "00c02b50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885388",
      "DATA",
      [
        "storage",
        "00c80928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008523e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008523cc.md#insn-008523e4) · [`008523e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008523cc.md#insn-008523e8) · [`00852400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/008523cc.md#insn-00852400)
- 新版 [`0088537c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-0088537c) · [`00885380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-00885380) · [`00885398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885364.md#insn-00885398)

~~~diff
- 008523e4 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 0088537c ["COPY", "register:4040:8", ["const:c80000:8"]]
- 008523e4 bytes 881d0090
+ 0088537c bytes c81f00f0
- 008523e8 ["COPY", "tmp:0:8", ["const:b50:8"]]
- 008523e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008523e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885380 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 00885380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008523e8 bytes 08412d91
+ 00885380 bytes 08a12491
- 00852400 ["INT_ADD", "register:40f0:8", ["const:852400:8", "const:4:8"]]
- 00852400 ["CALL", null, ["callee:00c538e0:8"]]
+ 00885398 ["INT_ADD", "register:40f0:8", ["const:885398:8", "const:4:8"]]
+ 00885398 ["CALL", null, ["callee:00c538e0:8"]]
- 00852400 bytes a4120e94
+ 00885398 bytes 52390f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb29da1c73bdc8364ca30f68c8b2650"></a>

### [`0085274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md) → [`008856e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md) FUN_008856e4

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 11件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0084d6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084d/0084d6d0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`007689e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/007689e8.md) [`00768e50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00768/00768e50.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00880668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00880/00880668.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 74.65% / 新版 80.30%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 2件, `store_value` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00885878",
      "incomplete_value": false,
      "site": "00885880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008528e0",
      "incomplete_value": false,
      "site": "008528e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00885754",
      "value": [
        "leaf",
        "ram:7689e8:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "008527bc",
      "value": [
        "leaf",
        "ram:73e6dc:8"
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
      "site": "00885798",
      "value": [
        "leaf",
        "ram:768e50:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00852800",
      "value": [
        "leaf",
        "ram:73eb44:8"
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
      "00885754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073e6dc"
      ]
    ],
    [
      "00885798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073eb44"
      ]
    ],
    [
      "00885880",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885754",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "007689e8"
      ]
    ],
    [
      "00885798",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00768e50"
      ]
    ],
    [
      "00885880",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008527bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md#insn-008527bc) · [`00852800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md#insn-00852800) · [`00852908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/0085274c.md#insn-00852908)
- 新版 [`00885754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-00885754) · [`00885798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-00885798) · [`008858a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/008856e4.md#insn-008858a0)

~~~diff
- 008527bc ["INT_ADD", "register:40f0:8", ["const:8527bc:8", "const:4:8"]]
- 008527bc ["CALL", null, ["ram:73e6dc:8"]]
+ 00885754 ["INT_ADD", "register:40f0:8", ["const:885754:8", "const:4:8"]]
+ 00885754 ["CALL", null, ["ram:7689e8:8"]]
- 008527bc bytes c8affb97
+ 00885754 bytes a58cfb97
- 00852800 ["INT_ADD", "register:40f0:8", ["const:852800:8", "const:4:8"]]
- 00852800 ["CALL", null, ["ram:73eb44:8"]]
+ 00885798 ["INT_ADD", "register:40f0:8", ["const:885798:8", "const:4:8"]]
+ 00885798 ["CALL", null, ["ram:768e50:8"]]
- 00852800 bytes d1b0fb97
+ 00885798 bytes ae8dfb97
- 00852908 ["INT_ADD", "register:40f0:8", ["const:852908:8", "const:4:8"]]
- 00852908 ["CALL", null, ["callee:00c538b0:8"]]
+ 008858a0 ["INT_ADD", "register:40f0:8", ["const:8858a0:8", "const:4:8"]]
+ 008858a0 ["CALL", null, ["callee:00c538b0:8"]]
- 00852908 bytes 56110e94
+ 008858a0 bytes 04380f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b08682cb778a88e183a9f9300f1de98"></a>

### [`00852c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852c58.md) → [`00885bf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885bf0.md) FUN_00885bf0

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 21.43% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00852c84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00852c88"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00852c8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00852c84",
      "DATA",
      [
        "storage",
        "00c02bc0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00852c90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885c38"
      ]
    ],
    [
      "unmatched:00852cbc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00885c1c",
      "DATA",
      [
        "storage",
        "00c80998",
        null,
        "undefined *"
      ]
    ],
    [
      "00885c28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885c38"
      ]
    ],
    [
      "00885c54",
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

- 旧版 [`00852c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852c58.md#insn-00852c84) · [`00852c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852c58.md#insn-00852c88) · [`00852c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852c58.md#insn-00852c8c)

~~~diff
- 00852c84 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00852c84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00852c84 bytes 090000f9
- 00852c88 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:10:8"]]
- 00852c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00852c88 bytes 0004803d
- 00852c8c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:20:8"]]
- 00852c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00852c8c bytes 081000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419da97b39cec519acedaafa79f93fb2"></a>

### [`00852ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ee8.md) → [`00885e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md) FUN_00885e80

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "00885e98",
      "incomplete_value": false,
      "site": "00885ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00852f00",
      "incomplete_value": false,
      "site": "00852f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00885ea4",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00885ea4",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ee8.md#insn-00852efc) · [`00852f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ee8.md#insn-00852f00) · [`00852f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852ee8.md#insn-00852f30)
- 新版 [`00885e94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md#insn-00885e94) · [`00885e98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md#insn-00885e98) · [`00885ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885e80.md#insn-00885ec8)

~~~diff
- 00852efc ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 00885e94 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00852efc bytes 881d0090
+ 00885e94 bytes c81f00f0
- 00852f00 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00852f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00852f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00885e98 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00885e98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00885e98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00885e98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00852f00 bytes 08413191
+ 00885e98 bytes 08a12891
- 00852f30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00852f30 ["INT_ADD", "register:40f0:8", ["const:852f30:8", "const:4:8"]]
- 00852f30 ["CALLIND", null, ["register:0:8"]]
+ 00885ec8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00885ec8 ["INT_ADD", "register:40f0:8", ["const:885ec8:8", "const:4:8"]]
+ 00885ec8 ["CALLIND", null, ["register:0:8"]]
- 00852f30 bytes 00013fd6
+ 00885ec8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdf48a0326df27a88327ef4bfb9eba12"></a>

### [`00852fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852fc4.md) → [`00885f5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md) FUN_00885f5c

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 69.77% / 新版 69.77%

CFGの説明率　旧版 8.00% / 新版 18.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00852ff8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00853008"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00885f90"
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
      "unmatched:00852ff8",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00852ffc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885fac"
      ]
    ],
    [
      "unmatched:00853024",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885fd8"
      ]
    ]
  ],
  "added": [
    [
      "00885f90",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ],
    [
      "00885f94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885fac"
      ]
    ],
    [
      "00885fbc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00885fd8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00852fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852fc4.md#insn-00852fdc) · [`00852ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852fc4.md#insn-00852ff8) · [`00852ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00852/00852fc4.md#insn-00852ffc)
- 新版 [`00885f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00885/00885f5c.md#insn-00885f74)

~~~diff
- 00852fdc ["INT_ADD", "register:40f0:8", ["const:852fdc:8", "const:4:8"]]
- 00852fdc ["CALL", null, ["callee:00c57a90:8"]]
+ 00885f74 ["INT_ADD", "register:40f0:8", ["const:885f74:8", "const:4:8"]]
+ 00885f74 ["CALL", null, ["callee:00c57a90:8"]]
- 00852fdc bytes 19200e94
+ 00885f74 bytes c7460f94
- 00852ff8 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00852ff8 ["COPY", "tmp:1:8", ["register:40a0:8"]]
- 00852ff8 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:10:8"]]
- 00852ff8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00852ff8 bytes 8a0601f8
- 00852ffc ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00852ffc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00852ffc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00852ffc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00852ffc bytes c9000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5cd01704be5bfe23aecfb9de8e571aa"></a>

### [`0085309c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085309c.md) → [`00886034`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md) FUN_00886034

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 88.37% / 新版 88.37%

CFGの説明率　旧版 69.23% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00886050",
      "incomplete_value": false,
      "site": "00886050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008530b8",
      "incomplete_value": false,
      "site": "008530b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008530d8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008530dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00886050",
      "DATA",
      [
        "storage",
        "00c02c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886050",
      "DATA",
      [
        "storage",
        "00c80a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085309c.md#insn-008530d8) · [`008530dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085309c.md#insn-008530dc)
- 新版 [`00886070`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886034.md#insn-00886070)

~~~diff
- 008530d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:10:8"]]
- 008530d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008530d8 bytes 890a00f9
- 008530dc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 008530dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008530dc bytes 8002803d
+ 00886070 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:10:8"]]
+ 00886070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00886070 bytes 890a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb09ef1438cd902d723c8c0f81237450"></a>

### [`00853228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md) → [`008861c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md) FUN_008861c0

採用 · 移動量 `+0x32f98` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 9件 [`0042ca08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca08.md) [`00432904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00432/00432904.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0044f8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0044f/0044f8a0.md) [`0045579c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00455/0045579c.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00764ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00764/00764ea0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 93.39% / 新版 93.39%

CFGの説明率　旧版 68.00% / 新版 75.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008862a4",
      "incomplete_value": false,
      "site": "008862a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0085330c",
      "incomplete_value": false,
      "site": "0085330c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00853400"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00886398"
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
      "unmatched:00853268",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0073ab94"
      ]
    ],
    [
      "0088623c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008533f4"
      ]
    ],
    [
      "008862a4",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00886200",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00764ea0"
      ]
    ],
    [
      "0088623c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088638c"
      ]
    ],
    [
      "008862a4",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md#insn-00853268) · [`00853360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md#insn-00853360) · [`008533f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853228.md#insn-008533f0)
- 新版 [`008862f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008861c0.md#insn-008862f8)

~~~diff
- 00853268 ["INT_ADD", "register:40f0:8", ["const:853268:8", "const:4:8"]]
- 00853268 ["CALL", null, ["ram:73ab94:8"]]
- 00853268 bytes 4b9efb97
- 00853360 ["INT_ADD", "register:40f0:8", ["const:853360:8", "const:4:8"]]
- 00853360 ["CALL", null, ["callee:0045579c:8"]]
+ 008862f8 ["INT_ADD", "register:40f0:8", ["const:8862f8:8", "const:4:8"]]
+ 008862f8 ["CALL", null, ["callee:0045579c:8"]]
- 00853360 bytes 697def97
+ 008862f8 bytes 293def97
- 008533f0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 008533f0 ["RETURN", null, ["register:0:8"]]
- 008533f0 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e502dcae5304752b7480a9416015df5e"></a>

### [`00853540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853540.md) → [`008864d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md) FUN_008864d8

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "008864f0",
      "incomplete_value": false,
      "site": "008864fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853558",
      "incomplete_value": false,
      "site": "00853564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "008864fc",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008864fc",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853540.md#insn-00853554) · [`00853558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853540.md#insn-00853558) · [`00853588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853540.md#insn-00853588)
- 新版 [`008864ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md#insn-008864ec) · [`008864f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md#insn-008864f0) · [`00886520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008864d8.md#insn-00886520)

~~~diff
- 00853554 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008864ec ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00853554 bytes 681d00f0
+ 008864ec bytes c81f00d0
- 00853558 ["COPY", "tmp:0:8", ["const:cc0:8"]]
- 00853558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008864f0 ["COPY", "tmp:0:8", ["const:a98:8"]]
+ 008864f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008864f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008864f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853558 bytes 08013391
+ 008864f0 bytes 08612a91
- 00853588 ["COPY", "register:0:8", ["register:4040:8"]]
- 00853588 ["INT_ADD", "register:40f0:8", ["const:853588:8", "const:4:8"]]
- 00853588 ["CALLIND", null, ["register:0:8"]]
+ 00886520 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00886520 ["INT_ADD", "register:40f0:8", ["const:886520:8", "const:4:8"]]
+ 00886520 ["CALLIND", null, ["register:0:8"]]
- 00853588 bytes 00013fd6
+ 00886520 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c44825f7f9f6cb7d1b85aa3b19ae32c"></a>

### [`00853624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853624.md) → [`008865bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008865bc.md) FUN_008865bc

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.21% / 新版 86.21%

CFGの説明率　旧版 42.86% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00853640"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "008865d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00853644"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00853640",
      "DATA",
      [
        "storage",
        "00c02cc0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00853644",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886604"
      ]
    ]
  ],
  "added": [
    [
      "008865d8",
      "DATA",
      [
        "storage",
        "00c80a98",
        null,
        "undefined *"
      ]
    ],
    [
      "008865dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00886604"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853624.md#insn-00853640) · [`00853644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853624.md#insn-00853644)
- 新版 [`008865d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008865bc.md#insn-008865d8)

~~~diff
- 00853640 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00853640 ["COPY", "tmp:1:8", ["register:4008:8"]]
- 00853640 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
- 00853640 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00853640 bytes 290401f8
- 00853644 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00853644 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00853644 bytes 480100b4
+ 008865d8 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 008865d8 ["COPY", "tmp:1:8", ["register:4008:8"]]
+ 008865d8 ["INT_ADD", "register:4008:8", ["register:4008:8", "const:10:8"]]
+ 008865d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 008865d8 bytes 290401f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b8e938675525523a775397bc6f1e6a0"></a>

### [`00853720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853720.md) → [`008866b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md) FUN_008866b8

採用 · 移動量 `+0x32f98` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 92.21% / 新版 92.21%

CFGの説明率　旧版 40.74% / 新版 36.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00853848"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "008867e0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0088674c",
      "incomplete_value": true,
      "site": "00886758",
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
      "0088676c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:0085383c"
      ]
    ],
    [
      "unmatched:00853840",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00853848",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088684c"
      ]
    ]
  ],
  "added": [
    [
      "0088676c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008867d4"
      ]
    ],
    [
      "008867d8",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "008867e0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088684c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008537c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853720.md#insn-008537c0) · [`008537e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853720.md#insn-008537e8) · [`00853838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853720.md#insn-00853838)
- 新版 [`00886758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008866b8.md#insn-00886758)

~~~diff
- 008537c0 ["INT_ADD", "register:40f0:8", ["const:8537c0:8", "const:4:8"]]
- 008537c0 ["CALL", null, ["callee:0043bae0:8"]]
+ 00886758 ["INT_ADD", "register:40f0:8", ["const:886758:8", "const:4:8"]]
+ 00886758 ["CALL", null, ["callee:0043bae0:8"]]
- 008537c0 bytes 0816ef97
+ 00886758 bytes e2d4ee97
- 008537e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 008537e8 ["INT_ADD", "register:40f0:8", ["const:8537e8:8", "const:4:8"]]
- 008537e8 ["CALLIND", null, ["register:0:8"]]
- 008537e8 bytes 00013fd6
- 00853838 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00853838 ["RETURN", null, ["register:0:8"]]
- 00853838 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9b00942656f2d181402d637b448a1d5"></a>

### [`0085393c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085393c.md) → [`008868d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md) FUN_008868d4

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

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
      "definition_site": "008868ec",
      "incomplete_value": false,
      "site": "008868f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c80000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00853954",
      "incomplete_value": false,
      "site": "00853958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c02000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "008868f0",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008868f0",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00853950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085393c.md#insn-00853950) · [`00853954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085393c.md#insn-00853954) · [`00853968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/0085393c.md#insn-00853968)
- 新版 [`008868e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-008868e8) · [`008868ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-008868ec) · [`00886900`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/008868d4.md#insn-00886900)

~~~diff
- 00853950 ["COPY", "register:4040:8", ["const:c02000:8"]]
+ 008868e8 ["COPY", "register:4040:8", ["const:c80000:8"]]
- 00853950 bytes 681d00f0
+ 008868e8 bytes c81f00d0
- 00853954 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00853954 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00853954 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008868ec ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 008868ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008868ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008868ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00853954 bytes 08813591
+ 008868ec bytes 08e12c91
- 00853968 ["INT_ADD", "register:40f0:8", ["const:853968:8", "const:4:8"]]
- 00853968 ["CALL", null, ["callee:00c538e0:8"]]
+ 00886900 ["INT_ADD", "register:40f0:8", ["const:886900:8", "const:4:8"]]
+ 00886900 ["CALL", null, ["callee:00c538e0:8"]]
- 00853968 bytes 4a0d0e94
+ 00886900 bytes f8330f94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66a08fd89919a3173f750786b00f3c5b"></a>

### [`00853998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853998.md) → [`00886930`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00886/00886930.md) FUN_00886930

採用 · 移動量 `+0x32f98` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008539c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008539c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008539c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:008539c0",
      "DATA",
      [
        "storage",
        "00c02d60",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008539cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088697c"
      ]
    ]
  ],
  "added": [
    [
      "00886958",
      "DATA",
      [
        "storage",
        "00c80b38",
        null,
        "undefined *"
      ]
    ],
    [
      "00886964",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "0088697c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008539c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853998.md#insn-008539c0) · [`008539c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853998.md#insn-008539c4) · [`008539c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853998.md#insn-008539c8)

~~~diff
- 008539c0 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 008539c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008539c0 bytes 090000f9
- 008539c4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 008539c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 008539c4 bytes 0080803c
- 008539c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:18:8"]]
- 008539c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008539c8 bytes 080c00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

