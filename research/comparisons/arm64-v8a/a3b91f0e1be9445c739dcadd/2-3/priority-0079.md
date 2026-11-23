# v15.7.4 → v16.0.0 · 最優先の変更候補 (79)

[一覧の目次](README.md)

<a id="compare-5837663e11c54f8c2491e8cfc17632ed"></a>

### [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) → [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) __cxa_call_unexpected

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 18件 [`00bbaa24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa24.md) [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bd4fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fd8.md) [`00bd4fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd4/00bd4fe4.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00c3746c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3746c.md) [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c3777c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3777c.md) [`00c51a20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a20.md) [`00c51a2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51a2c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, operands_and_dependencies, store_value

命令の説明率　旧版 97.69% / 新版 97.69%

CFGの説明率　旧版 90.00% / 新版 93.10%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c52c10",
      "incomplete_value": true,
      "site": "00c52c14",
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
      "definition_site": "00bd61c8",
      "incomplete_value": true,
      "site": "00bd61cc",
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
      "definition_site": "00c52c24",
      "incomplete_value": true,
      "site": "00c52c38",
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd61dc",
      "incomplete_value": true,
      "site": "00bd61f0",
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
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52c70",
      "incomplete_value": true,
      "site": "00c52c78",
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
                "const:a60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6228",
      "incomplete_value": true,
      "site": "00bd6230",
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
                "const:30:8"
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
      "00c52c0c",
      "READ",
      [
        "storage",
        "00c1c028",
        null,
        "pointer"
      ]
    ],
    [
      "00c52c14",
      "DATA",
      [
        "storage",
        "00c168c0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c52c24",
      "READ",
      [
        "storage",
        "00c1c030",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c52c0c",
      "READ",
      [
        "storage",
        "00c9ba58",
        null,
        "pointer"
      ]
    ],
    [
      "00c52c14",
      "DATA",
      [
        "storage",
        "00c96268",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00c52c24",
      "READ",
      [
        "storage",
        "00c9ba60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd61f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd61f0) · [`00bd6230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd6230) · [`00bd609c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md#insn-00bd609c)
- 新版 `00c52c38`（命令位置の公開資料なし） · `00c52c78`（命令位置の公開資料なし） · `00c52ae4`（命令位置の公開資料なし）

~~~diff
- 00bd61f0 ["INT_ADD", "register:40f0:8", ["const:bd61f0:8", "const:4:8"]]
- 00bd61f0 ["CALL", null, ["callee:00c52e80:8"]]
+ 00c52c38 ["INT_ADD", "register:40f0:8", ["const:c52c38:8", "const:4:8"]]
+ 00c52c38 ["CALL", null, ["callee:00c52e80:8"]]
- 00bd61f0 bytes 92000094
+ 00c52c38 bytes 92000094
- 00bd6230 ["INT_ADD", "register:40f0:8", ["const:bd6230:8", "const:4:8"]]
- 00bd6230 ["CALL", null, ["callee:00c57b10:8"]]
+ 00c52c78 ["INT_ADD", "register:40f0:8", ["const:c52c78:8", "const:4:8"]]
+ 00c52c78 ["CALL", null, ["callee:00c57b10:8"]]
- 00bd6230 bytes a4130094
+ 00c52c78 bytes a6130094
- 00bd609c ["INT_ADD", "register:40f0:8", ["const:bd609c:8", "const:4:8"]]
- 00bd609c ["CALL", null, ["callee:00c57c10:8"]]
+ 00c52ae4 ["INT_ADD", "register:40f0:8", ["const:c52ae4:8", "const:4:8"]]
+ 00c52ae4 ["CALL", null, ["callee:00c57c10:8"]]
- 00bd609c bytes 49140094
+ 00c52ae4 bytes 4b140094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e30c7aae719b1970aeefec4697dcd83e"></a>

### [`00bd6438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md) → [`00c52e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52e80.md) FUN_00c52e80

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd5ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5ad8.md) [`00bd6074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6074.md) · 呼出先 4件 [`00bbaa70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbaa70.md) [`00bd6290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6290.md) [`00bdb1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1c0.md) [`00bdb1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1d0.md)
- 新版 呼出元 2件 [`00c52520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52520.md) [`00c52abc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52abc.md) · 呼出先 4件 [`00c374b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c374b8.md) [`00c52cd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52cd8.md) [`00c57c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c10.md) [`00c57c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 73.33% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd64e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c52f28"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c52f18",
      "incomplete_value": true,
      "site": "00c52f2c",
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
      "00c52f14",
      "DATA",
      [
        "storage",
        "002fdf30",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd64e0",
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
      "00c52f14",
      "DATA",
      [
        "storage",
        "00313d68",
        null,
        null
      ]
    ],
    [
      "00c52f28",
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

- 旧版 [`00bd64e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md#insn-00bd64e0) · [`00bd64e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6438.md#insn-00bd64e4)
- 新版 `00c52f2c`（命令位置の公開資料なし） · `00c52f28`（命令位置の公開資料なし）

~~~diff
- 00bd64e0 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
- 00bd64e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bd64e0 bytes e80700f9
- 00bd64e4 ["INT_ADD", "register:40f0:8", ["const:bd64e4:8", "const:4:8"]]
- 00bd64e4 ["CALL", null, ["callee:00c52cd8:8"]]
+ 00c52f2c ["INT_ADD", "register:40f0:8", ["const:c52f2c:8", "const:4:8"]]
+ 00c52f2c ["CALL", null, ["callee:00c52cd8:8"]]
- 00bd64e4 bytes 6bffff97
+ 00c52f2c bytes 6bffff97
+ 00c52f28 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:8:8"]]
+ 00c52f28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00c52f28 bytes e80700f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3eaa8f8d9d9d3d18420a30223a7d70e2"></a>

### [`00bd6558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6558.md) → [`00c52fa0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52fa0.md) FUN_00c52fa0

採用 · 移動量 `+0x7ca48` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`00acba3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acb/00acba3c.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00b2b4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) [`00be8230`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00be8/00be8230.md) [`00beeaf8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beeaf8.md) [`00beef14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bee/00beef14.md) [`00bef16c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef16c.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 85.71% / 新版 92.31%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c53008",
      "incomplete_value": false,
      "site": "00c53010",
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
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6558.md#insn-00bd6578) · [`00bd658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6558.md#insn-00bd658c) · [`00bd65a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6558.md#insn-00bd65a4)
- 新版 `00c52fc0`（命令位置の公開資料なし） · `00c52fd4`（命令位置の公開資料なし） · `00c52fec`（命令位置の公開資料なし）

~~~diff
- 00bd6578 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd6578 ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00c52fc0 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c52fc0 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bd6578 bytes c3030054
+ 00c52fc0 bytes c3030054
- 00bd658c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd658c ["CBRANCH", null, ["local:b11:8", "tmp:0:1"]]
+ 00c52fd4 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c52fd4 ["CBRANCH", null, ["local:b10:8", "tmp:0:1"]]
- 00bd658c bytes 23030054
+ 00c52fd4 bytes 23030054
- 00bd65a4 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd65a4 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
+ 00c52fec ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00c52fec ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00bd65a4 bytes 4b010054
+ 00c52fec bytes 4b010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-656d18716af65c5374f25962c930bc08"></a>

### [`00bd6694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md) → [`00c530dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md) __emutls_get_address

採用 · 移動量 `+0x7ca48` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdd4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4a0.md) · 呼出先 11件 [`00bd68bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb2f0.md) [`00bdd1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1d0.md)
- 新版 呼出元 1件 [`00c59ef0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59ef0.md) · 呼出先 11件 [`00c53304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md) [`00c57d40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57d40.md) [`00c59c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59c20.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.80% / 新版 87.80%

CFGの説明率　旧版 68.75% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6750"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6754"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c53198"
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
      "00c53104",
      "READ",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00bd6710",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c90"
      ]
    ],
    [
      "unmatched:00bd6714",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c531f4"
      ]
    ]
  ],
  "added": [
    [
      "00c53104",
      "READ",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53158",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00c57c90"
      ]
    ],
    [
      "00c5315c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c531f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd66c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd66c0) · [`00bd66f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd66f0) · [`00bd6710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md#insn-00bd6710)
- 新版 `00c53108`（命令位置の公開資料なし） · `00c53138`（命令位置の公開資料なし）

~~~diff
- 00bd66c0 ["INT_ADD", "register:40f0:8", ["const:bd66c0:8", "const:4:8"]]
- 00bd66c0 ["CALL", null, ["callee:00c5ddf0:8"]]
+ 00c53108 ["INT_ADD", "register:40f0:8", ["const:c53108:8", "const:4:8"]]
+ 00c53108 ["CALL", null, ["callee:00c5ddf0:8"]]
- 00bd66c0 bytes cc2a0094
+ 00c53108 bytes 3a2b0094
- 00bd66f0 ["INT_ADD", "register:40f0:8", ["const:bd66f0:8", "const:4:8"]]
- 00bd66f0 ["CALL", null, ["callee:00c59ca0:8"]]
+ 00c53138 ["INT_ADD", "register:40f0:8", ["const:c53138:8", "const:4:8"]]
+ 00c53138 ["CALL", null, ["callee:00c59ca0:8"]]
- 00bd66f0 bytes d81a0094
+ 00c53138 bytes da1a0094
- 00bd6710 ["INT_ADD", "register:40f0:8", ["const:bd6710:8", "const:4:8"]]
- 00bd6710 ["CALL", null, ["callee:00c57c90:8"]]
- 00bd6710 bytes cc120094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eae5f4f286e284076057c11292b8a7bf"></a>

### [`00bd6880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md) → [`00c532c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c532c8.md) FUN_00c532c8

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`004182e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004182e8.md) · 呼出先 1件 [`00be1f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f50.md)
- 新版 呼出元 1件 [`0043ade8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ade8.md) · 呼出先 1件 [`00c5eb10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb10.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c532ec",
      "incomplete_value": true,
      "site": "00c532f0",
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
      "definition_site": "00bd68a4",
      "incomplete_value": true,
      "site": "00bd68a8",
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
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c532d0",
      "READ",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd68a4",
      "READ",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "00c532f4",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c532d0",
      "READ",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c532ec",
      "READ",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c532f4",
      "WRITE",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd68a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd68a8) · [`00bd6884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd6884) · [`00bd6888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6880.md#insn-00bd6888)
- 新版 `00c532f0`（命令位置の公開資料なし） · `00c532cc`（命令位置の公開資料なし） · `00c532d0`（命令位置の公開資料なし）

~~~diff
- 00bd68a8 ["INT_ADD", "register:40f0:8", ["const:bd68a8:8", "const:4:8"]]
- 00bd68a8 ["CALL", null, ["callee:00c5eb10:8"]]
+ 00c532f0 ["INT_ADD", "register:40f0:8", ["const:c532f0:8", "const:4:8"]]
+ 00c532f0 ["CALL", null, ["callee:00c5eb10:8"]]
- 00bd68a8 bytes aa2d0094
+ 00c532f0 bytes 082e0094
- 00bd6884 ["COPY", "register:4040:8", ["const:10a3000:8"]]
+ 00c532cc ["COPY", "register:4040:8", ["const:1128000:8"]]
- 00bd6884 bytes 682600b0
+ 00c532cc bytes a82600b0
- 00bd6888 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
- 00bd6888 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6888 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00c532d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8a0:8"]]
+ 00c532d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c532d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bd6888 bytes 08416639
+ 00c532d0 bytes 08816239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adff26496833a690b05c3990da4497e1"></a>

### [`00bd68bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md) → [`00c53304`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53304.md) FUN_00c53304

採用 · 移動量 `+0x7ca48` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bd6694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6694.md) · 呼出先 3件 [`00bd68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68f8.md) [`00bdd4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd4b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 1件 [`00c530dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c530dc.md) · 呼出先 3件 [`00c53340`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53340.md) [`00c59f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59f00.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c5332c",
      "incomplete_value": false,
      "site": "00c5332c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68e4",
      "incomplete_value": false,
      "site": "00bd68e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53310",
      "incomplete_value": false,
      "site": "00c5331c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd68c8",
      "incomplete_value": false,
      "site": "00bd68d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:994:8"
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
      "definition_site": "00c53318",
      "incomplete_value": false,
      "site": "00c5331c",
      "value": [
        "leaf",
        "const:c53340:8"
      ]
    },
    "old": {
      "definition_site": "00bd68d0",
      "incomplete_value": false,
      "site": "00bd68d4",
      "value": [
        "leaf",
        "const:bd68f8:8"
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
      "00c53310",
      "PARAM",
      [
        "storage",
        "010a3994",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53318",
      "PARAM",
      [
        "storage",
        "00bd68f8",
        null,
        null
      ]
    ],
    [
      "00c5332c",
      "WRITE",
      [
        "storage",
        "010a3990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c53310",
      "PARAM",
      [
        "storage",
        "011288a4",
        null,
        "undefined4"
      ]
    ],
    [
      "00c53318",
      "PARAM",
      [
        "storage",
        "00c53340",
        null,
        null
      ]
    ],
    [
      "00c5332c",
      "WRITE",
      [
        "storage",
        "011288a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd68d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68d4) · [`00bd68e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68e4) · [`00bd68c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd68bc.md#insn-00bd68c4)
- 新版 `00c5331c`（命令位置の公開資料なし） · `00c5332c`（命令位置の公開資料なし） · `00c5330c`（命令位置の公開資料なし）

~~~diff
- 00bd68d4 ["INT_ADD", "register:40f0:8", ["const:bd68d4:8", "const:4:8"]]
- 00bd68d4 ["CALL", null, ["callee:00c59f00:8"]]
+ 00c5331c ["INT_ADD", "register:40f0:8", ["const:c5331c:8", "const:4:8"]]
+ 00c5331c ["CALL", null, ["callee:00c59f00:8"]]
- 00bd68d4 bytes f71a0094
+ 00c5331c bytes f91a0094
- 00bd68e4 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bd68e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:990:8"]]
- 00bd68e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00c5332c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00c5332c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:8a0:8"]]
+ 00c5332c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bd68e4 bytes 09412639
+ 00c5332c bytes 09812239
- 00bd68c4 ["COPY", "register:4000:8", ["const:10a3000:8"]]
+ 00c5330c ["COPY", "register:4000:8", ["const:1128000:8"]]
- 00bd68c4 bytes 602600b0
+ 00c5330c bytes a02600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff3cf2c1dd27e54703dab143f62fee9a"></a>

### [`00bd69b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md) → [`00c53404`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53404.md) _INIT_0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) [`00be1f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f60.md) [`00be1f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f70.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md) [`00c5eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb30.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd69d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6a20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6a3c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd69d4",
      "WRITE",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00bd69e8",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd6a00",
      "PARAM",
      [
        "storage",
        "00299a3f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53424",
      "WRITE",
      [
        "storage",
        "011288e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00c53438",
      "PARAM",
      [
        "storage",
        "002a62f5",
        null,
        "string"
      ]
    ],
    [
      "00c53450",
      "PARAM",
      [
        "storage",
        "002a9918",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd69d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd69d4) · [`00bd69f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd69f0) · [`00bd6a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd69b4.md#insn-00bd6a0c)
- 新版 `00c53440`（命令位置の公開資料なし） · `00c5345c`（命令位置の公開資料なし）

~~~diff
- 00bd69d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00bd69d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00bd69d4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:9d0:8"]]
- 00bd69d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00bd69d4 bytes 3f412739
- 00bd69f0 ["INT_ADD", "register:40f0:8", ["const:bd69f0:8", "const:4:8"]]
- 00bd69f0 ["CALL", null, ["callee:00c5eb30:8"]]
+ 00c53440 ["INT_ADD", "register:40f0:8", ["const:c53440:8", "const:4:8"]]
+ 00c53440 ["CALL", null, ["callee:00c5eb30:8"]]
- 00bd69f0 bytes 602d0094
+ 00c53440 bytes bc2d0094
- 00bd6a0c ["INT_ADD", "register:40f0:8", ["const:bd6a0c:8", "const:4:8"]]
- 00bd6a0c ["CALL", null, ["callee:00c5cd30:8"]]
+ 00c5345c ["INT_ADD", "register:40f0:8", ["const:c5345c:8", "const:4:8"]]
+ 00c5345c ["CALL", null, ["callee:00c5cd30:8"]]
- 00bd6a0c bytes 09260094
+ 00c5345c bytes 35260094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5333cb7980a6d7471eedaa22ba78afe6"></a>

### [`00bd6cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md) → [`00c53748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53748.md) _INIT_1

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bd6a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6a4c.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md) [`00be1f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f60.md) [`00be1f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f70.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c5349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c5349c.md) [`00c5cd30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5c/00c5cd30.md) [`00c5eb20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb20.md) [`00c5eb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb30.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00c53754",
      "incomplete_value": true,
      "site": "00c53754",
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
      "definition_site": "00bd6d04",
      "incomplete_value": true,
      "site": "00bd6d04",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5376c",
      "incomplete_value": false,
      "site": "00c53774",
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
            "const:2f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d1c",
      "incomplete_value": false,
      "site": "00bd6d24",
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
            "const:7c0:8"
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
      "definition_site": "00c53784",
      "incomplete_value": false,
      "site": "00c53790",
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
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd6d34",
      "incomplete_value": false,
      "site": "00bd6d40",
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
            "const:a3f:8"
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
      "00c53750",
      "READ",
      [
        "storage",
        "010a39d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c5376c",
      "PARAM",
      [
        "storage",
        "002967c0",
        null,
        "string"
      ]
    ],
    [
      "00c53784",
      "PARAM",
      [
        "storage",
        "00299a3f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53750",
      "READ",
      [
        "storage",
        "011288e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00c5376c",
      "PARAM",
      [
        "storage",
        "002a62f5",
        null,
        "string"
      ]
    ],
    [
      "00c53784",
      "PARAM",
      [
        "storage",
        "002a9918",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d24) · [`00bd6d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d40) · [`00bd6d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6cf8.md#insn-00bd6d70)
- 新版 `00c53774`（命令位置の公開資料なし） · `00c53790`（命令位置の公開資料なし） · `00c537c0`（命令位置の公開資料なし）

~~~diff
- 00bd6d24 ["INT_ADD", "register:40f0:8", ["const:bd6d24:8", "const:4:8"]]
- 00bd6d24 ["CALL", null, ["callee:00c5eb30:8"]]
+ 00c53774 ["INT_ADD", "register:40f0:8", ["const:c53774:8", "const:4:8"]]
+ 00c53774 ["CALL", null, ["callee:00c5eb30:8"]]
- 00bd6d24 bytes 932c0094
+ 00c53774 bytes ef2c0094
- 00bd6d40 ["INT_ADD", "register:40f0:8", ["const:bd6d40:8", "const:4:8"]]
- 00bd6d40 ["CALL", null, ["callee:00c5cd30:8"]]
+ 00c53790 ["INT_ADD", "register:40f0:8", ["const:c53790:8", "const:4:8"]]
+ 00c53790 ["CALL", null, ["callee:00c5cd30:8"]]
- 00bd6d40 bytes 3c250094
+ 00c53790 bytes 68250094
- 00bd6d70 ["INT_ADD", "register:40f0:8", ["const:bd6d70:8", "const:4:8"]]
- 00bd6d70 ["CALL", null, ["ram:bd6a4c:8"]]
+ 00c537c0 ["INT_ADD", "register:40f0:8", ["const:c537c0:8", "const:4:8"]]
+ 00c537c0 ["CALL", null, ["ram:c5349c:8"]]
- 00bd6d70 bytes 37ffff97
+ 00c537c0 bytes 37ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0cea331c911d73a4866a7c33ed4380d"></a>

### [`00bd6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6dd0.md) → [`00c53820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53820.md) FUN_00c53820

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 3件 [`00bbac20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac20.md) [`00bbac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac54.md) [`00bbac88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbac88.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00c37668`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37668.md) [`00c3769c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c3769c.md) [`00c376d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c376d0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c53828",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c53828",
      "READ",
      [
        "storage",
        "011288e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6dd0.md#insn-00bd6dd4) · [`00bd6dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6dd0.md#insn-00bd6dd8)
- 新版 `00c53824`（命令位置の公開資料なし） · `00c53828`（命令位置の公開資料なし）

~~~diff
- 00bd6dd4 ["COPY", "register:4080:8", ["const:10a3000:8"]]
+ 00c53824 ["COPY", "register:4080:8", ["const:1128000:8"]]
- 00bd6dd4 bytes 702600b0
+ 00c53824 bytes b02600b0
- 00bd6dd8 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00bd6dd8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6dd8 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00c53828 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e0:8"]]
+ 00c53828 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c53828 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6dd8 bytes 10426739
+ 00c53828 bytes 10826339
~~~


<a id="compare-11f50459a02be4db22a7d42e18b65111"></a>

### [`00bd6e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md) → [`00c53880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53880.md) FUN_00c53880

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 8件 [`00b7383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b7383c.md) [`00b73874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73874.md) [`00b739ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b739ec.md) [`00b73a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b73/00b73a24.md) [`00b7e284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7e284.md) · 呼出先 0件 
- 新版 呼出元 8件 [`00bf0444`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf0444.md) [`00bf047c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf047c.md) [`00bf05f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf05f4.md) [`00bf062c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf0/00bf062c.md) [`00bfaccc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfaccc.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c53890",
      "incomplete_value": true,
      "site": "00c53894",
      "value": [
        "LOAD",
        "4",
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
      "00c53888",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c53888",
      "READ",
      [
        "storage",
        "011288e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e34) · [`00bd6e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e38) · [`00bd6e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e30.md#insn-00bd6e3c)
- 新版 `00c53884`（命令位置の公開資料なし） · `00c53888`（命令位置の公開資料なし） · `00c5388c`（命令位置の公開資料なし）

~~~diff
- 00bd6e34 ["COPY", "register:4080:8", ["const:10a3000:8"]]
+ 00c53884 ["COPY", "register:4080:8", ["const:1128000:8"]]
- 00bd6e34 bytes 702600b0
+ 00c53884 bytes b02600b0
- 00bd6e38 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00bd6e38 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6e38 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00c53888 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e0:8"]]
+ 00c53888 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c53888 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6e38 bytes 10426739
+ 00c53888 bytes 10826339
- 00bd6e3c ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
- 00bd6e3c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c5388c ["INT_EQUAL", "tmp:0:1", ["register:4080:4", "const:0:4"]]
+ 00c5388c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd6e3c bytes 70000034
+ 00c5388c bytes 70000034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94ea3c26cd41709904548e61c8a61139"></a>

### [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) → [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) FUN_00c538e0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 1480件 [`00418394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418394.md) [`004183ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004183ec.md) [`004185a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004185a8.md) [`004186bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/004186bc.md) [`00418b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418b18.md) · 呼出先 0件 
- 新版 呼出元 1539件 [`0043ae94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae94.md) [`0043aeec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043aeec.md) [`0043b0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b0a8.md) [`0043b1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b1bc.md) [`0043b618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b618.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c538e8",
      "READ",
      [
        "storage",
        "010a39d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00c538e8",
      "READ",
      [
        "storage",
        "011288e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd6e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md#insn-00bd6e94) · [`00bd6e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md#insn-00bd6e98)
- 新版 `00c538e4`（命令位置の公開資料なし） · `00c538e8`（命令位置の公開資料なし）

~~~diff
- 00bd6e94 ["COPY", "register:4080:8", ["const:10a3000:8"]]
+ 00c538e4 ["COPY", "register:4080:8", ["const:1128000:8"]]
- 00bd6e94 bytes 702600b0
+ 00c538e4 bytes b02600b0
- 00bd6e98 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:9d0:8"]]
- 00bd6e98 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bd6e98 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
+ 00c538e8 ["INT_ADD", "tmp:0:8", ["register:4080:8", "const:8e0:8"]]
+ 00c538e8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00c538e8 ["INT_ZEXT", "register:4080:8", ["tmp:1:1"]]
- 00bd6e98 bytes 10426739
+ 00c538e8 bytes 10826339
~~~


<a id="compare-5b65cb230194e7a5f57fe52121c06f7d"></a>

### [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) → [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) FUN_00c53910

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd5234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5234.md) [`00bd5458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd5458.md) [`00bd55e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd5/00bd55e8.md) · 呼出先 6件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) [`00bd7540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7540.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md)
- 新版 呼出元 3件 [`00c51c7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51c7c.md) [`00c51ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51ea0.md) [`00c52030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c52/00c52030.md) · 呼出先 6件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) [`00c53f90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53f90.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 47.06% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f60"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c539b0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd6f9c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd6f60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c539f0"
      ]
    ],
    [
      "unmatched:00bd6f90",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd6f94",
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
      "00c539b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c539f0"
      ]
    ],
    [
      "00c539e0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00c539e4",
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

- 旧版 [`00bd6f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md#insn-00bd6f60) · [`00bd6f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md#insn-00bd6f9c)
- 新版 `00c539b0`（命令位置の公開資料なし）

~~~diff
- 00bd6f60 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd6f60 ["CBRANCH", null, ["local:b12:8", "tmp:0:1"]]
- 00bd6f60 bytes 01020054
- 00bd6f9c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00bd6f9c ["RETURN", null, ["register:0:8"]]
- 00bd6f9c bytes c0035fd6
+ 00c539b0 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00c539b0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00c539b0 bytes 01020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582339e949bcc0d017b75a0c94fee5ac"></a>

### [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) → [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) FUN_00c53a08

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) · 呼出先 9件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd73d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd73d8.md) [`00bd7554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7554.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md)
- 新版 呼出元 2件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) · 呼出先 9件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53e28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53e28.md) [`00c53fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fa4.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 88.31% / 新版 88.31%

CFGの説明率　旧版 70.00% / 新版 77.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7050"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c53aa0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53ae0",
      "incomplete_value": true,
      "site": "00c53ae4",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7090",
      "incomplete_value": true,
      "site": "00bd7094",
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
            "const:130:8"
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
      "unmatched:00bd7078",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd707c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7084",
      "PARAM",
      [
        "storage",
        "0029d2b4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53ac8",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c53acc",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c53ad4",
      "PARAM",
      [
        "storage",
        "002ad53e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md#insn-00bd7050) · [`00bd7094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md#insn-00bd7094)
- 新版 `00c53ae4`（命令位置の公開資料なし） · `00c53aa0`（命令位置の公開資料なし）

~~~diff
- 00bd7050 ["COPY", "tmp:0:4", ["register:40b0:4"]]
- 00bd7050 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00bd7050 ["COPY", "tmp:0:4", ["register:40a8:4"]]
- 00bd7050 ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
- 00bd7050 bytes c102951a
- 00bd7094 ["INT_ADD", "register:40f0:8", ["const:bd7094:8", "const:4:8"]]
- 00bd7094 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c53ae4 ["INT_ADD", "register:40f0:8", ["const:c53ae4:8", "const:4:8"]]
+ 00c53ae4 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd7094 bytes bb2b0094
+ 00c53ae4 bytes 172c0094
+ 00c53aa0 ["COPY", "tmp:0:4", ["register:40b0:4"]]
+ 00c53aa0 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00c53aa0 ["COPY", "tmp:0:4", ["register:40a8:4"]]
+ 00c53aa0 ["INT_ZEXT", "register:4008:8", ["tmp:0:4"]]
+ 00c53aa0 bytes c102951a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89268a37dfa77d35bbaebf67791c3d71"></a>

### [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) → [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) FUN_00c53b3c

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 256件 [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043e940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e940.md) [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`00455270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00455/00455270.md) · 呼出先 7件 [`00bd6fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6fb8.md) [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) [`00bdadd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdadd8.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)
- 新版 呼出元 256件 [`00461470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/00461470.md) [`004617d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00461/004617d8.md) [`00467fbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467fbc.md) [`00473500`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00473/00473500.md) [`00478108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00478/00478108.md) · 呼出先 7件 [`00c53a08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53a08.md) [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) [`00c57828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57828.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.85% / 新版 84.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53bac",
      "incomplete_value": true,
      "site": "00c53bb0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd715c",
      "incomplete_value": true,
      "site": "00bd7160",
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
            "const:130:8"
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
      "definition_site": "00c53b94",
      "incomplete_value": false,
      "site": "00c53bb0",
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
            "const:e44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7144",
      "incomplete_value": false,
      "site": "00bd7160",
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
            "const:82b:8"
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
      "definition_site": "00c53ba0",
      "incomplete_value": false,
      "site": "00c53bb0",
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
            "const:67d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7150",
      "incomplete_value": false,
      "site": "00bd7160",
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
            "const:605:8"
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
      "00c53b94",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "00c53b98",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00c53ba0",
      "PARAM",
      [
        "storage",
        "002ac605",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c53b94",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c53b98",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c53ba0",
      "PARAM",
      [
        "storage",
        "002bd67d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7160) · [`00bd7108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7108) · [`00bd7120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md#insn-00bd7120)
- 新版 `00c53bb0`（命令位置の公開資料なし） · `00c53b58`（命令位置の公開資料なし） · `00c53b70`（命令位置の公開資料なし）

~~~diff
- 00bd7160 ["INT_ADD", "register:40f0:8", ["const:bd7160:8", "const:4:8"]]
- 00bd7160 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c53bb0 ["INT_ADD", "register:40f0:8", ["const:c53bb0:8", "const:4:8"]]
+ 00c53bb0 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd7160 bytes 882b0094
+ 00c53bb0 bytes e42b0094
- 00bd7108 ["INT_ADD", "register:40f0:8", ["const:bd7108:8", "const:4:8"]]
- 00bd7108 ["CALL", null, ["callee:00c57828:8"]]
+ 00c53b58 ["INT_ADD", "register:40f0:8", ["const:c53b58:8", "const:4:8"]]
+ 00c53b58 ["CALL", null, ["callee:00c57828:8"]]
- 00bd7108 bytes 340f0094
+ 00c53b58 bytes 340f0094
- 00bd7120 ["INT_ADD", "register:40f0:8", ["const:bd7120:8", "const:4:8"]]
- 00bd7120 ["CALL", null, ["callee:00c53a08:8"]]
+ 00c53b70 ["INT_ADD", "register:40f0:8", ["const:c53b70:8", "const:4:8"]]
+ 00c53b70 ["CALL", null, ["callee:00c53a08:8"]]
- 00bd7120 bytes a6ffff97
+ 00c53b70 bytes a6ffff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8505fddb32c7b3727763b85aac0ffbbb"></a>

### [`00bd7170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md) → [`00c53bc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53bc0.md) FUN_00c53bc0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) · 呼出先 4件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) [`00bd7554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7554.md) [`00bd7568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7568.md) [`00bd75a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75a8.md)
- 新版 呼出元 1件 [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) · 呼出先 4件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) [`00c53fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fa4.md) [`00c53fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53fb8.md) [`00c53ff8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53ff8.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 76.47% / 新版 81.25%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c53c08",
      "incomplete_value": false,
      "site": "00c53c1c",
      "value": [
        "leaf",
        "const:1:8"
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
      "definition_site": "00c53c0c",
      "incomplete_value": false,
      "site": "00c53c1c",
      "value": [
        "leaf",
        "const:1a:8"
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
      "definition_site": "00c53c04",
      "incomplete_value": true,
      "site": "00c53c1c",
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
            "register:40b0:8"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 2,
    "slot": 3
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00bd71cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md#insn-00bd71cc) · [`00bd71a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md#insn-00bd71a0) · [`00bd71a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7170.md#insn-00bd71a8)
- 新版 `00c53c1c`（命令位置の公開資料なし） · `00c53bf0`（命令位置の公開資料なし） · `00c53bf8`（命令位置の公開資料なし）

~~~diff
- 00bd71cc ["COPY", "register:0:8", ["register:4098:8"]]
- 00bd71cc ["INT_ADD", "register:40f0:8", ["const:bd71cc:8", "const:4:8"]]
- 00bd71cc ["CALLIND", null, ["register:0:8"]]
+ 00c53c1c ["COPY", "register:0:8", ["register:4098:8"]]
+ 00c53c1c ["INT_ADD", "register:40f0:8", ["const:c53c1c:8", "const:4:8"]]
+ 00c53c1c ["CALLIND", null, ["register:0:8"]]
- 00bd71cc bytes 60023fd6
+ 00c53c1c bytes 60023fd6
- 00bd71a0 ["INT_ADD", "register:40f0:8", ["const:bd71a0:8", "const:4:8"]]
- 00bd71a0 ["CALL", null, ["callee:00c53d80:8"]]
+ 00c53bf0 ["INT_ADD", "register:40f0:8", ["const:c53bf0:8", "const:4:8"]]
+ 00c53bf0 ["CALL", null, ["callee:00c53d80:8"]]
- 00bd71a0 bytes 64000094
+ 00c53bf0 bytes 64000094
- 00bd71a8 ["INT_ADD", "register:40f0:8", ["const:bd71a8:8", "const:4:8"]]
- 00bd71a8 ["CALL", null, ["callee:00c53fa4:8"]]
+ 00c53bf8 ["INT_ADD", "register:40f0:8", ["const:c53bf8:8", "const:4:8"]]
+ 00c53bf8 ["CALL", null, ["callee:00c53fa4:8"]]
- 00bd71a8 bytes eb000094
+ 00c53bf8 bytes eb000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61eed5150755222d3749e066d0547487"></a>

### [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) → [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) FUN_00c54020

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 3件 [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md)
- 新版 呼出元 3件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 呼出先 3件 [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 83.00% / 新版 83.00%

CFGの説明率　旧版 60.00% / 新版 69.23%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd75d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd75d4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd75d8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd75d4",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd75d8",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd75dc",
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
      "00c54024",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c54028",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c5402c",
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

- 旧版 [`00bd75d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md#insn-00bd75d4) · [`00bd75d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md#insn-00bd75d8) · [`00bd75dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md#insn-00bd75dc)

~~~diff
- 00bd75d4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bd75d4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bd75d4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffa0:8"]]
- 00bd75d4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00bd75d4 bytes fd7bbaa9
- 00bd75d8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00bd75d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00bd75d8 bytes fb0b00f9
- 00bd75dc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bd75dc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bd75dc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00bd75dc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd75dc bytes fa6702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b81a7bde450bb99c383b2f1517db9ad1"></a>

### [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) → [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) FUN_00c541b0

採用 · 移動量 `+0x7ca50` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) · 呼出先 6件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md)
- 新版 呼出元 2件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) · 呼出先 6件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 93.26% / 新版 93.26%

CFGの説明率　旧版 53.62% / 新版 61.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 4件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7878"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd796c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c542c8"
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
      "00c54214",
      "DATA",
      [
        "storage",
        "002ac658",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7878",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c542f8"
      ]
    ],
    [
      "00c542f0",
      "DATA",
      [
        "storage",
        "0029450c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54214",
      "DATA",
      [
        "storage",
        "002bd6d0",
        null,
        "string"
      ]
    ],
    [
      "00c542c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c542f8"
      ]
    ],
    [
      "00c542f0",
      "DATA",
      [
        "storage",
        "002a3e22",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md#insn-00bd7878) · [`00bd78b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md#insn-00bd78b0) · [`00bd796c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md#insn-00bd796c)
- 新版 `00c54300`（命令位置の公開資料なし）

~~~diff
- 00bd7878 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd7878 ["CBRANCH", null, ["local:b19:8", "tmp:0:1"]]
- 00bd7878 bytes 81010054
- 00bd78b0 ["INT_ADD", "register:40f0:8", ["const:bd78b0:8", "const:4:8"]]
- 00bd78b0 ["CALL", null, ["callee:00c5628c:8"]]
+ 00c54300 ["INT_ADD", "register:40f0:8", ["const:c54300:8", "const:4:8"]]
+ 00c54300 ["CALL", null, ["callee:00c5628c:8"]]
- 00bd78b0 bytes e3070094
+ 00c54300 bytes e3070094
- 00bd796c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd796c ["CBRANCH", null, ["local:b44:8", "tmp:0:1"]]
- 00bd796c bytes a1020054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df7568cc29e157caa369d3baa3d704f"></a>

### [`00bd7a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7a7c.md) → [`00c544cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c544cc.md) FUN_00c544cc

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 84.48% / 新版 84.48%

CFGの説明率　旧版 66.67% / 新版 76.19%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd7aa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c544f8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c545a0",
      "incomplete_value": true,
      "site": "00c545a4",
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
            "const:130:8"
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
      "unmatched:00bd7aa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54534"
      ]
    ],
    [
      "unmatched:00bd7b38",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7b3c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c544f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54534"
      ]
    ],
    [
      "00c54588",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c5458c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7a7c.md#insn-00bd7aa8) · [`00bd7b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7a7c.md#insn-00bd7b54)
- 新版 `00c545a4`（命令位置の公開資料なし） · `00c544f8`（命令位置の公開資料なし）

~~~diff
- 00bd7aa8 ["CBRANCH", null, ["local:b13:8", "register:101:1"]]
- 00bd7aa8 bytes e0010054
- 00bd7b54 ["INT_ADD", "register:40f0:8", ["const:bd7b54:8", "const:4:8"]]
- 00bd7b54 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c545a4 ["INT_ADD", "register:40f0:8", ["const:c545a4:8", "const:4:8"]]
+ 00c545a4 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd7b54 bytes 0b290094
+ 00c545a4 bytes 67290094
+ 00c544f8 ["CBRANCH", null, ["local:b12:8", "register:101:1"]]
+ 00c544f8 bytes e0010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a82976efe3e5be8b4cb31f7aef3a50d3"></a>

### [`00bd7b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md) → [`00c545b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c545b4.md) FUN_00c545b4

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.93% / 新版 87.93%

CFGの説明率　旧版 90.91% / 新版 95.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54688",
      "incomplete_value": true,
      "site": "00c5468c",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c38",
      "incomplete_value": true,
      "site": "00bd7c3c",
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
            "const:130:8"
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
      "definition_site": "00c54670",
      "incomplete_value": false,
      "site": "00c5468c",
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
            "const:e44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c20",
      "incomplete_value": false,
      "site": "00bd7c3c",
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
            "const:82b:8"
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
      "definition_site": "00c5467c",
      "incomplete_value": false,
      "site": "00c5468c",
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
            "const:d97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7c2c",
      "incomplete_value": false,
      "site": "00bd7c3c",
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
            "const:369:8"
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
      "unmatched:00bd7c20",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd7c24",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd7c2c",
      "PARAM",
      [
        "storage",
        "002a5369",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c54670",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c54674",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c5467c",
      "PARAM",
      [
        "storage",
        "002b5d97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7c3c) · [`00bd7c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7c18) · [`00bd7c1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7b64.md#insn-00bd7c1c)
- 新版 `00c5468c`（命令位置の公開資料なし） · `00c54668`（命令位置の公開資料なし） · `00c5466c`（命令位置の公開資料なし）

~~~diff
- 00bd7c3c ["INT_ADD", "register:40f0:8", ["const:bd7c3c:8", "const:4:8"]]
- 00bd7c3c ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c5468c ["INT_ADD", "register:40f0:8", ["const:c5468c:8", "const:4:8"]]
+ 00c5468c ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd7c3c bytes d1280094
+ 00c5468c bytes 2d290094
- 00bd7c18 ["COPY", "register:4098:8", ["const:c1b000:8"]]
+ 00c54668 ["COPY", "register:4098:8", ["const:c9b000:8"]]
- 00bd7c18 bytes 33020090
+ 00c54668 bytes 330200f0
- 00bd7c1c ["COPY", "register:4008:8", ["const:291000:8"]]
+ 00c5466c ["COPY", "register:4008:8", ["const:2a0000:8"]]
- 00bd7c1c bytes c1b5ffd0
+ 00c5466c bytes 61b2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e74305817d261dc1089752f628d1756e"></a>

### [`00bd7c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md) → [`00c546d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md) FUN_00c546d0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8040.md) [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54a90.md) [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 54.55% / 新版 60.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md#insn-00bd7cc4) · [`00bd7cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md#insn-00bd7cd0) · [`00bd7d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md#insn-00bd7d08)
- 新版 `00c54714`（命令位置の公開資料なし） · `00c54720`（命令位置の公開資料なし） · `00c54758`（命令位置の公開資料なし）

~~~diff
- 00bd7cc4 ["INT_ADD", "register:40f0:8", ["const:bd7cc4:8", "const:4:8"]]
- 00bd7cc4 ["CALL", null, ["callee:00c57c90:8"]]
+ 00c54714 ["INT_ADD", "register:40f0:8", ["const:c54714:8", "const:4:8"]]
+ 00c54714 ["CALL", null, ["callee:00c57c90:8"]]
- 00bd7cc4 bytes 5f0d0094
+ 00c54714 bytes 5f0d0094
- 00bd7cd0 ["INT_ADD", "register:40f0:8", ["const:bd7cd0:8", "const:4:8"]]
- 00bd7cd0 ["CALL", null, ["callee:00c54a90:8"]]
+ 00c54720 ["INT_ADD", "register:40f0:8", ["const:c54720:8", "const:4:8"]]
+ 00c54720 ["CALL", null, ["callee:00c54a90:8"]]
- 00bd7cd0 bytes dc000094
+ 00c54720 bytes dc000094
- 00bd7d08 ["COPY", "register:0:8", ["register:4040:8"]]
- 00bd7d08 ["INT_ADD", "register:40f0:8", ["const:bd7d08:8", "const:4:8"]]
- 00bd7d08 ["CALLIND", null, ["register:0:8"]]
+ 00c54758 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00c54758 ["INT_ADD", "register:40f0:8", ["const:c54758:8", "const:4:8"]]
+ 00c54758 ["CALLIND", null, ["register:0:8"]]
- 00bd7d08 bytes 00013fd6
+ 00c54758 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa64be8ee8bad9747a574e0ecc6bf0d9"></a>

### [`00bd7d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7d70.md) → [`00c547c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c547c0.md) FUN_00c547c0

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, cfg_edge_inventory, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00bd7d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7d70.md#insn-00bd7d78)
- 新版 `00c547c8`（命令位置の公開資料なし）

~~~diff
- 00bd7d78 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00bd7d78 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00c547c8 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00c547c8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00bd7d78 bytes c8000034
+ 00c547c8 bytes c8000034
~~~


<a id="compare-71ee3afce8fe84c217ccb88f4f1cd5e3"></a>

### [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) → [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) FUN_00c54848

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7330.md) · 呼出先 10件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) [`00bda69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c53d80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53d80.md) · 呼出先 10件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 75.68% / 新版 82.35%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c54898",
      "incomplete_value": false,
      "site": "00c548a8",
      "value": [
        "leaf",
        "const:c570ec:8"
      ]
    },
    "old": {
      "definition_site": "00bd7e48",
      "incomplete_value": false,
      "site": "00bd7e58",
      "value": [
        "leaf",
        "const:bda69c:8"
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c548d4",
      "incomplete_value": false,
      "site": "00c548d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7e84",
      "incomplete_value": false,
      "site": "00bd7e88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9e4:8"
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
      "definition_site": "00c5491c",
      "incomplete_value": false,
      "site": "00c54920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:1128000:8"
          ],
          [
            "leaf",
            "const:8f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd7ecc",
      "incomplete_value": false,
      "site": "00bd7ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:9e4:8"
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
      "00c54898",
      "PARAM",
      [
        "storage",
        "00bda69c",
        null,
        null
      ]
    ],
    [
      "00c548d4",
      "PARAM",
      [
        "storage",
        "010a39e4",
        null,
        null
      ]
    ],
    [
      "00c548e4",
      "READ",
      [
        "storage",
        "00c249c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c54898",
      "PARAM",
      [
        "storage",
        "00c570ec",
        null,
        null
      ]
    ],
    [
      "00c548d4",
      "PARAM",
      [
        "storage",
        "011288f4",
        null,
        null
      ]
    ],
    [
      "00c548e4",
      "READ",
      [
        "storage",
        "00ca44a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd7e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7e58) · [`00bd7e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7e88) · [`00bd7ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md#insn-00bd7ed0)
- 新版 `00c548a8`（命令位置の公開資料なし） · `00c548d8`（命令位置の公開資料なし） · `00c54920`（命令位置の公開資料なし）

~~~diff
- 00bd7e58 ["INT_ADD", "register:40f0:8", ["const:bd7e58:8", "const:4:8"]]
- 00bd7e58 ["CALL", null, ["callee:00c5eb70:8"]]
+ 00c548a8 ["INT_ADD", "register:40f0:8", ["const:c548a8:8", "const:4:8"]]
+ 00c548a8 ["CALL", null, ["callee:00c5eb70:8"]]
- 00bd7e58 bytes 56280094
+ 00c548a8 bytes b2280094
- 00bd7e88 ["INT_ADD", "register:40f0:8", ["const:bd7e88:8", "const:4:8"]]
- 00bd7e88 ["CALL", null, ["callee:00c5eb80:8"]]
+ 00c548d8 ["INT_ADD", "register:40f0:8", ["const:c548d8:8", "const:4:8"]]
+ 00c548d8 ["CALL", null, ["callee:00c5eb80:8"]]
- 00bd7e88 bytes 4e280094
+ 00c548d8 bytes aa280094
- 00bd7ed0 ["INT_ADD", "register:40f0:8", ["const:bd7ed0:8", "const:4:8"]]
- 00bd7ed0 ["CALL", null, ["callee:00c5eb60:8"]]
+ 00c54920 ["INT_ADD", "register:40f0:8", ["const:c54920:8", "const:4:8"]]
+ 00c54920 ["CALL", null, ["callee:00c5eb60:8"]]
- 00bd7ed0 bytes 34280094
+ 00c54920 bytes 90280094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08f271916710ea7a810930a2f2f7c61a"></a>

### [`00bd8040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8040.md) → [`00c54a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54a90.md) FUN_00c54a90

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00bd7c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c546d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 8.33% / 新版 8.33%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-2f618f650697a87f1788744195347147"></a>

### [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) → [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) FUN_00c54bb0

採用 · 移動量 `+0x7ca50` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7c80.md) · 呼出先 11件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) [`00bd92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md) [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md)
- 新版 呼出元 1件 [`00c546d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c546d0.md) · 呼出先 11件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 87.37% / 新版 87.37%

CFGの説明率　旧版 62.73% / 新版 71.13%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8474"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c54ec4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8340"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8340",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54e84"
      ]
    ],
    [
      "unmatched:00bd83c4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54e38"
      ]
    ],
    [
      "00c54ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd858c"
      ]
    ]
  ],
  "added": [
    [
      "00c54d90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54e84"
      ]
    ],
    [
      "00c54e14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54e38"
      ]
    ],
    [
      "00c54ea0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c54fdc"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd81ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md#insn-00bd81ac) · [`00bd8340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md#insn-00bd8340) · [`00bd83c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md#insn-00bd83c4)
- 新版 `00c54bfc`（命令位置の公開資料なし）

~~~diff
- 00bd81ac ["INT_ADD", "register:40f0:8", ["const:bd81ac:8", "const:4:8"]]
- 00bd81ac ["CALL", null, ["callee:00c54020:8"]]
+ 00c54bfc ["INT_ADD", "register:40f0:8", ["const:c54bfc:8", "const:4:8"]]
+ 00c54bfc ["CALL", null, ["callee:00c54020:8"]]
- 00bd81ac bytes 09fdff97
+ 00c54bfc bytes 09fdff97
- 00bd8340 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00bd8340 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00bd8340 ["CBRANCH", null, ["local:b44:8", "tmp:1:1"]]
- 00bd8340 bytes ad070054
- 00bd83c4 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd83c4 ["CBRANCH", null, ["local:b37:8", "tmp:0:1"]]
- 00bd83c4 bytes 21010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4b96f472f56675bf9b4707faa2af0e"></a>

### [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) → [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) FUN_00c55044

採用 · 移動量 `+0x7ca50` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) · 呼出先 8件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bdd3d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd3d0.md)
- 新版 呼出元 3件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 8件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c59e20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59e20.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 60.08% / 新版 60.08%

CFGの説明率　旧版 28.72% / 新版 34.62%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_condition` 2件, `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 23件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8644"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd8650"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bd8644",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8650",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bd8654",
      "WRITE",
      [
        "storage",
        "Stack[-0x6cc]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c55094",
      "WRITE",
      [
        "storage",
        "Stack[-0x98]",
        null,
        null
      ]
    ],
    [
      "00c550a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x88]",
        null,
        null
      ]
    ],
    [
      "00c550a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x6cc]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd8644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md#insn-00bd8644) · [`00bd8650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md#insn-00bd8650) · [`00bd8654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md#insn-00bd8654)

~~~diff
- 00bd8644 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd8644 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00bd8644 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00bd8644 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8644 bytes a8a73ca9
- 00bd8650 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00bd8650 ["COPY", "tmp:1:8", ["register:4058:8"]]
- 00bd8650 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00bd8650 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bd8650 bytes a8af3da9
- 00bd8654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:24:8"]]
- 00bd8654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4020:4"]]
- 00bd8654 bytes 642600b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-999e54c4c13216628efafbc48830334b"></a>

### [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) → [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) FUN_00c55bbc

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) · 呼出先 5件 [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) · 呼出先 5件 [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.61% / 新版 89.61%

CFGの説明率　旧版 82.14% / 新版 92.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c55cdc",
      "incomplete_value": true,
      "site": "00c55ce0",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd928c",
      "incomplete_value": true,
      "site": "00bd9290",
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
            "const:130:8"
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
      "definition_site": "00c55cc4",
      "incomplete_value": false,
      "site": "00c55ce0",
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
            "const:e44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9274",
      "incomplete_value": false,
      "site": "00bd9290",
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
            "const:82b:8"
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
      "definition_site": "00c55cd0",
      "incomplete_value": false,
      "site": "00c55ce0",
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
            "const:74a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bd9280",
      "incomplete_value": false,
      "site": "00bd9290",
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
            "const:337:8"
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
      "unmatched:00bd9274",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00bd9278",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00bd9280",
      "PARAM",
      [
        "storage",
        "0029f337",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c55cc4",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c55cc8",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c55cd0",
      "PARAM",
      [
        "storage",
        "002af74a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md#insn-00bd9290) · [`00bd9298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md#insn-00bd9298) · [`00bd9190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md#insn-00bd9190)
- 新版 `00c55ce0`（命令位置の公開資料なし） · `00c55ce8`（命令位置の公開資料なし） · `00c55be0`（命令位置の公開資料なし）

~~~diff
- 00bd9290 ["INT_ADD", "register:40f0:8", ["const:bd9290:8", "const:4:8"]]
- 00bd9290 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c55ce0 ["INT_ADD", "register:40f0:8", ["const:c55ce0:8", "const:4:8"]]
+ 00c55ce0 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd9290 bytes 3c230094
+ 00c55ce0 bytes 98230094
- 00bd9298 ["INT_ADD", "register:40f0:8", ["const:bd9298:8", "const:4:8"]]
- 00bd9298 ["CALL", null, ["callee:00c59db0:8"]]
+ 00c55ce8 ["INT_ADD", "register:40f0:8", ["const:c55ce8:8", "const:4:8"]]
+ 00c55ce8 ["CALL", null, ["callee:00c59db0:8"]]
- 00bd9298 bytes 32100094
+ 00c55ce8 bytes 32100094
- 00bd9190 ["BRANCH", null, ["local:b19:8"]]
+ 00c55be0 ["BRANCH", null, ["local:b18:8"]]
- 00bd9190 bytes 2c000014
+ 00c55be0 bytes 2c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45299932f060ae92928ec38ed37f653b"></a>

### [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) → [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) FUN_00c55f00

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) · 呼出先 5件 [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) · 呼出先 5件 [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 75.77% / 新版 75.77%

CFGの説明率　旧版 71.05% / 新版 78.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd94fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9570"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c55f4c"
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
      "00c55f44",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9808"
      ]
    ],
    [
      "unmatched:00bd94fc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55f8c"
      ]
    ],
    [
      "00c55f58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bd9808"
      ]
    ]
  ],
  "added": [
    [
      "00c55f44",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00c56258"
      ]
    ],
    [
      "00c55f4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c55f8c"
      ]
    ],
    [
      "00c55f58",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c56258"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd94fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md#insn-00bd94fc) · [`00bd9570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md#insn-00bd9570) · [`00bd96dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md#insn-00bd96dc)

~~~diff
- 00bd94fc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd94fc ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00bd94fc ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00bd94fc ["CBRANCH", null, ["local:b12:8", "tmp:2:1"]]
- 00bd94fc bytes 0c020054
- 00bd9570 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00bd9570 bytes 60040054
- 00bd96dc ["INT_ADD", "register:40f0:8", ["const:bd96dc:8", "const:4:8"]]
- 00bd96dc ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd96dc bytes 29220094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c986eea2672f93870ec1ac6c73337079"></a>

### [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) → [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) FUN_00c5628c

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 6件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 50.00% / 新版 56.82%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd98f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c562f0"
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
      "unmatched:00bd98a0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c563ec"
      ]
    ],
    [
      "unmatched:00bd98f4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c563ec"
      ]
    ],
    [
      "unmatched:00bd99a4",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00c562f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c563ec"
      ]
    ],
    [
      "00c56344",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c563ec"
      ]
    ],
    [
      "00c563f4",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd98a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md#insn-00bd98a0) · [`00bd98f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md#insn-00bd98f4) · [`00bd99c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md#insn-00bd99c0)

~~~diff
- 00bd98a0 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00bd98a0 bytes e0070054
- 00bd98f4 ["CBRANCH", null, ["local:b27:8", "register:101:1"]]
- 00bd98f4 bytes 40050054
- 00bd99c0 ["INT_ADD", "register:40f0:8", ["const:bd99c0:8", "const:4:8"]]
- 00bd99c0 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bd99c0 bytes 70210094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df0bfe5fe4a5ce581e95809f56b325ee"></a>

### [`00bd9a04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md) → [`00c56454`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56454.md) FUN_00c56454

採用 · 移動量 `+0x7ca50` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00bd8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd8160.md) [`00bd916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd916c.md) [`00bd92a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd92a0.md) · 呼出先 5件 [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 3件 [`00c54bb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54bb0.md) [`00c55bbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55bbc.md) [`00c55cf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55cf0.md) · 呼出先 5件 [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 71.20% / 新版 71.20%

CFGの説明率　旧版 49.40% / 新版 56.68%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_branch_alignment` 18件, `unresolved_call_alignment` 24件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9f00"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bd9f80"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00c56950"
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
      "00c564f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bda284"
      ]
    ],
    [
      "00c56500",
      "DATA",
      [
        "storage",
        "002fdff8",
        "switchD_00bd9ab8::switchdataD_002fdff8",
        "ushort"
      ]
    ],
    [
      "00c56508",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "unmatched:00bda284"
      ]
    ]
  ],
  "added": [
    [
      "00c564f8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c56cd4"
      ]
    ],
    [
      "00c56500",
      "DATA",
      [
        "storage",
        "00313e30",
        "switchD_00c56508::switchdataD_00313e30",
        "ushort"
      ]
    ],
    [
      "00c56508",
      "COMPUTED_JUMP",
      [
        "local_branch",
        "00c56cd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bd9b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md#insn-00bd9b18) · [`00bd9b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md#insn-00bd9b1c) · [`00bd9b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd9a04.md#insn-00bd9b64)

~~~diff
- 00bd9b18 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bd9b18 ["COPY", "tmp:1:1", ["tmp:0:1"]]
- 00bd9b18 ["COPY", "tmp:2:1", ["const:0:1"]]
- 00bd9b18 ["INT_AND", "tmp:3:1", ["tmp:2:1", "const:8:1"]]
- 00bd9b18 bytes c0314d7a
- 00bd9b1c ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bd9b1c ["BOOL_AND", "tmp:1:1", ["register:102:1", "tmp:0:1"]]
- 00bd9b1c ["COPY", "tmp:2:8", ["register:4060:8"]]
- 00bd9b1c ["CBRANCH", null, ["const:2:4", "tmp:1:1"]]
- 00bd9b1c bytes 8c819f9a
- 00bd9b64 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
- 00bd9b64 bytes e0f8ff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c2e0eb55c005eadc7dbd734225e470a"></a>

### [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) → [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) FUN_00c56e18

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bd7df8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7df8.md) · 呼出先 10件 [`00bd85f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd8/00bd85f4.md) [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)
- 新版 呼出元 1件 [`00c54848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54848.md) · 呼出先 10件 [`00c55044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55044.md) [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md) [`00c57c90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c90.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 79.56% / 新版 79.56%

CFGの説明率　旧版 36.67% / 新版 43.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件, `store_destination` 2件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c57090",
      "incomplete_value": true,
      "site": "00c57090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda640",
      "incomplete_value": true,
      "site": "00bda640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00c57094",
      "incomplete_value": true,
      "site": "00c57094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:4b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda644",
      "incomplete_value": true,
      "site": "00bda644",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bda64c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c56e9c",
      "PARAM",
      [
        "storage",
        "010a39e4",
        null,
        null
      ]
    ],
    [
      "00c56eac",
      "READ",
      [
        "storage",
        "00c249c8",
        null,
        "pointer"
      ]
    ],
    [
      "00c56eb0",
      "READ",
      [
        "storage",
        "00c249d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c56e9c",
      "PARAM",
      [
        "storage",
        "011288f4",
        null,
        null
      ]
    ],
    [
      "00c56eac",
      "READ",
      [
        "storage",
        "00ca44a8",
        null,
        "pointer"
      ]
    ],
    [
      "00c56eb0",
      "READ",
      [
        "storage",
        "00ca44b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md#insn-00bda43c) · [`00bda450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md#insn-00bda450) · [`00bda468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md#insn-00bda468)
- 新版 `00c56e8c`（命令位置の公開資料なし） · `00c56ea0`（命令位置の公開資料なし） · `00c56eb8`（命令位置の公開資料なし）

~~~diff
- 00bda43c ["INT_ADD", "register:40f0:8", ["const:bda43c:8", "const:4:8"]]
- 00bda43c ["CALL", null, ["callee:00c57504:8"]]
+ 00c56e8c ["INT_ADD", "register:40f0:8", ["const:c56e8c:8", "const:4:8"]]
+ 00c56e8c ["CALL", null, ["callee:00c57504:8"]]
- 00bda43c bytes 9e010094
+ 00c56e8c bytes 9e010094
- 00bda450 ["INT_ADD", "register:40f0:8", ["const:bda450:8", "const:4:8"]]
- 00bda450 ["CALL", null, ["callee:00c5eb80:8"]]
+ 00c56ea0 ["INT_ADD", "register:40f0:8", ["const:c56ea0:8", "const:4:8"]]
+ 00c56ea0 ["CALL", null, ["callee:00c5eb80:8"]]
- 00bda450 bytes dc1e0094
+ 00c56ea0 bytes 381f0094
- 00bda468 ["CBRANCH", null, ["local:b22:8", "register:102:1"]]
+ 00c56eb8 ["CBRANCH", null, ["local:b18:8", "register:102:1"]]
- 00bda468 bytes 22050054
+ 00c56eb8 bytes 22050054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87430ec9c42cbe6d335a8dad7add0e9b"></a>

### [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md) → [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) FUN_00c5721c

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `cfg_change`

- 旧版 呼出元 2件 [`00bda69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda69c.md) [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 4件 [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 2件 [`00c570ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c570ec.md) [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 呼出先 4件 [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 71.43% / 新版 76.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57264",
      "incomplete_value": true,
      "site": "00c57268",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda814",
      "incomplete_value": true,
      "site": "00bda818",
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
            "const:130:8"
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
      "definition_site": "00c57258",
      "incomplete_value": false,
      "site": "00c57268",
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
            "const:af1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bda808",
      "incomplete_value": false,
      "site": "00bda818",
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
            "const:284:8"
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
      "definition_site": "00c57284",
      "incomplete_value": true,
      "site": "00c572a4",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "1",
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
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00c57258",
      "PARAM",
      [
        "storage",
        "002a4284",
        null,
        "string"
      ]
    ],
    [
      "00c5725c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00c57264",
      "PARAM",
      [
        "storage",
        "010a58b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00c57258",
      "PARAM",
      [
        "storage",
        "002b4af1",
        null,
        "string"
      ]
    ],
    [
      "00c5725c",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ],
    [
      "00c57264",
      "PARAM",
      [
        "storage",
        "0112a8f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md#insn-00bda818) · [`00bda854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md#insn-00bda854) · [`00bda89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md#insn-00bda89c)
- 新版 `00c57268`（命令位置の公開資料なし） · `00c572a4`（命令位置の公開資料なし） · `00c572ec`（命令位置の公開資料なし）

~~~diff
- 00bda818 ["INT_ADD", "register:40f0:8", ["const:bda818:8", "const:4:8"]]
- 00bda818 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c57268 ["INT_ADD", "register:40f0:8", ["const:c57268:8", "const:4:8"]]
+ 00c57268 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bda818 bytes da1d0094
+ 00c57268 bytes 361e0094
- 00bda854 ["INT_ADD", "register:40f0:8", ["const:bda854:8", "const:4:8"]]
- 00bda854 ["CALL", null, ["callee:00c55f00:8"]]
+ 00c572a4 ["INT_ADD", "register:40f0:8", ["const:c572a4:8", "const:4:8"]]
+ 00c572a4 ["CALL", null, ["callee:00c55f00:8"]]
- 00bda854 bytes 17fbff97
+ 00c572a4 bytes 17fbff97
- 00bda89c ["INT_ADD", "register:40f0:8", ["const:bda89c:8", "const:4:8"]]
- 00bda89c ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c572ec ["INT_ADD", "register:40f0:8", ["const:c572ec:8", "const:4:8"]]
+ 00c572ec ["CALL", null, ["callee:00c5eb40:8"]]
- 00bda89c bytes b91d0094
+ 00c572ec bytes 151e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef19e2f9dc44f65a0d279979947550a"></a>

### [`00bda8ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md) → [`00c5733c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5733c.md) FUN_00c5733c

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) · 呼出先 3件 [`00bd7760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd7760.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bd983c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd983c.md)
- 新版 呼出元 1件 [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 3件 [`00c541b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c541b0.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5628c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c5628c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment

命令の説明率　旧版 99.12% / 新版 99.12%

CFGの説明率　旧版 71.43% / 新版 78.12%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_condition` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaa00"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c57450"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c5742c",
      "incomplete_value": true,
      "site": "00c5743c",
      "value": [
        "live",
        "register:40a0:8"
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
      "unmatched:00bdaa00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c57398"
      ]
    ]
  ],
  "added": [
    [
      "00c57450",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c57398"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bda9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md#insn-00bda9ec) · [`00bdaa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda8ec.md#insn-00bdaa00)
- 新版 `00c5743c`（命令位置の公開資料なし） · `00c57450`（命令位置の公開資料なし）

~~~diff
- 00bda9ec ["INT_ADD", "register:40f0:8", ["const:bda9ec:8", "const:4:8"]]
- 00bda9ec ["CALL", null, ["callee:00c55f00:8"]]
+ 00c5743c ["INT_ADD", "register:40f0:8", ["const:c5743c:8", "const:4:8"]]
+ 00c5743c ["CALL", null, ["callee:00c55f00:8"]]
- 00bda9ec bytes b1faff97
+ 00c5743c bytes b1faff97
- 00bdaa00 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00bdaa00 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00bdaa00 bytes 43faff54
+ 00c57450 ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
+ 00c57450 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00c57450 bytes 43faff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b6e1bdf141caa82b73acbaa3aa310b"></a>

### [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) → [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) FUN_00c57504

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bda3c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda3c8.md) · 呼出先 4件 [`00bd75d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd75d0.md) [`00bd94b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd9/00bd94b0.md) [`00bda7cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bda7cc.md) [`00bdac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md)
- 新版 呼出元 1件 [`00c56e18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c56/00c56e18.md) · 呼出先 4件 [`00c54020`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c54/00c54020.md) [`00c55f00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c55/00c55f00.md) [`00c5721c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5721c.md) [`00c5766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 34.78% / 新版 42.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaabc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdaac0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bdaabc",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdaac0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00bdaac4",
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
      "00c5750c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00c57510",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00c57514",
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

- 旧版 [`00bdaabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md#insn-00bdaabc) · [`00bdaac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md#insn-00bdaac0) · [`00bdaac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md#insn-00bdaac4)

~~~diff
- 00bdaabc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00bdaabc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00bdaabc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00bdaabc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdaabc bytes fd7b04a9
- 00bdaac0 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00bdaac0 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00bdaac0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00bdaac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdaac0 bytes fc6f05a9
- 00bdaac4 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00bdaac4 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00bdaac4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00bdaac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00bdaac4 bytes fa6706a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e4fa1f75c379843bb34893611bc8578"></a>

### [`00bdac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md) → [`00c5766c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md) FUN_00c5766c

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bdaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdaab4.md) · 呼出先 4件 [`00bdd360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd360.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md) [`00be1f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1f80.md) [`010a58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a58b8.md)
- 新版 呼出元 1件 [`00c57504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57504.md) · 呼出先 4件 [`00c59db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59db0.md) [`00c5ad40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5ad40.md) [`00c5eb40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5e/00c5eb40.md) [`0112a8f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0112a/0112a8f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 73.02% / 新版 73.02%

CFGの説明率　旧版 66.67% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00bdac38"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00c57688"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c57714",
      "incomplete_value": true,
      "site": "00c57718",
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
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bdacc4",
      "incomplete_value": true,
      "site": "00bdacc8",
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
            "const:130:8"
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
      "unmatched:00bdac38",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c576a8"
      ]
    ],
    [
      "00c576fc",
      "PARAM",
      [
        "storage",
        "0029182b",
        null,
        "string"
      ]
    ],
    [
      "00c57700",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00c57688",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00c576a8"
      ]
    ],
    [
      "00c576fc",
      "PARAM",
      [
        "storage",
        "002a0e44",
        null,
        "string"
      ]
    ],
    [
      "00c57700",
      "READ",
      [
        "storage",
        "00c9b778",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bdac38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md#insn-00bdac38) · [`00bdacc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md#insn-00bdacc8) · [`00bdad08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md#insn-00bdad08)
- 新版 `00c57718`（命令位置の公開資料なし）

~~~diff
- 00bdac38 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00bdac38 ["INT_EQUAL", "tmp:1:1", ["register:100:1", "register:103:1"]]
- 00bdac38 ["BOOL_AND", "tmp:2:1", ["tmp:0:1", "tmp:1:1"]]
- 00bdac38 ["CBRANCH", null, ["local:b6:8", "tmp:2:1"]]
- 00bdac38 bytes 0c010054
- 00bdacc8 ["INT_ADD", "register:40f0:8", ["const:bdacc8:8", "const:4:8"]]
- 00bdacc8 ["CALL", null, ["callee:00c5eb40:8"]]
+ 00c57718 ["INT_ADD", "register:40f0:8", ["const:c57718:8", "const:4:8"]]
+ 00c57718 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bdacc8 bytes ae1c0094
+ 00c57718 bytes 0a1d0094
- 00bdad08 ["INT_ADD", "register:40f0:8", ["const:bdad08:8", "const:4:8"]]
- 00bdad08 ["CALL", null, ["callee:00c5eb40:8"]]
- 00bdad08 bytes 9e1c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0607eded5b72e4101f2d7dabda4afbc8"></a>

### [`00bdadd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdadd8.md) → [`00c57828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57828.md) FUN_00c57828

採用 · 移動量 `+0x7ca50` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`00bd6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6ec0.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00c53910`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53910.md) [`00c53b3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c53b3c.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

