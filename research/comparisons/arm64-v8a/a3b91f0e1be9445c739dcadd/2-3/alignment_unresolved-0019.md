# v15.7.4 → v16.0.0 · 命令位置の検査未完了 (19)

[一覧の目次](README.md)

<a id="compare-04475d265ada9be4742dd92cdd5272d5"></a>

### [`00b99590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md) → [`00c15fd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c15/00c15fd8.md) _ZNKSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE13__get_percentERS4_S4_RjRKNS_5ctypeIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1660.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e250.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.52% / 新版 89.52%

CFGの説明率　旧版 47.37% / 新版 45.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b995d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b996e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c1601c"
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
      "unmatched:00b995d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16050"
      ]
    ],
    [
      "unmatched:00b996e8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1616c"
      ]
    ],
    [
      "unmatched:00b995fc",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1601c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c16050"
      ]
    ],
    [
      "00c16130",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1616c"
      ]
    ],
    [
      "00c16044",
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

- 旧版 [`00b995d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b995d4) · [`00b995fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b995fc) · [`00b9968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99590.md#insn-00b9968c)

~~~diff
- 00b995d4 ["CBRANCH", null, ["local:b7:8", "register:101:1"]]
- 00b995d4 bytes a0010054
- 00b995fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b995fc ["INT_ADD", "register:40f0:8", ["const:b995fc:8", "const:4:8"]]
- 00b995fc ["CALLIND", null, ["register:0:8"]]
- 00b995fc bytes 00013fd6
- 00b9968c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b9968c ["INT_ADD", "register:40f0:8", ["const:b9968c:8", "const:4:8"]]
- 00b9968c ["CALLIND", null, ["register:0:8"]]
- 00b9968c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f7b76755c25b8cfb3fbe04995071267"></a>

### [`00b99e48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99e48.md) → [`00c16890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c16/00c16890.md) _ZNKSt6__ndk110__time_put8__do_putEPcRS1_PK2tmcc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1670.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e260.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00b99eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c16900"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b99eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99e48.md#insn-00b99eb8) · [`00b99e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b99/00b99e48.md#insn-00b99e9c)
- 新版 `00c16900`（命令位置の公開資料なし） · `00c168e4`（命令位置の公開資料なし）

~~~diff
- 00b99eb8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b99eb8 ["RETURN", null, ["register:0:8"]]
- 00b99eb8 bytes c0035fd6
+ 00c16900 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c16900 ["RETURN", null, ["register:0:8"]]
+ 00c16900 bytes c0035fd6
- 00b99e9c ["INT_ADD", "register:40f0:8", ["const:b99e9c:8", "const:4:8"]]
- 00b99e9c ["CALL", null, ["callee:00c5e260:8"]]
+ 00c168e4 ["INT_ADD", "register:40f0:8", ["const:c168e4:8", "const:4:8"]]
+ 00c168e4 ["CALL", null, ["callee:00c5e260:8"]]
- 00b99e9c bytes f51d0194
+ 00c168e4 bytes 5f1e0194
~~~


<a id="compare-f6cb0c9f59291f27fde959119cac816a"></a>

### [`00b9a5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a5f8.md) → [`00c17040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c17040.md) _ZNKSt6__ndk117moneypunct_bynameIcLb0EE16do_negative_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a614"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1705c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a5f8.md#insn-00b9a614) · [`00b9a604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a5f8.md#insn-00b9a604)
- 新版 `00c1705c`（命令位置の公開資料なし） · `00c1704c`（命令位置の公開資料なし）

~~~diff
- 00b9a614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00b9a614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b9a614 bytes 090900f9
+ 00c1705c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
+ 00c1705c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c1705c bytes 090900f9
- 00b9a604 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b9a604 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b9a604 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b9a604 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c1704c ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c1704c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c1704c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c1704c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b9a604 bytes ca000037
+ 00c1704c bytes ca000037
~~~


<a id="compare-463e9e375fd7a15c8b8425311bf84b41"></a>

### [`00b9a6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a6c4.md) → [`00c1710c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c17/00c1710c.md) _ZNKSt6__ndk117moneypunct_bynameIcLb1EE16do_positive_signEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 50.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9a6dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c17124"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b9a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a6c4.md#insn-00b9a6dc) · [`00b9a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9a/00b9a6c4.md#insn-00b9a6d0)
- 新版 `00c17124`（命令位置の公開資料なし） · `00c17118`（命令位置の公開資料なし）

~~~diff
- 00b9a6dc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9a6dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9a6dc bytes 0001803d
+ 00c17124 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c17124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00c17124 bytes 0001803d
- 00b9a6d0 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00b9a6d0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b9a6d0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b9a6d0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c17118 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c17118 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c17118 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c17118 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b9a6d0 bytes ca000037
+ 00c17118 bytes ca000037
~~~


<a id="compare-6231640500601fba26d9efd19f381335"></a>

### [`00b9e17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md) → [`00c1abc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1abc4.md) FUN_00c1abc4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b9de50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9d/00b9de50.md) · 呼出先 8件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c1a898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1a/00c1a898.md) · 呼出先 8件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.50% / 新版 88.50%

CFGの説明率　旧版 60.42% / 新版 49.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e1c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e1c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9e290"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9e360",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1add4"
      ]
    ]
  ],
  "added": [
    [
      "00c1ada8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c1add4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9e1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e1c0) · [`00b9e1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e1c4) · [`00b9e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e17c.md#insn-00b9e290)

~~~diff
- 00b9e1c0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b9e1c0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9e1c0 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b9e1c0 ["COPY", "register:40a0:8", ["tmp:0:8"]]
- 00b9e1c0 bytes 34019a9a
- 00b9e1c4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b9e1c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9e1c4 ["COPY", "tmp:0:8", ["register:40d8:8"]]
- 00b9e1c4 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00b9e1c4 bytes 08019b9a
- 00b9e290 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b9e290 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b9e290 ["COPY", "tmp:0:8", ["register:40b8:8"]]
- 00b9e290 ["COPY", "register:4050:8", ["tmp:0:8"]]
- 00b9e290 bytes 8a03979a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29405359c328f5cf6ccc4957f21712e9"></a>

### [`00b9eb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md) → [`00c1b5b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b5b8.md) FUN_00c1b5b8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00b92808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92808.md) [`00b92c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b92/00b92c98.md) [`00b93f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b93/00b93f3c.md) [`00b943cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b94/00b943cc.md) [`00b9e6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9e6c4.md) · 呼出先 2件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md) [`00be1710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1710.md)
- 新版 呼出元 6件 [`00c0f250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f250.md) [`00c0f6e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0f/00c0f6e0.md) [`00c10984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10984.md) [`00c10e14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c10/00c10e14.md) [`00c1b10c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b10c.md) · 呼出先 2件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md) [`00c5e300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e300.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 97.78% / 新版 97.78%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ebe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9ebe4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1b62c"
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
      "unmatched:00b9ebe4",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1b62c",
      "WRITE",
      [
        "storage",
        "Stack[-0x80]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9ebe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md#insn-00b9ebe4) · [`00b9ebd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9e/00b9eb70.md#insn-00b9ebd4)
- 新版 `00c1b62c`（命令位置の公開資料なし） · `00c1b61c`（命令位置の公開資料なし）

~~~diff
- 00b9ebe4 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
- 00b9ebe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00b9ebe4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00b9ebe4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
- 00b9ebe4 bytes a0873dad
+ 00c1b62c ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffb0:8"]]
+ 00c1b62c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00c1b62c ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00c1b62c ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5020:16"]]
+ 00c1b62c bytes a0873dad
- 00b9ebd4 ["INT_ADD", "register:40f0:8", ["const:b9ebd4:8", "const:4:8"]]
- 00b9ebd4 ["CALL", null, ["callee:00c5e170:8"]]
+ 00c1b61c ["INT_ADD", "register:40f0:8", ["const:c1b61c:8", "const:4:8"]]
+ 00c1b61c ["CALL", null, ["callee:00c5e170:8"]]
- 00b9ebd4 bytes 6b0a0194
+ 00c1b61c bytes d50a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39f1207acd897bebf51db322c1321711"></a>

### [`00b9fd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md) → [`00c1c754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1c754.md) _ZNSt6__ndk111__money_putIwE8__formatEPwRS2_S3_jPKwS5_RKNS_5ctypeIwEEbRKNS_10money_base7patternEwwRKNS_12basic_stringIcNS_11char_traitsIcEEN

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1730.md) · 呼出先 1件 [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)
- 新版 呼出元 1件 [`00c5e320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e320.md) · 呼出先 1件 [`00c57b40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 77.55% / 新版 77.55%

CFGの説明率　旧版 65.66% / 新版 53.28%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 13件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9fd44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9fd5c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b9fd74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b9fd34",
      "READ",
      [
        "storage",
        "Stack[0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9fd38",
      "READ",
      [
        "storage",
        "Stack[0x18]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b9fd44",
      "WRITE",
      [
        "storage",
        "Stack[-0x74]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c1c77c",
      "READ",
      [
        "storage",
        "Stack[0x20]",
        null,
        null
      ]
    ],
    [
      "00c1c780",
      "READ",
      [
        "storage",
        "Stack[0x18]",
        null,
        null
      ]
    ],
    [
      "00c1c78c",
      "WRITE",
      [
        "storage",
        "Stack[-0x74]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b9fd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fd44) · [`00b9fd5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fd5c) · [`00b9fd74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b9f/00b9fd0c.md#insn-00b9fd74)

~~~diff
- 00b9fd44 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b9fd44 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffec:8"]]
- 00b9fd44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:4"]]
- 00b9fd44 bytes a8c31eb8
- 00b9fd5c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:14:8"]]
- 00b9fd5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b9fd5c bytes e81700b9
- 00b9fd74 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b9fd74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b9fd74 bytes e81300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f580f89e167ad899de117dc44bf50d2"></a>

### [`00ba0584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0584.md) → [`00c1cfcc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1c/00c1cfcc.md) _ZNKSt6__ndk18messagesIwE6do_getEliiRKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`006ad8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8e8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`006d76a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d76a4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba059c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c1cfe4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba059c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0584.md#insn-00ba059c) · [`00ba058c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba0584.md#insn-00ba058c)
- 新版 `00c1cfe4`（命令位置の公開資料なし） · `00c1cfd4`（命令位置の公開資料なし）

~~~diff
- 00ba059c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00ba059c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00ba059c bytes 090900f9
+ 00c1cfe4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
+ 00c1cfe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c1cfe4 bytes 090900f9
- 00ba058c ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
- 00ba058c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba058c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba058c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c1cfd4 ["INT_RIGHT", "tmp:0:4", ["register:4048:4", "const:0:4"]]
+ 00c1cfd4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c1cfd4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c1cfd4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba058c bytes c9000037
+ 00c1cfd4 bytes c9000037
~~~


<a id="compare-923a79bd37f219918d85b6aca2ee25aa"></a>

### [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) → [`00c1d138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d138.md) FUN_00c1d138

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)
- 新版 呼出元 2件 [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) [`00c21b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21b50.md) · 呼出先 2件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00c57c50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c50.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 75.00% / 新版 65.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba06f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba06f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba06f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba06f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba06f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba06fc",
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
      "00c1d13c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c1d140",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c1d144",
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

- 旧版 [`00ba06f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md#insn-00ba06f4) · [`00ba06f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md#insn-00ba06f8) · [`00ba06fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md#insn-00ba06fc)

~~~diff
- 00ba06f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba06f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba06f4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ba06f4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba06f4 bytes fd7bbda9
- 00ba06f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ba06f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00ba06f8 bytes f50b00f9
- 00ba06fc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba06fc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba06fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba06fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba06fc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9df7f5d0e6db6a285fadbf50eccecc66"></a>

### [`00ba3eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3eac.md) → [`00c208f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c20/00c208f4.md) FUN_00c208f4

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be18f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18f0.md)
- 新版 呼出元 2件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c21500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c21/00c21500.md) · 呼出先 1件 [`00c5e4e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4e0.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba3edc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c20924"
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
      "unmatched:00ba3ecc",
      "READ",
      [
        "storage",
        "00c1bf70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba3edc",
      "DATA",
      [
        "storage",
        "00c156e0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00c20914",
      "READ",
      [
        "storage",
        "00c9b9a0",
        null,
        "pointer"
      ]
    ],
    [
      "00c20924",
      "DATA",
      [
        "storage",
        "00c95088",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3eac.md#insn-00ba3edc) · [`00ba3ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3eac.md#insn-00ba3ec0)
- 新版 `00c20924`（命令位置の公開資料なし） · `00c20908`（命令位置の公開資料なし）

~~~diff
- 00ba3edc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ba3edc ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00ba3edc ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00ba3edc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba3edc bytes 082400a9
+ 00c20924 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c20924 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00c20924 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00c20924 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c20924 bytes 082400a9
- 00ba3ec0 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c20908 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00ba3ec0 bytes c8030090
+ 00c20908 bytes c80300f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f22f52bf007250b306c3a2f920a0dbb"></a>

### [`00ba7fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7fa4.md) → [`00c249ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c249ec.md) _ZNSt6__ndk16localeD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) · 呼出先 1件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)
- 新版 呼出元 1件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) · 呼出先 1件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 70.83% / 新版 70.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7fc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c24a0c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba7fe4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba7fc4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c24a20"
      ]
    ],
    [
      "00c24a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ba7fe8"
      ]
    ]
  ],
  "added": [
    [
      "00c24a0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c24a20"
      ]
    ],
    [
      "00c24a1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c24a30"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7fc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7fa4.md#insn-00ba7fc4) · [`00ba7fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7fa4.md#insn-00ba7fe4)
- 新版 `00c24a0c`（命令位置の公開資料なし）

~~~diff
- 00ba7fc4 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00ba7fc4 bytes a0000054
- 00ba7fe4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba7fe4 ["RETURN", null, ["register:0:8"]]
- 00ba7fe4 bytes c0035fd6
+ 00c24a0c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
+ 00c24a0c bytes a0000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3921a158183f5b5095a8f671e47e2663"></a>

### [`00ba81c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md) → [`00c24c0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24c0c.md) _ZNSt6__ndk16localeC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c1f064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f064.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8218"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c24c60"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md#insn-00ba8218) · [`00ba81e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba81c4.md#insn-00ba81e4)
- 新版 `00c24c60`（命令位置の公開資料なし） · `00c24c2c`（命令位置の公開資料なし）

~~~diff
- 00ba8218 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba8218 ["RETURN", null, ["register:0:8"]]
- 00ba8218 bytes c0035fd6
+ 00c24c60 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c24c60 ["RETURN", null, ["register:0:8"]]
+ 00c24c60 bytes c0035fd6
- 00ba81e4 ["INT_ADD", "register:40f0:8", ["const:ba81e4:8", "const:4:8"]]
- 00ba81e4 ["CALL", null, ["callee:00c57a90:8"]]
+ 00c24c2c ["INT_ADD", "register:40f0:8", ["const:c24c2c:8", "const:4:8"]]
+ 00c24c2c ["CALL", null, ["callee:00c57a90:8"]]
- 00ba81e4 bytes 97cb0094
+ 00c24c2c bytes 99cb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7305f535896a93ee63b14e91340814af"></a>

### [`00ba8470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8470.md) → [`00c24eb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24eb8.md) _ZNKSt6__ndk16locale4nameEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9a0.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00c5a3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3f0.md) · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8488"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c24ed0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8470.md#insn-00ba8488) · [`00ba847c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8470.md#insn-00ba847c)
- 新版 `00c24ed0`（命令位置の公開資料なし） · `00c24ec4`（命令位置の公開資料なし）

~~~diff
- 00ba8488 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
- 00ba8488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00ba8488 bytes 0a0900f9
+ 00c24ed0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
+ 00c24ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00c24ed0 bytes 0a0900f9
- 00ba847c ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00ba847c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ba847c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ba847c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c24ec4 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c24ec4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c24ec4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c24ec4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00ba847c bytes ca000037
+ 00c24ec4 bytes ca000037
~~~


<a id="compare-c9b1c57e891b6fc7e9f94da5a15f1e95"></a>

### [`00ba84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md) → [`00c24ee8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c24ee8.md) _ZNSt6__ndk16locale14__install_ctorERKS0_PNS0_5facetEl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7a64.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c244ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c24/00c244ac.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 16.67% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba84a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba84a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba84a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba84ac",
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
      "00c24eec",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c24ef0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c24ef4",
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

- 旧版 [`00ba84a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md#insn-00ba84a4) · [`00ba84a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md#insn-00ba84a8) · [`00ba84ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md#insn-00ba84ac)

~~~diff
- 00ba84a4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba84a4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba84a4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00ba84a4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba84a4 bytes fd7bbda9
- 00ba84a8 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba84a8 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba84a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ba84a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba84a8 bytes f65701a9
- 00ba84ac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ba84ac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ba84ac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ba84ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba84ac bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b57492b7aede4b6ef49eb40b8133643"></a>

### [`00ba89b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89b0.md) → [`00c253f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c253f8.md) _ZNSt6__ndk16locale5facetD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1920.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e510.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00ba89c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2540c"
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
      "unmatched:00ba89c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1920"
      ]
    ]
  ],
  "added": [
    [
      "00c2540c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e510"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba89c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89b0.md#insn-00ba89c4)
- 新版 `00c2540c`（命令位置の公開資料なし）

~~~diff
- 00ba89c4 ["INT_ADD", "register:40f0:8", ["const:ba89c4:8", "const:4:8"]]
- 00ba89c4 ["CALL", null, ["ram:be1920:8"]]
- 00ba89c4 bytes d7e30094
+ 00c2540c ["INT_ADD", "register:40f0:8", ["const:c2540c:8", "const:4:8"]]
+ 00c2540c ["CALL", null, ["ram:c5e510:8"]]
+ 00c2540c bytes 41e40094
~~~


<a id="compare-f0fdff48a6608645b8f5ba18ff0ad8a4"></a>

### [`00ba8c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c30.md) → [`00c25678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25678.md) _ZNSt6__ndk114collate_bynameIcED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1940.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e520.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba8c44"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2568c"
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
      "unmatched:00ba8c44",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1940"
      ]
    ]
  ],
  "added": [
    [
      "00c2568c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e520"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8c44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8c30.md#insn-00ba8c44)
- 新版 `00c2568c`（命令位置の公開資料なし）

~~~diff
- 00ba8c44 ["INT_ADD", "register:40f0:8", ["const:ba8c44:8", "const:4:8"]]
- 00ba8c44 ["CALL", null, ["ram:be1940:8"]]
- 00ba8c44 bytes 3fe30094
+ 00c2568c ["INT_ADD", "register:40f0:8", ["const:c2568c:8", "const:4:8"]]
+ 00c2568c ["CALL", null, ["ram:c5e520:8"]]
+ 00c2568c bytes a5e30094
~~~


<a id="compare-ca2610b6f3c3dd995ce310b150911ca3"></a>

### [`00ba9210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9210.md) → [`00c25c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c58.md) _ZNSt6__ndk114collate_bynameIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e550`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e550.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00ba9224"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c25c6c"
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
      "unmatched:00ba9224",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1970"
      ]
    ]
  ],
  "added": [
    [
      "00c25c6c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e550"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9210.md#insn-00ba9224)
- 新版 `00c25c6c`（命令位置の公開資料なし）

~~~diff
- 00ba9224 ["INT_ADD", "register:40f0:8", ["const:ba9224:8", "const:4:8"]]
- 00ba9224 ["CALL", null, ["ram:be1970:8"]]
- 00ba9224 bytes d3e10094
+ 00c25c6c ["INT_ADD", "register:40f0:8", ["const:c25c6c:8", "const:4:8"]]
+ 00c25c6c ["CALL", null, ["ram:c5e550:8"]]
+ 00c25c6c bytes 39e20094
~~~


<a id="compare-6e0fad0d764d50776b27dbe2e9653305"></a>

### [`00ba923c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md) → [`00c25c84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25c84.md) _ZNKSt6__ndk114collate_bynameIwE10do_compareEPKwS3_S3_S3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`006ad8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ad/006ad8a4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`006d7660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d7/006d7660.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.31% / 新版 87.31%

CFGの説明率　旧版 45.16% / 新版 35.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba924c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba924c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9250"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba924c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9250",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9254",
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
      "00c25c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00c25c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c25c9c",
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

- 旧版 [`00ba924c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba924c) · [`00ba9250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba9250) · [`00ba9254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba923c.md#insn-00ba9254)

~~~diff
- 00ba924c ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ba924c ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ba924c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ba924c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba924c bytes fa6705a9
- 00ba9250 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ba9250 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ba9250 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ba9250 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba9250 bytes f85f06a9
- 00ba9254 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ba9254 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ba9254 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00ba9254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ba9254 bytes f65707a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-312ca35d29298c35bec8948b5e115796"></a>

### [`00ba9688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md) → [`00c260d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260d0.md) _ZNSt6__ndk15ctypeIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be19a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19a0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e580.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba968c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba968c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9690"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba968c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9690",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba969c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be19a0"
      ]
    ]
  ],
  "added": [
    [
      "00c260d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c260d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c260e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e580"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba968c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md#insn-00ba968c) · [`00ba9690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md#insn-00ba9690) · [`00ba969c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9688.md#insn-00ba969c)

~~~diff
- 00ba968c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ba968c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ba968c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ba968c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ba968c bytes fd7bbea9
- 00ba9690 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ba9690 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ba9690 bytes f30b00f9
- 00ba969c ["INT_ADD", "register:40f0:8", ["const:ba969c:8", "const:4:8"]]
- 00ba969c ["CALL", null, ["ram:be19a0:8"]]
- 00ba969c bytes c1e00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e26fd95c5cad9faaf0d335cd24fb461"></a>

### [`00ba96b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96b4.md) → [`00c260fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c260fc.md) _ZNKSt6__ndk15ctypeIwE5do_isEmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 18.18% / 新版 18.18%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba96bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c26104"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba96dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba96bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ba96c8"
      ]
    ],
    [
      "unmatched:00ba96d0",
      "DATA",
      [
        "storage",
        "002fb120",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26104",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26110"
      ]
    ],
    [
      "00c26118",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba96bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96b4.md#insn-00ba96bc) · [`00ba96dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96b4.md#insn-00ba96dc)
- 新版 `00c26104`（命令位置の公開資料なし）

~~~diff
- 00ba96bc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba96bc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba96bc ["CBRANCH", null, ["local:b2:8", "tmp:1:1"]]
- 00ba96bc bytes 69000054
- 00ba96dc ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba96dc ["RETURN", null, ["register:0:8"]]
- 00ba96dc bytes c0035fd6
+ 00c26104 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c26104 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c26104 ["CBRANCH", null, ["local:b3:8", "tmp:1:1"]]
+ 00c26104 bytes 69000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7daabce7448101d17d633c31a7969a7e"></a>

### [`00ba96e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96e0.md) → [`00c26128`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26128.md) _ZNSt6__ndk15ctypeIcE13classic_tableEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba96ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c26134"
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
      "unmatched:00ba96e8",
      "DATA",
      [
        "storage",
        "002fb120",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26130",
      "DATA",
      [
        "storage",
        "00310f58",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba96ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96e0.md#insn-00ba96ec) · [`00ba96e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba96e0.md#insn-00ba96e4)
- 新版 `00c26134`（命令位置の公開資料なし）

~~~diff
- 00ba96ec ["COPY", "register:0:8", ["register:40f0:8"]]
- 00ba96ec ["RETURN", null, ["register:0:8"]]
- 00ba96ec bytes c0035fd6
+ 00c26134 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c26134 ["RETURN", null, ["register:0:8"]]
+ 00c26134 bytes c0035fd6
- 00ba96e4 ["COPY", "register:4000:8", ["const:2fb000:8"]]
- 00ba96e4 bytes 80baffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f50963683962324fba1ad706bdb875c"></a>

### [`00ba9ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9ad0.md) → [`00c26518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26518.md) _ZNKSt6__ndk15ctypeIwE8do_widenEPKcS3_Pw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 77.63% / 新版 77.63%

CFGの説明率　旧版 75.86% / 新版 68.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9b90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ba9b2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26580"
      ]
    ],
    [
      "unmatched:00ba9b44",
      "READ",
      [
        "storage",
        "002b11c0",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9b48",
      "READ",
      [
        "storage",
        "002b1a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26580"
      ]
    ],
    [
      "00c2658c",
      "READ",
      [
        "storage",
        "002c2800",
        null,
        null
      ]
    ],
    [
      "00c26590",
      "READ",
      [
        "storage",
        "002c3110",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9ad0.md#insn-00ba9b2c) · [`00ba9b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9ad0.md#insn-00ba9b80) · [`00ba9b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9ad0.md#insn-00ba9b90)

~~~diff
- 00ba9b2c ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
- 00ba9b2c bytes 62000054
- 00ba9b80 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:ffffffffffffffe0:8"]]
- 00ba9b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
- 00ba9b80 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ba9b80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:50c0:16"]]
- 00ba9b80 bytes a7193fad
- 00ba9b90 ["INT_ADD", "tmp:0:8", ["register:4068:8", "const:ffffffffffffffc0:8"]]
- 00ba9b90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5080:16"]]
- 00ba9b90 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ba9b90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00ba9b90 bytes a4413ead
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98df47c48cdafab42647aeb87879810f"></a>

### [`00ba9c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9c10.md) → [`00c26658`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26658.md) _ZNKSt6__ndk15ctypeIwE9do_narrowEPKwS3_cPc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.76% / 新版 87.76%

CFGの説明率　旧版 58.62% / 新版 48.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9d14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2675c"
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
      "unmatched:00ba9c50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c266c4"
      ]
    ],
    [
      "unmatched:00ba9ca4",
      "READ",
      [
        "storage",
        "002b1600",
        null,
        null
      ]
    ],
    [
      "unmatched:00ba9d1c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c266fc"
      ]
    ]
  ],
  "added": [
    [
      "00c26698",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c266c4"
      ]
    ],
    [
      "00c266ec",
      "READ",
      [
        "storage",
        "002c2c50",
        null,
        null
      ]
    ],
    [
      "00c26764",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c266fc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9c10.md#insn-00ba9c50) · [`00ba9d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9c10.md#insn-00ba9d14) · [`00ba9d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9c10.md#insn-00ba9d1c)

~~~diff
- 00ba9c50 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00ba9c50 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00ba9c50 ["CBRANCH", null, ["local:b8:8", "tmp:1:1"]]
- 00ba9c50 bytes 69010054
- 00ba9d14 ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:fffffffffffffff0:8"]]
- 00ba9d14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5060:16"]]
- 00ba9d14 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00ba9d14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5080:16"]]
- 00ba9d14 bytes 63913fad
- 00ba9d1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ba9d1c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00ba9d1c bytes c1fcff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-846f3a2910d52a055ffb2ca144749323"></a>

### [`00ba9dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9dd0.md) → [`00c26818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26818.md) _ZNSt6__ndk15ctypeIcED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00be19c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19c0.md) [`00be19d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19d0.md) · 呼出先 2件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md)
- 新版 呼出元 2件 [`00c5e5a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5a0.md) [`00c5e5b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e5b0.md) · 呼出先 2件 [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5ba40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba40.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9de4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2682c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ba9de8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c26820",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ba9de4",
      "DATA",
      [
        "storage",
        "00c139c0",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "unmatched:00ba9de8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ba9e20"
      ]
    ]
  ],
  "added": [
    [
      "00c26820",
      "READ",
      [
        "storage",
        "00c9b9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2682c",
      "DATA",
      [
        "storage",
        "00c93368",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00c26830",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26868"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9dd0.md#insn-00ba9de4) · [`00ba9de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9dd0.md#insn-00ba9de8)
- 新版 `00c2682c`（命令位置の公開資料なし）

~~~diff
- 00ba9de4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ba9de4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00ba9de4 bytes 090000f9
- 00ba9de8 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00ba9de8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00ba9de8 bytes c80100b4
+ 00c2682c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00c2682c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00c2682c bytes 090000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6032e6ca4d7086824bc02d672d3cf773"></a>

### [`00baa06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa06c.md) → [`00c26ab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26ab4.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 57.14% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa0f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c26b40"
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
      "00c26b18",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26b20",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00baa0e4",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26b18",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26b20",
      "PARAM",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c26b2c",
      "PARAM",
      [
        "storage",
        "002b613c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa06c.md#insn-00baa0f8) · [`00baa08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa06c.md#insn-00baa08c)
- 新版 `00c26b40`（命令位置の公開資料なし） · `00c26ad4`（命令位置の公開資料なし）

~~~diff
- 00baa0f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:990:8"]]
- 00baa0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00baa0f8 bytes c0ca04f9
+ 00c26b40 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:898:8"]]
+ 00c26b40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00c26b40 bytes c04e04f9
- 00baa08c ["CBRANCH", null, ["local:b9:8", "register:101:1"]]
+ 00c26ad4 ["CBRANCH", null, ["local:b11:8", "register:101:1"]]
- 00baa08c bytes 00040054
+ 00c26ad4 bytes 00040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c497830e4dfa06283f5e8e71cc277f5"></a>

### [`00baa14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa14c.md) → [`00c26b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26b94.md) _ZNKSt6__ndk15ctypeIcE8do_widenEPKcS3_Pc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 77.78% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa164"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c26bac"
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
      "unmatched:00baa164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26bcc"
      ]
    ]
  ],
  "added": [
    [
      "00c26bac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26bcc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa14c.md#insn-00baa164) · [`00baa158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa14c.md#insn-00baa158)
- 新版 `00c26bac`（命令位置の公開資料なし） · `00c26ba0`（命令位置の公開資料なし）

~~~diff
- 00baa164 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00baa164 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00baa164 bytes 03010054
+ 00c26bac ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c26bac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00c26bac bytes 03010054
- 00baa158 ["CBRANCH", null, ["local:b17:8", "register:101:1"]]
+ 00c26ba0 ["CBRANCH", null, ["local:b19:8", "register:101:1"]]
- 00baa158 bytes 00060054
+ 00c26ba0 bytes 00060054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-047ebab73c4c1c06ddee919d194e677d"></a>

### [`00baa230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa230.md) → [`00c26c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26c78.md) _ZNKSt6__ndk15ctypeIcE9do_narrowEPKcS3_cPc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 77.78% / 新版 72.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa2a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c26cec"
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
      "unmatched:00baa2ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26cd0"
      ]
    ]
  ],
  "added": [
    [
      "00c26cf4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c26cd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa230.md#insn-00baa2a4) · [`00baa2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa230.md#insn-00baa2ac)
- 新版 `00c26cec`（命令位置の公開資料なし）

~~~diff
- 00baa2a4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:fffffffffffffff0:8"]]
- 00baa2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00baa2a4 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00baa2a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
- 00baa2a4 bytes 41893fad
- 00baa2ac ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baa2ac ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00baa2ac bytes e1feff54
+ 00c26cec ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:fffffffffffffff0:8"]]
+ 00c26cec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
+ 00c26cec ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00c26cec ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5040:16"]]
+ 00c26cec bytes 41893fad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48ca5f069260ee586dfeef8a3d88c062"></a>

### [`00baa52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa52c.md) → [`00c26f74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c26/00c26f74.md) _ZNKSt6__ndk112ctype_bynameIcE10do_toupperEPcPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.24% / 新版 82.24%

CFGの説明率　旧版 72.00% / 新版 62.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c27070"
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
      "unmatched:00baa574",
      "READ",
      [
        "storage",
        "002b0b10",
        null,
        null
      ]
    ],
    [
      "unmatched:00baa584",
      "READ",
      [
        "storage",
        "002b1670",
        null,
        null
      ]
    ],
    [
      "unmatched:00baa588",
      "READ",
      [
        "storage",
        "002b1a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c26fbc",
      "READ",
      [
        "storage",
        "002c20e0",
        null,
        null
      ]
    ],
    [
      "00c26fcc",
      "READ",
      [
        "storage",
        "002c2cc0",
        null,
        null
      ]
    ],
    [
      "00c26fd0",
      "READ",
      [
        "storage",
        "002c3110",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa52c.md#insn-00baa628) · [`00baa630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa52c.md#insn-00baa630)
- 新版 `00c27070`（命令位置の公開資料なし）

~~~diff
- 00baa628 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fffffffffffffff0:8"]]
- 00baa628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
- 00baa628 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00baa628 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00baa628 bytes 87c13fad
- 00baa630 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baa630 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00baa630 bytes 41fbff54
+ 00c27070 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fffffffffffffff0:8"]]
+ 00c27070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
+ 00c27070 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
+ 00c27070 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
+ 00c27070 bytes 87c13fad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a09c77c8dc9997a2a808b95d1c8eb8f"></a>

### [`00baa6f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa6f4.md) → [`00c2713c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c2713c.md) _ZNKSt6__ndk112ctype_bynameIcE10do_tolowerEPcPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.18% / 新版 83.18%

CFGの説明率　旧版 44.00% / 新版 37.93%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa7f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baa7f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c27238"
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
      "unmatched:00baa724",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c27178"
      ]
    ],
    [
      "unmatched:00baa73c",
      "READ",
      [
        "storage",
        "002b0b10",
        null,
        null
      ]
    ],
    [
      "unmatched:00baa74c",
      "READ",
      [
        "storage",
        "002b1670",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c2716c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c27178"
      ]
    ],
    [
      "00c27184",
      "READ",
      [
        "storage",
        "002c20e0",
        null,
        null
      ]
    ],
    [
      "00c27194",
      "READ",
      [
        "storage",
        "002c2cc0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa6f4.md#insn-00baa724) · [`00baa7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa6f4.md#insn-00baa7f0) · [`00baa7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa6f4.md#insn-00baa7f8)

~~~diff
- 00baa724 ["CBRANCH", null, ["local:b5:8", "register:102:1"]]
- 00baa724 bytes 62000054
- 00baa7f0 ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fffffffffffffff0:8"]]
- 00baa7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:50e0:16"]]
- 00baa7f0 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00baa7f0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5200:16"]]
- 00baa7f0 bytes 87c13fad
- 00baa7f8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baa7f8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00baa7f8 bytes 41fbff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d52bb24530b756daa5750ff413a7eb56"></a>

### [`00baaa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md) → [`00c274b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c274b0.md) _ZNKSt6__ndk112ctype_bynameIwE5do_isEmw

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md) [`00be1a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a50.md) [`00be1a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a60.md) [`00be1a70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a70.md) [`00be1a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a80.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00c5e590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e590.md) [`00c5e630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e630.md) [`00c5e640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e640.md) [`00c5e650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e650.md) [`00c5e660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e660.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 85.00% / 新版 80.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baaa6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baaa6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baaa70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00baaa6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baaa70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baaa74",
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
      "00c274b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c274b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c274bc",
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

- 旧版 [`00baaa6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaa6c) · [`00baaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaa70) · [`00baaa74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baaa68.md#insn-00baaa74)

~~~diff
- 00baaa6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00baaa6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00baaa6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00baaa6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00baaa6c bytes fd7bbda9
- 00baaa70 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00baaa70 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00baaa70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00baaa70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baaa70 bytes f65701a9
- 00baaa74 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00baaa74 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00baaa74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00baaa74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baaa74 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a53671ab48506fbf144d5e3928061139"></a>

### [`00bab2f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab2f4.md) → [`00c27d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27d3c.md) _ZNSt6__ndk17codecvtIcc9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b20.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e700.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00bab308"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c27d50"
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
      "unmatched:00bab308",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1b20"
      ]
    ]
  ],
  "added": [
    [
      "00c27d50",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e700"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab2f4.md#insn-00bab308)
- 新版 `00c27d50`（命令位置の公開資料なし）

~~~diff
- 00bab308 ["INT_ADD", "register:40f0:8", ["const:bab308:8", "const:4:8"]]
- 00bab308 ["CALL", null, ["ram:be1b20:8"]]
- 00bab308 bytes 06da0094
+ 00c27d50 ["INT_ADD", "register:40f0:8", ["const:c27d50:8", "const:4:8"]]
+ 00c27d50 ["CALL", null, ["ram:c5e700:8"]]
+ 00c27d50 bytes 6cda0094
~~~


<a id="compare-5febf0940a97760efcfe35a24aa465cb"></a>

### [`00bab390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab390.md) → [`00c27dd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27dd8.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bdda20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda20.md) [`00be1800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1800.md) · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)
- 新版 呼出元 2件 [`00c5a470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a470.md) [`00c5e3f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e3f0.md) · 呼出先 3件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 14.29% / 新版 14.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bab394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bab394"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bab398"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bab394",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bab398",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bab3ac",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c27ddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c27de0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c27df4",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab390.md#insn-00bab394) · [`00bab398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab390.md#insn-00bab398) · [`00bab3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab390.md#insn-00bab3b8)

~~~diff
- 00bab394 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bab394 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bab394 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bab394 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bab394 bytes fd7bbea9
- 00bab398 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bab398 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bab398 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bab398 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bab398 bytes f44f01a9
- 00bab3b8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bab3b8 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bab3b8 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00bab3b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bab3b8 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e6bb69332535ab393a06ab890dccf62"></a>

### [`00babdd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md) → [`00c28820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c28820.md) _ZNSt6__ndk17codecvtIDsc9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e790`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e790.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00babddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00babddc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00babde0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00babddc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00babde0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00babdec",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1bb0"
      ]
    ]
  ],
  "added": [
    [
      "00c28824",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c28828",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c28834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e790"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00babddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md#insn-00babddc) · [`00babde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md#insn-00babde0) · [`00babdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babdd8.md#insn-00babdec)

~~~diff
- 00babddc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00babddc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00babddc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00babddc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00babddc bytes fd7bbea9
- 00babde0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00babde0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00babde0 bytes f30b00f9
- 00babdec ["INT_ADD", "register:40f0:8", ["const:babdec:8", "const:4:8"]]
- 00babdec ["CALL", null, ["ram:be1bb0:8"]]
- 00babdec bytes 71d70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a56e50515ba1643f7f3714c05f8faae1"></a>

### [`00bacaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md) → [`00c294ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md) FUN_00c294ec

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00baca3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00baca3c.md) [`00bad070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad070.md) [`00bad198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad198.md) [`00bad728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad728.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c29484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29484.md) [`00c29ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29ab8.md) [`00c29be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29be0.md) [`00c2a170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a170.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 97.93% / 新版 97.93%

CFGの説明率　旧版 85.88% / 新版 82.02%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bacb14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2955c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bacb2c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bacb2c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29714"
      ]
    ],
    [
      "unmatched:00bacb44",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29720"
      ]
    ]
  ],
  "added": [
    [
      "00c29574",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29714"
      ]
    ],
    [
      "00c2958c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29720"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bacb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md#insn-00bacb14) · [`00bacb2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md#insn-00bacb2c) · [`00bacb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacaa4.md#insn-00bacb44)

~~~diff
- 00bacb14 ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00bacb14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:8"]]
- 00bacb14 bytes ab0000f9
- 00bacb2c ["CBRANCH", null, ["local:b48:8", "register:102:1"]]
- 00bacb2c bytes 020d0054
- 00bacb44 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bacb44 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bacb44 ["CBRANCH", null, ["local:b50:8", "tmp:1:1"]]
- 00bacb44 bytes a80c0054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7e49494bdd3d20489479c48952f01d8"></a>

### [`00bacd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd2c.md) → [`00c29774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29774.md) FUN_00c29774

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`00bacd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd10.md) [`00bad100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad100.md) [`00bad230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad230.md) [`00bad7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad7c0.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00c29758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29758.md) [`00c29b48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29b48.md) [`00c29c78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29c78.md) [`00c2a208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a208.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.69% / 新版 96.69%

CFGの説明率　旧版 75.00% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bace9c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00baced0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bacef8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bace9c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ],
    [
      "unmatched:00baced0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ],
    [
      "unmatched:00bacef8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ]
  ],
  "added": [
    [
      "00c298e4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ],
    [
      "00c29918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ],
    [
      "00c29940",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c29950"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bace9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd2c.md#insn-00bace9c) · [`00baced0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd2c.md#insn-00baced0) · [`00bacef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacd2c.md#insn-00bacef8)

~~~diff
- 00bace9c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bace9c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bace9c ["CBRANCH", null, ["local:b48:8", "tmp:1:1"]]
- 00bace9c bytes 68030054
- 00baced0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00baced0 ["CBRANCH", null, ["local:b48:8", "tmp:0:1"]]
- 00baced0 bytes c1010054
- 00bacef8 ["CBRANCH", null, ["local:b48:8", "register:102:1"]]
- 00bacef8 bytes 82000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f0648db3a577e82a1ff39a85afe480"></a>

### [`00bacf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacf1c.md) → [`00c29964`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c29964.md) _ZNSt6__ndk17codecvtIDiDu9mbstate_tED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1be0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7c0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bacf30"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c29978"
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
      "unmatched:00bacf30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1be0"
      ]
    ]
  ],
  "added": [
    [
      "00c29978",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e7c0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bacf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bac/00bacf1c.md#insn-00bacf30)
- 新版 `00c29978`（命令位置の公開資料なし）

~~~diff
- 00bacf30 ["INT_ADD", "register:40f0:8", ["const:bacf30:8", "const:4:8"]]
- 00bacf30 ["CALL", null, ["ram:be1be0:8"]]
- 00bacf30 bytes 2cd30094
+ 00c29978 ["INT_ADD", "register:40f0:8", ["const:c29978:8", "const:4:8"]]
+ 00c29978 ["CALL", null, ["ram:c5e7c0:8"]]
+ 00c29978 bytes 92d30094
~~~


<a id="compare-6f117ea9b5337ff7d166b76e26e8d54b"></a>

### [`00bada24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bada24.md) → [`00c2a46c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a46c.md) FUN_00c2a46c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bada04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bada04.md) [`00bae45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae45c.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c2a44c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a44c.md) [`00c2aea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2aea4.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 85.71% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badaf8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2a540"
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
      "unmatched:00badaf8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a54c"
      ]
    ]
  ],
  "added": [
    [
      "00c2a540",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a54c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00badaf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bada24.md#insn-00badaf8) · [`00bada68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bada24.md#insn-00bada68)
- 新版 `00c2a540`（命令位置の公開資料なし） · `00c2a4b0`（命令位置の公開資料なし）

~~~diff
- 00badaf8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00badaf8 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00badaf8 ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
- 00badaf8 bytes 68000054
+ 00c2a540 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c2a540 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c2a540 ["CBRANCH", null, ["local:b18:8", "tmp:1:1"]]
+ 00c2a540 bytes 68000054
- 00bada68 ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
+ 00c2a4b0 ["CBRANCH", null, ["local:b18:8", "register:102:1"]]
- 00bada68 bytes e2040054
+ 00c2a4b0 bytes e2040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15f484dabf317573fccee716eedfa2d5"></a>

### [`00badb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badb28.md) → [`00c2a570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a570.md) _ZNKSt6__ndk115__codecvt_utf16IwLb1EE6do_outER9mbstate_tPKwS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 82.61% / 新版 79.17%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badb80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00badb84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2a5c8"
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
      "unmatched:00badb84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a634"
      ]
    ]
  ],
  "added": [
    [
      "00c2a5cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a634"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00badb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badb28.md#insn-00badb80) · [`00badb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badb28.md#insn-00badb84)
- 新版 `00c2a5c8`（命令位置の公開資料なし）

~~~diff
- 00badb80 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00badb80 ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 00badb80 ["COPY", "tmp:2:1", ["const:0:1"]]
- 00badb80 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 00badb80 bytes 00114bfa
- 00badb84 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00badb84 ["CBRANCH", null, ["local:b14:8", "tmp:0:1"]]
- 00badb84 bytes 43030054
+ 00c2a5c8 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c2a5c8 ["COPY", "tmp:1:1", ["tmp:0:1"]]
+ 00c2a5c8 ["COPY", "tmp:2:1", ["const:0:1"]]
+ 00c2a5c8 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
+ 00c2a5c8 bytes 00114bfa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e8046dcf2bccb66f2e464041867a054"></a>

### [`00badd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badd40.md) → [`00c2a788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a788.md) FUN_00c2a788

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00badd20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badd20.md) [`00bae690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae690.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c2a768`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a768.md) [`00c2b0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b0d8.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 86.21% / 新版 89.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bade14"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2a85c"
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
      "unmatched:00bade14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a868"
      ]
    ]
  ],
  "added": [
    [
      "00c2a85c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2a868"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bade14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badd40.md#insn-00bade14) · [`00badd84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badd40.md#insn-00badd84)
- 新版 `00c2a85c`（命令位置の公開資料なし） · `00c2a7cc`（命令位置の公開資料なし）

~~~diff
- 00bade14 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bade14 ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bade14 ["CBRANCH", null, ["local:b17:8", "tmp:1:1"]]
- 00bade14 bytes 68000054
+ 00c2a85c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c2a85c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
+ 00c2a85c ["CBRANCH", null, ["local:b16:8", "tmp:1:1"]]
+ 00c2a85c bytes 68000054
- 00badd84 ["CBRANCH", null, ["local:b17:8", "register:102:1"]]
+ 00c2a7cc ["CBRANCH", null, ["local:b16:8", "register:102:1"]]
- 00badd84 bytes e2040054
+ 00c2a7cc bytes e2040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c329d013efe83cf139f1e3e63cc0c848"></a>

### [`00badf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badf9c.md) → [`00c2a9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2a9e4.md) _ZNKSt6__ndk115__codecvt_utf16IDsLb0EE9do_lengthER9mbstate_tPKcS5_m

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae01c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2aa64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bae01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badf9c.md#insn-00bae01c) · [`00badfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00badf9c.md#insn-00badfdc)
- 新版 `00c2aa64`（命令位置の公開資料なし） · `00c2aa24`（命令位置の公開資料なし）

~~~diff
- 00bae01c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bae01c ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 00bae01c ["COPY", "tmp:2:1", ["const:2:1"]]
- 00bae01c ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 00bae01c bytes 623144fa
+ 00c2aa64 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c2aa64 ["COPY", "tmp:1:1", ["tmp:0:1"]]
+ 00c2aa64 ["COPY", "tmp:2:1", ["const:2:1"]]
+ 00c2aa64 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
+ 00c2aa64 bytes 623144fa
- 00badfdc ["INT_EQUAL", "tmp:0:1", ["register:4020:8", "const:0:8"]]
- 00badfdc ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00c2aa24 ["INT_EQUAL", "tmp:0:1", ["register:4020:8", "const:0:8"]]
+ 00c2aa24 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00badfdc bytes 640200b4
+ 00c2aa24 bytes 640200b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6891cac360376709c653dc678d5bc572"></a>

### [`00bae04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae04c.md) → [`00c2aa94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2aa94.md) _ZNKSt6__ndk115__codecvt_utf16IDsLb1EE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 83.33% / 新版 78.95%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae0b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2ab00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae0c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bae0c0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2aad0"
      ]
    ]
  ],
  "added": [
    [
      "00c2ab08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2aad0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae04c.md#insn-00bae0b8) · [`00bae0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae04c.md#insn-00bae0c0)
- 新版 `00c2ab00`（命令位置の公開資料なし）

~~~diff
- 00bae0b8 ["COPY", "tmp:0:4", ["register:4060:4"]]
- 00bae0b8 ["INT_ADD", "tmp:1:8", ["register:4028:8", "const:1:8"]]
- 00bae0b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bae0b8 bytes ac040039
- 00bae0c0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bae0c0 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bae0c0 bytes 43feff54
+ 00c2ab00 ["COPY", "tmp:0:4", ["register:4060:4"]]
+ 00c2ab00 ["INT_ADD", "tmp:1:8", ["register:4028:8", "const:1:8"]]
+ 00c2ab00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c2ab00 bytes ac040039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da0cb0c904e177952b89855a909325cb"></a>

### [`00bae0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae0e8.md) → [`00c2ab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2ab30.md) _ZNKSt6__ndk115__codecvt_utf16IDsLb1EE5do_inER9mbstate_tPKcS5_RS5_PDsS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 60.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae164"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2abac"
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
      "unmatched:00bae164",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ab78"
      ]
    ]
  ],
  "added": [
    [
      "00c2abac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ab78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae0e8.md#insn-00bae164) · [`00bae124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae0e8.md#insn-00bae124)
- 新版 `00c2abac`（命令位置の公開資料なし） · `00c2ab6c`（命令位置の公開資料なし）

~~~diff
- 00bae164 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bae164 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
- 00bae164 bytes 63feff54
+ 00c2abac ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c2abac ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00c2abac bytes 63feff54
- 00bae124 ["CBRANCH", null, ["local:b10:8", "register:102:1"]]
+ 00c2ab6c ["CBRANCH", null, ["local:b12:8", "register:102:1"]]
- 00bae124 bytes 22020054
+ 00c2ab6c bytes 22020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa0019c9daa8a00308b52ef83eacd61"></a>

### [`00bae1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae1a4.md) → [`00c2abec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2abec.md) _ZNKSt6__ndk115__codecvt_utf16IDsLb1EE9do_lengthER9mbstate_tPKcS5_m

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 26.32% / 新版 26.32%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae208"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae220"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c2ac50"
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
      "unmatched:00bae208",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ac78"
      ]
    ]
  ],
  "added": [
    [
      "00c2ac50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ac78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae1a4.md#insn-00bae208) · [`00bae220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae1a4.md#insn-00bae220)
- 新版 `00c2ac50`（命令位置の公開資料なし）

~~~diff
- 00bae208 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
- 00bae208 bytes 40010054
- 00bae220 ["COPY", "tmp:0:1", ["register:102:1"]]
- 00bae220 ["COPY", "tmp:1:1", ["const:2:1"]]
- 00bae220 ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 00bae220 ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 00bae220 bytes 022149fa
+ 00c2ac50 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 00c2ac50 bytes 40010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f2f8903d37ff0b45d217aa59a82b701"></a>

### [`00bae338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae338.md) → [`00c2ad80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2ad80.md) _ZNKSt6__ndk115__codecvt_utf16IDiLb0EE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.65% / 新版 93.65%

CFGの説明率　旧版 57.14% / 新版 62.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae39c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae3b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae404"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bae39c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae58"
      ]
    ],
    [
      "unmatched:00bae3b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae1c"
      ]
    ],
    [
      "unmatched:00bae404",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae6c"
      ]
    ]
  ],
  "added": [
    [
      "00c2ade4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae58"
      ]
    ],
    [
      "00c2ae00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae1c"
      ]
    ],
    [
      "00c2ae4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2ae6c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae338.md#insn-00bae39c) · [`00bae3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae338.md#insn-00bae3b8) · [`00bae404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae338.md#insn-00bae404)

~~~diff
- 00bae39c ["CBRANCH", null, ["local:b20:8", "register:102:1"]]
- 00bae39c bytes a2030054
- 00bae3b8 ["CBRANCH", null, ["local:b14:8", "register:101:1"]]
- 00bae3b8 bytes e0000054
- 00bae404 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bae404 ["CBRANCH", null, ["local:b22:8", "tmp:0:1"]]
- 00bae404 bytes 03010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf91ab578ca7476fc6c0c85ad2a2047"></a>

### [`00bae56c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae56c.md) → [`00c2afb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2a/00c2afb4.md) _ZNKSt6__ndk115__codecvt_utf16IDiLb1EE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 11.36% / 新版 16.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae578"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae58c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae5a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bae578",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2afe8"
      ]
    ],
    [
      "unmatched:00bae58c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2afe8"
      ]
    ],
    [
      "unmatched:00bae5a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2b08c"
      ]
    ]
  ],
  "added": [
    [
      "00c2afc0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2afe8"
      ]
    ],
    [
      "00c2afd4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2afe8"
      ]
    ],
    [
      "00c2aff0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c2b08c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bae578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae56c.md#insn-00bae578) · [`00bae58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae56c.md#insn-00bae58c) · [`00bae5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae56c.md#insn-00bae5a8)

~~~diff
- 00bae578 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bae578 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bae578 bytes 4b010054
- 00bae58c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bae58c ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bae58c bytes a1000054
- 00bae5a8 ["CBRANCH", null, ["local:b26:8", "register:102:1"]]
- 00bae5a8 bytes e2040054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-844b9f3a1bfc29eb476e4eae1375d4f9"></a>

### [`00bae73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae73c.md) → [`00c2b184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b184.md) FUN_00c2b184

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bae6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae6cc.md) [`00baee08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee08.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c2b114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b114.md) [`00c2b850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b850.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 99.28% / 新版 99.28%

CFGの説明率　旧版 85.71% / 新版 85.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bae7c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2b20c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bae7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae73c.md#insn-00bae7c4) · [`00bae7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae73c.md#insn-00bae7a8)
- 新版 `00c2b20c`（命令位置の公開資料なし） · `00c2b1f0`（命令位置の公開資料なし）

~~~diff
- 00bae7c4 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00bae7c4 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00bae7c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bae7c4 bytes 4b010039
+ 00c2b20c ["COPY", "tmp:0:4", ["register:4058:4"]]
+ 00c2b20c ["COPY", "tmp:1:8", ["register:4050:8"]]
+ 00c2b20c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c2b20c bytes 4b010039
- 00bae7a8 ["BRANCH", null, ["local:b8:8"]]
+ 00c2b1f0 ["BRANCH", null, ["local:b9:8"]]
- 00bae7a8 bytes 0d000014
+ 00c2b1f0 bytes 0d000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35cc7679ab2f96e05eff4406f6371089"></a>

### [`00baecc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baecc4.md) → [`00c2b70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b70c.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE6do_outER9mbstate_tPKDsS5_RS5_PcS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00babe6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00babe6c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c288b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c28/00c288b4.md)

変更の種類 call_argument_candidate, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00baed08",
      "incomplete_value": true,
      "site": "00baed10",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00baed0c",
      "incomplete_value": true,
      "site": "00baed10",
      "value": [
        "live",
        "register:4050:8"
      ]
    },
    "ordinal": 0,
    "slot": 5
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00baed10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baecc4.md#insn-00baed10) · [`00baed04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baecc4.md#insn-00baed04)
- 新版 `00c2b758`（命令位置の公開資料なし） · `00c2b74c`（命令位置の公開資料なし）

