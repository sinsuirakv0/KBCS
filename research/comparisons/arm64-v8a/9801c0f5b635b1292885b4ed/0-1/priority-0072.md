# v15.7.4 → v16.0.0 · 最優先の変更候補 (72)

[一覧の目次](README.md)

<a id="compare-b41b98a783c5ba26d7e08bf0a5608b95"></a>

### [`00b7bba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md) → [`00bf85ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md) FUN_00bf85ec

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00b7baac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7baac.md) [`00b7bc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bc78.md) [`00b7be8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md) [`00b7bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md) · 呼出先 3件 [`007aae6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007aa/007aae6c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)
- 新版 呼出元 4件 [`00bf84f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf84f4.md) [`00bf86c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf86c0.md) [`00bf88d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md) [`00bf89e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md) · 呼出先 3件 [`007dcedc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007dc/007dcedc.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57b70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8634",
      "incomplete_value": false,
      "site": "00bf863c",
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
            "const:72e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7bbec",
      "incomplete_value": false,
      "site": "00b7bbf4",
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
            "const:6b6:8"
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
      "00bf8634",
      "PARAM",
      [
        "storage",
        "002ac6b6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf8634",
      "PARAM",
      [
        "storage",
        "002bd72e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bbf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bbf4) · [`00b7bbe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bbe8) · [`00b7bbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md#insn-00b7bbec)
- 新版 [`00bf863c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf863c) · [`00bf8630`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf8630) · [`00bf8634`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md#insn-00bf8634)

~~~diff
- 00b7bbf4 ["INT_ADD", "register:40f0:8", ["const:b7bbf4:8", "const:4:8"]]
- 00b7bbf4 ["CALL", null, ["callee:00c57b70:8"]]
+ 00bf863c ["INT_ADD", "register:40f0:8", ["const:bf863c:8", "const:4:8"]]
+ 00bf863c ["CALL", null, ["callee:00c57b70:8"]]
- 00b7bbf4 bytes 4b7d0194
+ 00bf863c bytes 4d7d0194
- 00b7bbe8 ["COPY", "register:4008:8", ["const:2ac000:8"]]
+ 00bf8630 ["COPY", "register:4008:8", ["const:2bd000:8"]]
- 00b7bbe8 bytes 81b9ffb0
+ 00bf8630 bytes 21b6ffb0
- 00b7bbec ["COPY", "tmp:0:8", ["const:6b6:8"]]
- 00b7bbec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b7bbec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b7bbec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00bf8634 ["COPY", "tmp:0:8", ["const:72e:8"]]
+ 00bf8634 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8634 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00bf8634 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b7bbec bytes 21d81a91
+ 00bf8634 bytes 21b81c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-792811772baf7ac3c15b9b9ed476a1af"></a>

### [`00b7bc78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bc78.md) → [`00bf86c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf86c0.md) _ZNSt6__ndk112system_errorC2ENS_10error_codeEPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00be1160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1160.md) [`00be11b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be11b0.md) · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7bba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 2件 [`00c5dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd60.md) [`00c5ddb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5ddb0.md) · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf85ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 52.94% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf87a8",
      "incomplete_value": true,
      "site": "00bf87ac",
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
      "definition_site": "00b7bd60",
      "incomplete_value": true,
      "site": "00b7bd64",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf874c",
      "incomplete_value": true,
      "site": "00bf8758",
      "value": [
        "live",
        "register:40b0:8"
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7bd30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7bd30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fa0"
      ]
    ],
    [
      "00bf87a0",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf87ac",
      "DATA",
      [
        "storage",
        "00c12dc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf8778",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dba0"
      ]
    ],
    [
      "00bf87a0",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf87ac",
      "DATA",
      [
        "storage",
        "00c92770",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bc78.md#insn-00b7bd10) · [`00b7bd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bc78.md#insn-00b7bd30)
- 新版 [`00bf8758`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf86c0.md#insn-00bf8758) · [`00bf8778`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf86c0.md#insn-00bf8778)

~~~diff
- 00b7bd10 ["INT_ADD", "register:40f0:8", ["const:b7bd10:8", "const:4:8"]]
- 00b7bd10 ["CALL", null, ["callee:00c57c00:8"]]
+ 00bf8758 ["INT_ADD", "register:40f0:8", ["const:bf8758:8", "const:4:8"]]
+ 00bf8758 ["CALL", null, ["callee:00c57c00:8"]]
- 00b7bd10 bytes 287d0194
+ 00bf8758 bytes 2a7d0194
- 00b7bd30 ["INT_ADD", "register:40f0:8", ["const:b7bd30:8", "const:4:8"]]
- 00b7bd30 ["CALL", null, ["ram:be0fa0:8"]]
- 00b7bd30 bytes 9c940194
+ 00bf8778 ["INT_ADD", "register:40f0:8", ["const:bf8778:8", "const:4:8"]]
+ 00bf8778 ["CALL", null, ["ram:c5dba0:8"]]
+ 00bf8778 bytes 0a950194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c6ce9ce5798ca8f5484739d3e93e7f"></a>

### [`00b7bddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bddc.md) → [`00bf8824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8824.md) _ZNSt6__ndk112system_errorC1ENS_10error_codeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dba0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8894",
      "incomplete_value": true,
      "site": "00bf8898",
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
      "definition_site": "00b7be4c",
      "incomplete_value": true,
      "site": "00b7be50",
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
      "site": "00bf8878",
      "value": [
        "leaf",
        "ram:c5dba0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7be30",
      "value": [
        "leaf",
        "ram:be0fa0:8"
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
      "00bf8878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fa0"
      ]
    ],
    [
      "00bf8890",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8898",
      "DATA",
      [
        "storage",
        "00c12dc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf8878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dba0"
      ]
    ],
    [
      "00bf8890",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8898",
      "DATA",
      [
        "storage",
        "00c92770",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bddc.md#insn-00b7be30) · [`00b7be18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bddc.md#insn-00b7be18) · [`00b7be40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bddc.md#insn-00b7be40)
- 新版 [`00bf8878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8824.md#insn-00bf8878) · [`00bf8860`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8824.md#insn-00bf8860) · [`00bf8888`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8824.md#insn-00bf8888)

~~~diff
- 00b7be30 ["INT_ADD", "register:40f0:8", ["const:b7be30:8", "const:4:8"]]
- 00b7be30 ["CALL", null, ["ram:be0fa0:8"]]
+ 00bf8878 ["INT_ADD", "register:40f0:8", ["const:bf8878:8", "const:4:8"]]
+ 00bf8878 ["CALL", null, ["ram:c5dba0:8"]]
- 00b7be30 bytes 5c940194
+ 00bf8878 bytes ca940194
- 00b7be18 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7be18 ["INT_ADD", "register:40f0:8", ["const:b7be18:8", "const:4:8"]]
- 00b7be18 ["CALLIND", null, ["register:0:8"]]
+ 00bf8860 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bf8860 ["INT_ADD", "register:40f0:8", ["const:bf8860:8", "const:4:8"]]
+ 00bf8860 ["CALLIND", null, ["register:0:8"]]
- 00b7be18 bytes 20013fd6
+ 00bf8860 bytes 20013fd6
- 00b7be40 ["INT_ADD", "register:40f0:8", ["const:b7be40:8", "const:4:8"]]
- 00b7be40 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bf8888 ["INT_ADD", "register:40f0:8", ["const:bf8888:8", "const:4:8"]]
+ 00bf8888 ["CALL", null, ["callee:00c57ab0:8"]]
- 00b7be40 bytes 887c0194
+ 00bf8888 bytes 8a7c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c7efa97e0b658ab911329a385dea2b"></a>

### [`00b7be8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md) → [`00bf88d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md) _ZNSt6__ndk112system_errorC2EiRKNS_14error_categoryERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00b7bba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fa0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0043bae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bae0.md) [`00bf85ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dba0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8970",
      "incomplete_value": true,
      "site": "00bf8974",
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
      "definition_site": "00b7bf28",
      "incomplete_value": true,
      "site": "00b7bf2c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bf8940",
      "value": [
        "leaf",
        "ram:c5dba0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7bef8",
      "value": [
        "leaf",
        "ram:be0fa0:8"
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
      "00bf8940",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fa0"
      ]
    ],
    [
      "00bf8968",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8974",
      "DATA",
      [
        "storage",
        "00c12dc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf8940",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dba0"
      ]
    ],
    [
      "00bf8968",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8974",
      "DATA",
      [
        "storage",
        "00c92770",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7bef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md#insn-00b7bef8) · [`00b7bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md#insn-00b7bedc) · [`00b7beec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7be8c.md#insn-00b7beec)
- 新版 [`00bf8940`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md#insn-00bf8940) · [`00bf8924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md#insn-00bf8924) · [`00bf8934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf88d4.md#insn-00bf8934)

~~~diff
- 00b7bef8 ["INT_ADD", "register:40f0:8", ["const:b7bef8:8", "const:4:8"]]
- 00b7bef8 ["CALL", null, ["ram:be0fa0:8"]]
+ 00bf8940 ["INT_ADD", "register:40f0:8", ["const:bf8940:8", "const:4:8"]]
+ 00bf8940 ["CALL", null, ["ram:c5dba0:8"]]
- 00b7bef8 bytes 2a940194
+ 00bf8940 bytes 98940194
- 00b7bedc ["INT_ADD", "register:40f0:8", ["const:b7bedc:8", "const:4:8"]]
- 00b7bedc ["CALL", null, ["callee:0043bae0:8"]]
+ 00bf8924 ["INT_ADD", "register:40f0:8", ["const:bf8924:8", "const:4:8"]]
+ 00bf8924 ["CALL", null, ["callee:0043bae0:8"]]
- 00b7bedc bytes 4174e297
+ 00bf8924 bytes 6f0ce197
- 00b7beec ["INT_ADD", "register:40f0:8", ["const:b7beec:8", "const:4:8"]]
- 00b7beec ["CALL", null, ["callee:00bf85ec:8"]]
+ 00bf8934 ["INT_ADD", "register:40f0:8", ["const:bf8934:8", "const:4:8"]]
+ 00bf8934 ["CALL", null, ["callee:00bf85ec:8"]]
- 00b7beec bytes 2effff97
+ 00bf8934 bytes 2effff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cab67b769d028c3320c598aeee9f8c8c"></a>

### [`00b7bf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md) → [`00bf89e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md) _ZNSt6__ndk112system_errorC1EiRKNS_14error_categoryEPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00b7bba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bba4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043b724`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b724.md) [`00bf85ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf85ec.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57be0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57be0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8ad8",
      "incomplete_value": true,
      "site": "00bf8adc",
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
      "definition_site": "00b7c090",
      "incomplete_value": true,
      "site": "00b7c094",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bf8aa8",
      "value": [
        "leaf",
        "ram:c5dba0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c060",
      "value": [
        "leaf",
        "ram:be0fa0:8"
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
      "00bf8aa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fa0"
      ]
    ],
    [
      "00bf8ad0",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8adc",
      "DATA",
      [
        "storage",
        "00c12dc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf8aa8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dba0"
      ]
    ],
    [
      "00bf8ad0",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8adc",
      "DATA",
      [
        "storage",
        "00c92770",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md#insn-00b7c060) · [`00b7bfd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md#insn-00b7bfd4) · [`00b7c020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7b/00b7bf98.md#insn-00b7c020)
- 新版 [`00bf8aa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md#insn-00bf8aa8) · [`00bf8a1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md#insn-00bf8a1c) · [`00bf8a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf89e0.md#insn-00bf8a68)

~~~diff
- 00b7c060 ["INT_ADD", "register:40f0:8", ["const:b7c060:8", "const:4:8"]]
- 00b7c060 ["CALL", null, ["ram:be0fa0:8"]]
+ 00bf8aa8 ["INT_ADD", "register:40f0:8", ["const:bf8aa8:8", "const:4:8"]]
+ 00bf8aa8 ["CALL", null, ["ram:c5dba0:8"]]
- 00b7c060 bytes d0930194
+ 00bf8aa8 bytes 3e940194
- 00b7bfd4 ["INT_ADD", "register:40f0:8", ["const:b7bfd4:8", "const:4:8"]]
- 00b7bfd4 ["CALL", null, ["callee:00c57be0:8"]]
+ 00bf8a1c ["INT_ADD", "register:40f0:8", ["const:bf8a1c:8", "const:4:8"]]
+ 00bf8a1c ["CALL", null, ["callee:00c57be0:8"]]
- 00b7bfd4 bytes 6f7c0194
+ 00bf8a1c bytes 717c0194
- 00b7c020 ["INT_ADD", "register:40f0:8", ["const:b7c020:8", "const:4:8"]]
- 00b7c020 ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf8a68 ["INT_ADD", "register:40f0:8", ["const:bf8a68:8", "const:4:8"]]
+ 00bf8a68 ["CALL", null, ["callee:00c57a90:8"]]
- 00b7c020 bytes 087c0194
+ 00bf8a68 bytes 0a7c0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71eb803d0fdb707998b240ee69aa2e83"></a>

### [`00b7c110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c110.md) → [`00bf8b58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8b58.md) _ZNSt6__ndk112system_errorC1EiRKNS_14error_categoryE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fa0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dba0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dba0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf8bcc",
      "incomplete_value": true,
      "site": "00bf8bd0",
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
      "definition_site": "00b7c184",
      "incomplete_value": true,
      "site": "00b7c188",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bf8bac",
      "value": [
        "leaf",
        "ram:c5dba0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c164",
      "value": [
        "leaf",
        "ram:be0fa0:8"
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
      "00bf8bac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be0fa0"
      ]
    ],
    [
      "00bf8bc4",
      "READ",
      [
        "storage",
        "00c1bca0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8bd0",
      "DATA",
      [
        "storage",
        "00c12dc8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bf8bac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dba0"
      ]
    ],
    [
      "00bf8bc4",
      "READ",
      [
        "storage",
        "00c9b6d0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8bd0",
      "DATA",
      [
        "storage",
        "00c92770",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c110.md#insn-00b7c164) · [`00b7c14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c110.md#insn-00b7c14c) · [`00b7c174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c110.md#insn-00b7c174)
- 新版 [`00bf8bac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8b58.md#insn-00bf8bac) · [`00bf8b94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8b58.md#insn-00bf8b94) · [`00bf8bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8b58.md#insn-00bf8bbc)

~~~diff
- 00b7c164 ["INT_ADD", "register:40f0:8", ["const:b7c164:8", "const:4:8"]]
- 00b7c164 ["CALL", null, ["ram:be0fa0:8"]]
+ 00bf8bac ["INT_ADD", "register:40f0:8", ["const:bf8bac:8", "const:4:8"]]
+ 00bf8bac ["CALL", null, ["ram:c5dba0:8"]]
- 00b7c164 bytes 8f930194
+ 00bf8bac bytes fd930194
- 00b7c14c ["COPY", "register:0:8", ["register:4048:8"]]
- 00b7c14c ["INT_ADD", "register:40f0:8", ["const:b7c14c:8", "const:4:8"]]
- 00b7c14c ["CALLIND", null, ["register:0:8"]]
+ 00bf8b94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00bf8b94 ["INT_ADD", "register:40f0:8", ["const:bf8b94:8", "const:4:8"]]
+ 00bf8b94 ["CALLIND", null, ["register:0:8"]]
- 00b7c14c bytes 20013fd6
+ 00bf8b94 bytes 20013fd6
- 00b7c174 ["INT_ADD", "register:40f0:8", ["const:b7c174:8", "const:4:8"]]
- 00b7c174 ["CALL", null, ["callee:00c57ab0:8"]]
+ 00bf8bbc ["INT_ADD", "register:40f0:8", ["const:bf8bbc:8", "const:4:8"]]
+ 00bf8bbc ["CALL", null, ["callee:00c57ab0:8"]]
- 00b7c174 bytes bb7b0194
+ 00bf8bbc bytes bd7b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c302ea596e882609c4afa2f7b7874ace"></a>

### [`00b7c1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1f8.md) → [`00bf8c40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c40.md) _ZNSt6__ndk120__throw_system_errorEiPKc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) · 呼出先 1件 [`00b7c218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c218.md)
- 新版 呼出元 1件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) · 呼出先 1件 [`00bf8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c60.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bf8c5c",
      "value": [
        "leaf",
        "ram:bf8c60:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c214",
      "value": [
        "leaf",
        "ram:b7c218:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf8c58",
      "incomplete_value": false,
      "site": "00bf8c5c",
      "value": [
        "leaf",
        "const:ca43f0:8"
      ]
    },
    "old": {
      "definition_site": "00b7c210",
      "incomplete_value": false,
      "site": "00b7c214",
      "value": [
        "leaf",
        "const:c24910:8"
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
      "00bf8c58",
      "PARAM",
      [
        "storage",
        "00c24910",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8c5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00b7c218"
      ]
    ]
  ],
  "added": [
    [
      "00bf8c58",
      "PARAM",
      [
        "storage",
        "00ca43f0",
        null,
        "pointer"
      ]
    ],
    [
      "00bf8c5c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bf8c60"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1f8.md#insn-00b7c214) · [`00b7c210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c1f8.md#insn-00b7c210)
- 新版 [`00bf8c5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c40.md#insn-00bf8c5c) · [`00bf8c58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf8/00bf8c40.md#insn-00bf8c58)

~~~diff
- 00b7c214 ["INT_ADD", "register:40f0:8", ["const:b7c214:8", "const:4:8"]]
- 00b7c214 ["CALL", null, ["ram:b7c218:8"]]
+ 00bf8c5c ["INT_ADD", "register:40f0:8", ["const:bf8c5c:8", "const:4:8"]]
+ 00bf8c5c ["CALL", null, ["ram:bf8c60:8"]]
- 00b7c214 bytes 01000094
+ 00bf8c5c bytes 01000094
- 00b7c210 ["COPY", "register:4008:8", ["const:c24910:8"]]
+ 00bf8c58 ["COPY", "register:4008:8", ["const:ca43f0:8"]]
- 00b7c210 bytes 01385410
+ 00bf8c58 bytes c1bc5510
~~~


<a id="compare-0fec8638a193ba3c9800387215666cdb"></a>

### [`00b7c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md) → [`00bf9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md) _ZNSt6__ndk115future_categoryEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4c0.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c57f10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f10.md) · 呼出先 2件 [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9168",
      "incomplete_value": false,
      "site": "00bf916c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c720",
      "incomplete_value": false,
      "site": "00b7c724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "00bf9178",
      "incomplete_value": false,
      "site": "00bf917c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7c730",
      "incomplete_value": false,
      "site": "00b7c734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bf9154",
      "incomplete_value": false,
      "site": "00bf9160",
      "value": [
        "leaf",
        "const:ca43f8:8"
      ]
    },
    "old": {
      "definition_site": "00b7c70c",
      "incomplete_value": false,
      "site": "00b7c718",
      "value": [
        "leaf",
        "const:c24918:8"
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
      "00bf9148",
      "READ",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9154",
      "DATA",
      [
        "storage",
        "00c24918",
        null,
        null
      ]
    ],
    [
      "00bf9168",
      "PARAM",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bf9148",
      "READ",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf9154",
      "DATA",
      [
        "storage",
        "00ca43f8",
        null,
        null
      ]
    ],
    [
      "00bf9168",
      "PARAM",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c724) · [`00b7c734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c734) · [`00b7c6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c6ec.md#insn-00b7c6f8)
- 新版 [`00bf916c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf916c) · [`00bf917c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf917c) · [`00bf9140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9134.md#insn-00bf9140)

~~~diff
- 00b7c724 ["INT_ADD", "register:40f0:8", ["const:b7c724:8", "const:4:8"]]
- 00b7c724 ["CALL", null, ["callee:00c57a50:8"]]
+ 00bf916c ["INT_ADD", "register:40f0:8", ["const:bf916c:8", "const:4:8"]]
+ 00bf916c ["CALL", null, ["callee:00c57a50:8"]]
- 00b7c724 bytes 377a0194
+ 00bf916c bytes 397a0194
- 00b7c734 ["INT_ADD", "register:40f0:8", ["const:b7c734:8", "const:4:8"]]
- 00b7c734 ["CALL", null, ["callee:00c57a70:8"]]
+ 00bf917c ["INT_ADD", "register:40f0:8", ["const:bf917c:8", "const:4:8"]]
+ 00bf917c ["CALL", null, ["callee:00c57a70:8"]]
- 00b7c734 bytes 3b7a0194
+ 00bf917c bytes 3d7a0194
- 00b7c6f8 ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bf9140 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b7c6f8 bytes 282900d0
+ 00bf9140 bytes 682900b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85fbed9f105263e85df9e3608302ff5f"></a>

### [`00b7c73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c73c.md) → [`00bf9184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9184.md) _ZNSt6__ndk112future_errorC2ENS_10error_codeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4d0.md) · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0f90.md) [`00be1140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1140.md)
- 新版 呼出元 1件 [`00c57f20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f20.md) · 呼出先 3件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5db90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5db90.md) [`00c5dd40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c744"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7c748"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7c744",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7c748",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7c75c",
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
      "00bf918c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bf9190",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bf91a4",
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

- 旧版 [`00b7c744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c73c.md#insn-00b7c744) · [`00b7c748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c73c.md#insn-00b7c748) · [`00b7c75c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c73c.md#insn-00b7c75c)

~~~diff
- 00b7c744 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7c744 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7c744 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00b7c744 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7c744 bytes fd7b03a9
- 00b7c748 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:40:8"]]
- 00b7c748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7c748 bytes f32300f9
- 00b7c75c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00b7c75c ["COPY", "tmp:1:8", ["register:4010:8"]]
- 00b7c75c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b7c75c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7c75c bytes a10b3fa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28588e711ccf352d2d258d904827e018"></a>

### [`00b7c80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md) → [`00bf9254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md) _ZNSt6__ndk117__assoc_sub_state9set_valueEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb700.md) · 呼出先 5件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00c58150`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58150.md) · 呼出先 5件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

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
      "site": "00bf9288",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c840",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00bf9288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9288",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c840) · [`00b7c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c828) · [`00b7c85c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c80c.md#insn-00b7c85c)
- 新版 [`00bf9288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf9288) · [`00bf9270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf9270) · [`00bf92a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9254.md#insn-00bf92a4)

~~~diff
- 00b7c840 ["INT_ADD", "register:40f0:8", ["const:b7c840:8", "const:4:8"]]
- 00b7c840 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9288 ["INT_ADD", "register:40f0:8", ["const:bf9288:8", "const:4:8"]]
+ 00bf9288 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7c840 bytes 187b0194
+ 00bf9288 bytes 1a7b0194
- 00b7c828 ["INT_ADD", "register:40f0:8", ["const:b7c828:8", "const:4:8"]]
- 00b7c828 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf9270 ["INT_ADD", "register:40f0:8", ["const:bf9270:8", "const:4:8"]]
+ 00bf9270 ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7c828 bytes 9a7a0194
+ 00bf9270 bytes 9c7a0194
- 00b7c85c ["INT_ADD", "register:40f0:8", ["const:b7c85c:8", "const:4:8"]]
- 00b7c85c ["CALL", null, ["callee:00c57f80:8"]]
+ 00bf92a4 ["INT_ADD", "register:40f0:8", ["const:bf92a4:8", "const:4:8"]]
+ 00bf92a4 ["CALL", null, ["callee:00c57f80:8"]]
- 00b7c85c bytes 357b0194
+ 00bf92a4 bytes 377b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8ea8f1cba4200f75c63303380137720"></a>

### [`00b7c898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md) → [`00bf92e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md) _ZNSt6__ndk117__assoc_sub_state24set_value_at_thread_exitEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1220.md) · 呼出先 7件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00c5de20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de20.md) · 呼出先 7件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

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
      "site": "00bf9314",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c8cc",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00bf9314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8cc) · [`00b7c8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8b4) · [`00b7c8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c898.md#insn-00b7c8e0)
- 新版 [`00bf9314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf9314) · [`00bf92fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf92fc) · [`00bf9328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf92e0.md#insn-00bf9328)

~~~diff
- 00b7c8cc ["INT_ADD", "register:40f0:8", ["const:b7c8cc:8", "const:4:8"]]
- 00b7c8cc ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9314 ["INT_ADD", "register:40f0:8", ["const:bf9314:8", "const:4:8"]]
+ 00bf9314 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7c8cc bytes f57a0194
+ 00bf9314 bytes f77a0194
- 00b7c8b4 ["INT_ADD", "register:40f0:8", ["const:b7c8b4:8", "const:4:8"]]
- 00b7c8b4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf92fc ["INT_ADD", "register:40f0:8", ["const:bf92fc:8", "const:4:8"]]
+ 00bf92fc ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7c8b4 bytes 777a0194
+ 00bf92fc bytes 797a0194
- 00b7c8e0 ["INT_ADD", "register:40f0:8", ["const:b7c8e0:8", "const:4:8"]]
- 00b7c8e0 ["CALL", null, ["callee:00c57d30:8"]]
+ 00bf9328 ["INT_ADD", "register:40f0:8", ["const:bf9328:8", "const:4:8"]]
+ 00bf9328 ["CALL", null, ["callee:00c57d30:8"]]
- 00b7c8e0 bytes 807a0194
+ 00bf9328 bytes 827a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4261a53f85773d2a033999dc1bd1aa6"></a>

### [`00b7c92c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md) → [`00bf9374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md) _ZNSt6__ndk117__assoc_sub_state13set_exceptionESt13exception_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb510.md) · 呼出先 6件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb530.md)
- 新版 呼出元 1件 [`00c57f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f60.md) · 呼出先 6件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c57f80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57f80.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

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
      "site": "00bf93b4",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7c96c",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00bf93b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf93b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7c96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c96c) · [`00b7c950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c950) · [`00b7c97c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c92c.md#insn-00b7c97c)
- 新版 [`00bf93b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf93b4) · [`00bf9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf9398) · [`00bf93c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9374.md#insn-00bf93c4)

~~~diff
- 00b7c96c ["INT_ADD", "register:40f0:8", ["const:b7c96c:8", "const:4:8"]]
- 00b7c96c ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf93b4 ["INT_ADD", "register:40f0:8", ["const:bf93b4:8", "const:4:8"]]
+ 00bf93b4 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7c96c bytes cd7a0194
+ 00bf93b4 bytes cf7a0194
- 00b7c950 ["INT_ADD", "register:40f0:8", ["const:b7c950:8", "const:4:8"]]
- 00b7c950 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf9398 ["INT_ADD", "register:40f0:8", ["const:bf9398:8", "const:4:8"]]
+ 00bf9398 ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7c950 bytes 507a0194
+ 00bf9398 bytes 527a0194
- 00b7c97c ["INT_ADD", "register:40f0:8", ["const:b7c97c:8", "const:4:8"]]
- 00b7c97c ["CALL", null, ["callee:00c5db30:8"]]
+ 00bf93c4 ["INT_ADD", "register:40f0:8", ["const:bf93c4:8", "const:4:8"]]
+ 00bf93c4 ["CALL", null, ["callee:00c5db30:8"]]
- 00b7c97c bytes 6d910194
+ 00bf93c4 bytes db910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a627dc6385ec9a37782422250695f0f"></a>

### [`00b7c9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md) → [`00bf9418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md) _ZNSt6__ndk117__assoc_sub_state28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1240.md) · 呼出先 8件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)
- 新版 呼出元 1件 [`00c5de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de40.md) · 呼出先 8件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

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
      "site": "00bf9458",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7ca10",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00bf9458",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9458",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7ca10) · [`00b7c9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7c9f4) · [`00b7ca20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7c9d0.md#insn-00b7ca20)
- 新版 [`00bf9458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf9458) · [`00bf943c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf943c) · [`00bf9468`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9418.md#insn-00bf9468)

~~~diff
- 00b7ca10 ["INT_ADD", "register:40f0:8", ["const:b7ca10:8", "const:4:8"]]
- 00b7ca10 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9458 ["INT_ADD", "register:40f0:8", ["const:bf9458:8", "const:4:8"]]
+ 00bf9458 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7ca10 bytes a47a0194
+ 00bf9458 bytes a67a0194
- 00b7c9f4 ["INT_ADD", "register:40f0:8", ["const:b7c9f4:8", "const:4:8"]]
- 00b7c9f4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf943c ["INT_ADD", "register:40f0:8", ["const:bf943c:8", "const:4:8"]]
+ 00bf943c ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7c9f4 bytes 277a0194
+ 00bf943c bytes 297a0194
- 00b7ca20 ["INT_ADD", "register:40f0:8", ["const:b7ca20:8", "const:4:8"]]
- 00b7ca20 ["CALL", null, ["callee:00c5db30:8"]]
+ 00bf9468 ["INT_ADD", "register:40f0:8", ["const:bf9468:8", "const:4:8"]]
+ 00bf9468 ["CALL", null, ["callee:00c5db30:8"]]
- 00b7ca20 bytes 44910194
+ 00bf9468 bytes b2910194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cc647e0348bc708d07bd1729ce18e4f"></a>

### [`00b7cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md) → [`00bf9500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md) _ZNSt6__ndk117__assoc_sub_state4copyEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1260.md) · 呼出先 7件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md) [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`00c5de60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de60.md) · 呼出先 7件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) [`00c57ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ce0.md) [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "site": "00bf9584",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7cb3c",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "site": "00bf95cc",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7cb84",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bf9584",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "00bf95cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9584",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "00bf95cc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cb3c) · [`00b7cb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cb84) · [`00b7cae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cab8.md#insn-00b7cae4)
- 新版 [`00bf9584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf9584) · [`00bf95cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf95cc) · [`00bf952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9500.md#insn-00bf952c)

~~~diff
- 00b7cb3c ["INT_ADD", "register:40f0:8", ["const:b7cb3c:8", "const:4:8"]]
- 00b7cb3c ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9584 ["INT_ADD", "register:40f0:8", ["const:bf9584:8", "const:4:8"]]
+ 00bf9584 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7cb3c bytes 597a0194
+ 00bf9584 bytes 5b7a0194
- 00b7cb84 ["INT_ADD", "register:40f0:8", ["const:b7cb84:8", "const:4:8"]]
- 00b7cb84 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf95cc ["INT_ADD", "register:40f0:8", ["const:bf95cc:8", "const:4:8"]]
+ 00bf95cc ["CALL", null, ["ram:c57ef0:8"]]
- 00b7cb84 bytes 477a0194
+ 00bf95cc bytes 497a0194
- 00b7cae4 ["INT_ADD", "register:40f0:8", ["const:b7cae4:8", "const:4:8"]]
- 00b7cae4 ["CALL", null, ["callee:00c57ce0:8"]]
+ 00bf952c ["INT_ADD", "register:40f0:8", ["const:bf952c:8", "const:4:8"]]
+ 00bf952c ["CALL", null, ["callee:00c57ce0:8"]]
- 00b7cae4 bytes eb790194
+ 00bf952c bytes ed790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f1e826d44b11318e821bc0955fc3d61"></a>

### [`00b7cba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md) → [`00bf95e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md) _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb650.md) · 呼出先 3件 [`00bdb2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2a0.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md)
- 新版 呼出元 1件 [`00c580a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580a0.md) · 呼出先 3件 [`00c57cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cf0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf966c",
      "incomplete_value": false,
      "site": "00bf9674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:9db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7cc24",
      "incomplete_value": false,
      "site": "00b7cc2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "00bf966c",
      "PARAM",
      [
        "storage",
        "002ad6b5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf966c",
      "PARAM",
      [
        "storage",
        "002be9db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cc2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cc2c) · [`00b7cbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cbcc) · [`00b7cbfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7cba0.md#insn-00b7cbfc)
- 新版 [`00bf9674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9674) · [`00bf9614`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9614) · [`00bf9644`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf95e8.md#insn-00bf9644)

~~~diff
- 00b7cc2c ["INT_ADD", "register:40f0:8", ["const:b7cc2c:8", "const:4:8"]]
- 00b7cc2c ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9674 ["INT_ADD", "register:40f0:8", ["const:bf9674:8", "const:4:8"]]
+ 00bf9674 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7cc2c bytes a9790194
+ 00bf9674 bytes ab790194
- 00b7cbcc ["INT_ADD", "register:40f0:8", ["const:b7cbcc:8", "const:4:8"]]
- 00b7cbcc ["CALL", null, ["callee:00c58080:8"]]
+ 00bf9614 ["INT_ADD", "register:40f0:8", ["const:bf9614:8", "const:4:8"]]
+ 00bf9614 ["CALL", null, ["callee:00c58080:8"]]
- 00b7cbcc bytes 997a0194
+ 00bf9614 bytes 9b7a0194
- 00b7cbfc ["INT_ADD", "register:40f0:8", ["const:b7cbfc:8", "const:4:8"]]
- 00b7cbfc ["CALL", null, ["callee:00c57cf0:8"]]
+ 00bf9644 ["INT_ADD", "register:40f0:8", ["const:bf9644:8", "const:4:8"]]
+ 00bf9644 ["CALL", null, ["callee:00c57cf0:8"]]
- 00b7cbfc bytes a9790194
+ 00bf9644 bytes ab790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4af3474f34f132669913b436f0efe733"></a>

### [`00b7ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md) → [`00bf987c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md) _ZNSt6__ndk17promiseIvEC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf98ac",
      "incomplete_value": true,
      "site": "00bf98ac",
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
      "definition_site": "00b7ce64",
      "incomplete_value": true,
      "site": "00b7ce64",
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
      "00bf98a0",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "00bf98ac",
      "DATA",
      [
        "storage",
        "00c12f30",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00bf98a0",
      "READ",
      [
        "storage",
        "00c9a850",
        null,
        "pointer"
      ]
    ],
    [
      "00bf98ac",
      "DATA",
      [
        "storage",
        "00c928d8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ce4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md#insn-00b7ce4c) · [`00b7ce50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md#insn-00b7ce50) · [`00b7ce58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce34.md#insn-00b7ce58)
- 新版 [`00bf9894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md#insn-00bf9894) · [`00bf9898`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md#insn-00bf9898) · [`00bf98a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf987c.md#insn-00bf98a0)

~~~diff
- 00b7ce4c ["INT_ADD", "register:40f0:8", ["const:b7ce4c:8", "const:4:8"]]
- 00b7ce4c ["CALL", null, ["callee:00c57a90:8"]]
+ 00bf9894 ["INT_ADD", "register:40f0:8", ["const:bf9894:8", "const:4:8"]]
+ 00bf9894 ["CALL", null, ["callee:00c57a90:8"]]
- 00b7ce4c bytes 7d780194
+ 00bf9894 bytes 7f780194
- 00b7ce50 ["COPY", "register:4040:8", ["const:c1a000:8"]]
+ 00bf9898 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00b7ce50 bytes e80400d0
+ 00bf9898 bytes 080500b0
- 00b7ce58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
- 00b7ce58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bf98a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:850:8"]]
+ 00bf98a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7ce58 bytes 083147f9
+ 00bf98a0 bytes 082944f9
~~~


<a id="compare-1f2c0d6ed789ceafa947388e6b0dac6e"></a>

### [`00b7ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md) → [`00bf98d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md) _ZNSt6__ndk17promiseIvED1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 14件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0045a688`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a688.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.22% / 新版 80.22%

CFGの説明率　旧版 59.09% / 新版 65.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件, `store_value` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7cef4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bf9978",
      "incomplete_value": true,
      "site": "00bf9980",
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
      "definition_site": "00b7cf30",
      "incomplete_value": true,
      "site": "00b7cf38",
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
      "00bf9908",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ],
    [
      "00bf9928",
      "READ",
      [
        "storage",
        "010a2068",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b7cef4",
      "DATA",
      [
        "storage",
        "00c24918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bf9908",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ],
    [
      "00bf9928",
      "READ",
      [
        "storage",
        "01126f70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bf993c",
      "DATA",
      [
        "storage",
        "00ca43f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7cec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cec0) · [`00b7cef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cef4) · [`00b7cf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7c/00b7ce88.md#insn-00b7cf00)
- 新版 [`00bf9908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md#insn-00bf9908) · [`00bf9948`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf98d0.md#insn-00bf9948)

~~~diff
- 00b7cec0 ["INT_ADD", "register:40f0:8", ["const:b7cec0:8", "const:4:8"]]
- 00b7cec0 ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9908 ["INT_ADD", "register:40f0:8", ["const:bf9908:8", "const:4:8"]]
+ 00bf9908 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7cec0 bytes 78790194
+ 00bf9908 bytes 7a790194
- 00b7cef4 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b7cef4 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00b7cef4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffff0:8"]]
- 00b7cef4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7cef4 bytes a8273fa9
- 00b7cf00 ["INT_ADD", "register:40f0:8", ["const:b7cf00:8", "const:4:8"]]
- 00b7cf00 ["CALL", null, ["callee:00c5dd40:8"]]
+ 00bf9948 ["INT_ADD", "register:40f0:8", ["const:bf9948:8", "const:4:8"]]
+ 00bf9948 ["CALL", null, ["callee:00c5dd40:8"]]
- 00b7cf00 bytes 90900194
+ 00bf9948 bytes fe900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6af98dc4ef76498998e6e4c9213eee"></a>

### [`00b7d0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md) → [`00bf9b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md) _ZNSt6__ndk17promiseIvE28set_exception_at_thread_exitESt13exception_ptr

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`004377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377fc.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb660.md) [`00be1240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1240.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0045a694`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0045a/0045a694.md) [`00c57ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ef0.md) [`00c580b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c580b0.md) [`00c5de40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de40.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

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
      "site": "00bf9b64",
      "value": [
        "leaf",
        "ram:c57ef0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7d11c",
      "value": [
        "leaf",
        "ram:bdb4a0:8"
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
      "00bf9b64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb4a0"
      ]
    ]
  ],
  "added": [
    [
      "00bf9b64",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57ef0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d11c) · [`00b7d108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d108) · [`00b7d114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d0ec.md#insn-00b7d114)
- 新版 [`00bf9b64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b64) · [`00bf9b50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b50) · [`00bf9b5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9b34.md#insn-00bf9b5c)

~~~diff
- 00b7d11c ["INT_ADD", "register:40f0:8", ["const:b7d11c:8", "const:4:8"]]
- 00b7d11c ["CALL", null, ["ram:bdb4a0:8"]]
+ 00bf9b64 ["INT_ADD", "register:40f0:8", ["const:bf9b64:8", "const:4:8"]]
+ 00bf9b64 ["CALL", null, ["ram:c57ef0:8"]]
- 00b7d11c bytes e1780194
+ 00bf9b64 bytes e3780194
- 00b7d108 ["INT_ADD", "register:40f0:8", ["const:b7d108:8", "const:4:8"]]
- 00b7d108 ["CALL", null, ["callee:00c580b0:8"]]
+ 00bf9b50 ["INT_ADD", "register:40f0:8", ["const:bf9b50:8", "const:4:8"]]
+ 00bf9b50 ["CALL", null, ["callee:00c580b0:8"]]
- 00b7d108 bytes 56790194
+ 00bf9b50 bytes 58790194
- 00b7d114 ["INT_ADD", "register:40f0:8", ["const:b7d114:8", "const:4:8"]]
- 00b7d114 ["CALL", null, ["callee:00c5de40:8"]]
+ 00bf9b5c ["INT_ADD", "register:40f0:8", ["const:bf9b5c:8", "const:4:8"]]
+ 00bf9b5c ["CALL", null, ["callee:00c5de40:8"]]
- 00b7d114 bytes 4b900194
+ 00bf9b5c bytes b9900194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc2c2ef4552fab71aaa999998f855e1"></a>

### [`00b7d2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md) → [`00bf9ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md) _ZNSt6__ndk15mutexD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`00418338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418338.md) [`0042f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00468c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00468/00468c18.md) [`0056c7d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c7d8.md) · 呼出先 1件 [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md)
- 新版 呼出元 6件 [`0043ae38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae38.md) [`004524a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/004524a8.md) [`00452c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00452/00452c14.md) [`0048bab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048b/0048bab0.md) [`0058f670`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0058f/0058f670.md) · 呼出先 1件 [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b7d2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d2a0.md#insn-00b7d2ac)
- 新版 [`00bf9cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ce8.md#insn-00bf9cf4)

~~~diff
- 00b7d2ac ["INT_ADD", "register:40f0:8", ["const:b7d2ac:8", "const:4:8"]]
- 00b7d2ac ["CALL", null, ["callee:00c5b290:8"]]
+ 00bf9cf4 ["INT_ADD", "register:40f0:8", ["const:bf9cf4:8", "const:4:8"]]
+ 00bf9cf4 ["CALL", null, ["callee:00c5b290:8"]]
- 00b7d2ac bytes 59850194
+ 00bf9cf4 bytes 67850194
~~~


<a id="compare-45215c936dd9455e9d3b3f66f1bbabb2"></a>

### [`00b7d334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md) → [`00bf9d7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md) _ZNSt6__ndk115recursive_mutexC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd270.md) · 呼出先 6件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde810.md) [`00bdefd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefd0.md) [`00bdefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefe0.md) [`00bdeff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md)
- 新版 呼出元 1件 [`00c59cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59cc0.md) · 呼出先 6件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b290`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b290.md) [`00c5ba80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba80.md) [`00c5ba90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba90.md) [`00c5baa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5baa0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 64.29% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9db4",
      "incomplete_value": true,
      "site": "00bf9db8",
      "value": [
        "live",
        "register:4098:8"
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
      "definition_site": "00bf9db0",
      "incomplete_value": true,
      "site": "00bf9db8",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9e18",
      "incomplete_value": false,
      "site": "00bf9e1c",
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
            "const:7f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d3d0",
      "incomplete_value": false,
      "site": "00b7d3d4",
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
            "const:a38:8"
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
      "00bf9e18",
      "PARAM",
      [
        "storage",
        "00298a38",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9e18",
      "PARAM",
      [
        "storage",
        "002a87f6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d370) · [`00b7d3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d3d4) · [`00b7d350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d334.md#insn-00b7d350)
- 新版 [`00bf9db8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9db8) · [`00bf9e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9e1c) · [`00bf9d98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9d7c.md#insn-00bf9d98)

~~~diff
- 00b7d370 ["INT_ADD", "register:40f0:8", ["const:b7d370:8", "const:4:8"]]
- 00b7d370 ["CALL", null, ["callee:00c5ba80:8"]]
+ 00bf9db8 ["INT_ADD", "register:40f0:8", ["const:bf9db8:8", "const:4:8"]]
+ 00bf9db8 ["CALL", null, ["callee:00c5ba80:8"]]
- 00b7d370 bytes 18870194
+ 00bf9db8 bytes 32870194
- 00b7d3d4 ["INT_ADD", "register:40f0:8", ["const:b7d3d4:8", "const:4:8"]]
- 00b7d3d4 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9e1c ["INT_ADD", "register:40f0:8", ["const:bf9e1c:8", "const:4:8"]]
+ 00bf9e1c ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d3d4 bytes bf770194
+ 00bf9e1c bytes c1770194
- 00b7d350 ["INT_ADD", "register:40f0:8", ["const:b7d350:8", "const:4:8"]]
- 00b7d350 ["CALL", null, ["callee:00c5baa0:8"]]
+ 00bf9d98 ["INT_ADD", "register:40f0:8", ["const:bf9d98:8", "const:4:8"]]
+ 00bf9d98 ["CALL", null, ["callee:00c5baa0:8"]]
- 00b7d350 bytes 28870194
+ 00bf9d98 bytes 42870194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea0c06f655acd15aaf1fb3e90868aa6"></a>

### [`00b7d3f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md) → [`00bf9e40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md) _ZNSt6__ndk115recursive_mutex4lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd290.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md)
- 新版 呼出元 1件 [`00c59ce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ce0.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9e64",
      "incomplete_value": false,
      "site": "00bf9e68",
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
            "const:43e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d41c",
      "incomplete_value": false,
      "site": "00b7d420",
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
            "const:803:8"
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
      "00bf9e64",
      "PARAM",
      [
        "storage",
        "00297803",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9e64",
      "PARAM",
      [
        "storage",
        "002a743e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d420) · [`00b7d404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d404) · [`00b7d418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d3f8.md#insn-00b7d418)
- 新版 [`00bf9e68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e68) · [`00bf9e4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e4c) · [`00bf9e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9e40.md#insn-00bf9e60)

~~~diff
- 00b7d420 ["INT_ADD", "register:40f0:8", ["const:b7d420:8", "const:4:8"]]
- 00b7d420 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9e68 ["INT_ADD", "register:40f0:8", ["const:bf9e68:8", "const:4:8"]]
+ 00bf9e68 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d420 bytes ac770194
+ 00bf9e68 bytes ae770194
- 00b7d404 ["INT_ADD", "register:40f0:8", ["const:b7d404:8", "const:4:8"]]
- 00b7d404 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bf9e4c ["INT_ADD", "register:40f0:8", ["const:bf9e4c:8", "const:4:8"]]
+ 00bf9e4c ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d404 bytes 07850194
+ 00bf9e4c bytes 15850194
- 00b7d418 ["COPY", "register:4008:8", ["const:297000:8"]]
+ 00bf9e60 ["COPY", "register:4008:8", ["const:2a7000:8"]]
- 00b7d418 bytes c1b8ffd0
+ 00bf9e60 bytes 61b5ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-097643983f6dd775706118c6de4aadc0"></a>

### [`00b7d488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md) → [`00bf9ed0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md) _ZNSt6__ndk111timed_mutexD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.47% / 新版 89.47%

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
      "site": "00bf9ef8",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7d4b0",
      "value": [
        "leaf",
        "ram:bdb280:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9f14",
      "incomplete_value": false,
      "site": "00bf9f18",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d4cc",
      "incomplete_value": false,
      "site": "00b7d4d0",
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
            "const:112:8"
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
      "00bf9ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ],
    [
      "00bf9f14",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9ef8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ],
    [
      "00bf9f14",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d4b0) · [`00b7d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d4d0) · [`00b7d49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d488.md#insn-00b7d49c)
- 新版 [`00bf9ef8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9ef8) · [`00bf9f18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9f18) · [`00bf9ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9ed0.md#insn-00bf9ee4)

~~~diff
- 00b7d4b0 ["INT_ADD", "register:40f0:8", ["const:b7d4b0:8", "const:4:8"]]
- 00b7d4b0 ["CALL", null, ["ram:bdb280:8"]]
+ 00bf9ef8 ["INT_ADD", "register:40f0:8", ["const:bf9ef8:8", "const:4:8"]]
+ 00bf9ef8 ["CALL", null, ["ram:c57cd0:8"]]
- 00b7d4b0 bytes 74770194
+ 00bf9ef8 bytes 76770194
- 00b7d4d0 ["INT_ADD", "register:40f0:8", ["const:b7d4d0:8", "const:4:8"]]
- 00b7d4d0 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9f18 ["INT_ADD", "register:40f0:8", ["const:bf9f18:8", "const:4:8"]]
+ 00bf9f18 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d4d0 bytes 80770194
+ 00bf9f18 bytes 82770194
- 00b7d49c ["INT_ADD", "register:40f0:8", ["const:b7d49c:8", "const:4:8"]]
- 00b7d49c ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bf9ee4 ["INT_ADD", "register:40f0:8", ["const:bf9ee4:8", "const:4:8"]]
+ 00bf9ee4 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d49c bytes e1840194
+ 00bf9ee4 bytes ef840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-130c21e4d188eec5d3d7b6ca012702e0"></a>

### [`00b7d4dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md) → [`00bf9f24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md) _ZNSt6__ndk111timed_mutex4lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bf9fa8",
      "incomplete_value": false,
      "site": "00bf9fac",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d560",
      "incomplete_value": false,
      "site": "00b7d564",
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
            "const:112:8"
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
      "00bf9fa8",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bf9fa8",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d564) · [`00b7d500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d500) · [`00b7d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d4dc.md#insn-00b7d518)
- 新版 [`00bf9fac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9fac) · [`00bf9f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9f48) · [`00bf9f60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf9/00bf9f24.md#insn-00bf9f60)

~~~diff
- 00b7d564 ["INT_ADD", "register:40f0:8", ["const:b7d564:8", "const:4:8"]]
- 00b7d564 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bf9fac ["INT_ADD", "register:40f0:8", ["const:bf9fac:8", "const:4:8"]]
+ 00bf9fac ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d564 bytes 5b770194
+ 00bf9fac bytes 5d770194
- 00b7d500 ["INT_ADD", "register:40f0:8", ["const:b7d500:8", "const:4:8"]]
- 00b7d500 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bf9f48 ["INT_ADD", "register:40f0:8", ["const:bf9f48:8", "const:4:8"]]
+ 00bf9f48 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d500 bytes c8840194
+ 00bf9f48 bytes d6840194
- 00b7d518 ["INT_ADD", "register:40f0:8", ["const:b7d518:8", "const:4:8"]]
- 00b7d518 ["CALL", null, ["callee:00c58080:8"]]
+ 00bf9f60 ["INT_ADD", "register:40f0:8", ["const:bf9f60:8", "const:4:8"]]
+ 00bf9f60 ["CALL", null, ["callee:00c58080:8"]]
- 00b7d518 bytes 46780194
+ 00bf9f60 bytes 48780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-756ffde56de4c764043fb8132315dab9"></a>

### [`00b7d5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md) → [`00bfa014`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md) _ZNSt6__ndk111timed_mutex6unlockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa058",
      "incomplete_value": false,
      "site": "00bfa05c",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d610",
      "incomplete_value": false,
      "site": "00b7d614",
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
            "const:112:8"
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
      "00bfa058",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa058",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d614) · [`00b7d5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d5e0) · [`00b7d5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d5cc.md#insn-00b7d5f0)
- 新版 [`00bfa05c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa05c) · [`00bfa028`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa028) · [`00bfa038`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa014.md#insn-00bfa038)

~~~diff
- 00b7d614 ["INT_ADD", "register:40f0:8", ["const:b7d614:8", "const:4:8"]]
- 00b7d614 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa05c ["INT_ADD", "register:40f0:8", ["const:bfa05c:8", "const:4:8"]]
+ 00bfa05c ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d614 bytes 2f770194
+ 00bfa05c bytes 31770194
- 00b7d5e0 ["INT_ADD", "register:40f0:8", ["const:b7d5e0:8", "const:4:8"]]
- 00b7d5e0 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bfa028 ["INT_ADD", "register:40f0:8", ["const:bfa028:8", "const:4:8"]]
+ 00bfa028 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d5e0 bytes 90840194
+ 00bfa028 bytes 9e840194
- 00b7d5f0 ["INT_ADD", "register:40f0:8", ["const:b7d5f0:8", "const:4:8"]]
- 00b7d5f0 ["CALL", null, ["callee:00c58d10:8"]]
+ 00bfa038 ["INT_ADD", "register:40f0:8", ["const:bfa038:8", "const:4:8"]]
+ 00bfa038 ["CALL", null, ["callee:00c58d10:8"]]
- 00b7d5f0 bytes 347b0194
+ 00bfa038 bytes 367b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ef5aee65f4ff4363fafaa4701b892d"></a>

### [`00b7d63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md) → [`00bfa084`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md) _ZNSt6__ndk121recursive_timed_mutexD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57a60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a60.md) [`00c57cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cd0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 89.47% / 新版 89.47%

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
      "site": "00bfa0ac",
      "value": [
        "leaf",
        "ram:c57cd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7d664",
      "value": [
        "leaf",
        "ram:bdb280:8"
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa0c8",
      "incomplete_value": false,
      "site": "00bfa0cc",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d680",
      "incomplete_value": false,
      "site": "00b7d684",
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
            "const:112:8"
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
      "00bfa0ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb280"
      ]
    ],
    [
      "00bfa0c8",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa0ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57cd0"
      ]
    ],
    [
      "00bfa0c8",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d664) · [`00b7d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d684) · [`00b7d650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d63c.md#insn-00b7d650)
- 新版 [`00bfa0ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa0ac) · [`00bfa0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa0cc) · [`00bfa098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa084.md#insn-00bfa098)

~~~diff
- 00b7d664 ["INT_ADD", "register:40f0:8", ["const:b7d664:8", "const:4:8"]]
- 00b7d664 ["CALL", null, ["ram:bdb280:8"]]
+ 00bfa0ac ["INT_ADD", "register:40f0:8", ["const:bfa0ac:8", "const:4:8"]]
+ 00bfa0ac ["CALL", null, ["ram:c57cd0:8"]]
- 00b7d664 bytes 07770194
+ 00bfa0ac bytes 09770194
- 00b7d684 ["INT_ADD", "register:40f0:8", ["const:b7d684:8", "const:4:8"]]
- 00b7d684 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa0cc ["INT_ADD", "register:40f0:8", ["const:bfa0cc:8", "const:4:8"]]
+ 00bfa0cc ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d684 bytes 13770194
+ 00bfa0cc bytes 15770194
- 00b7d650 ["INT_ADD", "register:40f0:8", ["const:b7d650:8", "const:4:8"]]
- 00b7d650 ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bfa098 ["INT_ADD", "register:40f0:8", ["const:bfa098:8", "const:4:8"]]
+ 00bfa098 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d650 bytes 74840194
+ 00bfa098 bytes 82840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79772cd57e3517beb5157dbfa87a785b"></a>

### [`00b7d690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md) → [`00bfa0d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md) _ZNSt6__ndk121recursive_timed_mutex4lockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdb630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb630.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58080.md) [`00c58220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58220.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.92% / 新版 95.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa184",
      "incomplete_value": false,
      "site": "00bfa188",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d73c",
      "incomplete_value": false,
      "site": "00b7d740",
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
            "const:112:8"
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
      "definition_site": "00bfa190",
      "incomplete_value": false,
      "site": "00bfa198",
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
            "const:cfa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d748",
      "incomplete_value": false,
      "site": "00b7d750",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:3e4:8"
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
      "00bfa184",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ],
    [
      "00bfa190",
      "PARAM",
      [
        "storage",
        "002943e4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa184",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ],
    [
      "00bfa190",
      "PARAM",
      [
        "storage",
        "002a3cfa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d740) · [`00b7d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d750) · [`00b7d6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d690.md#insn-00b7d6a8)
- 新版 [`00bfa188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa188) · [`00bfa198`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa198) · [`00bfa0f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa0d8.md#insn-00bfa0f0)

~~~diff
- 00b7d740 ["INT_ADD", "register:40f0:8", ["const:b7d740:8", "const:4:8"]]
- 00b7d740 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa188 ["INT_ADD", "register:40f0:8", ["const:bfa188:8", "const:4:8"]]
+ 00bfa188 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d740 bytes e4760194
+ 00bfa188 bytes e6760194
- 00b7d750 ["INT_ADD", "register:40f0:8", ["const:b7d750:8", "const:4:8"]]
- 00b7d750 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa198 ["INT_ADD", "register:40f0:8", ["const:bfa198:8", "const:4:8"]]
+ 00bfa198 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d750 bytes e0760194
+ 00bfa198 bytes e2760194
- 00b7d6a8 ["INT_ADD", "register:40f0:8", ["const:b7d6a8:8", "const:4:8"]]
- 00b7d6a8 ["CALL", null, ["callee:00c58220:8"]]
+ 00bfa0f0 ["INT_ADD", "register:40f0:8", ["const:bfa0f0:8", "const:4:8"]]
+ 00bfa0f0 ["CALL", null, ["callee:00c58220:8"]]
- 00b7d6a8 bytes 4a780194
+ 00bfa0f0 bytes 4c780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf7ffcb5a6cf013cd3bf2f3554ac008f"></a>

### [`00b7d7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md) → [`00bfa240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md) _ZNSt6__ndk121recursive_timed_mutex6unlockEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdc2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc2c0.md) [`00bde820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde820.md) [`00bde830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde830.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c58d10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58d10.md) [`00c5b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2a0.md) [`00c5b2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5b2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa2a8",
      "incomplete_value": false,
      "site": "00bfa2ac",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d860",
      "incomplete_value": false,
      "site": "00b7d864",
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
            "const:112:8"
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
      "00bfa2a8",
      "PARAM",
      [
        "storage",
        "002a1112",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa2a8",
      "PARAM",
      [
        "storage",
        "002b175e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d864) · [`00b7d80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d80c) · [`00b7d828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d7f8.md#insn-00b7d828)
- 新版 [`00bfa2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa2ac) · [`00bfa254`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa254) · [`00bfa270`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa240.md#insn-00bfa270)

~~~diff
- 00b7d864 ["INT_ADD", "register:40f0:8", ["const:b7d864:8", "const:4:8"]]
- 00b7d864 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa2ac ["INT_ADD", "register:40f0:8", ["const:bfa2ac:8", "const:4:8"]]
+ 00bfa2ac ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d864 bytes 9b760194
+ 00bfa2ac bytes 9d760194
- 00b7d80c ["INT_ADD", "register:40f0:8", ["const:b7d80c:8", "const:4:8"]]
- 00b7d80c ["CALL", null, ["callee:00c5b2a0:8"]]
+ 00bfa254 ["INT_ADD", "register:40f0:8", ["const:bfa254:8", "const:4:8"]]
+ 00bfa254 ["CALL", null, ["callee:00c5b2a0:8"]]
- 00b7d80c bytes 05840194
+ 00bfa254 bytes 13840194
- 00b7d828 ["INT_ADD", "register:40f0:8", ["const:b7d828:8", "const:4:8"]]
- 00b7d828 ["CALL", null, ["callee:00c5b2b0:8"]]
+ 00bfa270 ["INT_ADD", "register:40f0:8", ["const:bfa270:8", "const:4:8"]]
+ 00bfa270 ["CALL", null, ["callee:00c5b2b0:8"]]
- 00b7d828 bytes 02840194
+ 00bfa270 bytes 10840194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2923b6e759a170f904614132c9b12a3"></a>

### [`00b7d894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md) → [`00bfa2dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md) _ZNSt6__ndk16thread4joinEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb320.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0660.md)
- 新版 呼出元 1件 [`00c57d70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d70.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa320",
      "incomplete_value": false,
      "site": "00bfa324",
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
            "const:20b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d8d8",
      "incomplete_value": false,
      "site": "00b7d8dc",
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
            "const:6d6:8"
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
      "00bfa320",
      "PARAM",
      [
        "storage",
        "002966d6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa320",
      "PARAM",
      [
        "storage",
        "002a620b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8dc) · [`00b7d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8b4) · [`00b7d8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d894.md#insn-00b7d8d4)
- 新版 [`00bfa324`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa324) · [`00bfa2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa2fc) · [`00bfa31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa2dc.md#insn-00bfa31c)

~~~diff
- 00b7d8dc ["INT_ADD", "register:40f0:8", ["const:b7d8dc:8", "const:4:8"]]
- 00b7d8dc ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa324 ["INT_ADD", "register:40f0:8", ["const:bfa324:8", "const:4:8"]]
+ 00bfa324 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d8dc bytes 7d760194
+ 00bfa324 bytes 7f760194
- 00b7d8b4 ["INT_ADD", "register:40f0:8", ["const:b7d8b4:8", "const:4:8"]]
- 00b7d8b4 ["CALL", null, ["callee:00c5d240:8"]]
+ 00bfa2fc ["INT_ADD", "register:40f0:8", ["const:bfa2fc:8", "const:4:8"]]
+ 00bfa2fc ["CALL", null, ["callee:00c5d240:8"]]
- 00b7d8b4 bytes 6b8b0194
+ 00bfa2fc bytes d18b0194
- 00b7d8d4 ["COPY", "register:4008:8", ["const:296000:8"]]
+ 00bfa31c ["COPY", "register:4008:8", ["const:2a6000:8"]]
- 00b7d8d4 bytes c1b8ffb0
+ 00bfa31c bytes 61b5ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7882805f191b726db979399fee3ca98f"></a>

### [`00b7d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md) → [`00bfa328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md) _ZNSt6__ndk16thread6detachEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb6c0.md) · 呼出先 2件 [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be1280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1280.md)
- 新版 呼出元 1件 [`00c58110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58110.md) · 呼出先 2件 [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5de80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5de80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa368",
      "incomplete_value": false,
      "site": "00bfa36c",
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
            "const:50b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7d920",
      "incomplete_value": false,
      "site": "00b7d924",
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
            "const:186:8"
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
      "00bfa368",
      "PARAM",
      [
        "storage",
        "0029e186",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa368",
      "PARAM",
      [
        "storage",
        "002ae50b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7d924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d924) · [`00b7d8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d8fc) · [`00b7d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d8e0.md#insn-00b7d91c)
- 新版 [`00bfa36c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa36c) · [`00bfa344`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa344) · [`00bfa364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa328.md#insn-00bfa364)

~~~diff
- 00b7d924 ["INT_ADD", "register:40f0:8", ["const:b7d924:8", "const:4:8"]]
- 00b7d924 ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa36c ["INT_ADD", "register:40f0:8", ["const:bfa36c:8", "const:4:8"]]
+ 00bfa36c ["CALL", null, ["callee:00c57d20:8"]]
- 00b7d924 bytes 6b760194
+ 00bfa36c bytes 6d760194
- 00b7d8fc ["INT_ADD", "register:40f0:8", ["const:b7d8fc:8", "const:4:8"]]
- 00b7d8fc ["CALL", null, ["callee:00c5de80:8"]]
+ 00bfa344 ["INT_ADD", "register:40f0:8", ["const:bfa344:8", "const:4:8"]]
+ 00bfa344 ["CALL", null, ["callee:00c5de80:8"]]
- 00b7d8fc bytes 618e0194
+ 00bfa344 bytes cf8e0194
- 00b7d91c ["COPY", "register:4008:8", ["const:29e000:8"]]
+ 00bfa364 ["COPY", "register:4008:8", ["const:2ae000:8"]]
- 00b7d91c bytes 01b9ffb0
+ 00bfa364 bytes a1b5ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8b6d699a35eb20ab03a6d22774f289"></a>

### [`00b7d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md) → [`00bfa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md) _ZNSt6__ndk119__thread_local_dataEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2e0.md) · 呼出先 3件 [`00b7da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)
- 新版 呼出元 1件 [`00c57d30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d30.md) · 呼出先 3件 [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfa47c",
      "incomplete_value": true,
      "site": "00bfa47c",
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
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7da34",
      "incomplete_value": true,
      "site": "00b7da34",
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa458",
      "incomplete_value": false,
      "site": "00bfa45c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7da10",
      "incomplete_value": false,
      "site": "00b7da14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:80:8"
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
      "definition_site": "00bfa46c",
      "incomplete_value": false,
      "site": "00bfa470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1126000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7da24",
      "incomplete_value": false,
      "site": "00b7da28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
      "00bfa438",
      "READ",
      [
        "storage",
        "010a2080",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa440",
      "READ",
      [
        "storage",
        "010a2078",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa440",
      "DATA",
      [
        "storage",
        "010a2070",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfa438",
      "READ",
      [
        "storage",
        "01126f88",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfa440",
      "READ",
      [
        "storage",
        "01126f80",
        null,
        "undefined8"
      ]
    ],
    [
      "00bfa440",
      "DATA",
      [
        "storage",
        "01126f78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7da14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da14) · [`00b7da28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da28) · [`00b7da34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md#insn-00b7da34)
- 新版 [`00bfa45c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa45c) · [`00bfa470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa470) · [`00bfa47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md#insn-00bfa47c)

~~~diff
- 00b7da14 ["INT_ADD", "register:40f0:8", ["const:b7da14:8", "const:4:8"]]
- 00b7da14 ["CALL", null, ["callee:00c57a50:8"]]
+ 00bfa45c ["INT_ADD", "register:40f0:8", ["const:bfa45c:8", "const:4:8"]]
+ 00bfa45c ["CALL", null, ["callee:00c57a50:8"]]
- 00b7da14 bytes 7b750194
+ 00bfa45c bytes 7d750194
- 00b7da28 ["INT_ADD", "register:40f0:8", ["const:b7da28:8", "const:4:8"]]
- 00b7da28 ["CALL", null, ["callee:00bfa4a0:8"]]
+ 00bfa470 ["INT_ADD", "register:40f0:8", ["const:bfa470:8", "const:4:8"]]
+ 00bfa470 ["CALL", null, ["callee:00bfa4a0:8"]]
- 00b7da28 bytes 0c000094
+ 00bfa470 bytes 0c000094
- 00b7da34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
- 00b7da34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00bfa47c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f80:8"]]
+ 00bfa47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00b7da34 bytes 933e00f9
+ 00bfa47c bytes 93c207f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c39bb4da281669152b12875e9fac117"></a>

### [`00b7da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md) → [`00bfa4a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md) FUN_00bfa4a0

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7d9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7d9d4.md) · 呼出先 3件 [`00b7de0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de0c.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00bdd4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4b0.md)
- 新版 呼出元 1件 [`00bfa41c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa41c.md) · 呼出先 3件 [`00bfa854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa854.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 69.23% / 新版 69.23%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa4b0",
      "incomplete_value": false,
      "site": "00bfa4b4",
      "value": [
        "leaf",
        "const:bfa854:8"
      ]
    },
    "old": {
      "definition_site": "00b7da68",
      "incomplete_value": false,
      "site": "00b7da6c",
      "value": [
        "leaf",
        "const:b7de0c:8"
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7da88"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bfa4d0"
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
      "00bfa4b0",
      "PARAM",
      [
        "storage",
        "00b7de0c",
        null,
        null
      ]
    ],
    [
      "00bfa4b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b7da80"
      ]
    ],
    [
      "unmatched:00b7da84",
      "PARAM",
      [
        "storage",
        "0029440d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa4b0",
      "PARAM",
      [
        "storage",
        "00bfa854",
        null,
        null
      ]
    ],
    [
      "00bfa4b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bfa4c8"
      ]
    ],
    [
      "00bfa4cc",
      "PARAM",
      [
        "storage",
        "002a3d23",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7da6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da6c) · [`00b7da7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da7c) · [`00b7da88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7da58.md#insn-00b7da88)
- 新版 [`00bfa4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa4a0.md#insn-00bfa4b4)

~~~diff
- 00b7da6c ["INT_ADD", "register:40f0:8", ["const:b7da6c:8", "const:4:8"]]
- 00b7da6c ["CALL", null, ["callee:00c59f00:8"]]
+ 00bfa4b4 ["INT_ADD", "register:40f0:8", ["const:bfa4b4:8", "const:4:8"]]
+ 00bfa4b4 ["CALL", null, ["callee:00c59f00:8"]]
- 00b7da6c bytes 917e0194
+ 00bfa4b4 bytes 937e0194
- 00b7da7c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b7da7c ["RETURN", null, ["register:0:8"]]
- 00b7da7c bytes c0035fd6
- 00b7da88 ["INT_ADD", "register:40f0:8", ["const:b7da88:8", "const:4:8"]]
- 00b7da88 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7da88 bytes 12760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad214941b3ac0360f0a66305c8e503a"></a>

### [`00b7de44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md) → [`00bfa88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md) _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md) · 呼出先 4件 [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0630.md)
- 新版 呼出元 1件 [`00c57fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fa0.md) · 呼出先 4件 [`00c57cb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cb0.md) [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d210.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa8e8",
      "incomplete_value": false,
      "site": "00bfa8f8",
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
            "const:9c2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7dea0",
      "incomplete_value": false,
      "site": "00b7deb0",
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
            "const:155:8"
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
      "unmatched:00b7dea0",
      "PARAM",
      [
        "storage",
        "002a4155",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa8e8",
      "PARAM",
      [
        "storage",
        "002b49c2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7deb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7deb0) · [`00b7de74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7de74) · [`00b7de94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7de44.md#insn-00b7de94)
- 新版 [`00bfa8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8f8) · [`00bfa8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8bc) · [`00bfa8dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md#insn-00bfa8dc)

~~~diff
- 00b7deb0 ["INT_ADD", "register:40f0:8", ["const:b7deb0:8", "const:4:8"]]
- 00b7deb0 ["CALL", null, ["callee:00c57cb0:8"]]
+ 00bfa8f8 ["INT_ADD", "register:40f0:8", ["const:bfa8f8:8", "const:4:8"]]
+ 00bfa8f8 ["CALL", null, ["callee:00c57cb0:8"]]
- 00b7deb0 bytes ec740194
+ 00bfa8f8 bytes ee740194
- 00b7de74 ["INT_ADD", "register:40f0:8", ["const:b7de74:8", "const:4:8"]]
- 00b7de74 ["CALL", null, ["callee:00c5d210:8"]]
+ 00bfa8bc ["INT_ADD", "register:40f0:8", ["const:bfa8bc:8", "const:4:8"]]
+ 00bfa8bc ["CALL", null, ["callee:00c5d210:8"]]
- 00b7de74 bytes ef890194
+ 00bfa8bc bytes 558a0194
- 00b7de94 ["INT_ADD", "register:40f0:8", ["const:b7de94:8", "const:4:8"]]
- 00b7de94 ["CALL", null, ["callee:00c57cc0:8"]]
+ 00bfa8dc ["INT_ADD", "register:40f0:8", ["const:bfa8dc:8", "const:4:8"]]
+ 00bfa8dc ["CALL", null, ["callee:00c57cc0:8"]]
- 00b7de94 bytes f7740194
+ 00bfa8dc bytes f9740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f063524632f42662a59d6146a42dcd5"></a>

### [`00b7df0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md) → [`00bfa954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md) _ZNSt6__ndk113random_deviceclEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md) · 呼出先 3件 [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bdb2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2d0.md) [`00be0670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0670.md)
- 新版 呼出元 1件 [`00c57fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57fb0.md) · 呼出先 3件 [`00c57cc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57cc0.md) [`00c57d20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d20.md) [`00c5d250`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5d250.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfa9d0",
      "incomplete_value": false,
      "site": "00bfa9d4",
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
            "const:d02:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7df88",
      "incomplete_value": false,
      "site": "00b7df8c",
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
            "const:60:8"
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
      "definition_site": "00bfa9dc",
      "incomplete_value": false,
      "site": "00bfa9e4",
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
            "const:46b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7df94",
      "incomplete_value": false,
      "site": "00b7df9c",
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
            "const:245:8"
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
      "00bfa9d0",
      "PARAM",
      [
        "storage",
        "002a8060",
        null,
        "string"
      ]
    ],
    [
      "00bfa9dc",
      "PARAM",
      [
        "storage",
        "0029c245",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfa9d0",
      "PARAM",
      [
        "storage",
        "002b8d02",
        null,
        "string"
      ]
    ],
    [
      "00bfa9dc",
      "PARAM",
      [
        "storage",
        "002ac46b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7df8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df8c) · [`00b7df9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df9c) · [`00b7df30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7df0c.md#insn-00b7df30)
- 新版 [`00bfa9d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa9d4) · [`00bfa9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa9e4) · [`00bfa978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa954.md#insn-00bfa978)

~~~diff
- 00b7df8c ["INT_ADD", "register:40f0:8", ["const:b7df8c:8", "const:4:8"]]
- 00b7df8c ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa9d4 ["INT_ADD", "register:40f0:8", ["const:bfa9d4:8", "const:4:8"]]
+ 00bfa9d4 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7df8c bytes d1740194
+ 00bfa9d4 bytes d3740194
- 00b7df9c ["INT_ADD", "register:40f0:8", ["const:b7df9c:8", "const:4:8"]]
- 00b7df9c ["CALL", null, ["callee:00c57d20:8"]]
+ 00bfa9e4 ["INT_ADD", "register:40f0:8", ["const:bfa9e4:8", "const:4:8"]]
+ 00bfa9e4 ["CALL", null, ["callee:00c57d20:8"]]
- 00b7df9c bytes cd740194
+ 00bfa9e4 bytes cf740194
- 00b7df30 ["INT_ADD", "register:40f0:8", ["const:b7df30:8", "const:4:8"]]
- 00b7df30 ["CALL", null, ["callee:00c57cc0:8"]]
+ 00bfa978 ["INT_ADD", "register:40f0:8", ["const:bfa978:8", "const:4:8"]]
+ 00bfa978 ["CALL", null, ["callee:00c57cc0:8"]]
- 00b7df30 bytes d0740194
+ 00bfa978 bytes d2740194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78a6462c3246b9cf5f67ac548b058944"></a>

### [`00b7e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e0cc.md) → [`00bfab14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab14.md) _ZNSt6__ndk18ios_base7failureC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERKNS_10error_codeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1150.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5dd50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd50.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfab3c",
      "incomplete_value": true,
      "site": "00bfab40",
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
      "definition_site": "00b7e0f4",
      "incomplete_value": true,
      "site": "00b7e0f8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e0e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bfab30"
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
      "unmatched:00b7e0e8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1150"
      ]
    ],
    [
      "00bfab38",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfab40",
      "DATA",
      [
        "storage",
        "00c12fd8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bfab30",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dd50"
      ]
    ],
    [
      "00bfab38",
      "READ",
      [
        "storage",
        "00c9b6e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfab40",
      "DATA",
      [
        "storage",
        "00c92980",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e0cc.md#insn-00b7e0e8) · [`00b7e0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e0cc.md#insn-00b7e0ec)
- 新版 [`00bfab30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab14.md#insn-00bfab30) · [`00bfab34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab14.md#insn-00bfab34)

~~~diff
- 00b7e0e8 ["INT_ADD", "register:40f0:8", ["const:b7e0e8:8", "const:4:8"]]
- 00b7e0e8 ["CALL", null, ["ram:be1150:8"]]
- 00b7e0e8 bytes 1a8c0194
+ 00bfab30 ["INT_ADD", "register:40f0:8", ["const:bfab30:8", "const:4:8"]]
+ 00bfab30 ["CALL", null, ["ram:c5dd50:8"]]
+ 00bfab30 bytes 888c0194
- 00b7e0ec ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfab34 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b7e0ec bytes e80400b0
+ 00bfab34 bytes 080500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfd293d757afcf93ef3cc348dd228a72"></a>

### [`00b7e10c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e10c.md) → [`00bfab54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab54.md) _ZNSt6__ndk18ios_base7failureC1EPKcRKNS_10error_codeE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be1300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1300.md) · 呼出先 1件 [`00be1160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1160.md)
- 新版 呼出元 1件 [`00c5df00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df00.md) · 呼出先 1件 [`00c5dd60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dd60.md)

変更の種類 call, call_count, cfg_edge_inventory, constant, operands_and_dependencies, operation_sequence, store_value, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfab7c",
      "incomplete_value": true,
      "site": "00bfab80",
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
      "definition_site": "00b7e134",
      "incomplete_value": true,
      "site": "00b7e138",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e128"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00bfab70"
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
      "unmatched:00b7e128",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1160"
      ]
    ],
    [
      "00bfab78",
      "READ",
      [
        "storage",
        "00c1bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfab80",
      "DATA",
      [
        "storage",
        "00c12fd8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bfab70",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dd60"
      ]
    ],
    [
      "00bfab78",
      "READ",
      [
        "storage",
        "00c9b6e8",
        null,
        "pointer"
      ]
    ],
    [
      "00bfab80",
      "DATA",
      [
        "storage",
        "00c92980",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e10c.md#insn-00b7e128) · [`00b7e12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e10c.md#insn-00b7e12c)
- 新版 [`00bfab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab54.md#insn-00bfab70) · [`00bfab74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab54.md#insn-00bfab74)

~~~diff
- 00b7e128 ["INT_ADD", "register:40f0:8", ["const:b7e128:8", "const:4:8"]]
- 00b7e128 ["CALL", null, ["ram:be1160:8"]]
- 00b7e128 bytes 0e8c0194
+ 00bfab70 ["INT_ADD", "register:40f0:8", ["const:bfab70:8", "const:4:8"]]
+ 00bfab70 ["CALL", null, ["ram:c5dd60:8"]]
+ 00bfab70 bytes 7c8c0194
- 00b7e12c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfab74 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b7e12c bytes e80400b0
+ 00bfab74 bytes 080500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-204325b95b34b13da586ad880ea0f9bc"></a>

### [`00b7e284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) → [`00bfaccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md) _ZNSt6__ndk18ios_base6xallocEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bface0",
      "incomplete_value": true,
      "site": "00bface4",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:6f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e298",
      "incomplete_value": true,
      "site": "00b7e29c",
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
                "const:cc8:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bface0",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00bface0",
      "PARAM",
      [
        "storage",
        "010a2090",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bface0",
      "READ",
      [
        "storage",
        "00c9b6f8",
        null,
        "pointer"
      ]
    ],
    [
      "00bface0",
      "PARAM",
      [
        "storage",
        "01126f98",
        "_ZNSt6__ndk18ios_base9__xindex_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md#insn-00b7e29c) · [`00b7e290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md#insn-00b7e290) · [`00b7e298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md#insn-00b7e298)
- 新版 [`00bface4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md#insn-00bface4) · [`00bfacd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md#insn-00bfacd8) · [`00bface0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md#insn-00bface0)

~~~diff
- 00b7e29c ["INT_ADD", "register:40f0:8", ["const:b7e29c:8", "const:4:8"]]
- 00b7e29c ["CALL", null, ["callee:00c53880:8"]]
+ 00bface4 ["INT_ADD", "register:40f0:8", ["const:bface4:8", "const:4:8"]]
+ 00bface4 ["CALL", null, ["callee:00c53880:8"]]
- 00b7e29c bytes e5620194
+ 00bface4 bytes e7620194
- 00b7e290 ["COPY", "register:4008:8", ["const:c1b000:8"]]
+ 00bfacd8 ["COPY", "register:4008:8", ["const:c9b000:8"]]
- 00b7e290 bytes e10400b0
+ 00bfacd8 bytes 010500b0
- 00b7e298 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cc8:8"]]
- 00b7e298 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bface0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:6f8:8"]]
+ 00bface0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e298 bytes 216446f9
+ 00bface0 bytes 217c43f9
~~~


<a id="compare-16f7fa833fe9f6b63e90e7d2904614e5"></a>

### [`00b7e3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md) → [`00bfae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md) _ZNSt6__ndk18ios_base5pwordEi

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 68.75% / 新版 84.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e3c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7e3c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7e3c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e3c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b7e3cc",
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
      "00bfae0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bfae10",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00bfae14",
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

- 旧版 [`00b7e3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e3c4) · [`00b7e3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e3c8) · [`00b7e3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md#insn-00b7e3cc)

~~~diff
- 00b7e3c4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b7e3c4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b7e3c4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00b7e3c4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b7e3c4 bytes fd7bbca9
- 00b7e3c8 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b7e3c8 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b7e3c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b7e3c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e3c8 bytes f85f01a9
- 00b7e3cc ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00b7e3cc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00b7e3cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b7e3cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b7e3cc bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9853a6076ea03cb983c1745b6bdc775c"></a>

### [`00b7e4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md) → [`00bfaf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md) _ZNSt6__ndk18ios_base17register_callbackEPFvNS0_5eventERS0_iEi

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) [`00bdd250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) [`00c59ca0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ca0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfaff4",
      "incomplete_value": false,
      "site": "00bfaff8",
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
            "const:45a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e5ac",
      "incomplete_value": false,
      "site": "00b7e5b0",
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
            "const:81f:8"
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
      "00bfaff4",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfaff4",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e5b0) · [`00b7e528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e528) · [`00b7e554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md#insn-00b7e554)
- 新版 [`00bfaff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaff8) · [`00bfaf70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaf70) · [`00bfaf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md#insn-00bfaf9c)

~~~diff
- 00b7e5b0 ["INT_ADD", "register:40f0:8", ["const:b7e5b0:8", "const:4:8"]]
- 00b7e5b0 ["CALL", null, ["callee:00bfb11c:8"]]
+ 00bfaff8 ["INT_ADD", "register:40f0:8", ["const:bfaff8:8", "const:4:8"]]
+ 00bfaff8 ["CALL", null, ["callee:00bfb11c:8"]]
- 00b7e5b0 bytes 49000094
+ 00bfaff8 bytes 49000094
- 00b7e528 ["INT_ADD", "register:40f0:8", ["const:b7e528:8", "const:4:8"]]
- 00b7e528 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00bfaf70 ["INT_ADD", "register:40f0:8", ["const:bfaf70:8", "const:4:8"]]
+ 00bfaf70 ["CALL", null, ["callee:00c59ca0:8"]]
- 00b7e528 bytes 4a7b0194
+ 00bfaf70 bytes 4c7b0194
- 00b7e554 ["INT_ADD", "register:40f0:8", ["const:b7e554:8", "const:4:8"]]
- 00b7e554 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00bfaf9c ["INT_ADD", "register:40f0:8", ["const:bfaf9c:8", "const:4:8"]]
+ 00bfaf9c ["CALL", null, ["callee:00c59ca0:8"]]
- 00b7e554 bytes 3f7b0194
+ 00bfaf9c bytes 417b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-034d67c6e895d627b5fbf005c169f8c0"></a>

### [`00b7e5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md) → [`00bfaffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md) _ZNSt6__ndk18ios_baseD1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be12f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12f0.md) · 呼出先 2件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)
- 新版 呼出元 2件 [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md) [`00c5def0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5def0.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c58260`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58260.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb020",
      "incomplete_value": true,
      "site": "00bfb024",
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
      "definition_site": "00b7e5d8",
      "incomplete_value": true,
      "site": "00b7e5dc",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfb064",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7e61c",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfb018",
      "READ",
      [
        "storage",
        "00c1bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb024",
      "DATA",
      [
        "storage",
        "00c13000",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bfb064",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfb018",
      "READ",
      [
        "storage",
        "00c9b700",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb024",
      "DATA",
      [
        "storage",
        "00c929a8",
        null,
        "undefined1[32]"
      ]
    ],
    [
      "00bfb064",
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

- 旧版 [`00b7e61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e61c) · [`00b7e5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e5c8) · [`00b7e5d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e5b4.md#insn-00b7e5d0)
- 新版 [`00bfb064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb064) · [`00bfb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb010) · [`00bfb018`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaffc.md#insn-00bfb018)

~~~diff
- 00b7e61c ["INT_ADD", "register:40f0:8", ["const:b7e61c:8", "const:4:8"]]
- 00b7e61c ["CALL", null, ["ram:bdb440:8"]]
+ 00bfb064 ["INT_ADD", "register:40f0:8", ["const:bfb064:8", "const:4:8"]]
+ 00bfb064 ["CALL", null, ["ram:c57e90:8"]]
- 00b7e61c bytes 89730194
+ 00bfb064 bytes 8b730194
- 00b7e5c8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfb010 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b7e5c8 bytes e80400b0
+ 00bfb010 bytes 08050090
- 00b7e5d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00b7e5d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:700:8"]]
+ 00bfb018 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7e5d0 bytes 086946f9
+ 00bfb018 bytes 088143f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42dc1aac09226e1c304af9a933c717c"></a>

### [`00b7e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md) → [`00bfb0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md) _ZNSt6__ndk18ios_base5clearEj

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) · 呼出先 1件 [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md)
- 新版 呼出元 1件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) · 呼出先 1件 [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb114",
      "incomplete_value": false,
      "site": "00bfb118",
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
            "const:45a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e6cc",
      "incomplete_value": false,
      "site": "00b7e6d0",
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
            "const:81f:8"
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
      "00bfb114",
      "PARAM",
      [
        "storage",
        "0029781f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bfb114",
      "PARAM",
      [
        "storage",
        "002a745a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md#insn-00b7e6d0) · [`00b7e6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md#insn-00b7e6c8) · [`00b7e6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md#insn-00b7e6cc)
- 新版 [`00bfb118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md#insn-00bfb118) · [`00bfb110`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md#insn-00bfb110) · [`00bfb114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md#insn-00bfb114)

~~~diff
- 00b7e6d0 ["INT_ADD", "register:40f0:8", ["const:b7e6d0:8", "const:4:8"]]
- 00b7e6d0 ["CALL", null, ["callee:00bfb11c:8"]]
+ 00bfb118 ["INT_ADD", "register:40f0:8", ["const:bfb118:8", "const:4:8"]]
+ 00bfb118 ["CALL", null, ["callee:00bfb11c:8"]]
- 00b7e6d0 bytes 01000094
+ 00bfb118 bytes 01000094
- 00b7e6c8 ["COPY", "register:4000:8", ["const:297000:8"]]
+ 00bfb110 ["COPY", "register:4000:8", ["const:2a7000:8"]]
- 00b7e6c8 bytes c0b8ffb0
+ 00bfb110 bytes 60b5ff90
- 00b7e6cc ["COPY", "tmp:0:8", ["const:81f:8"]]
- 00b7e6cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e6cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b7e6cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bfb114 ["COPY", "tmp:0:8", ["const:45a:8"]]
+ 00bfb114 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb114 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bfb114 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b7e6cc bytes 007c2091
+ 00bfb114 bytes 00681191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d88f14ea10c6a0db92a9c5ad8392c097"></a>

### [`00b7e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md) → [`00bfb11c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md) FUN_00bfb11c

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00b7e2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e2ac.md) [`00b7e3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e3c0.md) [`00b7e4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e4d4.md) [`00b7e694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e694.md) · 呼出先 6件 [`00b7e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e14c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 4件 [`00bfacf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfacf4.md) [`00bfae08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfae08.md) [`00bfaf1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaf1c.md) [`00bfb0dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb0dc.md) · 呼出先 6件 [`00bfab94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfab94.md) [`00c57a50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a50.md) [`00c57a70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a70.md) [`00c57af0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57af0.md) [`00c57b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57b10.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb15c",
      "incomplete_value": false,
      "site": "00bfb15c",
      "value": [
        "leaf",
        "const:ca4400:8"
      ]
    },
    "old": {
      "definition_site": "00b7e714",
      "incomplete_value": false,
      "site": "00b7e714",
      "value": [
        "leaf",
        "const:c24920:8"
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfb17c",
      "incomplete_value": true,
      "site": "00bfb184",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:708:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e734",
      "incomplete_value": true,
      "site": "00b7e73c",
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
                "const:cd8:8"
              ]
            ]
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
      "definition_site": "00bfb180",
      "incomplete_value": true,
      "site": "00bfb184",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:6f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e738",
      "incomplete_value": true,
      "site": "00b7e73c",
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
                "const:cc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bfb148",
      "READ",
      [
        "storage",
        "010a2088",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb15c",
      "DATA",
      [
        "storage",
        "00c24920",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb17c",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfb148",
      "READ",
      [
        "storage",
        "01126f90",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb15c",
      "DATA",
      [
        "storage",
        "00ca4400",
        null,
        "pointer"
      ]
    ],
    [
      "00bfb17c",
      "READ",
      [
        "storage",
        "00c9b708",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e73c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e73c) · [`00b7e748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e748) · [`00b7e758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e6d4.md#insn-00b7e758)
- 新版 [`00bfb184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb184) · [`00bfb190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb190) · [`00bfb1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb11c.md#insn-00bfb1a0)

~~~diff
- 00b7e73c ["INT_ADD", "register:40f0:8", ["const:b7e73c:8", "const:4:8"]]
- 00b7e73c ["CALL", null, ["callee:00c57b10:8"]]
+ 00bfb184 ["INT_ADD", "register:40f0:8", ["const:bfb184:8", "const:4:8"]]
+ 00bfb184 ["CALL", null, ["callee:00c57b10:8"]]
- 00b7e73c bytes 61720194
+ 00bfb184 bytes 63720194
- 00b7e748 ["INT_ADD", "register:40f0:8", ["const:b7e748:8", "const:4:8"]]
- 00b7e748 ["CALL", null, ["callee:00c57a50:8"]]
+ 00bfb190 ["INT_ADD", "register:40f0:8", ["const:bfb190:8", "const:4:8"]]
+ 00bfb190 ["CALL", null, ["callee:00c57a50:8"]]
- 00b7e748 bytes 2e720194
+ 00bfb190 bytes 30720194
- 00b7e758 ["INT_ADD", "register:40f0:8", ["const:b7e758:8", "const:4:8"]]
- 00b7e758 ["CALL", null, ["callee:00c57a70:8"]]
+ 00bfb1a0 ["INT_ADD", "register:40f0:8", ["const:bfb1a0:8", "const:4:8"]]
+ 00bfb1a0 ["CALL", null, ["callee:00c57a70:8"]]
- 00b7e758 bytes 32720194
+ 00bfb1a0 bytes 34720194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db67c231f012208f8c2e58c858bc3edd"></a>

### [`00b7e774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e774.md) → [`00bfb1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md) _ZNSt6__ndk18ios_base4initEPv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)

変更の種類 constant, control_flow, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfb1cc",
      "incomplete_value": true,
      "site": "00bfb1e0",
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
                "const:ff0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7e784",
      "incomplete_value": true,
      "site": "00b7e798",
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
                "const:950:8"
              ]
            ]
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
      "00bfb1cc",
      "READ",
      [
        "storage",
        "002b1950",
        null,
        null
      ]
    ],
    [
      "00bfb204",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd950"
      ]
    ]
  ],
  "added": [
    [
      "00bfb1cc",
      "READ",
      [
        "storage",
        "002c2ff0",
        null,
        null
      ]
    ],
    [
      "00bfb204",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a3a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7e778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e774.md#insn-00b7e778) · [`00b7e784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e774.md#insn-00b7e784) · [`00b7e7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e774.md#insn-00b7e7bc)
- 新版 [`00bfb1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md#insn-00bfb1c0) · [`00bfb1cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md#insn-00bfb1cc) · [`00bfb204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb1bc.md#insn-00bfb204)

~~~diff
- 00b7e778 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00bfb1c0 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 00b7e778 bytes 89b9fff0
+ 00bfb1c0 bytes 29b6fff0
- 00b7e784 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:950:8"]]
- 00b7e784 ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
- 00b7e784 ["COPY", "register:5010:8", ["const:0:8"]]
- 00b7e784 ["COPY", "register:5018:8", ["const:0:8"]]
+ 00bfb1cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
+ 00bfb1cc ["LOAD", "register:5000:16", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb1cc ["COPY", "register:5010:8", ["const:0:8"]]
+ 00bfb1cc ["COPY", "register:5018:8", ["const:0:8"]]
- 00b7e784 bytes 2055c23d
+ 00bfb1cc bytes 20fdc33d
- 00b7e7bc ["BRANCH", null, ["ram:bdd950:8"]]
+ 00bfb204 ["BRANCH", null, ["ram:c5a3a0:8"]]
- 00b7e7bc bytes 657c0114
+ 00bfb204 bytes 677c0114
~~~


<a id="compare-3d783f30e4001ec5b70ec6379e23f2a8"></a>

### [`00b7eb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md) → [`00bfb564`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md) _ZNSt6__ndk18ios_base4swapERS0_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md) · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md) · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.59% / 新版 98.59%

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
      "site": "00bfb5f8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7ebb0",
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
      "00bfb5f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfb5f8",
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

- 旧版 [`00b7ebb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7ebb0) · [`00b7eb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7eb90) · [`00b7eb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7eb1c.md#insn-00b7eb9c)
- 新版 [`00bfb5f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5f8) · [`00bfb5d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5d8) · [`00bfb5e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb564.md#insn-00bfb5e4)

~~~diff
- 00b7ebb0 ["INT_ADD", "register:40f0:8", ["const:b7ebb0:8", "const:4:8"]]
- 00b7ebb0 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfb5f8 ["INT_ADD", "register:40f0:8", ["const:bfb5f8:8", "const:4:8"]]
+ 00bfb5f8 ["CALL", null, ["ram:c57e90:8"]]
- 00b7ebb0 bytes 24720194
+ 00bfb5f8 bytes 26720194
- 00b7eb90 ["INT_ADD", "register:40f0:8", ["const:b7eb90:8", "const:4:8"]]
- 00b7eb90 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfb5d8 ["INT_ADD", "register:40f0:8", ["const:bfb5d8:8", "const:4:8"]]
+ 00bfb5d8 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7eb90 bytes 7c7b0194
+ 00bfb5d8 bytes 7e7b0194
- 00b7eb9c ["INT_ADD", "register:40f0:8", ["const:b7eb9c:8", "const:4:8"]]
- 00b7eb9c ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bfb5e4 ["INT_ADD", "register:40f0:8", ["const:bfb5e4:8", "const:4:8"]]
+ 00bfb5e4 ["CALL", null, ["callee:00c5dee0:8"]]
- 00b7eb9c bytes d1890194
+ 00bfb5e4 bytes 3f8a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-317d28d1c83dc6c22fc561a82fdaea7f"></a>

### [`00b7ec90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md) → [`00bfb6d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md) _ZNSt6__ndk18ios_base15sync_with_stdioEb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bfb6e8",
      "incomplete_value": false,
      "site": "00bfb6e8",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7eca0",
      "incomplete_value": false,
      "site": "00b7eca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00bfb6e4",
      "READ",
      [
        "storage",
        "00c24928",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb6e8",
      "WRITE",
      [
        "storage",
        "00c24928",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bfb6e4",
      "READ",
      [
        "storage",
        "00ca4408",
        null,
        "undefined1"
      ]
    ],
    [
      "00bfb6e8",
      "WRITE",
      [
        "storage",
        "00ca4408",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7eca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md#insn-00b7eca0) · [`00b7ec94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md#insn-00b7ec94) · [`00b7ec9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec90.md#insn-00b7ec9c)
- 新版 [`00bfb6e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md#insn-00bfb6e8) · [`00bfb6dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md#insn-00bfb6dc) · [`00bfb6e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6d8.md#insn-00bfb6e4)

~~~diff
- 00b7eca0 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b7eca0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:928:8"]]
- 00b7eca0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00bfb6e8 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00bfb6e8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "const:408:8"]]
+ 00bfb6e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b7eca0 bytes 49a12439
+ 00bfb6e8 bytes 49211039
- 00b7ec94 ["COPY", "register:4050:8", ["const:c24000:8"]]
+ 00bfb6dc ["COPY", "register:4050:8", ["const:ca4000:8"]]
- 00b7ec94 bytes 2a0500d0
+ 00bfb6dc bytes 4a0500b0
- 00b7ec9c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:928:8"]]
- 00b7ec9c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b7ec9c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bfb6e4 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:408:8"]]
+ 00bfb6e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bfb6e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b7ec9c bytes 48a16439
+ 00bfb6e4 bytes 48215039
~~~


<a id="compare-a4e0fc65240e4b0bec14c1fc1386735e"></a>

### [`00b7f02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md) → [`00bfba74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00c57df0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57df0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfba94",
      "incomplete_value": true,
      "site": "00bfba94",
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
      "definition_site": "00b7f04c",
      "incomplete_value": true,
      "site": "00b7f04c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfba98",
      "value": [
        "leaf",
        "ram:c5a3a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f050",
      "value": [
        "leaf",
        "ram:bdd950:8"
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
      "00bfba8c",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00bfba94",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ],
    [
      "00bfba98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd950"
      ]
    ]
  ],
  "added": [
    [
      "00bfba8c",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00bfba94",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bfba98",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a3a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md#insn-00b7f050) · [`00b7f03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md#insn-00b7f03c) · [`00b7f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f02c.md#insn-00b7f044)
- 新版 [`00bfba98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md#insn-00bfba98) · [`00bfba84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md#insn-00bfba84) · [`00bfba8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfba74.md#insn-00bfba8c)

~~~diff
- 00b7f050 ["INT_ADD", "register:40f0:8", ["const:b7f050:8", "const:4:8"]]
- 00b7f050 ["CALL", null, ["ram:bdd950:8"]]
+ 00bfba98 ["INT_ADD", "register:40f0:8", ["const:bfba98:8", "const:4:8"]]
+ 00bfba98 ["CALL", null, ["ram:c5a3a0:8"]]
- 00b7f050 bytes 407a0194
+ 00bfba98 bytes 427a0194
- 00b7f03c ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfba84 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b7f03c bytes e8040090
+ 00bfba84 bytes 08050090
- 00b7f044 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 00b7f044 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfba8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 00bfba8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f044 bytes 082945f9
+ 00bfba8c bytes 082542f9
~~~


<a id="compare-5c414fe3f0c9eded0721ef10db81fac0"></a>

### [`00b7f070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md) → [`00bfbab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1ERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbae0",
      "incomplete_value": true,
      "site": "00bfbae0",
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
      "definition_site": "00b7f098",
      "incomplete_value": true,
      "site": "00b7f098",
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
      "00bfbad4",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbae0",
      "DATA",
      [
        "storage",
        "00c11220",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfbad4",
      "READ",
      [
        "storage",
        "00c9b448",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbae0",
      "DATA",
      [
        "storage",
        "00c908b0",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md#insn-00b7f080) · [`00b7f08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md#insn-00b7f08c) · [`00b7f09c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f070.md#insn-00b7f09c)
- 新版 [`00bfbac8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md#insn-00bfbac8) · [`00bfbad4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md#insn-00bfbad4) · [`00bfbae4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbab8.md#insn-00bfbae4)

~~~diff
- 00b7f080 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfbac8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b7f080 bytes e8040090
+ 00bfbac8 bytes 08050090
- 00b7f08c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
- 00b7f08c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbad4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:448:8"]]
+ 00bfbad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f08c bytes 082945f9
+ 00bfbad4 bytes 082542f9
- 00b7f09c ["INT_ADD", "register:40f0:8", ["const:b7f09c:8", "const:4:8"]]
- 00b7f09c ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfbae4 ["INT_ADD", "register:40f0:8", ["const:bfbae4:8", "const:4:8"]]
+ 00bfbae4 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7f09c bytes 397a0194
+ 00bfbae4 bytes 3b7a0194
~~~


<a id="compare-f58d26129d395e1c610dc0a4574af394"></a>

### [`00b7f118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md) → [`00bfbb60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md) _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "00bfbba4",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f15c",
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
      "00bfbba4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfbba4",
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

- 旧版 [`00b7f15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f15c) · [`00b7f13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f13c) · [`00b7f148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f118.md#insn-00b7f148)
- 新版 [`00bfbba4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbba4) · [`00bfbb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbb84) · [`00bfbb90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbb60.md#insn-00bfbb90)

~~~diff
- 00b7f15c ["INT_ADD", "register:40f0:8", ["const:b7f15c:8", "const:4:8"]]
- 00b7f15c ["CALL", null, ["ram:bdb440:8"]]
+ 00bfbba4 ["INT_ADD", "register:40f0:8", ["const:bfbba4:8", "const:4:8"]]
+ 00bfbba4 ["CALL", null, ["ram:c57e90:8"]]
- 00b7f15c bytes b9700194
+ 00bfbba4 bytes bb700194
- 00b7f13c ["INT_ADD", "register:40f0:8", ["const:b7f13c:8", "const:4:8"]]
- 00b7f13c ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bfbb84 ["INT_ADD", "register:40f0:8", ["const:bfbb84:8", "const:4:8"]]
+ 00bfbb84 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b7f13c bytes 117a0194
+ 00bfbb84 bytes 137a0194
- 00b7f148 ["INT_ADD", "register:40f0:8", ["const:b7f148:8", "const:4:8"]]
- 00b7f148 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bfbb90 ["INT_ADD", "register:40f0:8", ["const:bfbb90:8", "const:4:8"]]
+ 00bfbb90 ["CALL", null, ["callee:00c5dee0:8"]]
- 00b7f148 bytes 66880194
+ 00bfbb90 bytes d4880194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91071ea59e1b8f8a6bb74748083a86dc"></a>

### [`00b7f278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md) → [`00bfbcc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbcec",
      "incomplete_value": true,
      "site": "00bfbcec",
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
      "definition_site": "00b7f2a4",
      "incomplete_value": true,
      "site": "00b7f2a4",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bfbcf0",
      "incomplete_value": true,
      "site": "00bfbcf0",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f2a8",
      "incomplete_value": true,
      "site": "00b7f2a8",
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
            "const:18:8"
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
      "00bfbcdc",
      "READ",
      [
        "storage",
        "00c1b440",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbcec",
      "DATA",
      [
        "storage",
        "00c13090",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbcf0",
      "DATA",
      [
        "storage",
        "00c13068",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfbcdc",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbcec",
      "DATA",
      [
        "storage",
        "00c92a38",
        null,
        "pointer"
      ]
    ],
    [
      "00bfbcf0",
      "DATA",
      [
        "storage",
        "00c92a10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md#insn-00b7f288) · [`00b7f294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md#insn-00b7f294) · [`00b7f2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f278.md#insn-00b7f2b0)
- 新版 [`00bfbcd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcd0) · [`00bfbcdc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcdc) · [`00bfbcf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbcc0.md#insn-00bfbcf8)

~~~diff
- 00b7f288 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bfbcd0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
- 00b7f288 bytes e8040090
+ 00bfbcd0 bytes e80400f0
- 00b7f294 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:440:8"]]
- 00b7f294 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bfbcdc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
+ 00bfbcdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b7f294 bytes 082142f9
+ 00bfbcdc bytes 081947f9
- 00b7f2b0 ["INT_ADD", "register:40f0:8", ["const:b7f2b0:8", "const:4:8"]]
- 00b7f2b0 ["CALL", null, ["callee:00c57de0:8"]]
+ 00bfbcf8 ["INT_ADD", "register:40f0:8", ["const:bfbcf8:8", "const:4:8"]]
+ 00bfbcf8 ["CALL", null, ["callee:00c57de0:8"]]
- 00b7f2b0 bytes 38700194
+ 00bfbcf8 bytes 3a700194
~~~


<a id="compare-c2150d99161d3f6c9ce0503236ee3675"></a>

### [`00b7f5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md) → [`00bfbff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.84% / 新版 98.84%

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
      "site": "00bfc024",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f5dc",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfc024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfc024",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f5dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f5dc) · [`00b7f640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f640) · [`00b7f678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f5ac.md#insn-00b7f678)
- 新版 [`00bfc024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc024) · [`00bfc088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc088) · [`00bfc0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfbff4.md#insn-00bfc0c0)

~~~diff
- 00b7f5dc ["INT_ADD", "register:40f0:8", ["const:b7f5dc:8", "const:4:8"]]
- 00b7f5dc ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc024 ["INT_ADD", "register:40f0:8", ["const:bfc024:8", "const:4:8"]]
+ 00bfc024 ["CALL", null, ["ram:c599d0:8"]]
- 00b7f5dc bytes 69760194
+ 00bfc024 bytes 6b760194
- 00b7f640 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f640 ["INT_ADD", "register:40f0:8", ["const:b7f640:8", "const:4:8"]]
- 00b7f640 ["CALLIND", null, ["register:0:8"]]
+ 00bfc088 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc088 ["INT_ADD", "register:40f0:8", ["const:bfc088:8", "const:4:8"]]
+ 00bfc088 ["CALLIND", null, ["register:0:8"]]
- 00b7f640 bytes 00013fd6
+ 00bfc088 bytes 00013fd6
- 00b7f678 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b7f678 ["INT_ADD", "register:40f0:8", ["const:b7f678:8", "const:4:8"]]
- 00b7f678 ["CALLIND", null, ["register:0:8"]]
+ 00bfc0c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfc0c0 ["INT_ADD", "register:40f0:8", ["const:bfc0c0:8", "const:4:8"]]
+ 00bfc0c0 ["CALLIND", null, ["register:0:8"]]
- 00b7f678 bytes 00013fd6
+ 00bfc0c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c804387b8b04bef69ccdf1268a541943"></a>

### [`00b7f768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md) → [`00bfc1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md) FUN_00bfc1b0

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f760.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc1a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1a8.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00bfc1dc",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f794",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc204",
      "incomplete_value": true,
      "site": "00bfc208",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f7bc",
      "incomplete_value": true,
      "site": "00b7f7c0",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc238",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f7f0",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc204",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc204",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc1dc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc204",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc204",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f794) · [`00b7f7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f7c0) · [`00b7f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f768.md#insn-00b7f7f0)
- 新版 [`00bfc1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc1dc) · [`00bfc208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc208) · [`00bfc238`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc1b0.md#insn-00bfc238)

~~~diff
- 00b7f794 ["INT_ADD", "register:40f0:8", ["const:b7f794:8", "const:4:8"]]
- 00b7f794 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc1dc ["INT_ADD", "register:40f0:8", ["const:bfc1dc:8", "const:4:8"]]
+ 00bfc1dc ["CALL", null, ["ram:c599d0:8"]]
- 00b7f794 bytes fb750194
+ 00bfc1dc bytes fd750194
- 00b7f7c0 ["INT_ADD", "register:40f0:8", ["const:b7f7c0:8", "const:4:8"]]
- 00b7f7c0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc208 ["INT_ADD", "register:40f0:8", ["const:bfc208:8", "const:4:8"]]
+ 00bfc208 ["CALL", null, ["callee:00c57e80:8"]]
- 00b7f7c0 bytes 1c6f0194
+ 00bfc208 bytes 1e6f0194
- 00b7f7f0 ["INT_ADD", "register:40f0:8", ["const:b7f7f0:8", "const:4:8"]]
- 00b7f7f0 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc238 ["INT_ADD", "register:40f0:8", ["const:bfc238:8", "const:4:8"]]
+ 00bfc238 ["CALL", null, ["ram:c57e90:8"]]
- 00b7f7f0 bytes 146f0194
+ 00bfc238 bytes 166f0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f70a2432f61185914fbe1208ef3ce21"></a>

### [`00b7f8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md) → [`00bfc2e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md) FUN_00bfc2e8

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7f898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f898.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc2e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e0.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.31% / 新版 95.31%

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
      "site": "00bfc314",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f8cc",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc33c",
      "incomplete_value": true,
      "site": "00bfc340",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7f8f4",
      "incomplete_value": true,
      "site": "00b7f8f8",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc370",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7f928",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc33c",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc33c",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc314",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc33c",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc33c",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7f8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f8cc) · [`00b7f8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f8f8) · [`00b7f928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f8a0.md#insn-00b7f928)
- 新版 [`00bfc314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc314) · [`00bfc340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc340) · [`00bfc370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc2e8.md#insn-00bfc370)

~~~diff
- 00b7f8cc ["INT_ADD", "register:40f0:8", ["const:b7f8cc:8", "const:4:8"]]
- 00b7f8cc ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc314 ["INT_ADD", "register:40f0:8", ["const:bfc314:8", "const:4:8"]]
+ 00bfc314 ["CALL", null, ["ram:c599d0:8"]]
- 00b7f8cc bytes ad750194
+ 00bfc314 bytes af750194
- 00b7f8f8 ["INT_ADD", "register:40f0:8", ["const:b7f8f8:8", "const:4:8"]]
- 00b7f8f8 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc340 ["INT_ADD", "register:40f0:8", ["const:bfc340:8", "const:4:8"]]
+ 00bfc340 ["CALL", null, ["callee:00c57e80:8"]]
- 00b7f8f8 bytes ce6e0194
+ 00bfc340 bytes d06e0194
- 00b7f928 ["INT_ADD", "register:40f0:8", ["const:b7f928:8", "const:4:8"]]
- 00b7f928 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc370 ["INT_ADD", "register:40f0:8", ["const:bfc370:8", "const:4:8"]]
+ 00bfc370 ["CALL", null, ["ram:c57e90:8"]]
- 00b7f928 bytes c66e0194
+ 00bfc370 bytes c86e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a61dfc6068ca03eacd276cc1bf9bbbe3"></a>

### [`00b7fa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md) → [`00bfc460`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md) FUN_00bfc460

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa10.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc458`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc458.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00bfc48c",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fa44",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc4b4",
      "incomplete_value": true,
      "site": "00bfc4b8",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fa6c",
      "incomplete_value": true,
      "site": "00b7fa70",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc4e8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7faa0",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc48c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc4b4",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc4b4",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc48c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc4b4",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc4b4",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7fa44) · [`00b7fa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7fa70) · [`00b7faa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fa18.md#insn-00b7faa0)
- 新版 [`00bfc48c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc48c) · [`00bfc4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc4b8) · [`00bfc4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc460.md#insn-00bfc4e8)

~~~diff
- 00b7fa44 ["INT_ADD", "register:40f0:8", ["const:b7fa44:8", "const:4:8"]]
- 00b7fa44 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc48c ["INT_ADD", "register:40f0:8", ["const:bfc48c:8", "const:4:8"]]
+ 00bfc48c ["CALL", null, ["ram:c599d0:8"]]
- 00b7fa44 bytes 4f750194
+ 00bfc48c bytes 51750194
- 00b7fa70 ["INT_ADD", "register:40f0:8", ["const:b7fa70:8", "const:4:8"]]
- 00b7fa70 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc4b8 ["INT_ADD", "register:40f0:8", ["const:bfc4b8:8", "const:4:8"]]
+ 00bfc4b8 ["CALL", null, ["callee:00c57e80:8"]]
- 00b7fa70 bytes 706e0194
+ 00bfc4b8 bytes 726e0194
- 00b7faa0 ["INT_ADD", "register:40f0:8", ["const:b7faa0:8", "const:4:8"]]
- 00b7faa0 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc4e8 ["INT_ADD", "register:40f0:8", ["const:bfc4e8:8", "const:4:8"]]
+ 00bfc4e8 ["CALL", null, ["ram:c57e90:8"]]
- 00b7faa0 bytes 686e0194
+ 00bfc4e8 bytes 6a6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f31f856a6d388c2272b935d5be4691"></a>

### [`00b7fb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md) → [`00bfc598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md) FUN_00bfc598

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb48.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc590.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.38% / 新版 95.38%

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
      "site": "00bfc5c4",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fb7c",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc5ec",
      "incomplete_value": true,
      "site": "00bfc5f0",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fba4",
      "incomplete_value": true,
      "site": "00b7fba8",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc620",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fbd8",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc5c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc5ec",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc5ec",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc5c4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc5ec",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc5ec",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fb7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fb7c) · [`00b7fba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fba8) · [`00b7fbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fb50.md#insn-00b7fbd8)
- 新版 [`00bfc5c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc5c4) · [`00bfc5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc5f0) · [`00bfc620`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc598.md#insn-00bfc620)

~~~diff
- 00b7fb7c ["INT_ADD", "register:40f0:8", ["const:b7fb7c:8", "const:4:8"]]
- 00b7fb7c ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc5c4 ["INT_ADD", "register:40f0:8", ["const:bfc5c4:8", "const:4:8"]]
+ 00bfc5c4 ["CALL", null, ["ram:c599d0:8"]]
- 00b7fb7c bytes 01750194
+ 00bfc5c4 bytes 03750194
- 00b7fba8 ["INT_ADD", "register:40f0:8", ["const:b7fba8:8", "const:4:8"]]
- 00b7fba8 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc5f0 ["INT_ADD", "register:40f0:8", ["const:bfc5f0:8", "const:4:8"]]
+ 00bfc5f0 ["CALL", null, ["callee:00c57e80:8"]]
- 00b7fba8 bytes 226e0194
+ 00bfc5f0 bytes 246e0194
- 00b7fbd8 ["INT_ADD", "register:40f0:8", ["const:b7fbd8:8", "const:4:8"]]
- 00b7fbd8 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc620 ["INT_ADD", "register:40f0:8", ["const:bfc620:8", "const:4:8"]]
+ 00bfc620 ["CALL", null, ["ram:c57e90:8"]]
- 00b7fbd8 bytes 1a6e0194
+ 00bfc620 bytes 1c6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-234f29fca72b1710198cd75454014e54"></a>

### [`00b7fccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md) → [`00bfc714`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md) FUN_00bfc714

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fcc4.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc70c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00bfc740",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fcf8",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc768",
      "incomplete_value": true,
      "site": "00bfc76c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fd20",
      "incomplete_value": true,
      "site": "00b7fd24",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc79c",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fd54",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc740",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc768",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc768",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc740",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc768",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc768",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fcf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fcf8) · [`00b7fd24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fd24) · [`00b7fd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fccc.md#insn-00b7fd54)
- 新版 [`00bfc740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc740) · [`00bfc76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc76c) · [`00bfc79c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc714.md#insn-00bfc79c)

~~~diff
- 00b7fcf8 ["INT_ADD", "register:40f0:8", ["const:b7fcf8:8", "const:4:8"]]
- 00b7fcf8 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc740 ["INT_ADD", "register:40f0:8", ["const:bfc740:8", "const:4:8"]]
+ 00bfc740 ["CALL", null, ["ram:c599d0:8"]]
- 00b7fcf8 bytes a2740194
+ 00bfc740 bytes a4740194
- 00b7fd24 ["INT_ADD", "register:40f0:8", ["const:b7fd24:8", "const:4:8"]]
- 00b7fd24 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc76c ["INT_ADD", "register:40f0:8", ["const:bfc76c:8", "const:4:8"]]
+ 00bfc76c ["CALL", null, ["callee:00c57e80:8"]]
- 00b7fd24 bytes c36d0194
+ 00bfc76c bytes c56d0194
- 00b7fd54 ["INT_ADD", "register:40f0:8", ["const:b7fd54:8", "const:4:8"]]
- 00b7fd54 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc79c ["INT_ADD", "register:40f0:8", ["const:bfc79c:8", "const:4:8"]]
+ 00bfc79c ["CALL", null, ["ram:c57e90:8"]]
- 00b7fd54 bytes bb6d0194
+ 00bfc79c bytes bd6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c3b54fe08f97549d32ec8b1202fd652"></a>

### [`00b7fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md) → [`00bfc84c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md) FUN_00bfc84c

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b7fdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fdfc.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc844.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00bfc878",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fe30",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc8a0",
      "incomplete_value": true,
      "site": "00bfc8a4",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7fe58",
      "incomplete_value": true,
      "site": "00b7fe5c",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfc8d4",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b7fe8c",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfc878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfc8a0",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc8a0",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc878",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc8a0",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc8a0",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7fe30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe30) · [`00b7fe5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe5c) · [`00b7fe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7fe04.md#insn-00b7fe8c)
- 新版 [`00bfc878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc878) · [`00bfc8a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc8a4) · [`00bfc8d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc84c.md#insn-00bfc8d4)

~~~diff
- 00b7fe30 ["INT_ADD", "register:40f0:8", ["const:b7fe30:8", "const:4:8"]]
- 00b7fe30 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfc878 ["INT_ADD", "register:40f0:8", ["const:bfc878:8", "const:4:8"]]
+ 00bfc878 ["CALL", null, ["ram:c599d0:8"]]
- 00b7fe30 bytes 54740194
+ 00bfc878 bytes 56740194
- 00b7fe5c ["INT_ADD", "register:40f0:8", ["const:b7fe5c:8", "const:4:8"]]
- 00b7fe5c ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc8a4 ["INT_ADD", "register:40f0:8", ["const:bfc8a4:8", "const:4:8"]]
+ 00bfc8a4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b7fe5c bytes 756d0194
+ 00bfc8a4 bytes 776d0194
- 00b7fe8c ["INT_ADD", "register:40f0:8", ["const:b7fe8c:8", "const:4:8"]]
- 00b7fe8c ["CALL", null, ["ram:bdb440:8"]]
+ 00bfc8d4 ["INT_ADD", "register:40f0:8", ["const:bfc8d4:8", "const:4:8"]]
+ 00bfc8d4 ["CALL", null, ["ram:c57e90:8"]]
- 00b7fe8c bytes 6d6d0194
+ 00bfc8d4 bytes 6f6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44a6097567886c961a201eeae1a31184"></a>

### [`00b7ff3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md) → [`00bfc984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md) FUN_00bfc984

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b7ff34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff34.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfc97c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc97c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ff68"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfc9d8",
      "incomplete_value": true,
      "site": "00bfc9dc",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b7ff90",
      "incomplete_value": true,
      "site": "00b7ff94",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b7ffc4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b7ff68",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b7ff90",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b7ff90",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfc9b0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfc9d8",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfc9d8",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b7ff68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ff68) · [`00b7ff94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ff94) · [`00b7ffc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7ff3c.md#insn-00b7ffc4)
- 新版 [`00bfc9dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfc984.md#insn-00bfc9dc)

~~~diff
- 00b7ff68 ["INT_ADD", "register:40f0:8", ["const:b7ff68:8", "const:4:8"]]
- 00b7ff68 ["CALL", null, ["ram:bdcf80:8"]]
- 00b7ff68 bytes 06740194
- 00b7ff94 ["INT_ADD", "register:40f0:8", ["const:b7ff94:8", "const:4:8"]]
- 00b7ff94 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfc9dc ["INT_ADD", "register:40f0:8", ["const:bfc9dc:8", "const:4:8"]]
+ 00bfc9dc ["CALL", null, ["callee:00c57e80:8"]]
- 00b7ff94 bytes 276d0194
+ 00bfc9dc bytes 296d0194
- 00b7ffc4 ["INT_ADD", "register:40f0:8", ["const:b7ffc4:8", "const:4:8"]]
- 00b7ffc4 ["CALL", null, ["ram:bdb440:8"]]
- 00b7ffc4 bytes 1f6d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618007e3da366b96730e7152a8c468de"></a>

### [`00b80074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md) → [`00bfcabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcabc.md) FUN_00bfcabc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b8006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8006c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfcab4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcab4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 39.58% / 新版 39.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8009c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfcae4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b800a8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b8009c",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b800a0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b800a4",
      "READ",
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
      "00bfcae4",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "00bfcae8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfcaec",
      "READ",
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

- 旧版 [`00b8009c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b8009c) · [`00b800a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b800a0) · [`00b800a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80074.md#insn-00b800a8)

~~~diff
- 00b8009c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b8009c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b8009c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b8009c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b8009c bytes bfc31fb8
- 00b800a0 ["INT_ADD", "register:40f0:8", ["const:b800a0:8", "const:4:8"]]
- 00b800a0 ["CALL", null, ["ram:bdcf80:8"]]
- 00b800a0 bytes b8730194
- 00b800a8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b800a8 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00b800a8 bytes a8030034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7a26254b2f953402823e71c3b8dde68"></a>

### [`00b801ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801ac.md) → [`00bfcbf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbf4.md) FUN_00bfcbf4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b801a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801a4.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfcbec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcbec.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801b4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b801b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b801b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b801b8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b801d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfcbfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfcc00",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bfcc1c",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b801b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801ac.md#insn-00b801b4) · [`00b801b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801ac.md#insn-00b801b8) · [`00b801d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b801ac.md#insn-00b801d4)

~~~diff
- 00b801b4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b801b4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b801b4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b801b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b801b4 bytes fd7b01a9
- 00b801b8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b801b8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b801b8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b801b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b801b8 bytes f44f02a9
- 00b801d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b801d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b801d4 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b801d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b801d4 bytes bfc31fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e786686703e20a7cbed8224750eb45a1"></a>

### [`00b802e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md) → [`00bfcd2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd2c.md) FUN_00bfcd2c

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b802dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802dc.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfcd24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcd24.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.58% / 新版 64.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b802ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b802ec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b802f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b802ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b802f0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8030c",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfcd34",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfcd38",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bfcd54",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b802ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b802ec) · [`00b802f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b802f0) · [`00b8030c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b802e4.md#insn-00b8030c)

~~~diff
- 00b802ec ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b802ec ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b802ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b802ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b802ec bytes fd7b01a9
- 00b802f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b802f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b802f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b802f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b802f0 bytes f44f02a9
- 00b8030c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b8030c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b8030c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b8030c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b8030c bytes bfc31fb8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f4d7d5003599e69ea1451c1b9aca968"></a>

### [`00b80414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80414.md) → [`00bfce5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce5c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsERd

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b8041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bfce64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b80418",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bfce64"
      ]
    ]
  ],
  "added": [
    [
      "00bfce60",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bfce64"
      ]
    ]
  ]
}
~~~


<a id="compare-de80bb5f786c4d3cd8da610bb3f5cf7b"></a>

### [`00b8041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md) → [`00bfce64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce64.md) FUN_00bfce64

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80414.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfce5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfce5c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 56.25% / 新版 56.25%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80444"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfce8c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b80450"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b80444",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b80448",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b8044c",
      "READ",
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
      "00bfce8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x24]",
        null,
        null
      ]
    ],
    [
      "00bfce90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfce94",
      "READ",
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

- 旧版 [`00b80444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80444) · [`00b80448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80448) · [`00b80450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8041c.md#insn-00b80450)

~~~diff
- 00b80444 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b80444 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b80444 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:fffffffffffffffc:8"]]
- 00b80444 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:4"]]
- 00b80444 bytes bfc31fb8
- 00b80448 ["INT_ADD", "register:40f0:8", ["const:b80448:8", "const:4:8"]]
- 00b80448 ["CALL", null, ["ram:bdcf80:8"]]
- 00b80448 bytes ce720194
- 00b80450 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00b80450 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
- 00b80450 bytes a8030034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d56fc8fa9579be0daccf9777ff74b9e"></a>

### [`00b80554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md) → [`00bfcf9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md) FUN_00bfcf9c

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b8054c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8054c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfcf94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf94.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

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
      "site": "00bfcfc8",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80580",
      "value": [
        "leaf",
        "ram:bdcf80:8"
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfcff0",
      "incomplete_value": true,
      "site": "00bfcff4",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b805a8",
      "incomplete_value": true,
      "site": "00b805ac",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfd024",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b805dc",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00bfcfc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "00bfcff0",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcff0",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfcfc8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfcff0",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfcff0",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b80580) · [`00b805ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b805ac) · [`00b805dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80554.md#insn-00b805dc)
- 新版 [`00bfcfc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfcfc8) · [`00bfcff4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfcff4) · [`00bfd024`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfc/00bfcf9c.md#insn-00bfd024)

~~~diff
- 00b80580 ["INT_ADD", "register:40f0:8", ["const:b80580:8", "const:4:8"]]
- 00b80580 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfcfc8 ["INT_ADD", "register:40f0:8", ["const:bfcfc8:8", "const:4:8"]]
+ 00bfcfc8 ["CALL", null, ["ram:c599d0:8"]]
- 00b80580 bytes 80720194
+ 00bfcfc8 bytes 82720194
- 00b805ac ["INT_ADD", "register:40f0:8", ["const:b805ac:8", "const:4:8"]]
- 00b805ac ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfcff4 ["INT_ADD", "register:40f0:8", ["const:bfcff4:8", "const:4:8"]]
+ 00bfcff4 ["CALL", null, ["callee:00c57e80:8"]]
- 00b805ac bytes a16b0194
+ 00bfcff4 bytes a36b0194
- 00b805dc ["INT_ADD", "register:40f0:8", ["const:b805dc:8", "const:4:8"]]
- 00b805dc ["CALL", null, ["ram:bdb440:8"]]
+ 00bfd024 ["INT_ADD", "register:40f0:8", ["const:bfd024:8", "const:4:8"]]
+ 00bfd024 ["CALL", null, ["ram:c57e90:8"]]
- 00b805dc bytes 996b0194
+ 00bfd024 bytes 9b6b0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-544153d1af01f357bdfc60bfe88bbf49"></a>

### [`00b8068c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md) → [`00bfd0d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md) FUN_00bfd0d4

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b80684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80684.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00bfd0cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0cc.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 79.17% / 新版 79.17%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b806b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd128",
      "incomplete_value": true,
      "site": "00bfd12c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b806e0",
      "incomplete_value": true,
      "site": "00b806e4",
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8070c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b806b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b806e0",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b806e0",
      "PARAM",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00bfd100",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfd128",
      "READ",
      [
        "storage",
        "00c9b710",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd128",
      "PARAM",
      [
        "storage",
        "01127778",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b806b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b806b8) · [`00b806e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b806e4) · [`00b8070c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b8068c.md#insn-00b8070c)
- 新版 [`00bfd12c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd0d4.md#insn-00bfd12c)

~~~diff
- 00b806b8 ["INT_ADD", "register:40f0:8", ["const:b806b8:8", "const:4:8"]]
- 00b806b8 ["CALL", null, ["ram:bdcf80:8"]]
- 00b806b8 bytes 32720194
- 00b806e4 ["INT_ADD", "register:40f0:8", ["const:b806e4:8", "const:4:8"]]
- 00b806e4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfd12c ["INT_ADD", "register:40f0:8", ["const:bfd12c:8", "const:4:8"]]
+ 00bfd12c ["CALL", null, ["callee:00c57e80:8"]]
- 00b806e4 bytes 536b0194
+ 00bfd12c bytes 556b0194
- 00b8070c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8070c ["INT_ADD", "register:40f0:8", ["const:b8070c:8", "const:4:8"]]
- 00b8070c ["CALLIND", null, ["register:0:8"]]
- 00b8070c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db50da059c2ea22c398175fd428e8611"></a>

### [`00b807bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md) → [`00bfd204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1360.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c5df60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df60.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.96% / 新版 97.96%

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
      "site": "00bfd22c",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b807e4",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfd22c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfd22c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b807e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b807e4) · [`00b8082c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b8082c) · [`00b8085c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b807bc.md#insn-00b8085c)
- 新版 [`00bfd22c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd22c) · [`00bfd274`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd274) · [`00bfd2a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd204.md#insn-00bfd2a4)

~~~diff
- 00b807e4 ["INT_ADD", "register:40f0:8", ["const:b807e4:8", "const:4:8"]]
- 00b807e4 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfd22c ["INT_ADD", "register:40f0:8", ["const:bfd22c:8", "const:4:8"]]
+ 00bfd22c ["CALL", null, ["ram:c599d0:8"]]
- 00b807e4 bytes e7710194
+ 00bfd22c bytes e9710194
- 00b8082c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8082c ["INT_ADD", "register:40f0:8", ["const:b8082c:8", "const:4:8"]]
- 00b8082c ["CALLIND", null, ["register:0:8"]]
+ 00bfd274 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd274 ["INT_ADD", "register:40f0:8", ["const:bfd274:8", "const:4:8"]]
+ 00bfd274 ["CALLIND", null, ["register:0:8"]]
- 00b8082c bytes 00013fd6
+ 00bfd274 bytes 00013fd6
- 00b8085c ["INT_ADD", "register:40f0:8", ["const:b8085c:8", "const:4:8"]]
- 00b8085c ["CALL", null, ["callee:00c57ea0:8"]]
+ 00bfd2a4 ["INT_ADD", "register:40f0:8", ["const:bfd2a4:8", "const:4:8"]]
+ 00bfd2a4 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b8085c bytes fd6a0194
+ 00bfd2a4 bytes ff6a0194
~~~


<a id="compare-b63a57854bbdbf9d1674aa5e70a35fcd"></a>

### [`00b80910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md) → [`00bfd358`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPcl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1370.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df70.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd398",
      "incomplete_value": true,
      "site": "00bfd39c",
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
      "definition_site": "00b80950",
      "incomplete_value": true,
      "site": "00b80954",
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
      "site": "00bfd3b8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80970",
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
      "00bfd398",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd398",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd3b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfd398",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd398",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd3b8",
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

- 旧版 [`00b80954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80954) · [`00b80970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80970) · [`00b80944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80910.md#insn-00b80944)
- 新版 [`00bfd39c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd39c) · [`00bfd3b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd3b8) · [`00bfd38c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd358.md#insn-00bfd38c)

~~~diff
- 00b80954 ["INT_ADD", "register:40f0:8", ["const:b80954:8", "const:4:8"]]
- 00b80954 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfd39c ["INT_ADD", "register:40f0:8", ["const:bfd39c:8", "const:4:8"]]
+ 00bfd39c ["CALL", null, ["callee:00c57e80:8"]]
- 00b80954 bytes b76a0194
+ 00bfd39c bytes b96a0194
- 00b80970 ["INT_ADD", "register:40f0:8", ["const:b80970:8", "const:4:8"]]
- 00b80970 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfd3b8 ["INT_ADD", "register:40f0:8", ["const:bfd3b8:8", "const:4:8"]]
+ 00bfd3b8 ["CALL", null, ["ram:c57e90:8"]]
- 00b80970 bytes b46a0194
+ 00bfd3b8 bytes b66a0194
- 00b80944 ["INT_ADD", "register:40f0:8", ["const:b80944:8", "const:4:8"]]
- 00b80944 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bfd38c ["INT_ADD", "register:40f0:8", ["const:bfd38c:8", "const:4:8"]]
+ 00bfd38c ["CALL", null, ["callee:00c57e70:8"]]
- 00b80944 bytes b76a0194
+ 00bfd38c bytes b96a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa634ddd950b1823e603b7b4edf0e6b5"></a>

### [`00b809b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md) → [`00bfd3fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1370.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c5df70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df70.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.95% / 新版 98.95%

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
      "site": "00bfd438",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b809f0",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfd438",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfd438",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b809f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b809f0) · [`00b80a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b80a6c) · [`00b80aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md#insn-00b80aac)
- 新版 [`00bfd438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd438) · [`00bfd4b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd4b4) · [`00bfd4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd3fc.md#insn-00bfd4f4)

~~~diff
- 00b809f0 ["INT_ADD", "register:40f0:8", ["const:b809f0:8", "const:4:8"]]
- 00b809f0 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfd438 ["INT_ADD", "register:40f0:8", ["const:bfd438:8", "const:4:8"]]
+ 00bfd438 ["CALL", null, ["ram:c599d0:8"]]
- 00b809f0 bytes 64710194
+ 00bfd438 bytes 66710194
- 00b80a6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80a6c ["INT_ADD", "register:40f0:8", ["const:b80a6c:8", "const:4:8"]]
- 00b80a6c ["CALLIND", null, ["register:0:8"]]
+ 00bfd4b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd4b4 ["INT_ADD", "register:40f0:8", ["const:bfd4b4:8", "const:4:8"]]
+ 00bfd4b4 ["CALLIND", null, ["register:0:8"]]
- 00b80a6c bytes 00013fd6
+ 00bfd4b4 bytes 00013fd6
- 00b80aac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80aac ["INT_ADD", "register:40f0:8", ["const:b80aac:8", "const:4:8"]]
- 00b80aac ["CALLIND", null, ["register:0:8"]]
+ 00bfd4f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd4f4 ["INT_ADD", "register:40f0:8", ["const:bfd4f4:8", "const:4:8"]]
+ 00bfd4f4 ["CALLIND", null, ["register:0:8"]]
- 00b80aac bytes 00013fd6
+ 00bfd4f4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fea5a207d3a9efc040298d174e5954d"></a>

### [`00b80b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md) → [`00bfd5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1380.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df80.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd608",
      "incomplete_value": true,
      "site": "00bfd60c",
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
      "definition_site": "00b80bc0",
      "incomplete_value": true,
      "site": "00b80bc4",
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
      "site": "00bfd628",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80be0",
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
      "00bfd608",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd608",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd628",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfd608",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd608",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd628",
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

- 旧版 [`00b80bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80bc4) · [`00b80be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80be0) · [`00b80bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80b88.md#insn-00b80bb4)
- 新版 [`00bfd60c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd60c) · [`00bfd628`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd628) · [`00bfd5fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd5d0.md#insn-00bfd5fc)

~~~diff
- 00b80bc4 ["INT_ADD", "register:40f0:8", ["const:b80bc4:8", "const:4:8"]]
- 00b80bc4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfd60c ["INT_ADD", "register:40f0:8", ["const:bfd60c:8", "const:4:8"]]
+ 00bfd60c ["CALL", null, ["callee:00c57e80:8"]]
- 00b80bc4 bytes 1b6a0194
+ 00bfd60c bytes 1d6a0194
- 00b80be0 ["INT_ADD", "register:40f0:8", ["const:b80be0:8", "const:4:8"]]
- 00b80be0 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfd628 ["INT_ADD", "register:40f0:8", ["const:bfd628:8", "const:4:8"]]
+ 00bfd628 ["CALL", null, ["ram:c57e90:8"]]
- 00b80be0 bytes 186a0194
+ 00bfd628 bytes 1a6a0194
- 00b80bb4 ["INT_ADD", "register:40f0:8", ["const:b80bb4:8", "const:4:8"]]
- 00b80bb4 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bfd5fc ["INT_ADD", "register:40f0:8", ["const:bfd5fc:8", "const:4:8"]]
+ 00bfd5fc ["CALL", null, ["callee:00c57e70:8"]]
- 00b80bb4 bytes 1b6a0194
+ 00bfd5fc bytes 1d6a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b64869750cf1443d483e2678c4c6979"></a>

### [`00b80c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md) → [`00bfd664`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1380.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c5df80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df80.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

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
      "site": "00bfd698",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80c50",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfd698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfd698",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80c50) · [`00b80cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80cb4) · [`00b80cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80c1c.md#insn-00b80cf8)
- 新版 [`00bfd698`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd698) · [`00bfd6fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd6fc) · [`00bfd740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md#insn-00bfd740)

~~~diff
- 00b80c50 ["INT_ADD", "register:40f0:8", ["const:b80c50:8", "const:4:8"]]
- 00b80c50 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfd698 ["INT_ADD", "register:40f0:8", ["const:bfd698:8", "const:4:8"]]
+ 00bfd698 ["CALL", null, ["ram:c599d0:8"]]
- 00b80c50 bytes cc700194
+ 00bfd698 bytes ce700194
- 00b80cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80cb4 ["INT_ADD", "register:40f0:8", ["const:b80cb4:8", "const:4:8"]]
- 00b80cb4 ["CALLIND", null, ["register:0:8"]]
+ 00bfd6fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd6fc ["INT_ADD", "register:40f0:8", ["const:bfd6fc:8", "const:4:8"]]
+ 00bfd6fc ["CALLIND", null, ["register:0:8"]]
- 00b80cb4 bytes 00013fd6
+ 00bfd6fc bytes 00013fd6
- 00b80cf8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80cf8 ["INT_ADD", "register:40f0:8", ["const:b80cf8:8", "const:4:8"]]
- 00b80cf8 ["CALLIND", null, ["register:0:8"]]
+ 00bfd740 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd740 ["INT_ADD", "register:40f0:8", ["const:bfd740:8", "const:4:8"]]
+ 00bfd740 ["CALLIND", null, ["register:0:8"]]
- 00b80cf8 bytes 00013fd6
+ 00bfd740 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3259baadeba879f1fb4d4090ea668375"></a>

### [`00b80d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md) → [`00bfd7d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPcl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be1390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1390.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5df90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df90.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfd814",
      "incomplete_value": true,
      "site": "00bfd818",
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
      "definition_site": "00b80dcc",
      "incomplete_value": true,
      "site": "00b80dd0",
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
      "site": "00bfd834",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80dec",
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
      "00bfd814",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd814",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd834",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfd814",
      "READ",
      [
        "storage",
        "00c9a830",
        null,
        "pointer"
      ]
    ],
    [
      "00bfd814",
      "PARAM",
      [
        "storage",
        "01127a18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfd834",
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

- 旧版 [`00b80dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dd0) · [`00b80dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dec) · [`00b80dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80d8c.md#insn-00b80dc0)
- 新版 [`00bfd818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd818) · [`00bfd834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd834) · [`00bfd808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd7d4.md#insn-00bfd808)

~~~diff
- 00b80dd0 ["INT_ADD", "register:40f0:8", ["const:b80dd0:8", "const:4:8"]]
- 00b80dd0 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfd818 ["INT_ADD", "register:40f0:8", ["const:bfd818:8", "const:4:8"]]
+ 00bfd818 ["CALL", null, ["callee:00c57e80:8"]]
- 00b80dd0 bytes 98690194
+ 00bfd818 bytes 9a690194
- 00b80dec ["INT_ADD", "register:40f0:8", ["const:b80dec:8", "const:4:8"]]
- 00b80dec ["CALL", null, ["ram:bdb440:8"]]
+ 00bfd834 ["INT_ADD", "register:40f0:8", ["const:bfd834:8", "const:4:8"]]
+ 00bfd834 ["CALL", null, ["ram:c57e90:8"]]
- 00b80dec bytes 95690194
+ 00bfd834 bytes 97690194
- 00b80dc0 ["INT_ADD", "register:40f0:8", ["const:b80dc0:8", "const:4:8"]]
- 00b80dc0 ["CALL", null, ["callee:00c57e70:8"]]
+ 00bfd808 ["INT_ADD", "register:40f0:8", ["const:bfd808:8", "const:4:8"]]
+ 00bfd808 ["CALL", null, ["callee:00c57e70:8"]]
- 00b80dc0 bytes 98690194
+ 00bfd808 bytes 9a690194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54da453514d67c73939f37007c502aa1"></a>

### [`00b80e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md) → [`00bfd878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1390.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c5df90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df90.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.15% / 新版 99.15%

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
      "site": "00bfd8b8",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b80e70",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfd8b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfd8b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b80e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80e70) · [`00b80eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80eb4) · [`00b80f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b80e30.md#insn-00b80f0c)
- 新版 [`00bfd8b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd8b8) · [`00bfd8fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd8fc) · [`00bfd954`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md#insn-00bfd954)

~~~diff
- 00b80e70 ["INT_ADD", "register:40f0:8", ["const:b80e70:8", "const:4:8"]]
- 00b80e70 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfd8b8 ["INT_ADD", "register:40f0:8", ["const:bfd8b8:8", "const:4:8"]]
+ 00bfd8b8 ["CALL", null, ["ram:c599d0:8"]]
- 00b80e70 bytes 44700194
+ 00bfd8b8 bytes 46700194
- 00b80eb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80eb4 ["INT_ADD", "register:40f0:8", ["const:b80eb4:8", "const:4:8"]]
- 00b80eb4 ["CALLIND", null, ["register:0:8"]]
+ 00bfd8fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd8fc ["INT_ADD", "register:40f0:8", ["const:bfd8fc:8", "const:4:8"]]
+ 00bfd8fc ["CALLIND", null, ["register:0:8"]]
- 00b80eb4 bytes 00013fd6
+ 00bfd8fc bytes 00013fd6
- 00b80f0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b80f0c ["INT_ADD", "register:40f0:8", ["const:b80f0c:8", "const:4:8"]]
- 00b80f0c ["CALLIND", null, ["register:0:8"]]
+ 00bfd954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfd954 ["INT_ADD", "register:40f0:8", ["const:bfd954:8", "const:4:8"]]
+ 00bfd954 ["CALLIND", null, ["register:0:8"]]
- 00b80f0c bytes 00013fd6
+ 00bfd954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a635135956b8086890484c8450baab8b"></a>

### [`00b81074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md) → [`00bfdabc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.89% / 新版 98.89%

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
      "site": "00bfdaf0",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b810a8",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfdaf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfdaf0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b810a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b810a8) · [`00b81100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b81100) · [`00b8117c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81074.md#insn-00b8117c)
- 新版 [`00bfdaf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdaf0) · [`00bfdb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdb48) · [`00bfdbc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md#insn-00bfdbc4)

~~~diff
- 00b810a8 ["INT_ADD", "register:40f0:8", ["const:b810a8:8", "const:4:8"]]
- 00b810a8 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfdaf0 ["INT_ADD", "register:40f0:8", ["const:bfdaf0:8", "const:4:8"]]
+ 00bfdaf0 ["CALL", null, ["ram:c599d0:8"]]
- 00b810a8 bytes b66f0194
+ 00bfdaf0 bytes b86f0194
- 00b81100 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81100 ["INT_ADD", "register:40f0:8", ["const:b81100:8", "const:4:8"]]
- 00b81100 ["CALLIND", null, ["register:0:8"]]
+ 00bfdb48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdb48 ["INT_ADD", "register:40f0:8", ["const:bfdb48:8", "const:4:8"]]
+ 00bfdb48 ["CALLIND", null, ["register:0:8"]]
- 00b81100 bytes 00013fd6
+ 00bfdb48 bytes 00013fd6
- 00b8117c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8117c ["INT_ADD", "register:40f0:8", ["const:b8117c:8", "const:4:8"]]
- 00b8117c ["CALLIND", null, ["register:0:8"]]
+ 00bfdbc4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bfdbc4 ["INT_ADD", "register:40f0:8", ["const:bfdbc4:8", "const:4:8"]]
+ 00bfdbc4 ["CALLIND", null, ["register:0:8"]]
- 00b8117c bytes 00013fd6
+ 00bfdbc4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc38ff9e79f4c4375745be4da5e66bd1"></a>

### [`00b81330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md) → [`00bfdd78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4readEPcl

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc280.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c58cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58cd0.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81360"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8138c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfddf8",
      "incomplete_value": true,
      "site": "00bfde04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
    "old": null,
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
      "unmatched:00b81360",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b8138c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfdda8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfddd4",
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

- 旧版 [`00b81360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b81360) · [`00b8138c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b8138c) · [`00b813bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81330.md#insn-00b813bc)
- 新版 [`00bfde04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdd78.md#insn-00bfde04)

~~~diff
- 00b81360 ["INT_ADD", "register:40f0:8", ["const:b81360:8", "const:4:8"]]
- 00b81360 ["CALL", null, ["ram:bdcf80:8"]]
- 00b81360 bytes 086f0194
- 00b8138c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b8138c ["INT_ADD", "register:40f0:8", ["const:b8138c:8", "const:4:8"]]
- 00b8138c ["CALLIND", null, ["register:0:8"]]
- 00b8138c bytes 00013fd6
- 00b813bc ["INT_ADD", "register:40f0:8", ["const:b813bc:8", "const:4:8"]]
- 00b813bc ["CALL", null, ["callee:00c57ea0:8"]]
+ 00bfde04 ["INT_ADD", "register:40f0:8", ["const:bfde04:8", "const:4:8"]]
+ 00bfde04 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b813bc bytes 25680194
+ 00bfde04 bytes 27680194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dcb2d71e0cb5b5272999435266360c9"></a>

### [`00b81578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md) → [`00bfdfc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7putbackEc

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 23.53% / 新版 30.77%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8159c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bfdfe4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfdff4",
      "incomplete_value": true,
      "site": "00bfe000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "definition_site": "00b815ac",
      "incomplete_value": true,
      "site": "00b815b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
      "unmatched:00b815c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b8161c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfe010",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfe064",
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

- 旧版 [`00b8159c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b8159c) · [`00b815b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b815b8) · [`00b815c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81578.md#insn-00b815c8)
- 新版 [`00bfe000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdfc0.md#insn-00bfe000)

~~~diff
- 00b8159c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b8159c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b8159c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b8159c bytes 1f0400f9
- 00b815b8 ["INT_ADD", "register:40f0:8", ["const:b815b8:8", "const:4:8"]]
- 00b815b8 ["CALL", null, ["callee:00c57ea0:8"]]
+ 00bfe000 ["INT_ADD", "register:40f0:8", ["const:bfe000:8", "const:4:8"]]
+ 00bfe000 ["CALL", null, ["callee:00c57ea0:8"]]
- 00b815b8 bytes a6670194
+ 00bfe000 bytes a8670194
- 00b815c8 ["INT_ADD", "register:40f0:8", ["const:b815c8:8", "const:4:8"]]
- 00b815c8 ["CALL", null, ["ram:bdcf80:8"]]
- 00b815c8 bytes 6e6e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef215405bdc6ab48ff6b7885968857a0"></a>

### [`00b816ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md) → [`00bfe0f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5ungetEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 66.67% / 新版 72.73%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81714"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bfe15c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfe140",
      "value": [
        "leaf",
        "ram:c599d0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b816f8",
      "value": [
        "leaf",
        "ram:bdcf80:8"
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
      "00bfe140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b81714",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bfe198"
      ]
    ]
  ],
  "added": [
    [
      "00bfe140",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfe15c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bfe198"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b816f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md#insn-00b816f8) · [`00b81714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b816ac.md#insn-00b81714)
- 新版 [`00bfe140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md#insn-00bfe140) · [`00bfe15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe0f4.md#insn-00bfe15c)

~~~diff
- 00b816f8 ["INT_ADD", "register:40f0:8", ["const:b816f8:8", "const:4:8"]]
- 00b816f8 ["CALL", null, ["ram:bdcf80:8"]]
+ 00bfe140 ["INT_ADD", "register:40f0:8", ["const:bfe140:8", "const:4:8"]]
+ 00bfe140 ["CALL", null, ["ram:c599d0:8"]]
- 00b816f8 bytes 226e0194
+ 00bfe140 bytes 246e0194
- 00b81714 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00b81714 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00b81714 bytes e00100b4
+ 00bfe15c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00bfe15c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00bfe15c bytes e00100b4
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c015761ecb373c0df3839b72dd24c79"></a>

### [`00b817d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md) → [`00bfe21c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe21c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE4syncEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 61.54% / 新版 61.54%

CFGの説明率　旧版 9.09% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b817e0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b817dc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b817e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b817f8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ]
  ],
  "added": [
    [
      "00bfe224",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00bfe228",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00bfe240",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b817dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b817dc) · [`00b817e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b817e0) · [`00b817f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b817d4.md#insn-00b817f8)

~~~diff
- 00b817dc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b817dc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b817dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b817dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b817dc bytes fd7b01a9
- 00b817e0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b817e0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b817e0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b817e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b817e0 bytes f44f02a9
- 00b817f8 ["INT_ADD", "register:40f0:8", ["const:b817f8:8", "const:4:8"]]
- 00b817f8 ["CALL", null, ["ram:bdcf80:8"]]
- 00b817f8 bytes e26d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f03ff545c66d50f00fda7c821e715d0c"></a>

### [`00b818c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md) → [`00bfe30c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe30c.md) _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE5seekgENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdc9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9b0.md) · 呼出先 2件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdcf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf80.md)
- 新版 呼出元 1件 [`00c59400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59400.md) · 呼出先 2件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c599d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c599d0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8194c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00bfe394"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81910"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81910",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdcf80"
      ]
    ],
    [
      "unmatched:00b81940",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00bfe358",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c599d0"
      ]
    ],
    [
      "00bfe388",
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

- 旧版 [`00b81910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b81910) · [`00b81940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b81940) · [`00b8194c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b818c4.md#insn-00b8194c)

~~~diff
- 00b81910 ["INT_ADD", "register:40f0:8", ["const:b81910:8", "const:4:8"]]
- 00b81910 ["CALL", null, ["ram:bdcf80:8"]]
- 00b81910 bytes 9c6d0194
- 00b81940 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b81940 ["INT_ADD", "register:40f0:8", ["const:b81940:8", "const:4:8"]]
- 00b81940 ["CALLIND", null, ["register:0:8"]]
- 00b81940 bytes 00013fd6
- 00b8194c ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b8194c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00b8194c ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00b8194c ["INT_ZEXT", "register:40a0:8", ["tmp:0:4"]]
- 00b8194c bytes 1401941a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f665cd4d4c5a77936dca1c6b1828139"></a>

### [`00b81a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md) → [`00bfe474`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe474.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b81a5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b81a48",
      "READ",
      [
        "storage",
        "00c1bce8",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b81a58",
      "DATA",
      [
        "storage",
        "00c130f0",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b81a5c",
      "DATA",
      [
        "storage",
        "00c130c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bfe490",
      "READ",
      [
        "storage",
        "00c9b718",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe4a0",
      "DATA",
      [
        "storage",
        "00c92a98",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe4a4",
      "DATA",
      [
        "storage",
        "00c92a70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b81a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md#insn-00b81a4c) · [`00b81a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md#insn-00b81a58) · [`00b81a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81a2c.md#insn-00b81a5c)

~~~diff
- 00b81a4c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:38:8"]]
- 00b81a4c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b81a4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b81a4c bytes 1f1c00f9
- 00b81a58 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b81a58 ["INT_ADD", "register:40a0:8", ["register:40a0:8", "const:8:8"]]
- 00b81a58 ["STORE", null, ["const:1b1:8", "register:40a0:8", "tmp:0:8"]]
- 00b81a58 bytes 898e00f8
- 00b81a5c ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00b81a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b81a5c bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcde6e7fba4110460f1ad3de871531de"></a>

### [`00b81aa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md) → [`00bfe4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe4e8.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfe510",
      "incomplete_value": true,
      "site": "00bfe518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4000:8"
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
    "old": null,
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfe514",
      "incomplete_value": true,
      "site": "00bfe518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
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
    "old": null,
    "ordinal": 0,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b81ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md#insn-00b81ad0) · [`00b81ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md#insn-00b81ac0) · [`00b81ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81aa0.md#insn-00b81ac4)
- 新版 [`00bfe518`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe4e8.md#insn-00bfe518)

~~~diff
- 00b81ad0 ["INT_ADD", "register:40f0:8", ["const:b81ad0:8", "const:4:8"]]
- 00b81ad0 ["CALL", null, ["callee:00c5df20:8"]]
+ 00bfe518 ["INT_ADD", "register:40f0:8", ["const:bfe518:8", "const:4:8"]]
+ 00bfe518 ["CALL", null, ["callee:00c5df20:8"]]
- 00b81ad0 bytes 147e0194
+ 00bfe518 bytes 827e0194
- 00b81ac0 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b81ac0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b81ac0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b81ac0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b81ac0 bytes 1300088b
- 00b81ac4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00b81ac4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b81ac4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b81ac4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b81ac4 bytes 3400098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82694fe4b8c086e12a1ff9587d108e82"></a>

### [`00b81c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md) → [`00bfe6d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfe728",
      "incomplete_value": true,
      "site": "00bfe72c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81ce0",
      "incomplete_value": true,
      "site": "00b81ce4",
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfe738",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b81cf0",
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
      "definition_site": "00bfe770",
      "incomplete_value": true,
      "site": "00bfe774",
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
      "definition_site": "00b81d28",
      "incomplete_value": true,
      "site": "00b81d2c",
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
      "00bfe728",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe728",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfe738",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfe728",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe728",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfe738",
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

- 旧版 [`00b81ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81ce4) · [`00b81cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81cf0) · [`00b81d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81c8c.md#insn-00b81d2c)
- 新版 [`00bfe72c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe72c) · [`00bfe738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe738) · [`00bfe774`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe6d4.md#insn-00bfe774)

~~~diff
- 00b81ce4 ["INT_ADD", "register:40f0:8", ["const:b81ce4:8", "const:4:8"]]
- 00b81ce4 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfe72c ["INT_ADD", "register:40f0:8", ["const:bfe72c:8", "const:4:8"]]
+ 00bfe72c ["CALL", null, ["callee:00c57e80:8"]]
- 00b81ce4 bytes d3650194
+ 00bfe72c bytes d5650194
- 00b81cf0 ["INT_ADD", "register:40f0:8", ["const:b81cf0:8", "const:4:8"]]
- 00b81cf0 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfe738 ["INT_ADD", "register:40f0:8", ["const:bfe738:8", "const:4:8"]]
+ 00bfe738 ["CALL", null, ["ram:c57e90:8"]]
- 00b81cf0 bytes d4650194
+ 00bfe738 bytes d6650194
- 00b81d2c ["INT_ADD", "register:40f0:8", ["const:b81d2c:8", "const:4:8"]]
- 00b81d2c ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfe774 ["INT_ADD", "register:40f0:8", ["const:bfe774:8", "const:4:8"]]
+ 00bfe774 ["CALL", null, ["callee:00c57e80:8"]]
- 00b81d2c bytes c1650194
+ 00bfe774 bytes c3650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ea7595dc8ca87ad19d596d4252e2cc"></a>

### [`00b81e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md) → [`00bfe864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 2件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfe8b8",
      "incomplete_value": true,
      "site": "00bfe8bc",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b81e70",
      "incomplete_value": true,
      "site": "00b81e74",
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfe8c8",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b81e80",
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
      "definition_site": "00bfe900",
      "incomplete_value": true,
      "site": "00bfe904",
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
      "definition_site": "00b81eb8",
      "incomplete_value": true,
      "site": "00b81ebc",
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
      "00bfe8b8",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8b8",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfe8c8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfe8b8",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfe8b8",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfe8c8",
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

- 旧版 [`00b81e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81e74) · [`00b81e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81e80) · [`00b81ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81e1c.md#insn-00b81ebc)
- 新版 [`00bfe8bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe8bc) · [`00bfe8c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe8c8) · [`00bfe904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md#insn-00bfe904)

~~~diff
- 00b81e74 ["INT_ADD", "register:40f0:8", ["const:b81e74:8", "const:4:8"]]
- 00b81e74 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfe8bc ["INT_ADD", "register:40f0:8", ["const:bfe8bc:8", "const:4:8"]]
+ 00bfe8bc ["CALL", null, ["callee:00c57e80:8"]]
- 00b81e74 bytes 6f650194
+ 00bfe8bc bytes 71650194
- 00b81e80 ["INT_ADD", "register:40f0:8", ["const:b81e80:8", "const:4:8"]]
- 00b81e80 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfe8c8 ["INT_ADD", "register:40f0:8", ["const:bfe8c8:8", "const:4:8"]]
+ 00bfe8c8 ["CALL", null, ["ram:c57e90:8"]]
- 00b81e80 bytes 70650194
+ 00bfe8c8 bytes 72650194
- 00b81ebc ["INT_ADD", "register:40f0:8", ["const:b81ebc:8", "const:4:8"]]
- 00b81ebc ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfe904 ["INT_ADD", "register:40f0:8", ["const:bfe904:8", "const:4:8"]]
+ 00bfe904 ["CALL", null, ["callee:00c57e80:8"]]
- 00b81ebc bytes 5d650194
+ 00bfe904 bytes 5f650194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df1a50a90dd7498f03531c1431192b95"></a>

### [`00b81fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md) → [`00bfe9f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 call, call_argument_candidate, call_count, cfg_edge_inventory, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 11.11% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82004"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82010"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfea90",
      "incomplete_value": true,
      "site": "00bfea94",
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
      "definition_site": "00b82048",
      "incomplete_value": true,
      "site": "00b8204c",
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
      "unmatched:00b82000",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b82000",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b82004",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00bfea48",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfea48",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfea4c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b82004) · [`00b82010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b82010) · [`00b8204c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b81/00b81fac.md#insn-00b8204c)
- 新版 [`00bfea94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md#insn-00bfea94)

~~~diff
- 00b82004 ["INT_ADD", "register:40f0:8", ["const:b82004:8", "const:4:8"]]
- 00b82004 ["CALL", null, ["callee:00c57e80:8"]]
- 00b82004 bytes 0b650194
- 00b82010 ["INT_ADD", "register:40f0:8", ["const:b82010:8", "const:4:8"]]
- 00b82010 ["CALL", null, ["ram:bdb440:8"]]
- 00b82010 bytes 0c650194
- 00b8204c ["INT_ADD", "register:40f0:8", ["const:b8204c:8", "const:4:8"]]
- 00b8204c ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfea94 ["INT_ADD", "register:40f0:8", ["const:bfea94:8", "const:4:8"]]
+ 00bfea94 ["CALL", null, ["callee:00c57e80:8"]]
- 00b8204c bytes f9640194
+ 00bfea94 bytes fb640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7ef35b78818991fdb24ab9c5ca79a67"></a>

### [`00b8213c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md) → [`00bfeb84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.32% / 新版 75.32%

CFGの説明率　旧版 27.27% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82144"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82148"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82148"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82144",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b82148",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b8214c",
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
      "00bfeb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00bfeb90",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00bfeb94",
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

- 旧版 [`00b82144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b82144) · [`00b82148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b82148) · [`00b8214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8213c.md#insn-00b8214c)

~~~diff
- 00b82144 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:20:8"]]
- 00b82144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:8"]]
- 00b82144 bytes e81300fd
- 00b82148 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b82148 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b82148 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:28:8"]]
- 00b82148 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b82148 bytes fdfb02a9
- 00b8214c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00b8214c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00b8214c bytes f71f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859a2bfdbed6bbffb809aa03a9475ca7"></a>

### [`00b822d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md) → [`00bfed1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 82.67% / 新版 82.67%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b8232c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82338"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfedb8",
      "incomplete_value": true,
      "site": "00bfedbc",
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
      "definition_site": "00b82370",
      "incomplete_value": true,
      "site": "00b82374",
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
      "unmatched:00b82328",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b82328",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "unmatched:00b8232c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ],
  "added": [
    [
      "00bfed70",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfed70",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfed74",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57e80"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8232c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b8232c) · [`00b82338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b82338) · [`00b82374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md#insn-00b82374)
- 新版 [`00bfedbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfed1c.md#insn-00bfedbc)

~~~diff
- 00b8232c ["INT_ADD", "register:40f0:8", ["const:b8232c:8", "const:4:8"]]
- 00b8232c ["CALL", null, ["callee:00c57e80:8"]]
- 00b8232c bytes 41640194
- 00b82338 ["INT_ADD", "register:40f0:8", ["const:b82338:8", "const:4:8"]]
- 00b82338 ["CALL", null, ["ram:bdb440:8"]]
- 00b82338 bytes 42640194
- 00b82374 ["INT_ADD", "register:40f0:8", ["const:b82374:8", "const:4:8"]]
- 00b82374 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfedbc ["INT_ADD", "register:40f0:8", ["const:bfedbc:8", "const:4:8"]]
+ 00bfedbc ["CALL", null, ["callee:00c57e80:8"]]
- 00b82374 bytes 2f640194
+ 00bfedbc bytes 31640194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fe2bcbde73165bcebf0d4ea51b9b668"></a>

### [`00b82464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md) → [`00bfeeac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEPKv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfef00",
      "incomplete_value": true,
      "site": "00bfef04",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b824b8",
      "incomplete_value": true,
      "site": "00b824bc",
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfef10",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b824c8",
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
      "definition_site": "00bfef48",
      "incomplete_value": true,
      "site": "00bfef4c",
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
      "definition_site": "00b82500",
      "incomplete_value": true,
      "site": "00b82504",
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
      "00bfef00",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00bfef00",
      "PARAM",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfef10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfef00",
      "READ",
      [
        "storage",
        "00c9b438",
        null,
        "pointer"
      ]
    ],
    [
      "00bfef00",
      "PARAM",
      [
        "storage",
        "01127798",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfef10",
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

- 旧版 [`00b824bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b824bc) · [`00b824c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b824c8) · [`00b82504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82464.md#insn-00b82504)
- 新版 [`00bfef04`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfef04) · [`00bfef10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfef10) · [`00bfef4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeeac.md#insn-00bfef4c)

~~~diff
- 00b824bc ["INT_ADD", "register:40f0:8", ["const:b824bc:8", "const:4:8"]]
- 00b824bc ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfef04 ["INT_ADD", "register:40f0:8", ["const:bfef04:8", "const:4:8"]]
+ 00bfef04 ["CALL", null, ["callee:00c57e80:8"]]
- 00b824bc bytes dd630194
+ 00bfef04 bytes df630194
- 00b824c8 ["INT_ADD", "register:40f0:8", ["const:b824c8:8", "const:4:8"]]
- 00b824c8 ["CALL", null, ["ram:bdb440:8"]]
+ 00bfef10 ["INT_ADD", "register:40f0:8", ["const:bfef10:8", "const:4:8"]]
+ 00bfef10 ["CALL", null, ["ram:c57e90:8"]]
- 00b824c8 bytes de630194
+ 00bfef10 bytes e0630194
- 00b82504 ["INT_ADD", "register:40f0:8", ["const:b82504:8", "const:4:8"]]
- 00b82504 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfef4c ["INT_ADD", "register:40f0:8", ["const:bfef4c:8", "const:4:8"]]
+ 00bfef4c ["CALL", null, ["callee:00c57e80:8"]]
- 00b82504 bytes cb630194
+ 00bfef4c bytes cd630194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06c8642d12ecf535c7388d9f546bbf5"></a>

### [`00b8274c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md) → [`00bff194`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpENS_4fposI9mbstate_tEE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

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
      "site": "00bff220",
      "value": [
        "leaf",
        "ram:c57eb0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b827d8",
      "value": [
        "leaf",
        "ram:bdb460:8"
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
      "00bff220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb460"
      ]
    ]
  ],
  "added": [
    [
      "00bff220",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57eb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b827d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b827d8) · [`00b82778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b82778) · [`00b827b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b8274c.md#insn-00b827b0)
- 新版 [`00bff220`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff220) · [`00bff1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff1c0) · [`00bff1f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff194.md#insn-00bff1f8)

~~~diff
- 00b827d8 ["INT_ADD", "register:40f0:8", ["const:b827d8:8", "const:4:8"]]
- 00b827d8 ["CALL", null, ["ram:bdb460:8"]]
+ 00bff220 ["INT_ADD", "register:40f0:8", ["const:bff220:8", "const:4:8"]]
+ 00bff220 ["CALL", null, ["ram:c57eb0:8"]]
- 00b827d8 bytes 22630194
+ 00bff220 bytes 24630194
- 00b82778 ["INT_ADD", "register:40f0:8", ["const:b82778:8", "const:4:8"]]
- 00b82778 ["CALL", null, ["callee:00c57e60:8"]]
+ 00bff1c0 ["INT_ADD", "register:40f0:8", ["const:bff1c0:8", "const:4:8"]]
+ 00bff1c0 ["CALL", null, ["callee:00c57e60:8"]]
- 00b82778 bytes 26630194
+ 00bff1c0 bytes 28630194
- 00b827b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b827b0 ["INT_ADD", "register:40f0:8", ["const:b827b0:8", "const:4:8"]]
- 00b827b0 ["CALLIND", null, ["register:0:8"]]
+ 00bff1f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff1f8 ["INT_ADD", "register:40f0:8", ["const:bff1f8:8", "const:4:8"]]
+ 00bff1f8 ["CALLIND", null, ["register:0:8"]]
- 00b827b0 bytes 00013fd6
+ 00bff1f8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442424b0bde74f36d475c1194dba6db7"></a>

### [`00b82810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md) → [`00bff258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md) _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5seekpExNS_8ios_base7seekdirE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb410.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e60.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c57eb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57eb0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

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
      "site": "00bff2e4",
      "value": [
        "leaf",
        "ram:c57eb0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b8289c",
      "value": [
        "leaf",
        "ram:bdb460:8"
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
      "00bff2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb460"
      ]
    ]
  ],
  "added": [
    [
      "00bff2e4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c57eb0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8289c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b8289c) · [`00b8283c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b8283c) · [`00b82874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82810.md#insn-00b82874)
- 新版 [`00bff2e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff2e4) · [`00bff284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff284) · [`00bff2bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff258.md#insn-00bff2bc)

~~~diff
- 00b8289c ["INT_ADD", "register:40f0:8", ["const:b8289c:8", "const:4:8"]]
- 00b8289c ["CALL", null, ["ram:bdb460:8"]]
+ 00bff2e4 ["INT_ADD", "register:40f0:8", ["const:bff2e4:8", "const:4:8"]]
+ 00bff2e4 ["CALL", null, ["ram:c57eb0:8"]]
- 00b8289c bytes f1620194
+ 00bff2e4 bytes f3620194
- 00b8283c ["INT_ADD", "register:40f0:8", ["const:b8283c:8", "const:4:8"]]
- 00b8283c ["CALL", null, ["callee:00c57e60:8"]]
+ 00bff284 ["INT_ADD", "register:40f0:8", ["const:bff284:8", "const:4:8"]]
+ 00bff284 ["CALL", null, ["callee:00c57e60:8"]]
- 00b8283c bytes f5620194
+ 00bff284 bytes f7620194
- 00b82874 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b82874 ["INT_ADD", "register:40f0:8", ["const:b82874:8", "const:4:8"]]
- 00b82874 ["CALLIND", null, ["register:0:8"]]
+ 00bff2bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00bff2bc ["INT_ADD", "register:40f0:8", ["const:bff2bc:8", "const:4:8"]]
+ 00bff2bc ["CALLIND", null, ["register:0:8"]]
- 00b82874 bytes 00013fd6
+ 00bff2bc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-944134fced05ccdf19575960fdc754ff"></a>

### [`00b82974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md) → [`00bff3bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEEC1EPNS_15basic_streambufIcS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bff3e8",
      "incomplete_value": true,
      "site": "00bff3e8",
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
      "definition_site": "00b829a0",
      "incomplete_value": true,
      "site": "00b829a0",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bff3ec",
      "incomplete_value": true,
      "site": "00bff3ec",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b829a4",
      "incomplete_value": true,
      "site": "00b829a4",
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
            "const:18:8"
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
      "definition_site": "00bff40c",
      "incomplete_value": true,
      "site": "00bff418",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b829c4",
      "incomplete_value": true,
      "site": "00b829d0",
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
            "const:18:8"
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
      "00bff3d8",
      "READ",
      [
        "storage",
        "00c1bcf0",
        null,
        "pointer"
      ]
    ],
    [
      "00bff3e8",
      "DATA",
      [
        "storage",
        "00c135b0",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bff3ec",
      "DATA",
      [
        "storage",
        "00c13588",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00bff3d8",
      "READ",
      [
        "storage",
        "00c9b720",
        null,
        "pointer"
      ]
    ],
    [
      "00bff3e8",
      "DATA",
      [
        "storage",
        "00c92f58",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bff3ec",
      "DATA",
      [
        "storage",
        "00c92f30",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b82984) · [`00b82990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b82990) · [`00b829ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82974.md#insn-00b829ac)
- 新版 [`00bff3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff3cc) · [`00bff3d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff3d8) · [`00bff3f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff3bc.md#insn-00bff3f4)

~~~diff
- 00b82984 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bff3cc ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b82984 bytes c80400b0
+ 00bff3cc bytes e8040090
- 00b82990 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cf0:8"]]
- 00b82990 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bff3d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:720:8"]]
+ 00bff3d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82990 bytes 087946f9
+ 00bff3d8 bytes 089143f9
- 00b829ac ["INT_ADD", "register:40f0:8", ["const:b829ac:8", "const:4:8"]]
- 00b829ac ["CALL", null, ["callee:00c57de0:8"]]
+ 00bff3f4 ["INT_ADD", "register:40f0:8", ["const:bff3f4:8", "const:4:8"]]
+ 00bff3f4 ["CALL", null, ["callee:00c57de0:8"]]
- 00b829ac bytes 79620194
+ 00bff3f4 bytes 7b620194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b6b4916ddb8f8d1a03ee7a055e60fc3"></a>

### [`00b82a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md) → [`00bff47c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff47c.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5cce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cce0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82a34.md#insn-00b82a4c)
- 新版 [`00bff494`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff47c.md#insn-00bff494)

~~~diff
- 00b82a4c ["INT_ADD", "register:40f0:8", ["const:b82a4c:8", "const:4:8"]]
- 00b82a4c ["CALL", null, ["callee:00c5cce0:8"]]
+ 00bff494 ["INT_ADD", "register:40f0:8", ["const:bff494:8", "const:4:8"]]
+ 00bff494 ["CALL", null, ["callee:00c5cce0:8"]]
- 00b82a4c bytes e5750194
+ 00bff494 bytes 13760194
~~~


<a id="compare-e609922f7efe520d8e7b2433d752d2ca"></a>

### [`00b82acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md) → [`00bff514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff514.md) _ZNSt6__ndk114basic_iostreamIcNS_11char_traitsIcEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1320.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5df20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5df20.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82ae4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82ae8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bff52c"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00b82ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md#insn-00b82ae4) · [`00b82ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md#insn-00b82ae8) · [`00b82b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82acc.md#insn-00b82b04)
- 新版 [`00bff54c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff514.md#insn-00bff54c)

~~~diff
- 00b82ae4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00b82ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b82ae4 bytes 080400f9
- 00b82ae8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
- 00b82ae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00b82ae8 bytes 290400f9
- 00b82b04 ["INT_ADD", "register:40f0:8", ["const:b82b04:8", "const:4:8"]]
- 00b82b04 ["CALL", null, ["callee:00c5df20:8"]]
+ 00bff54c ["INT_ADD", "register:40f0:8", ["const:bff54c:8", "const:4:8"]]
+ 00bff54c ["CALL", null, ["callee:00c5df20:8"]]
- 00b82b04 bytes 077a0194
+ 00bff54c bytes 757a0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf21490c8737b00345212cee1efbeea6"></a>

### [`00b82b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b40.md) → [`00bff588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff588.md) _ZNSt6__ndk19basic_iosIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfb0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00b82b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82b40.md#insn-00b82b54)
- 新版 [`00bff59c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff588.md#insn-00bff59c)

~~~diff
- 00b82b54 ["INT_ADD", "register:40f0:8", ["const:b82b54:8", "const:4:8"]]
- 00b82b54 ["CALL", null, ["callee:00c5dfb0:8"]]
+ 00bff59c ["INT_ADD", "register:40f0:8", ["const:bff59c:8", "const:4:8"]]
+ 00bff59c ["CALL", null, ["callee:00c5dfb0:8"]]
- 00b82b54 bytes 177a0194
+ 00bff59c bytes 857a0194
~~~


<a id="compare-594bf5158d5dc27ba1779f746930a896"></a>

### [`00b82c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c00.md) → [`00bff648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff648.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEED0Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be13d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c5dfd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfd0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

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
      "site": "00bff65c",
      "value": [
        "leaf",
        "ram:c5dfd0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b82c14",
      "value": [
        "leaf",
        "ram:be13d0:8"
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
      "00bff65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be13d0"
      ]
    ]
  ],
  "added": [
    [
      "00bff65c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5dfd0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82c00.md#insn-00b82c14)
- 新版 [`00bff65c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff648.md#insn-00bff65c)

~~~diff
- 00b82c14 ["INT_ADD", "register:40f0:8", ["const:b82c14:8", "const:4:8"]]
- 00b82c14 ["CALL", null, ["ram:be13d0:8"]]
+ 00bff65c ["INT_ADD", "register:40f0:8", ["const:bff65c:8", "const:4:8"]]
+ 00bff65c ["CALL", null, ["ram:c5dfd0:8"]]
- 00b82c14 bytes ef790194
+ 00bff65c bytes 5d7a0194
~~~


<a id="compare-91391c68463cb2715b502871d7235723"></a>

### [`00b82e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md) → [`00bff8e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC2Ev

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13e0.md) · 呼出先 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md)
- 新版 呼出元 1件 [`00c5dfe0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dfe0.md) · 呼出先 1件 [`00c5a3a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3a0.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bff900",
      "incomplete_value": true,
      "site": "00bff900",
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
      "definition_site": "00b82eb8",
      "incomplete_value": true,
      "site": "00b82eb8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bff904",
      "value": [
        "leaf",
        "ram:c5a3a0:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b82ebc",
      "value": [
        "leaf",
        "ram:bdd950:8"
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
      "00bff8f8",
      "READ",
      [
        "storage",
        "00c1bd00",
        null,
        "pointer"
      ]
    ],
    [
      "00bff900",
      "DATA",
      [
        "storage",
        "00c131d0",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bff904",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdd950"
      ]
    ]
  ],
  "added": [
    [
      "00bff8f8",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "00bff900",
      "DATA",
      [
        "storage",
        "00c92b78",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00bff904",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5a3a0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md#insn-00b82ebc) · [`00b82ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md#insn-00b82ea8) · [`00b82eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82e98.md#insn-00b82eb0)
- 新版 [`00bff904`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md#insn-00bff904) · [`00bff8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md#insn-00bff8f0) · [`00bff8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff8e0.md#insn-00bff8f8)

~~~diff
- 00b82ebc ["INT_ADD", "register:40f0:8", ["const:b82ebc:8", "const:4:8"]]
- 00b82ebc ["CALL", null, ["ram:bdd950:8"]]
+ 00bff904 ["INT_ADD", "register:40f0:8", ["const:bff904:8", "const:4:8"]]
+ 00bff904 ["CALL", null, ["ram:c5a3a0:8"]]
- 00b82ebc bytes a56a0194
+ 00bff904 bytes a76a0194
- 00b82ea8 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bff8f0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b82ea8 bytes c80400b0
+ 00bff8f0 bytes e8040090
- 00b82eb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
- 00b82eb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bff8f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:730:8"]]
+ 00bff8f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b82eb0 bytes 088146f9
+ 00bff8f8 bytes 089943f9
~~~


<a id="compare-6d8e4a5db6aee6fa2baaddce82b6638d"></a>

### [`00b82edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82edc.md) → [`00bff924`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEC1ERKS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 81.82% / 新版 81.82%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b82f04"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00bff94c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bff93c",
      "incomplete_value": true,
      "site": "00bff950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b82ef8",
      "READ",
      [
        "storage",
        "00c1bd00",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00b82f04",
      "DATA",
      [
        "storage",
        "00c131d0",
        null,
        "undefined1[128]"
      ]
    ]
  ],
  "added": [
    [
      "00bff940",
      "READ",
      [
        "storage",
        "00c9b730",
        null,
        "pointer"
      ]
    ],
    [
      "00bff94c",
      "DATA",
      [
        "storage",
        "00c92b78",
        null,
        "undefined1[128]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b82f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82edc.md#insn-00b82f04) · [`00b82f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82edc.md#insn-00b82f08)
- 新版 [`00bff950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md#insn-00bff950) · [`00bff94c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff924.md#insn-00bff94c)

~~~diff
- 00b82f04 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00b82f04 ["COPY", "tmp:1:8", ["register:4000:8"]]
- 00b82f04 ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
- 00b82f04 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00b82f04 bytes 088400f8
- 00b82f08 ["INT_ADD", "register:40f0:8", ["const:b82f08:8", "const:4:8"]]
- 00b82f08 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bff950 ["INT_ADD", "register:40f0:8", ["const:bff950:8", "const:4:8"]]
+ 00bff950 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b82f08 bytes 9e6a0194
+ 00bff950 bytes a06a0194
+ 00bff94c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00bff94c ["COPY", "tmp:1:8", ["register:4000:8"]]
+ 00bff94c ["INT_ADD", "register:4000:8", ["register:4000:8", "const:8:8"]]
+ 00bff94c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00bff94c bytes 088400f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51c42e7357584854b396cdc72dcd3e54"></a>

### [`00b82f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md) → [`00bff9cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md) _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE4swapERS3_

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c5a3d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a3d0.md) [`00c5dee0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dee0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

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
      "site": "00bffa10",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b82fc8",
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
      "00bffa10",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bffa10",
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

- 旧版 [`00b82fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fc8) · [`00b82fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fa8) · [`00b82fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82f84.md#insn-00b82fb4)
- 新版 [`00bffa10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bffa10) · [`00bff9f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bff9f0) · [`00bff9fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff9cc.md#insn-00bff9fc)

~~~diff
- 00b82fc8 ["INT_ADD", "register:40f0:8", ["const:b82fc8:8", "const:4:8"]]
- 00b82fc8 ["CALL", null, ["ram:bdb440:8"]]
+ 00bffa10 ["INT_ADD", "register:40f0:8", ["const:bffa10:8", "const:4:8"]]
+ 00bffa10 ["CALL", null, ["ram:c57e90:8"]]
- 00b82fc8 bytes 1e610194
+ 00bffa10 bytes 20610194
- 00b82fa8 ["INT_ADD", "register:40f0:8", ["const:b82fa8:8", "const:4:8"]]
- 00b82fa8 ["CALL", null, ["callee:00c5a3d0:8"]]
+ 00bff9f0 ["INT_ADD", "register:40f0:8", ["const:bff9f0:8", "const:4:8"]]
+ 00bff9f0 ["CALL", null, ["callee:00c5a3d0:8"]]
- 00b82fa8 bytes 766a0194
+ 00bff9f0 bytes 786a0194
- 00b82fb4 ["INT_ADD", "register:40f0:8", ["const:b82fb4:8", "const:4:8"]]
- 00b82fb4 ["CALL", null, ["callee:00c5dee0:8"]]
+ 00bff9fc ["INT_ADD", "register:40f0:8", ["const:bff9fc:8", "const:4:8"]]
+ 00bff9fc ["CALL", null, ["callee:00c5dee0:8"]]
- 00b82fb4 bytes cb780194
+ 00bff9fc bytes 39790194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1b262a7d77d99fda6d22ed616933c27"></a>

### [`00b83340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md) → [`00bffd88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEEC1EPNS_15basic_streambufIwS2_EE

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57de0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.27% / 新版 77.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bffdb4",
      "incomplete_value": true,
      "site": "00bffdb4",
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
      "definition_site": "00b8336c",
      "incomplete_value": true,
      "site": "00b8336c",
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bffdb8",
      "incomplete_value": true,
      "site": "00bffdb8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83370",
      "incomplete_value": true,
      "site": "00b83370",
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
            "const:18:8"
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
      "00bffda4",
      "READ",
      [
        "storage",
        "00c1bd08",
        null,
        "pointer"
      ]
    ],
    [
      "00bffdb4",
      "DATA",
      [
        "storage",
        "00c13280",
        null,
        "pointer"
      ]
    ],
    [
      "00bffdb8",
      "DATA",
      [
        "storage",
        "00c13258",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bffda4",
      "READ",
      [
        "storage",
        "00c9b738",
        null,
        "pointer"
      ]
    ],
    [
      "00bffdb4",
      "DATA",
      [
        "storage",
        "00c92c28",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00bffdb8",
      "DATA",
      [
        "storage",
        "00c92c00",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b83350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md#insn-00b83350) · [`00b8335c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md#insn-00b8335c) · [`00b83378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83340.md#insn-00b83378)
- 新版 [`00bffd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md#insn-00bffd98) · [`00bffda4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md#insn-00bffda4) · [`00bffdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffd88.md#insn-00bffdc0)

~~~diff
- 00b83350 ["COPY", "register:4040:8", ["const:c1b000:8"]]
+ 00bffd98 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00b83350 bytes c8040090
+ 00bffd98 bytes e8040090
- 00b8335c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
- 00b8335c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bffda4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:738:8"]]
+ 00bffda4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b8335c bytes 088546f9
+ 00bffda4 bytes 089d43f9
- 00b83378 ["INT_ADD", "register:40f0:8", ["const:b83378:8", "const:4:8"]]
- 00b83378 ["CALL", null, ["callee:00c57de0:8"]]
+ 00bffdc0 ["INT_ADD", "register:40f0:8", ["const:bffdc0:8", "const:4:8"]]
+ 00bffdc0 ["CALL", null, ["callee:00c57de0:8"]]
- 00b83378 bytes 06600194
+ 00bffdc0 bytes 08600194
~~~


<a id="compare-6acd595454765148259a801839c7ac6c"></a>

### [`00b834ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md) → [`00bffef4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md) _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md)
- 新版 呼出元 1件 [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.32% / 新版 98.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bfff84",
      "incomplete_value": true,
      "site": "00bfff88",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b8353c",
      "incomplete_value": true,
      "site": "00b83540",
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00bfff94",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b8354c",
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
      "00bfff84",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00bfff84",
      "PARAM",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfff94",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00bfff84",
      "READ",
      [
        "storage",
        "00c9b740",
        null,
        "pointer"
      ]
    ],
    [
      "00bfff84",
      "PARAM",
      [
        "storage",
        "01127a08",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00bfff94",
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

- 旧版 [`00b83540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b83540) · [`00b8354c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b8354c) · [`00b8350c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md#insn-00b8350c)
- 新版 [`00bfff88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff88) · [`00bfff94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff94) · [`00bfff54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bffef4.md#insn-00bfff54)

~~~diff
- 00b83540 ["INT_ADD", "register:40f0:8", ["const:b83540:8", "const:4:8"]]
- 00b83540 ["CALL", null, ["callee:00c57e80:8"]]
+ 00bfff88 ["INT_ADD", "register:40f0:8", ["const:bfff88:8", "const:4:8"]]
+ 00bfff88 ["CALL", null, ["callee:00c57e80:8"]]
- 00b83540 bytes bc5f0194
+ 00bfff88 bytes be5f0194
- 00b8354c ["INT_ADD", "register:40f0:8", ["const:b8354c:8", "const:4:8"]]
- 00b8354c ["CALL", null, ["ram:bdb440:8"]]
+ 00bfff94 ["INT_ADD", "register:40f0:8", ["const:bfff94:8", "const:4:8"]]
+ 00bfff94 ["CALL", null, ["ram:c57e90:8"]]
- 00b8354c bytes bd5f0194
+ 00bfff94 bytes bf5f0194
- 00b8350c ["INT_ADD", "register:40f0:8", ["const:b8350c:8", "const:4:8"]]
- 00b8350c ["CALL", null, ["callee:00c5dff0:8"]]
+ 00bfff54 ["INT_ADD", "register:40f0:8", ["const:bfff54:8", "const:4:8"]]
+ 00bfff54 ["CALL", null, ["callee:00c5dff0:8"]]
- 00b8350c bytes b9770194
+ 00bfff54 bytes 27780194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3faab83ac74bc41f3816971efe4871e2"></a>

### [`00b8369c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md) → [`00c000e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md) _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be13f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be13f0.md) · 呼出先 3件 [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1400.md) [`00be1410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1410.md)
- 新版 呼出元 1件 [`00c5dff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5d/00c5dff0.md) · 呼出先 3件 [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e000.md) [`00c5e010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e010.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

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
      "site": "00c00164",
      "value": [
        "leaf",
        "ram:c5e010:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b8371c",
      "value": [
        "leaf",
        "ram:be1410:8"
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
      "00c00164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00be1410"
      ]
    ]
  ],
  "added": [
    [
      "00c00164",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00c5e010"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b8371c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b8371c) · [`00b836d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b836d0) · [`00b836f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b8369c.md#insn-00b836f4)
- 新版 [`00c00164`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c00164) · [`00c00118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c00118) · [`00c0013c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c000e4.md#insn-00c0013c)

~~~diff
- 00b8371c ["INT_ADD", "register:40f0:8", ["const:b8371c:8", "const:4:8"]]
- 00b8371c ["CALL", null, ["ram:be1410:8"]]
+ 00c00164 ["INT_ADD", "register:40f0:8", ["const:c00164:8", "const:4:8"]]
+ 00c00164 ["CALL", null, ["ram:c5e010:8"]]
- 00b8371c bytes 3d770194
+ 00c00164 bytes ab770194
- 00b836d0 ["INT_ADD", "register:40f0:8", ["const:b836d0:8", "const:4:8"]]
- 00b836d0 ["CALL", null, ["callee:00c5e000:8"]]
+ 00c00118 ["INT_ADD", "register:40f0:8", ["const:c00118:8", "const:4:8"]]
+ 00c00118 ["CALL", null, ["callee:00c5e000:8"]]
- 00b836d0 bytes 4c770194
+ 00c00118 bytes ba770194
- 00b836f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b836f4 ["INT_ADD", "register:40f0:8", ["const:b836f4:8", "const:4:8"]]
- 00b836f4 ["CALLIND", null, ["register:0:8"]]
+ 00c0013c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c0013c ["INT_ADD", "register:40f0:8", ["const:c0013c:8", "const:4:8"]]
+ 00c0013c ["CALLIND", null, ["register:0:8"]]
- 00b836f4 bytes 00013fd6
+ 00c0013c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e53c7b3c99ce96e845d4fb6d143452d"></a>

### [`00b839b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md) → [`00c003fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md) FUN_00c003fc

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b839ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839ac.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c003f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003f4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00450",
      "incomplete_value": true,
      "site": "00c00454",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83a08",
      "incomplete_value": true,
      "site": "00b83a0c",
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00484",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b83a3c",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00450",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00450",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00484",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00450",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00450",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00484",
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

- 旧版 [`00b83a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b83a0c) · [`00b83a3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b83a3c) · [`00b839e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b839b4.md#insn-00b839e0)
- 新版 [`00c00454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00454) · [`00c00484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00484) · [`00c00428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c003fc.md#insn-00c00428)

~~~diff
- 00b83a0c ["INT_ADD", "register:40f0:8", ["const:b83a0c:8", "const:4:8"]]
- 00b83a0c ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00454 ["INT_ADD", "register:40f0:8", ["const:c00454:8", "const:4:8"]]
+ 00c00454 ["CALL", null, ["callee:00c57e80:8"]]
- 00b83a0c bytes 895e0194
+ 00c00454 bytes 8b5e0194
- 00b83a3c ["INT_ADD", "register:40f0:8", ["const:b83a3c:8", "const:4:8"]]
- 00b83a3c ["CALL", null, ["ram:bdb440:8"]]
+ 00c00484 ["INT_ADD", "register:40f0:8", ["const:c00484:8", "const:4:8"]]
+ 00c00484 ["CALL", null, ["ram:c57e90:8"]]
- 00b83a3c bytes 815e0194
+ 00c00484 bytes 835e0194
- 00b839e0 ["INT_ADD", "register:40f0:8", ["const:b839e0:8", "const:4:8"]]
- 00b839e0 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00428 ["INT_ADD", "register:40f0:8", ["const:c00428:8", "const:4:8"]]
+ 00c00428 ["CALL", null, ["callee:00c5e020:8"]]
- 00b839e0 bytes 90760194
+ 00c00428 bytes fe760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20b2ee62c61ea667a720f9d38d684b4d"></a>

### [`00b83aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md) → [`00c00534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md) FUN_00c00534

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83ae4.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c0052c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c0052c.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00588",
      "incomplete_value": true,
      "site": "00c0058c",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83b40",
      "incomplete_value": true,
      "site": "00b83b44",
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c005bc",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b83b74",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00588",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00588",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c005bc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00588",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00588",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c005bc",
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

- 旧版 [`00b83b44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b44) · [`00b83b74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b74) · [`00b83b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83aec.md#insn-00b83b18)
- 新版 [`00c0058c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c0058c) · [`00c005bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c005bc) · [`00c00560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c00534.md#insn-00c00560)

~~~diff
- 00b83b44 ["INT_ADD", "register:40f0:8", ["const:b83b44:8", "const:4:8"]]
- 00b83b44 ["CALL", null, ["callee:00c57e80:8"]]
+ 00c0058c ["INT_ADD", "register:40f0:8", ["const:c0058c:8", "const:4:8"]]
+ 00c0058c ["CALL", null, ["callee:00c57e80:8"]]
- 00b83b44 bytes 3b5e0194
+ 00c0058c bytes 3d5e0194
- 00b83b74 ["INT_ADD", "register:40f0:8", ["const:b83b74:8", "const:4:8"]]
- 00b83b74 ["CALL", null, ["ram:bdb440:8"]]
+ 00c005bc ["INT_ADD", "register:40f0:8", ["const:c005bc:8", "const:4:8"]]
+ 00c005bc ["CALL", null, ["ram:c57e90:8"]]
- 00b83b74 bytes 335e0194
+ 00c005bc bytes 355e0194
- 00b83b18 ["INT_ADD", "register:40f0:8", ["const:b83b18:8", "const:4:8"]]
- 00b83b18 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c00560 ["INT_ADD", "register:40f0:8", ["const:c00560:8", "const:4:8"]]
+ 00c00560 ["CALL", null, ["callee:00c5e020:8"]]
- 00b83b18 bytes 42760194
+ 00c00560 bytes b0760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b80da4ba742f888d7294c30753cda4"></a>

### [`00b83c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md) → [`00c006ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md) FUN_00c006ac

採用 · 移動量 `+0x7ca48` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b83c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c5c.md) · 呼出先 5件 [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00be1420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1420.md)
- 新版 呼出元 1件 [`00c006a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006a4.md) · 呼出先 5件 [`00c57e70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e70.md) [`00c57e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e80.md) [`00c57e90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57e90.md) [`00c57ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ea0.md) [`00c5e020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5e020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c00700",
      "incomplete_value": true,
      "site": "00c00704",
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
                "const:c9b000:8"
              ],
              [
                "leaf",
                "const:748:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b83cb8",
      "incomplete_value": true,
      "site": "00b83cbc",
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00c00734",
      "value": [
        "leaf",
        "ram:c57e90:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00b83cec",
      "value": [
        "leaf",
        "ram:bdb440:8"
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
      "00c00700",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00c00700",
      "PARAM",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00734",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "00bdb440"
      ]
    ]
  ],
  "added": [
    [
      "00c00700",
      "READ",
      [
        "storage",
        "00c9b748",
        null,
        "pointer"
      ]
    ],
    [
      "00c00700",
      "PARAM",
      [
        "storage",
        "01127788",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00c00734",
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

- 旧版 [`00b83cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83cbc) · [`00b83cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83cec) · [`00b83c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b83c64.md#insn-00b83c90)
- 新版 [`00c00704`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c00704) · [`00c00734`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c00734) · [`00c006d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c00/00c006ac.md#insn-00c006d8)

~~~diff
- 00b83cbc ["INT_ADD", "register:40f0:8", ["const:b83cbc:8", "const:4:8"]]
- 00b83cbc ["CALL", null, ["callee:00c57e80:8"]]
+ 00c00704 ["INT_ADD", "register:40f0:8", ["const:c00704:8", "const:4:8"]]
+ 00c00704 ["CALL", null, ["callee:00c57e80:8"]]
- 00b83cbc bytes dd5d0194
+ 00c00704 bytes df5d0194
- 00b83cec ["INT_ADD", "register:40f0:8", ["const:b83cec:8", "const:4:8"]]
- 00b83cec ["CALL", null, ["ram:bdb440:8"]]
+ 00c00734 ["INT_ADD", "register:40f0:8", ["const:c00734:8", "const:4:8"]]
+ 00c00734 ["CALL", null, ["ram:c57e90:8"]]
- 00b83cec bytes d55d0194
+ 00c00734 bytes d75d0194
- 00b83c90 ["INT_ADD", "register:40f0:8", ["const:b83c90:8", "const:4:8"]]
- 00b83c90 ["CALL", null, ["callee:00c5e020:8"]]
+ 00c006d8 ["INT_ADD", "register:40f0:8", ["const:c006d8:8", "const:4:8"]]
+ 00c006d8 ["CALL", null, ["callee:00c5e020:8"]]
- 00b83c90 bytes e4750194
+ 00c006d8 bytes 52760194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