~~~diff
- 00baed10 ["INT_ADD", "register:40f0:8", ["const:baed10:8", "const:4:8"]]
- 00baed10 ["CALL", null, ["callee:00c288b4:8"]]
+ 00c2b758 ["INT_ADD", "register:40f0:8", ["const:c2b758:8", "const:4:8"]]
+ 00c2b758 ["CALL", null, ["callee:00c288b4:8"]]
- 00baed10 bytes 57f4ff97
+ 00c2b758 bytes 57f4ff97
- 00baed04 ["COPY", "register:4000:8", ["register:4048:8"]]
- 00baed04 bytes e00309aa
+ 00c2b74c ["COPY", "register:4000:8", ["register:4048:8"]]
+ 00c2b74c bytes e00309aa
~~~


<a id="compare-15a97b8884695e096b1ba989783571b0"></a>

### [`00baee78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee78.md) → [`00c2b8c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b8c0.md) _ZNKSt6__ndk120__codecvt_utf8_utf16IDiE5do_inER9mbstate_tPKcS5_RS5_PDiS7_RS7_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bae9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00bae9d4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c2b41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b41c.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

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
      "site": "00baeeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baeeac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2b8f4"
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
      "unmatched:00baeeac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baeec4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bae9d4"
      ]
    ]
  ],
  "added": [
    [
      "00c2b8f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00c2b90c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c2b41c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baeeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee78.md#insn-00baeeac) · [`00baeec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baee78.md#insn-00baeec4)
- 新版 `00c2b8f4`（命令位置の公開資料なし）

~~~diff
- 00baeeac ["COPY", "tmp:0:8", ["register:4028:8"]]
- 00baeeac ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00baeeac ["COPY", "tmp:2:8", ["register:8:8"]]
- 00baeeac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baeeac bytes e50b00a9
- 00baeec4 ["INT_ADD", "register:40f0:8", ["const:baeec4:8", "const:4:8"]]
- 00baeec4 ["CALL", null, ["ram:bae9d4:8"]]
- 00baeec4 bytes c4feff97
+ 00c2b8f4 ["COPY", "tmp:0:8", ["register:4028:8"]]
+ 00c2b8f4 ["COPY", "tmp:1:8", ["register:4010:8"]]
+ 00c2b8f4 ["COPY", "tmp:2:8", ["register:8:8"]]
+ 00c2b8f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c2b8f4 bytes e50b00a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-245a97cffd1804cc78798c61a48b1761"></a>

### [`00baef4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef4c.md) → [`00c2b994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b994.md) _ZNSt6__ndk116__narrow_to_utf8ILm16EED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1bf0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7d0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baef50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baef50"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baef54"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00baef50",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baef54",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00baef60",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1bf0"
      ]
    ]
  ],
  "added": [
    [
      "00c2b998",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c2b99c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c2b9a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e7d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baef50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef4c.md#insn-00baef50) · [`00baef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef4c.md#insn-00baef54) · [`00baef60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baef4c.md#insn-00baef60)

~~~diff
- 00baef50 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00baef50 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00baef50 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00baef50 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00baef50 bytes fd7bbea9
- 00baef54 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00baef54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00baef54 bytes f30b00f9
- 00baef60 ["INT_ADD", "register:40f0:8", ["const:baef60:8", "const:4:8"]]
- 00baef60 ["CALL", null, ["ram:be1bf0:8"]]
- 00baef60 bytes 24cb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a3eabb9d1c5198f360355abd2ee1afc"></a>

### [`00baefa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baefa4.md) → [`00c2b9ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2b9ec.md) _ZNSt6__ndk117__widen_from_utf8ILm16EED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c10.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e7f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e7f0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00baefb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2ba00"
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
      "unmatched:00baefb8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1c10"
      ]
    ]
  ],
  "added": [
    [
      "00c2ba00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e7f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baefb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baefa4.md#insn-00baefb8)
- 新版 `00c2ba00`（命令位置の公開資料なし）

~~~diff
- 00baefb8 ["INT_ADD", "register:40f0:8", ["const:baefb8:8", "const:4:8"]]
- 00baefb8 ["CALL", null, ["ram:be1c10:8"]]
- 00baefb8 bytes 16cb0094
+ 00c2ba00 ["INT_ADD", "register:40f0:8", ["const:c2ba00:8", "const:4:8"]]
+ 00c2ba00 ["CALL", null, ["ram:c5e7f0:8"]]
+ 00c2ba00 bytes 7ccb0094
~~~


<a id="compare-01a22dd730d6a4a2839524e6cd0d0fdf"></a>

### [`00baf0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf0a8.md) → [`00c2baf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2baf0.md) _ZNSt6__ndk18numpunctIcED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e820.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00baf0bc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2bb04"
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
      "unmatched:00baf0bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1c40"
      ]
    ]
  ],
  "added": [
    [
      "00c2bb04",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e820"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf0a8.md#insn-00baf0bc)
- 新版 `00c2bb04`（命令位置の公開資料なし）

~~~diff
- 00baf0bc ["INT_ADD", "register:40f0:8", ["const:baf0bc:8", "const:4:8"]]
- 00baf0bc ["CALL", null, ["ram:be1c40:8"]]
- 00baf0bc bytes e1ca0094
+ 00c2bb04 ["INT_ADD", "register:40f0:8", ["const:c2bb04:8", "const:4:8"]]
+ 00c2bb04 ["CALL", null, ["ram:c5e820:8"]]
+ 00c2bb04 bytes 47cb0094
~~~


<a id="compare-9df1029121654d6ff94a8ef634cef344"></a>

### [`00baf124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf124.md) → [`00c2bb6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bb6c.md) _ZNSt6__ndk18numpunctIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e840.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00baf138"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2bb80"
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
      "unmatched:00baf138",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1c60"
      ]
    ]
  ],
  "added": [
    [
      "00c2bb80",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e840"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf124.md#insn-00baf138)
- 新版 `00c2bb80`（命令位置の公開資料なし）

~~~diff
- 00baf138 ["INT_ADD", "register:40f0:8", ["const:baf138:8", "const:4:8"]]
- 00baf138 ["CALL", null, ["ram:be1c60:8"]]
- 00baf138 bytes caca0094
+ 00c2bb80 ["INT_ADD", "register:40f0:8", ["const:c2bb80:8", "const:4:8"]]
+ 00c2bb80 ["CALL", null, ["ram:c5e840:8"]]
+ 00c2bb80 bytes 30cb0094
~~~


<a id="compare-2513b25f35867d16205e11a95282af3a"></a>

### [`00baf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf1b0.md) → [`00c2bbf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bbf8.md) _ZNKSt6__ndk18numpunctIwE11do_groupingEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf1c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2bc10"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00baf1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf1b0.md#insn-00baf1c8) · [`00baf1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf1b0.md#insn-00baf1bc)
- 新版 `00c2bc10`（命令位置の公開資料なし） · `00c2bc04`（命令位置の公開資料なし）

~~~diff
- 00baf1c8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00baf1c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00baf1c8 bytes 0001803d
+ 00c2bc10 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c2bc10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
+ 00c2bc10 bytes 0001803d
- 00baf1bc ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
- 00baf1bc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00baf1bc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00baf1bc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00c2bc04 ["INT_RIGHT", "tmp:0:4", ["register:4050:4", "const:0:4"]]
+ 00c2bc04 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00c2bc04 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00c2bc04 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00baf1bc bytes ca000037
+ 00c2bc04 bytes ca000037
~~~


<a id="compare-43eb8fcacd8a2258191ad73c439e883e"></a>

### [`00baf358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf358.md) → [`00c2bda0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2b/00c2bda0.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e850.md)

変更の種類 comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

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
      "site": "00baf38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf38c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2bdd4"
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
      "00c2bdc8",
      "READ",
      [
        "storage",
        "00c1bfc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00baf38c",
      "DATA",
      [
        "storage",
        "00c13c18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2bdc8",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2bdd4",
      "DATA",
      [
        "storage",
        "00c935c0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf38c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf358.md#insn-00baf38c) · [`00baf3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf358.md#insn-00baf3a0)
- 新版 `00c2bdd4`（命令位置の公開資料なし）

~~~diff
- 00baf38c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00baf38c ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00baf38c ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00baf38c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baf38c bytes 082400a9
- 00baf3a0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00baf3a0 ["RETURN", null, ["register:0:8"]]
- 00baf3a0 bytes c0035fd6
+ 00c2bdd4 ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00c2bdd4 ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00c2bdd4 ["COPY", "tmp:2:8", ["register:4000:8"]]
+ 00c2bdd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
+ 00c2bdd4 bytes 082400a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cff39eff4c17fed432f6b4046de0b832"></a>

### [`00baf68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf68c.md) → [`00c2c0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c0d4.md) _ZNSt6__ndk115numpunct_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1880.md) · 呼出先 1件 [`00be1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c70.md)
- 新版 呼出元 1件 [`00c5e470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e470.md) · 呼出先 1件 [`00c5e850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e850.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

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
      "site": "00baf6b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf6b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf6c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00baf6b4",
      "READ",
      [
        "storage",
        "00c1bfc8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00baf6c0",
      "DATA",
      [
        "storage",
        "00c13c18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00c2c0fc",
      "READ",
      [
        "storage",
        "00c9b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00c2c108",
      "DATA",
      [
        "storage",
        "00c935c0",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf68c.md#insn-00baf6b8) · [`00baf6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf68c.md#insn-00baf6c0)
- 新版 `00c2c100`（命令位置の公開資料なし）

~~~diff
- 00baf6b8 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00baf6b8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00baf6b8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00baf6b8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00baf6b8 bytes 1ffc01a9
- 00baf6c0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00baf6c0 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00baf6c0 ["COPY", "tmp:2:8", ["register:4000:8"]]
- 00baf6c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00baf6c0 bytes 082400a9
+ 00c2c100 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00c2c100 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00c2c100 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00c2c100 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 00c2c100 bytes 1ffc01a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5327f67744bd8b53e95444b416dba31a"></a>

### [`00baf6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf6fc.md) → [`00c2c144`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c144.md) _ZNSt6__ndk115numpunct_bynameIcED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e870`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e870.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf710"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c2c158"
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
      "unmatched:00baf710",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1c90"
      ]
    ]
  ],
  "added": [
    [
      "00c2c158",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e870"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf6fc.md#insn-00baf710)
- 新版 `00c2c158`（命令位置の公開資料なし）

~~~diff
- 00baf710 ["INT_ADD", "register:40f0:8", ["const:baf710:8", "const:4:8"]]
- 00baf710 ["CALL", null, ["ram:be1c90:8"]]
- 00baf710 bytes 60c90094
+ 00c2c158 ["INT_ADD", "register:40f0:8", ["const:c2c158:8", "const:4:8"]]
+ 00c2c158 ["CALL", null, ["ram:c5e870:8"]]
+ 00c2c158 bytes c6c90094
~~~


<a id="compare-ba21d8bfeb4812094aa0a85178a63746"></a>

### [`00baf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md) → [`00c2c170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c170.md) FUN_00c2c170

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00baf7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf7b4.md) [`00bb6910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb6/00bb6910.md) [`00bb760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb760c.md) · 呼出先 1件 [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)
- 新版 呼出元 3件 [`00c2c1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c1fc.md) [`00c33358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33358.md) [`00c34054`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34054.md) · 呼出先 1件 [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf72c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00baf72c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c2c174"
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
      "unmatched:00baf72c",
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
      "00c2c174",
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

- 旧版 [`00baf72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md#insn-00baf72c) · [`00baf730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md#insn-00baf730)
- 新版 `00c2c174`（命令位置の公開資料なし）

~~~diff
- 00baf72c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00baf72c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00baf72c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00baf72c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00baf72c bytes fd7bbfa9
+ 00c2c174 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c2c174 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c2c174 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c2c174 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c2c174 bytes fd7bbfa9
- 00baf730 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00baf730 bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09faf1f88f6130dd3e51a84d8dfaf086"></a>

### [`00bafa34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa34.md) → [`00c2c47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c2c/00c2c47c.md) _ZNSt6__ndk115numpunct_bynameIwED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1cb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e890.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bafa38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bafa38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bafa3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bafa38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bafa3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bafa48",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1cb0"
      ]
    ]
  ],
  "added": [
    [
      "00c2c480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c2c484",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c2c490",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e890"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa34.md#insn-00bafa38) · [`00bafa3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa34.md#insn-00bafa3c) · [`00bafa48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa34.md#insn-00bafa48)

~~~diff
- 00bafa38 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bafa38 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bafa38 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bafa38 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bafa38 bytes fd7bbea9
- 00bafa3c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bafa3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bafa3c bytes f30b00f9
- 00bafa48 ["INT_ADD", "register:40f0:8", ["const:bafa48:8", "const:4:8"]]
- 00bafa48 ["CALL", null, ["ram:be1cb0:8"]]
- 00bafa48 bytes 9ac80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f04a3d1efd5ac83c0f87af1af66f272"></a>

### [`00bb51d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb51d4.md) → [`00c31c1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c1c.md) _ZNSt6__ndk112ctype_bynameIwED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00be1a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a40.md) [`00be1d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d40.md) · 呼出先 2件 [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md)
- 新版 呼出元 2件 [`00c5e620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e620.md) [`00c5e920`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e920.md) · 呼出先 2件 [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

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
      "site": "00bb51f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c31c40"
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
      "unmatched:00bb51ec",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb51f8",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "unmatched:00bb5210",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1a20"
      ]
    ]
  ],
  "added": [
    [
      "00c31c34",
      "READ",
      [
        "storage",
        "00c9b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00c31c40",
      "DATA",
      [
        "storage",
        "00c93438",
        null,
        "undefined1[136]"
      ]
    ],
    [
      "00c31c58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e600"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb51f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb51d4.md#insn-00bb51f8) · [`00bb51e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb51d4.md#insn-00bb51e4)
- 新版 `00c31c40`（命令位置の公開資料なし） · `00c31c2c`（命令位置の公開資料なし）

~~~diff
- 00bb51f8 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00bb51f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb51f8 bytes 680200f9
+ 00c31c40 ["COPY", "tmp:0:8", ["register:4098:8"]]
+ 00c31c40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c31c40 bytes 680200f9
- 00bb51e4 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00c31c2c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00bb51e4 bytes 280300d0
+ 00c31c2c bytes 480300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86b4c36220a9f4e54c73c095d5980ab7"></a>

### [`00bb5218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5218.md) → [`00c31c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c31/00c31c60.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be18b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18b0.md) · 呼出先 6件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be1a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a20.md) [`00be1a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a30.md) [`00be1cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cd0.md)
- 新版 呼出元 1件 [`00c5e4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e4a0.md) · 呼出先 6件 [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5e600`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e600.md) [`00c5e610`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e610.md) [`00c5e8b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e8b0.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.27% / 新版 70.27%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5264"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5284"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c31cac"
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
      "unmatched:00bb5258",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1a30"
      ]
    ],
    [
      "unmatched:00bb5264",
      "DATA",
      [
        "storage",
        "00c15f78",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00bb5264",
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
      "00c31ca0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e610"
      ]
    ],
    [
      "00c31cac",
      "DATA",
      [
        "storage",
        "00c95920",
        null,
        "undefined *"
      ]
    ],
    [
      "00c31cac",
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

- 旧版 [`00bb5258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5218.md#insn-00bb5258) · [`00bb5264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5218.md#insn-00bb5264) · [`00bb5284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5218.md#insn-00bb5284)

~~~diff
- 00bb5258 ["INT_ADD", "register:40f0:8", ["const:bb5258:8", "const:4:8"]]
- 00bb5258 ["CALL", null, ["ram:be1a30:8"]]
- 00bb5258 bytes f6b10094
- 00bb5264 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bb5264 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb5264 bytes e80700f9
- 00bb5284 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bb5284 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb5284 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47aa4d6059cf8dfd3f1ff0b2ca9dff6e"></a>

### [`00bb5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5b68.md) → [`00c325b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c325b0.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d70.md) · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)
- 新版 呼出元 1件 [`00c5e950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e950.md) · 呼出先 4件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 38.89% / 新版 38.89%

CFGの説明率　旧版 9.09% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5be4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3262c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb5b94"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb5b88",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bb5b94",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c32608"
      ]
    ],
    [
      "unmatched:00bb5b98",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c325d0",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c325dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c32608"
      ]
    ],
    [
      "00c325e0",
      "READ",
      [
        "storage",
        "01127898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5b68.md#insn-00bb5b94) · [`00bb5ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5b68.md#insn-00bb5ba0) · [`00bb5bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb5/00bb5b68.md#insn-00bb5bc8)

~~~diff
- 00bb5b94 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bb5b94 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bb5b94 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bb5b94 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bb5b94 bytes 68010036
- 00bb5ba0 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bb5ba0 bytes 60000054
- 00bb5bc8 ["INT_ADD", "register:40f0:8", ["const:bb5bc8:8", "const:4:8"]]
- 00bb5bc8 ["CALL", null, ["callee:00c57a50:8"]]
- 00bb5bc8 bytes 0e950094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a90fe354051a71d595d540fc606f00b0"></a>

### [`00bb7dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dc0.md) → [`00c34808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34808.md) FUN_00c34808

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7dc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7dc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb7dc4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb7dc8",
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
      "00c3480c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c34810",
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

- 旧版 [`00bb7dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dc0.md#insn-00bb7dc4) · [`00bb7dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7dc0.md#insn-00bb7dc8)
- 新版 `00c3480c`（命令位置の公開資料なし）

~~~diff
- 00bb7dc4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb7dc4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb7dc4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb7dc4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb7dc4 bytes fd7bbea9
- 00bb7dc8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bb7dc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bb7dc8 bytes f30b00f9
+ 00c3480c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c3480c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c3480c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c3480c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c3480c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b65955859aed7559ac92ddfceb03abf8"></a>

### [`00bb7f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f4c.md) → [`00c34994`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34994.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bdda30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda30.md) [`00be1b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1b30.md) · 呼出先 5件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)
- 新版 呼出元 2件 [`00c5a480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a480.md) [`00c5e710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e710.md) · 呼出先 5件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f00.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md) [`00c5ce20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5ce20.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 36.59% / 新版 36.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7f78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb7fdc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c349c0"
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
      "unmatched:00bb7f6c",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bb7f78",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "unmatched:00bb7f84",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c349b4",
      "READ",
      [
        "storage",
        "00c9b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00c349c0",
      "DATA",
      [
        "storage",
        "00c934c0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00c349cc",
      "READ",
      [
        "storage",
        "011278a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f4c.md#insn-00bb7f78) · [`00bb7f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f4c.md#insn-00bb7f88) · [`00bb7f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb7f4c.md#insn-00bb7f94)

~~~diff
- 00bb7f78 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bb7f78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb7f78 bytes 080000f9
- 00bb7f88 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bb7f88 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bb7f88 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bb7f88 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bb7f88 bytes 88010036
- 00bb7f94 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00bb7f94 bytes 60000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb719493c1c0aa0f38af981b6361734d"></a>

### [`00bb8724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md) → [`00c3516c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3516c.md) FUN_00c3516c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb8690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8690.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c350d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c350d8.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb872c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb8728",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb872c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb8738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bb8690"
      ]
    ]
  ],
  "added": [
    [
      "00c35170",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c35174",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c35180",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c350d8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md#insn-00bb8728) · [`00bb872c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md#insn-00bb872c) · [`00bb8738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8724.md#insn-00bb8738)

~~~diff
- 00bb8728 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb8728 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb8728 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb8728 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb8728 bytes fd7bbea9
- 00bb872c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bb872c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bb872c bytes f30b00f9
- 00bb8738 ["INT_ADD", "register:40f0:8", ["const:bb8738:8", "const:4:8"]]
- 00bb8738 ["CALL", null, ["ram:bb8690:8"]]
- 00bb8738 bytes d6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995d5d9f28aa90196159c4acd7bf9aaa"></a>

### [`00bb87e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md) → [`00c3522c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3522c.md) FUN_00c3522c

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb8750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8750.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c35198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35198.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb87ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb87e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb87ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bb87f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bb8750"
      ]
    ]
  ],
  "added": [
    [
      "00c35230",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c35234",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c35240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c35198"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb87e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md#insn-00bb87e8) · [`00bb87ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md#insn-00bb87ec) · [`00bb87f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb87e4.md#insn-00bb87f8)

~~~diff
- 00bb87e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bb87e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bb87e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bb87e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bb87e8 bytes fd7bbea9
- 00bb87ec ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bb87ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bb87ec bytes f30b00f9
- 00bb87f8 ["INT_ADD", "register:40f0:8", ["const:bb87f8:8", "const:4:8"]]
- 00bb87f8 ["CALL", null, ["ram:bb8750:8"]]
- 00bb87f8 bytes d6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01725b229066c7f507710d9e0fa370e6"></a>

### [`00bb88a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88a4.md) → [`00c352ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c352ec.md) FUN_00c352ec

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bb8810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8810.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c35258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35258.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00bb88b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c35300"
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
      "unmatched:00bb88b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bb8810"
      ]
    ]
  ],
  "added": [
    [
      "00c35300",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c35258"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb88b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb88a4.md#insn-00bb88b8)
- 新版 `00c35300`（命令位置の公開資料なし）

~~~diff
- 00bb88b8 ["INT_ADD", "register:40f0:8", ["const:bb88b8:8", "const:4:8"]]
- 00bb88b8 ["CALL", null, ["ram:bb8810:8"]]
- 00bb88b8 bytes d6ffff97
+ 00c35300 ["INT_ADD", "register:40f0:8", ["const:c35300:8", "const:4:8"]]
+ 00c35300 ["CALL", null, ["ram:c35258:8"]]
+ 00c35300 bytes d6ffff97
~~~


<a id="compare-c381876adb2bff188790c9b7fa8933fa"></a>

### [`00bb8a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a38.md) → [`00c35480`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35480.md) FUN_00c35480

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5e170`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e170.md)

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 33.33% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c354a0"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a38.md#insn-00bb8a58) · [`00bb8a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a38.md#insn-00bb8a4c)
- 新版 `00c354a0`（命令位置の公開資料なし） · `00c35494`（命令位置の公開資料なし）

~~~diff
- 00bb8a58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb8a58 ["RETURN", null, ["register:0:8"]]
- 00bb8a58 bytes c0035fd6
+ 00c354a0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c354a0 ["RETURN", null, ["register:0:8"]]
+ 00c354a0 bytes c0035fd6
- 00bb8a4c ["INT_ADD", "register:40f0:8", ["const:bb8a4c:8", "const:4:8"]]
- 00bb8a4c ["CALL", null, ["callee:00c5e170:8"]]
+ 00c35494 ["INT_ADD", "register:40f0:8", ["const:c35494:8", "const:4:8"]]
+ 00c35494 ["CALL", null, ["callee:00c5e170:8"]]
- 00bb8a4c bytes cda20094
+ 00c35494 bytes 37a30094
~~~


<a id="compare-126d945e1ee4ef6bd76258b6673a431f"></a>

### [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) → [`00c3561c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c3561c.md) FUN_00c3561c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 54件 [`00ba082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba082c.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md) · 呼出先 6件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00bb8a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 54件 [`00c1d274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1d/00c1d274.md) [`00c1f7a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f7a8.md) [`00c1f8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1f8d4.md) [`00c1fa00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fa00.md) [`00c1fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1f/00c1fb2c.md) · 呼出先 6件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00c354a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c354a8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 76.00% / 新版 70.37%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb8ce4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c3572c"
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
      "unmatched:00bb8ce4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c35754"
      ]
    ]
  ],
  "added": [
    [
      "00c3572c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c35754"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md#insn-00bb8ce4) · [`00bb8bfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md#insn-00bb8bfc)
- 新版 `00c3572c`（命令位置の公開資料なし） · `00c35644`（命令位置の公開資料なし）

~~~diff
- 00bb8ce4 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00bb8ce4 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00bb8ce4 bytes 400100b4
+ 00c3572c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00c3572c ["CBRANCH", null, ["local:b18:8", "tmp:0:1"]]
+ 00c3572c bytes 400100b4
- 00bb8bfc ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bb8bfc ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00bb8bfc ["CBRANCH", null, ["local:b6:8", "tmp:1:1"]]
+ 00c35644 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c35644 ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
+ 00c35644 ["CBRANCH", null, ["local:b7:8", "tmp:1:1"]]
- 00bb8bfc bytes 29030054
+ 00c35644 bytes 29030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3dd0cd38bdd61e241ac8ae55cf63fe7"></a>

### [`00bb92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md) → [`00c35ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c35/00c35ce8.md) FUN_00c35ce8

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bb70c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb7/00bb70c4.md) · 呼出先 2件 [`00b75a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75a68.md) [`00b771b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b77/00b771b0.md)
- 新版 呼出元 1件 [`00c33b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c33/00c33b0c.md) · 呼出先 2件 [`00bf24b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf2/00bf24b0.md) [`00bf3bf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf3/00bf3bf8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 78.26% / 新版 78.26%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb92c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb92cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c35d0c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bb92c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md#insn-00bb92c4) · [`00bb92cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md#insn-00bb92cc) · [`00bb92f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb92a0.md#insn-00bb92f4)

~~~diff
- 00bb92c4 ["COPY", "tmp:0:8", ["register:4050:8"]]
- 00bb92c4 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb92c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb92c4 ["COPY", "register:4098:8", ["tmp:0:8"]]
- 00bb92c4 bytes 5301899a
- 00bb92cc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bb92cc ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bb92cc ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00bb92cc ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00bb92cc bytes 08018b9a
- 00bb92f4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bb92f4 ["RETURN", null, ["register:0:8"]]
- 00bb92f4 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2d8d9ddd10463d0b38f5192ba4b7e2b"></a>

### [`00bba00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md) → [`00c36a54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36a54.md) FUN_00c36a54

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bb82c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82c4.md) [`00bb82f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb82f4.md) · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)
- 新版 呼出元 2件 [`00c34d0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d0c.md) [`00c34d3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c34/00c34d3c.md) · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cdd0.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 63.44% / 新版 67.05%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba010"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba014"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bba010",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba014",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c36c28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c36af0"
      ]
    ]
  ],
  "added": [
    [
      "00c36a58",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c36a5c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c36be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c36af0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md#insn-00bba010) · [`00bba014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md#insn-00bba014) · [`00bba1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba00c.md#insn-00bba1e0)

~~~diff
- 00bba010 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bba010 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bba010 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bba010 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bba010 bytes fd7bbea9
- 00bba014 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bba014 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bba014 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bba014 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bba014 bytes f44f01a9
- 00bba1e0 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00bba1e0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00bba1e0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00bba1e0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00bba1e0 bytes 48f70736
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac74684ee44b9b5c57ab006db60f017"></a>

### [`00bba3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba3ac.md) → [`00c36df4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36df4.md) _ZNSt6__ndk111regex_errorC1ENS_15regex_constants10error_typeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd960.md) · 呼出先 1件 [`00bdda80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda80.md)
- 新版 呼出元 1件 [`00c5a3b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3b0.md) · 呼出先 1件 [`00c5a4d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a4d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 29.63% / 新版 29.63%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba3b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba3b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba3b4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bba3b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba3b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba3cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bba3e4"
      ]
    ]
  ],
  "added": [
    [
      "00c36df8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c36dfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c36e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c36e2c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba3ac.md#insn-00bba3b0) · [`00bba3b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba3ac.md#insn-00bba3b4) · [`00bba3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba3ac.md#insn-00bba3cc)

~~~diff
- 00bba3b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bba3b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bba3b0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bba3b0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bba3b0 bytes fd7bbea9
- 00bba3b4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00bba3b4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00bba3b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00bba3b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bba3b4 bytes f44f01a9
- 00bba3cc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bba3cc ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bba3cc ["CBRANCH", null, ["local:b4:8", "tmp:1:1"]]
- 00bba3cc bytes c8000054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edcafeb58b7f6a4818af521b1b4d9e83"></a>

### [`00bba420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md) → [`00c36e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36e68.md) _ZNSt6__ndk111regex_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdd970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd970.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5a3c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3c0.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bba424",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba428",
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
      "00c36e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c36e70",
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

- 旧版 [`00bba424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md#insn-00bba424) · [`00bba428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba420.md#insn-00bba428)
- 新版 `00c36e6c`（命令位置の公開資料なし）

~~~diff
- 00bba424 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bba424 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bba424 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bba424 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bba424 bytes fd7bbea9
- 00bba428 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bba428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bba428 bytes f30b00f9
+ 00c36e6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c36e6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c36e6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c36e6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c36e6c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea020ca03e8f7b74bcf9c4bae4a48103"></a>

### [`00bba5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba5b0.md) → [`00c36ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c36/00c36ff8.md) _ZNKSt6__ndk123__match_any_but_newlineIcE6__execERNS_7__stateIcEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 65.00% / 新版 65.00%

CFGの説明率　旧版 10.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba5f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba5f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3703c"
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
      "unmatched:00bba5bc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3701c"
      ]
    ]
  ],
  "added": [
    [
      "00c37004",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c3701c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba5b0.md#insn-00bba5bc) · [`00bba5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba5b0.md#insn-00bba5f4) · [`00bba5f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba5b0.md#insn-00bba5f8)

~~~diff
- 00bba5bc ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bba5bc bytes c0000054
- 00bba5f4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:10:8"]]
- 00bba5f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bba5f4 bytes 2a0800f9
- 00bba5f8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
- 00bba5f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bba5f8 bytes 282800f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e77e039b87e051343a2030a754e5c7"></a>

### [`00bba600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba600.md) → [`00c37048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37048.md) _ZNKSt6__ndk123__match_any_but_newlineIwE6__execERNS_7__stateIwEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 22.22% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c37098"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba620"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bba620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba600.md#insn-00bba620) · [`00bba650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba600.md#insn-00bba650) · [`00bba654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba600.md#insn-00bba654)

~~~diff
- 00bba620 ["COPY", "tmp:0:1", ["register:102:1"]]
- 00bba620 ["COPY", "tmp:1:1", ["const:4:1"]]
- 00bba620 ["INT_AND", "tmp:2:1", ["tmp:1:1", "const:8:1"]]
- 00bba620 ["INT_EQUAL", "register:100:1", ["tmp:2:1", "const:8:1"]]
- 00bba620 bytes 24294d7a
- 00bba650 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:50:8"]]
- 00bba650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bba650 bytes 282800f9
- 00bba654 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bba654 ["RETURN", null, ["register:0:8"]]
- 00bba654 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdd3b4e5d2372aef0a0cd06d81f712de"></a>

### [`00bba658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba658.md) → [`00c370a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370a0.md) __cxa_bad_cast

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdce90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce90.md) · 呼出先 4件 [`00bbb0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb0fc.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be1480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1480.md)
- 新版 呼出元 1件 [`00c598e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c598e0.md) · 呼出先 4件 [`00c37b44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b44.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e080.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 3件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba65c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba65c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba660"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bba65c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba660",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bba66c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57af0"
      ]
    ]
  ],
  "added": [
    [
      "00c370a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c370a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c370b4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57af0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba65c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba658.md#insn-00bba65c) · [`00bba660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba658.md#insn-00bba660) · [`00bba66c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba658.md#insn-00bba66c)

~~~diff
- 00bba65c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bba65c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bba65c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bba65c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bba65c bytes fd7bbea9
- 00bba660 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bba660 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bba660 bytes f30b00f9
- 00bba66c ["INT_ADD", "register:40f0:8", ["const:bba66c:8", "const:4:8"]]
- 00bba66c ["CALL", null, ["callee:00c57af0:8"]]
- 00bba66c bytes 8d820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-089a40a37c5a812e1e70f35663315068"></a>

### [`00bba690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba690.md) → [`00c370d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c370d8.md) __cxa_bad_typeid

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb158.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00be1db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1db0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c37ba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ba0.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c5e970`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e970.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba6ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba6c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c370f4"
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
      "unmatched:00bba6ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1db0"
      ]
    ],
    [
      "unmatched:00bba6bc",
      "READ",
      [
        "storage",
        "00c1bfe8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bba6bc",
      "PARAM",
      [
        "storage",
        "00c16bf8",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00c370f4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e970"
      ]
    ],
    [
      "00c37104",
      "READ",
      [
        "storage",
        "00c9ba18",
        null,
        "pointer"
      ]
    ],
    [
      "00c37104",
      "PARAM",
      [
        "storage",
        "00c965a0",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba690.md#insn-00bba6ac) · [`00bba6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba690.md#insn-00bba6c4)
- 新版 `00c370f4`（命令位置の公開資料なし）

~~~diff
- 00bba6ac ["INT_ADD", "register:40f0:8", ["const:bba6ac:8", "const:4:8"]]
- 00bba6ac ["CALL", null, ["ram:be1db0:8"]]
- 00bba6ac bytes c19d0094
- 00bba6c4 ["INT_ADD", "register:40f0:8", ["const:bba6c4:8", "const:4:8"]]
- 00bba6c4 ["CALL", null, ["callee:00c57b10:8"]]
- 00bba6c4 bytes 7f820094
+ 00c370f4 ["INT_ADD", "register:40f0:8", ["const:c370f4:8", "const:4:8"]]
+ 00c370f4 ["CALL", null, ["ram:c5e970:8"]]
+ 00c370f4 bytes 1f9e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3d94563b0310c7d3f9bb232bd74bf24"></a>

### [`00bba6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba6c8.md) → [`00c37110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37110.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md) [`00c57c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c30.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bba6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c37144"
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
      "unmatched:00bba6f4",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bba6f4",
      "PARAM",
      [
        "storage",
        "00c16908",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00bba6f8",
      "READ",
      [
        "storage",
        "00c1ade8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c3713c",
      "READ",
      [
        "storage",
        "00c9a7d0",
        null,
        "pointer"
      ]
    ],
    [
      "00c3713c",
      "PARAM",
      [
        "storage",
        "00c962b0",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00c37140",
      "READ",
      [
        "storage",
        "00c9a7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba6c8.md#insn-00bba6fc) · [`00bba6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba6c8.md#insn-00bba6dc)
- 新版 `00c37144`（命令位置の公開資料なし） · `00c37124`（命令位置の公開資料なし）

~~~diff
- 00bba6fc ["INT_ADD", "register:40f0:8", ["const:bba6fc:8", "const:4:8"]]
- 00bba6fc ["CALL", null, ["callee:00c57b10:8"]]
- 00bba6fc bytes 71820094
+ 00c37144 ["INT_ADD", "register:40f0:8", ["const:c37144:8", "const:4:8"]]
+ 00c37144 ["CALL", null, ["callee:00c57b10:8"]]
+ 00c37144 bytes 73820094
- 00bba6dc ["INT_ADD", "register:40f0:8", ["const:bba6dc:8", "const:4:8"]]
- 00bba6dc ["CALL", null, ["callee:00c57af0:8"]]
+ 00c37124 ["INT_ADD", "register:40f0:8", ["const:c37124:8", "const:4:8"]]
+ 00c37124 ["CALL", null, ["callee:00c57af0:8"]]
- 00bba6dc bytes 71820094
+ 00c37124 bytes 73820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d15109b3cc55594335129ef16dcc3266"></a>

### [`00bbaaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaaa0.md) → [`00c374e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374e8.md) _ZSt15get_new_handlerv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e20.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5e9e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e9e0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaab0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c374f8"
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
      "unmatched:00bbaaa8",
      "READ",
      [
        "storage",
        "00c1c008",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbaaac",
      "READ",
      [
        "storage",
        "010a3758",
        "__cxa_new_handler",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c374f0",
      "READ",
      [
        "storage",
        "00c9ba38",
        null,
        "pointer"
      ]
    ],
    [
      "00c374f4",
      "READ",
      [
        "storage",
        "01128660",
        "__cxa_new_handler",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaaa0.md#insn-00bbaab0) · [`00bbaaa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaaa0.md#insn-00bbaaa4)
- 新版 `00c374f8`（命令位置の公開資料なし）

~~~diff
- 00bbaab0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbaab0 ["RETURN", null, ["register:0:8"]]
- 00bbaab0 bytes c0035fd6
+ 00c374f8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c374f8 ["RETURN", null, ["register:0:8"]]
+ 00c374f8 bytes c0035fd6
- 00bbaaa4 ["COPY", "register:4040:8", ["const:c1c000:8"]]
- 00bbaaa4 bytes 080300d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4145e9b4b96d1d4299626075b3272b7"></a>

### [`00bbac00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md) → [`00c37648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md) FUN_00c37648

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bba9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bba9d0.md) [`00bbaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa40.md) [`00bbac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md) · 呼出先 1件 [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 3件 [`00c37418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37418.md) [`00c37488`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37488.md) [`00c37668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37668.md) · 呼出先 1件 [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbac04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbac04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbac18"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbac04",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbac18",
      "WRITE",
      [
        "storage",
        "00c249a0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbac18",
      "DATA",
      [
        "storage",
        "002a123a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3764c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37660",
      "WRITE",
      [
        "storage",
        "00ca4480",
        null,
        "pointer"
      ]
    ],
    [
      "00c37660",
      "DATA",
      [
        "storage",
        "002b1886",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md#insn-00bbac04) · [`00bbac18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md#insn-00bbac18) · [`00bbac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md#insn-00bbac1c)

~~~diff
- 00bbac04 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbac04 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbac04 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbac04 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbac04 bytes fd7bbfa9
- 00bbac18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9a0:8"]]
- 00bbac18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bbac18 bytes 09d104f9
- 00bbac1c ["INT_ADD", "register:40f0:8", ["const:bbac1c:8", "const:4:8"]]
- 00bbac1c ["CALL", null, ["callee:00c57c20:8"]]
- 00bbac1c bytes 6d810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-058602ed7f4d29342fac1e7d58382c96"></a>

### [`00bbac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md) → [`00c37668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37668.md) _ZSt14set_unexpectedPFvvE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbac00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac00.md) [`00bd6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6dd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c37648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37648.md) [`00c53820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53820.md)

変更の種類 cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbac3c",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbac3c",
      "PARAM",
      [
        "storage",
        "00c24998",
        "__cxa_unexpected_handler",
        "pointer"
      ]
    ],
    [
      "00c37688",
      "PARAM",
      [
        "storage",
        "00bbac00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c37684",
      "READ",
      [
        "storage",
        "00c9ba28",
        null,
        "pointer"
      ]
    ],
    [
      "00c37684",
      "PARAM",
      [
        "storage",
        "00ca4478",
        "__cxa_unexpected_handler",
        "pointer"
      ]
    ],
    [
      "00c37688",
      "PARAM",
      [
        "storage",
        "00c37648",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md#insn-00bbac2c) · [`00bbac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md#insn-00bbac38) · [`00bbac3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md#insn-00bbac3c)
- 新版 `00c37674`（命令位置の公開資料なし） · `00c37680`（命令位置の公開資料なし）

~~~diff
- 00bbac2c ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00c37674 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00bbac2c bytes 010300b0
+ 00c37674 bytes 21030090
- 00bbac38 ["COPY", "register:4040:8", ["const:bbac00:8"]]
+ 00c37680 ["COPY", "register:4040:8", ["const:c37648:8"]]
- 00bbac38 bytes 48feff10
+ 00c37680 bytes 48feff10
- 00bbac3c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
- 00bbac3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbac3c bytes 21fc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-435ed209b6b15648315b2f9258268da9"></a>

### [`00bbac88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md) → [`00c376d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c376d0.md) _ZSt15set_new_handlerPFvvE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6dd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53820.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbac8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbac8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c376d4"
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
      "unmatched:00bbac8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbac98",
      "READ",
      [
        "storage",
        "00c1c008",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbac98",
      "PARAM",
      [
        "storage",
        "010a3758",
        "__cxa_new_handler",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00c376d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c376e0",
      "READ",
      [
        "storage",
        "00c9ba38",
        null,
        "pointer"
      ]
    ],
    [
      "00c376e0",
      "PARAM",
      [
        "storage",
        "01128660",
        "__cxa_new_handler",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbac8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md#insn-00bbac8c) · [`00bbac9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md#insn-00bbac9c) · [`00bbaca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md#insn-00bbaca8)

~~~diff
- 00bbac8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbac8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbac8c ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbac8c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbac8c bytes fd7bbfa9
- 00bbac9c ["INT_ADD", "register:40f0:8", ["const:bbac9c:8", "const:4:8"]]
- 00bbac9c ["CALL", null, ["callee:00c53820:8"]]
- 00bbac9c bytes 4d700094
- 00bbaca8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbaca8 ["RETURN", null, ["register:0:8"]]
- 00bbaca8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a1317e1562add911d3deb79dd088fac"></a>

### [`00bbad04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad04.md) → [`00c3774c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3774c.md) __cxa_pure_virtual

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 16.67% / 新版 16.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c37750"
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
      "unmatched:00bbad08",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbad14",
      "PARAM",
      [
        "storage",
        "0029083e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37750",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c3775c",
      "PARAM",
      [
        "storage",
        "0029fd80",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbad08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad04.md#insn-00bbad08) · [`00bbad0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad04.md#insn-00bbad0c)
- 新版 `00c37750`（命令位置の公開資料なし）

~~~diff
- 00bbad08 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbad08 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbad08 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbad08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbad08 bytes fd7bbfa9
+ 00c37750 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37750 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37750 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c37750 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37750 bytes fd7bbfa9
- 00bbad0c ["COPY", "register:40e8:8", ["register:8:8"]]
- 00bbad0c bytes fd030091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b864e21ec7c73f14f95e4bd0c1fdb507"></a>

### [`00bbad1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad1c.md) → [`00c37764`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37764.md) __cxa_deleted_virtual

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bbb19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb19c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c37be4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37be4.md)

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
      "site": "00bbad20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c37768"
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
      "unmatched:00bbad20",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbad2c",
      "PARAM",
      [
        "storage",
        "002a533a",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bbad30",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c37be4"
      ]
    ]
  ],
  "added": [
    [
      "00c37768",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37774",
      "PARAM",
      [
        "storage",
        "002b5d68",
        null,
        "string"
      ]
    ],
    [
      "00c37778",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c37be4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbad20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad1c.md#insn-00bbad20) · [`00bbad30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad1c.md#insn-00bbad30)
- 新版 `00c37768`（命令位置の公開資料なし）

~~~diff
- 00bbad20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbad20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbad20 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
- 00bbad20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbad20 bytes fd7bbfa9
- 00bbad30 ["INT_ADD", "register:40f0:8", ["const:bbad30:8", "const:4:8"]]
- 00bbad30 ["CALL", null, ["callee:00c37be4:8"]]
- 00bbad30 bytes 1b010094
+ 00c37768 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37768 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37768 ["INT_ADD", "register:8:8", ["register:8:8", "const:fffffffffffffff0:8"]]
+ 00c37768 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37768 bytes fd7bbfa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f4e0147ec443ae463f68b566cc6b01d"></a>

### [`00bbad3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad3c.md) → [`00c37784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37784.md) _ZNSt9exceptionD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea00.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad40"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad44"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbad40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbad44",
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
      "00c37788",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3778c",
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

- 旧版 [`00bbad40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad3c.md#insn-00bbad40) · [`00bbad44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad3c.md#insn-00bbad44)
- 新版 `00c37788`（命令位置の公開資料なし）

~~~diff
- 00bbad40 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbad40 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbad40 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbad40 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbad40 bytes fd7bbea9
- 00bbad44 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbad44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbad44 bytes f30b00f9
+ 00c37788 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37788 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37788 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c37788 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37788 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f4f86617abf50d7665af27473a3fdfe"></a>

### [`00bbad68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad68.md) → [`00c377b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377b0.md) _ZNKSt9exception4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad74"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c377bc"
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
      "unmatched:00bbad70",
      "DATA",
      [
        "storage",
        "00294469",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c377b8",
      "DATA",
      [
        "storage",
        "002a3d7f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad68.md#insn-00bbad74) · [`00bbad6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad68.md#insn-00bbad6c)
- 新版 `00c377bc`（命令位置の公開資料なし）

~~~diff
- 00bbad74 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbad74 ["RETURN", null, ["register:0:8"]]
- 00bbad74 bytes c0035fd6
+ 00c377bc ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c377bc ["RETURN", null, ["register:0:8"]]
+ 00c377bc bytes c0035fd6
- 00bbad6c ["COPY", "register:4000:8", ["const:294000:8"]]
- 00bbad6c bytes c0b6ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-006d3a7a9597885574a11baabf212282"></a>

### [`00bbad78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad78.md) → [`00c377c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377c0.md) _ZNSt13bad_exceptionD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e50.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea10.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad7c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbad80"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbad7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbad80",
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
      "00c377c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c377c8",
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

- 旧版 [`00bbad7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad78.md#insn-00bbad7c) · [`00bbad80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad78.md#insn-00bbad80)
- 新版 `00c377c4`（命令位置の公開資料なし）

~~~diff
- 00bbad7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbad7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbad7c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbad7c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbad7c bytes fd7bbea9
- 00bbad80 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbad80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbad80 bytes f30b00f9
+ 00c377c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c377c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c377c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c377c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c377c4 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88365da6f541ad08847317ef3ee4389d"></a>

### [`00bbada4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbada4.md) → [`00c377ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377ec.md) _ZNKSt13bad_exception4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbadb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c377f8"
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
      "unmatched:00bbadac",
      "DATA",
      [
        "storage",
        "0029e1b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c377f4",
      "DATA",
      [
        "storage",
        "002ae539",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbadb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbada4.md#insn-00bbadb0) · [`00bbada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbada4.md#insn-00bbada8)
- 新版 `00c377f8`（命令位置の公開資料なし）

~~~diff
- 00bbadb0 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbadb0 ["RETURN", null, ["register:0:8"]]
- 00bbadb0 bytes c0035fd6
+ 00c377f8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c377f8 ["RETURN", null, ["register:0:8"]]
+ 00c377f8 bytes c0035fd6
- 00bbada8 ["COPY", "register:4000:8", ["const:29e000:8"]]
- 00bbada8 bytes 20b7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a92bad3ad79e2f8f650bff85619ea51c"></a>

### [`00bbadb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadb4.md) → [`00c377fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c377fc.md) _ZNSt9bad_allocC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdbbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbf0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c58640`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58640.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bbadc4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c3780c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbadc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbadbc",
      "READ",
      [
        "storage",
        "00c1c018",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbadc4",
      "DATA",
      [
        "storage",
        "00c16838",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37804",
      "READ",
      [
        "storage",
        "00c9ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00c3780c",
      "DATA",
      [
        "storage",
        "00c961e0",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbadc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadb4.md#insn-00bbadc4) · [`00bbadc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadb4.md#insn-00bbadc8)
- 新版 `00c3780c`（命令位置の公開資料なし）

~~~diff
- 00bbadc4 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bbadc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbadc4 bytes 080000f9
- 00bbadc8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbadc8 ["RETURN", null, ["register:0:8"]]
- 00bbadc8 bytes c0035fd6
+ 00c3780c ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00c3780c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c3780c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a5ad0446b1d570c3f98ba715aa9bf61"></a>

### [`00bbadcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadcc.md) → [`00c37814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37814.md) _ZNSt9bad_allocD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdbc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc00.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c58650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58650.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbadd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbadd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbadd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbadd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbadd4",
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
      "00c37818",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c3781c",
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

- 旧版 [`00bbadd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadcc.md#insn-00bbadd0) · [`00bbadd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadcc.md#insn-00bbadd4)
- 新版 `00c37818`（命令位置の公開資料なし）

~~~diff
- 00bbadd0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbadd0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbadd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbadd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbadd0 bytes fd7bbea9
- 00bbadd4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbadd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbadd4 bytes f30b00f9
+ 00c37818 ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37818 ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37818 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c37818 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37818 bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ed1231e343c9666855a023bf2910c3e"></a>

### [`00bbadf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadf8.md) → [`00c37840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37840.md) _ZNKSt9bad_alloc4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae04"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c3784c"
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
      "unmatched:00bbae00",
      "DATA",
      [
        "storage",
        "0029aab2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37848",
      "DATA",
      [
        "storage",
        "002aaa93",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbae04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadf8.md#insn-00bbae04) · [`00bbadfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbadf8.md#insn-00bbadfc)
- 新版 `00c3784c`（命令位置の公開資料なし）

~~~diff
- 00bbae04 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbae04 ["RETURN", null, ["register:0:8"]]
- 00bbae04 bytes c0035fd6
+ 00c3784c ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c3784c ["RETURN", null, ["register:0:8"]]
+ 00c3784c bytes c0035fd6
- 00bbadfc ["COPY", "register:4000:8", ["const:29a000:8"]]
- 00bbadfc bytes 00b7ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33cf7d08e0b1261ef45fbd36d1e3666e"></a>

### [`00bbae08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae08.md) → [`00c37850`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37850.md) _ZNSt20bad_array_new_lengthC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1e0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c57c30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c30.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

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
      "site": "00bbae18"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c37860"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae1c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbae10",
      "READ",
      [
        "storage",
        "00c1c020",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bbae18",
      "DATA",
      [
        "storage",
        "00c16860",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00c37858",
      "READ",
      [
        "storage",
        "00c9ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00c37860",
      "DATA",
      [
        "storage",
        "00c96208",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbae18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae08.md#insn-00bbae18) · [`00bbae1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae08.md#insn-00bbae1c)
- 新版 `00c37860`（命令位置の公開資料なし）

~~~diff
- 00bbae18 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00bbae18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bbae18 bytes 080000f9
- 00bbae1c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbae1c ["RETURN", null, ["register:0:8"]]
- 00bbae1c bytes c0035fd6
+ 00c37860 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00c37860 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c37860 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c857abf98ce13536db757f586ee6cf8"></a>

### [`00bbae4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae4c.md) → [`00c37894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37894.md) _ZNKSt20bad_array_new_length4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbae58"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c378a0"
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
      "unmatched:00bbae54",
      "DATA",
      [
        "storage",
        "00295706",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c3789c",
      "DATA",
      [
        "storage",
        "002a513f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbae58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae4c.md#insn-00bbae58) · [`00bbae50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbae4c.md#insn-00bbae50)
- 新版 `00c378a0`（命令位置の公開資料なし）

~~~diff
- 00bbae58 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbae58 ["RETURN", null, ["register:0:8"]]
- 00bbae58 bytes c0035fd6
+ 00c378a0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c378a0 ["RETURN", null, ["register:0:8"]]
+ 00c378a0 bytes c0035fd6
- 00bbae50 ["COPY", "register:4000:8", ["const:295000:8"]]
- 00bbae50 bytes c0b6fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a8d96f239771543486b33cddb62211b"></a>

### [`00bbaf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf44.md) → [`00c3798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3798c.md) _ZNSt13runtime_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dbd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dbd0.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbaf58"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c379a0"
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
      "unmatched:00bbaf58",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fd0"
      ]
    ]
  ],
  "added": [
    [
      "00c379a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dbd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaf44.md#insn-00bbaf58)
- 新版 `00c379a0`（命令位置の公開資料なし）

~~~diff
- 00bbaf58 ["INT_ADD", "register:40f0:8", ["const:bbaf58:8", "const:4:8"]]
- 00bbaf58 ["CALL", null, ["ram:be0fd0:8"]]
- 00bbaf58 bytes 1e980094
+ 00c379a0 ["INT_ADD", "register:40f0:8", ["const:c379a0:8", "const:4:8"]]
+ 00c379a0 ["CALL", null, ["ram:c5dbd0:8"]]
+ 00c379a0 bytes 8c980094
~~~


<a id="compare-29495acf8f1f2ed4711340fcbbcca61b"></a>

### [`00bbafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafd4.md) → [`00c37a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a1c.md) _ZNSt12length_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b00.md)

変更の種類 call, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbafe8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00c37a30"
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
      "unmatched:00bbafe8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb0b0"
      ]
    ]
  ],
  "added": [
    [
      "00c37a30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57b00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbafe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbafd4.md#insn-00bbafe8)
- 新版 `00c37a30`（命令位置の公開資料なし）

~~~diff
- 00bbafe8 ["INT_ADD", "register:40f0:8", ["const:bbafe8:8", "const:4:8"]]
- 00bbafe8 ["CALL", null, ["ram:bdb0b0:8"]]
- 00bbafe8 bytes 32800094
+ 00c37a30 ["INT_ADD", "register:40f0:8", ["const:c37a30:8", "const:4:8"]]
+ 00c37a30 ["CALL", null, ["ram:c57b00:8"]]
+ 00c37a30 bytes 34800094
~~~


<a id="compare-abdd78c2f9ef992a7cac29bb2cd1d038"></a>

### [`00bbb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md) → [`00c37a48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37a48.md) _ZNSt12out_of_rangeD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ca0.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb004"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb008"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb004",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb008",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb014",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb250"
      ]
    ]
  ],
  "added": [
    [
      "00c37a4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37a50",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37a5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ca0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md#insn-00bbb004) · [`00bbb008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md#insn-00bbb008) · [`00bbb014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb000.md#insn-00bbb014)

~~~diff
- 00bbb004 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbb004 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbb004 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbb004 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbb004 bytes fd7bbea9
- 00bbb008 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbb008 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbb008 bytes f30b00f9
- 00bbb014 ["INT_ADD", "register:40f0:8", ["const:bbb014:8", "const:4:8"]]
- 00bbb014 ["CALL", null, ["ram:bdb250:8"]]
- 00bbb014 bytes 8f800094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-230738481275b342a863a20bf70e8e11"></a>

### [`00bbb084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb084.md) → [`00c37acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37acc.md) _ZNSt15underflow_errorD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea40.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 45.45% / 新版 45.45%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb08c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb088",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb08c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1e80"
      ]
    ]
  ],
  "added": [
    [
      "00c37ad0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37ad4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c37ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5ea40"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb084.md#insn-00bbb088) · [`00bbb08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb084.md#insn-00bbb08c) · [`00bbb098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb084.md#insn-00bbb098)

~~~diff
- 00bbb088 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbb088 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbb088 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbb088 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbb088 bytes fd7bbea9
- 00bbb08c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbb08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbb08c bytes f30b00f9
- 00bbb098 ["INT_ADD", "register:40f0:8", ["const:bbb098:8", "const:4:8"]]
- 00bbb098 ["CALL", null, ["ram:be1e80:8"]]
- 00bbb098 bytes 7a9b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a26ab4f34d10b55b38d41af1baeeffd"></a>

### [`00bbb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb130.md) → [`00c37b78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37b78.md) _ZNKSt8bad_cast4whatEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb13c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00c37b84"
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
      "unmatched:00bbb138",
      "DATA",
      [
        "storage",
        "00294478",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c37b80",
      "DATA",
      [
        "storage",
        "002a3d8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb130.md#insn-00bbb13c) · [`00bbb134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb130.md#insn-00bbb134)
- 新版 `00c37b84`（命令位置の公開資料なし）

~~~diff
- 00bbb13c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bbb13c ["RETURN", null, ["register:0:8"]]
- 00bbb13c bytes c0035fd6
+ 00c37b84 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00c37b84 ["RETURN", null, ["register:0:8"]]
+ 00c37b84 bytes c0035fd6
- 00bbb134 ["COPY", "register:4000:8", ["const:294000:8"]]
- 00bbb134 bytes c0b6ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b3dc622a9207c2a77e87c3d9c508e31"></a>

### [`00bbb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb160.md) → [`00c37ba8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ba8.md) _ZNSt10bad_typeidD0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1dc0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5e980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e980.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb164"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb168"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb164",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb168",
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
      "00c37bac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37bb0",
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

- 旧版 [`00bbb164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb160.md#insn-00bbb164) · [`00bbb168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb160.md#insn-00bbb168)
- 新版 `00c37bac`（命令位置の公開資料なし）

~~~diff
- 00bbb164 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbb164 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbb164 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbb164 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbb164 bytes fd7bbea9
- 00bbb168 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbb168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbb168 bytes f30b00f9
+ 00c37bac ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37bac ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37bac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c37bac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37bac bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1761019d4fbc9748a4ca41ae63e31764"></a>

### [`00bbb370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb370.md) → [`00c37db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37db8.md) FUN_00c37db8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb374"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb378"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb374",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb378",
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
      "00c37dbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37dc0",
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

- 旧版 [`00bbb374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb370.md#insn-00bbb374) · [`00bbb378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb370.md#insn-00bbb378)
- 新版 `00c37dbc`（命令位置の公開資料なし）

~~~diff
- 00bbb374 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbb374 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbb374 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbb374 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbb374 bytes fd7bbea9
- 00bbb378 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbb378 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbb378 bytes f30b00f9
+ 00c37dbc ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37dbc ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37dbc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c37dbc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37dbc bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ac3c80cdd55f0c09737108311d30f24"></a>

### [`00bbb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb420.md) → [`00c37e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37e68.md) FUN_00c37e68

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be1e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1e90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5ea50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5ea50.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 63.64% / 新版 63.64%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb424"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bbb428"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bbb424",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bbb428",
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
      "00c37e6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00c37e70",
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

- 旧版 [`00bbb424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb420.md#insn-00bbb424) · [`00bbb428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbb420.md#insn-00bbb428)
- 新版 `00c37e6c`（命令位置の公開資料なし）

~~~diff
- 00bbb424 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bbb424 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bbb424 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00bbb424 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bbb424 bytes fd7bbea9
- 00bbb428 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bbb428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00bbb428 bytes f30b00f9
+ 00c37e6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00c37e6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00c37e6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00c37e6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00c37e6c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

