# v15.7.3 → v15.7.4 · 最優先の変更候補 (58)

[一覧の目次](README.md)

<a id="compare-cdef971abb68cdb3b9805aa55afe6cea"></a>

### [`00a93728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93728.md) → [`00a9376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a9376c.md) FUN_00a9376c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`005bc280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc280.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`005bc280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc280.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a93738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93728.md#insn-00a93738)
- 新版 `00a9377c`（命令位置の公開資料なし）

~~~diff
- 00a93738 ["INT_ADD", "register:40f0:8", ["const:a93738:8", "const:4:8"]]
- 00a93738 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9377c ["INT_ADD", "register:40f0:8", ["const:a9377c:8", "const:4:8"]]
+ 00a9377c ["CALL", null, ["callee:0081f580:8"]]
- 00a93738 bytes 922ff697
+ 00a9377c bytes 812ff697
~~~


<a id="compare-197eb3079b345d82c94d58af1da09662"></a>

### [`00a93b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b24.md) → [`00a93b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93b68.md) FUN_00a93b68

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) · 呼出先 1件 [`00a99420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99420.md)
- 新版 呼出元 1件 [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) · 呼出先 1件 [`00a99464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99464.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a93b28",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a99464"
      ]
    ]
  ],
  "added": [
    [
      "00a93b6c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00a99464"
      ]
    ]
  ]
}
~~~


<a id="compare-a17fcb6dc3bb83ecc993fbc857ef1762"></a>

### [`00a93b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b78.md) → [`00a93bbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a93/00a93bbc.md) _INIT_242

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 81.36% / 新版 81.36%

CFGの説明率　旧版 22.73% / 新版 20.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 14件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93ba8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93bf4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a93c14"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a93ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a93bb4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a93c1c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a93bec",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00a93bf8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a93c1c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a93ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b78.md#insn-00a93ba8) · [`00a93bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b78.md#insn-00a93bf4)
- 新版 `00a93bec`（命令位置の公開資料なし）

~~~diff
- 00a93ba8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a93ba8 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00a93ba8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00a93ba8 bytes a9831ff8
+ 00a93bec ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00a93bec ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
+ 00a93bec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
+ 00a93bec bytes a9831ff8
- 00a93bf4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:31:8"]]
- 00a93bf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00a93bf4 bytes e013833c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc3c02506fa54500d978fe9d41b2b4c6"></a>

### [`00a96aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96aa8.md) → [`00a96aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96aec.md) FUN_00a96aec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a96b10",
      "incomplete_value": true,
      "site": "00a96b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a96acc",
      "incomplete_value": true,
      "site": "00a96ad0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a96ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96aa8.md#insn-00a96ad0) · [`00a96abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96aa8.md#insn-00a96abc) · [`00a96acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96aa8.md#insn-00a96acc)
- 新版 `00a96b14`（命令位置の公開資料なし） · `00a96b00`（命令位置の公開資料なし）

~~~diff
- 00a96ad0 ["INT_ADD", "register:40f0:8", ["const:a96ad0:8", "const:4:8"]]
- 00a96ad0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96b14 ["INT_ADD", "register:40f0:8", ["const:a96b14:8", "const:4:8"]]
+ 00a96b14 ["CALL", null, ["callee:005c2710:8"]]
- 00a96ad0 bytes 10afec97
+ 00a96b14 bytes ffaeec97
- 00a96abc ["INT_ADD", "register:40f0:8", ["const:a96abc:8", "const:4:8"]]
- 00a96abc ["CALL", null, ["callee:0081f580:8"]]
+ 00a96b00 ["INT_ADD", "register:40f0:8", ["const:a96b00:8", "const:4:8"]]
+ 00a96b00 ["CALL", null, ["callee:0081f580:8"]]
- 00a96abc bytes b122f697
+ 00a96b00 bytes a022f697
- 00a96acc ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a96acc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a96acc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a96acc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a96acc bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c43bdeed401a296d95e6d8840e1b8d0"></a>

### [`00a96bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96bf8.md) → [`00a96c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96c3c.md) FUN_00a96c3c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 4件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a96c1c",
      "incomplete_value": true,
      "site": "00a96c20",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00a96c64"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00a96ca8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a96c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96bf8.md#insn-00a96c20) · [`00a96c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96bf8.md#insn-00a96c64)
- 新版 `00a96c64`（命令位置の公開資料なし） · `00a96ca8`（命令位置の公開資料なし）

~~~diff
- 00a96c20 ["INT_ADD", "register:40f0:8", ["const:a96c20:8", "const:4:8"]]
- 00a96c20 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96c64 ["INT_ADD", "register:40f0:8", ["const:a96c64:8", "const:4:8"]]
+ 00a96c64 ["CALL", null, ["callee:005c2710:8"]]
- 00a96c20 bytes bcaeec97
+ 00a96c64 bytes abaeec97
- 00a96c64 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a96c64 ["RETURN", null, ["register:0:8"]]
- 00a96c64 bytes c0035fd6
+ 00a96ca8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00a96ca8 ["RETURN", null, ["register:0:8"]]
+ 00a96ca8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e63e434e84dc50b07ea293fad290dfc2"></a>

### [`00a96c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96c68.md) → [`00a96cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96cac.md) FUN_00a96cac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96c68.md#insn-00a96c7c) · [`00a96c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96c68.md#insn-00a96c90) · [`00a96c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96c68.md#insn-00a96c9c)
- 新版 `00a96cc0`（命令位置の公開資料なし） · `00a96cd4`（命令位置の公開資料なし） · `00a96ce0`（命令位置の公開資料なし）

~~~diff
- 00a96c7c ["INT_ADD", "register:40f0:8", ["const:a96c7c:8", "const:4:8"]]
- 00a96c7c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96cc0 ["INT_ADD", "register:40f0:8", ["const:a96cc0:8", "const:4:8"]]
+ 00a96cc0 ["CALL", null, ["callee:0081f580:8"]]
- 00a96c7c bytes 4122f697
+ 00a96cc0 bytes 3022f697
- 00a96c90 ["INT_ADD", "register:40f0:8", ["const:a96c90:8", "const:4:8"]]
- 00a96c90 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96cd4 ["INT_ADD", "register:40f0:8", ["const:a96cd4:8", "const:4:8"]]
+ 00a96cd4 ["CALL", null, ["callee:005c2710:8"]]
- 00a96c90 bytes a0aeec97
+ 00a96cd4 bytes 8faeec97
- 00a96c9c ["BRANCH", null, ["local:b3:8"]]
+ 00a96ce0 ["BRANCH", null, ["local:b4:8"]]
- 00a96c9c bytes 0c000014
+ 00a96ce0 bytes 0c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-756402c364cfb22727b2a542ce0da195"></a>

### [`00a96cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96cd8.md) → [`00a96d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96d1c.md) FUN_00a96d1c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`005ced48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ced48.md) [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`005ced48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ced48.md) [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96cd8.md#insn-00a96cf0) · [`00a96d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96cd8.md#insn-00a96d04) · [`00a96d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96cd8.md#insn-00a96d0c)
- 新版 `00a96d34`（命令位置の公開資料なし） · `00a96d48`（命令位置の公開資料なし） · `00a96d50`（命令位置の公開資料なし）

~~~diff
- 00a96cf0 ["INT_ADD", "register:40f0:8", ["const:a96cf0:8", "const:4:8"]]
- 00a96cf0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a96d34 ["INT_ADD", "register:40f0:8", ["const:a96d34:8", "const:4:8"]]
+ 00a96d34 ["CALL", null, ["callee:0081f580:8"]]
- 00a96cf0 bytes 2422f697
+ 00a96d34 bytes 1322f697
- 00a96d04 ["INT_ADD", "register:40f0:8", ["const:a96d04:8", "const:4:8"]]
- 00a96d04 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96d48 ["INT_ADD", "register:40f0:8", ["const:a96d48:8", "const:4:8"]]
+ 00a96d48 ["CALL", null, ["callee:005c2710:8"]]
- 00a96d04 bytes 83aeec97
+ 00a96d48 bytes 72aeec97
- 00a96d0c ["INT_ADD", "register:40f0:8", ["const:a96d0c:8", "const:4:8"]]
- 00a96d0c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96d50 ["INT_ADD", "register:40f0:8", ["const:a96d50:8", "const:4:8"]]
+ 00a96d50 ["CALL", null, ["callee:0081f580:8"]]
- 00a96d0c bytes 1d22f697
+ 00a96d50 bytes 0c22f697
~~~


<a id="compare-7ab0e786d66f8fa25e888e2d2c8927fc"></a>

### [`00a96d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96d58.md) → [`00a96d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96d9c.md) FUN_00a96d9c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96d58.md#insn-00a96d6c) · [`00a96d80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96d58.md#insn-00a96d80) · [`00a96d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96d58.md#insn-00a96d84)
- 新版 `00a96db0`（命令位置の公開資料なし） · `00a96dc4`（命令位置の公開資料なし） · `00a96dc8`（命令位置の公開資料なし）

~~~diff
- 00a96d6c ["INT_ADD", "register:40f0:8", ["const:a96d6c:8", "const:4:8"]]
- 00a96d6c ["CALL", null, ["callee:0081f580:8"]]
+ 00a96db0 ["INT_ADD", "register:40f0:8", ["const:a96db0:8", "const:4:8"]]
+ 00a96db0 ["CALL", null, ["callee:0081f580:8"]]
- 00a96d6c bytes 0522f697
+ 00a96db0 bytes f421f697
- 00a96d80 ["INT_ADD", "register:40f0:8", ["const:a96d80:8", "const:4:8"]]
- 00a96d80 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96dc4 ["INT_ADD", "register:40f0:8", ["const:a96dc4:8", "const:4:8"]]
+ 00a96dc4 ["CALL", null, ["callee:005c2710:8"]]
- 00a96d80 bytes 64aeec97
+ 00a96dc4 bytes 53aeec97
- 00a96d84 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00a96d84 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a96d84 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a96d84 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a96dc8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00a96dc8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a96dc8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a96dc8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a96d84 bytes a0010037
+ 00a96dc8 bytes a0010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789fe0e5d176506e8664f993bc5b54b5"></a>

### [`00a96ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ea8.md) → [`00a96eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a96eec.md) FUN_00a96eec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e60f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e60f0.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a96ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ea8.md#insn-00a96ebc) · [`00a96ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ea8.md#insn-00a96ed0) · [`00a96edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a96ea8.md#insn-00a96edc)
- 新版 `00a96f00`（命令位置の公開資料なし） · `00a96f14`（命令位置の公開資料なし） · `00a96f20`（命令位置の公開資料なし）

~~~diff
- 00a96ebc ["INT_ADD", "register:40f0:8", ["const:a96ebc:8", "const:4:8"]]
- 00a96ebc ["CALL", null, ["callee:0081f580:8"]]
+ 00a96f00 ["INT_ADD", "register:40f0:8", ["const:a96f00:8", "const:4:8"]]
+ 00a96f00 ["CALL", null, ["callee:0081f580:8"]]
- 00a96ebc bytes b121f697
+ 00a96f00 bytes a021f697
- 00a96ed0 ["INT_ADD", "register:40f0:8", ["const:a96ed0:8", "const:4:8"]]
- 00a96ed0 ["CALL", null, ["callee:005c2710:8"]]
+ 00a96f14 ["INT_ADD", "register:40f0:8", ["const:a96f14:8", "const:4:8"]]
+ 00a96f14 ["CALL", null, ["callee:005c2710:8"]]
- 00a96ed0 bytes 10aeec97
+ 00a96f14 bytes ffadec97
- 00a96edc ["BRANCH", null, ["local:b4:8"]]
+ 00a96f20 ["BRANCH", null, ["local:b3:8"]]
- 00a96edc bytes 0c000014
+ 00a96f20 bytes 0c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea054cf2cd580406cf669b34d3d39b48"></a>

### [`00a972f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a972f4.md) → [`00a97338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97338.md) FUN_00a97338

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a972f4.md#insn-00a97310)
- 新版 `00a97354`（命令位置の公開資料なし）

~~~diff
- 00a97310 ["INT_ADD", "register:40f0:8", ["const:a97310:8", "const:4:8"]]
- 00a97310 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97354 ["INT_ADD", "register:40f0:8", ["const:a97354:8", "const:4:8"]]
+ 00a97354 ["CALL", null, ["callee:0081f580:8"]]
- 00a97310 bytes 9c20f697
+ 00a97354 bytes 8b20f697
~~~


<a id="compare-6d0ed35a6f211fe8c1c96a97c34ff788"></a>

### [`00a978ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a978ec.md) → [`00a97930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97930.md) FUN_00a97930

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00a97968",
      "incomplete_value": true,
      "site": "00a97974",
      "value": [
        "INT_ZEXT",
        "8",
        [
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
    "old": null,
    "ordinal": 0,
    "slot": 0
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a97900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a978ec.md#insn-00a97900)
- 新版 `00a97944`（命令位置の公開資料なし）

~~~diff
- 00a97900 ["INT_ADD", "register:40f0:8", ["const:a97900:8", "const:4:8"]]
- 00a97900 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97944 ["INT_ADD", "register:40f0:8", ["const:a97944:8", "const:4:8"]]
+ 00a97944 ["CALL", null, ["callee:0081f580:8"]]
- 00a97900 bytes 201ff697
+ 00a97944 bytes 0f1ff697
~~~


<a id="compare-8ab5b32ebe0681551a38b625d95cd1e3"></a>

### [`00a97934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97934.md) → [`00a97978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97978.md) FUN_00a97978

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97934.md#insn-00a97950)
- 新版 `00a97994`（命令位置の公開資料なし）

~~~diff
- 00a97950 ["INT_ADD", "register:40f0:8", ["const:a97950:8", "const:4:8"]]
- 00a97950 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97994 ["INT_ADD", "register:40f0:8", ["const:a97994:8", "const:4:8"]]
+ 00a97994 ["CALL", null, ["callee:0081f580:8"]]
- 00a97950 bytes 0c1ff697
+ 00a97994 bytes fb1ef697
~~~


<a id="compare-c964f935f06a952cc7e6c75673ce84cb"></a>

### [`00a97aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97aec.md) → [`00a97b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97b30.md) FUN_00a97b30

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97aec.md#insn-00a97b08)
- 新版 `00a97b4c`（命令位置の公開資料なし）

~~~diff
- 00a97b08 ["INT_ADD", "register:40f0:8", ["const:a97b08:8", "const:4:8"]]
- 00a97b08 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97b4c ["INT_ADD", "register:40f0:8", ["const:a97b4c:8", "const:4:8"]]
+ 00a97b4c ["CALL", null, ["callee:0081f580:8"]]
- 00a97b08 bytes 9e1ef697
+ 00a97b4c bytes 8d1ef697
~~~


<a id="compare-a30f13cced2f9517e19b419e6ca09cc5"></a>

### [`00a97c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97c8c.md) → [`00a97cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97cd0.md) FUN_00a97cd0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a97ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97c8c.md#insn-00a97ca0) · [`00a97cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97c8c.md#insn-00a97cb4) · [`00a97cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97c8c.md#insn-00a97cc0)
- 新版 `00a97ce4`（命令位置の公開資料なし） · `00a97cf8`（命令位置の公開資料なし） · `00a97d04`（命令位置の公開資料なし）

~~~diff
- 00a97ca0 ["INT_ADD", "register:40f0:8", ["const:a97ca0:8", "const:4:8"]]
- 00a97ca0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a97ce4 ["INT_ADD", "register:40f0:8", ["const:a97ce4:8", "const:4:8"]]
+ 00a97ce4 ["CALL", null, ["callee:0081f580:8"]]
- 00a97ca0 bytes 381ef697
+ 00a97ce4 bytes 271ef697
- 00a97cb4 ["INT_ADD", "register:40f0:8", ["const:a97cb4:8", "const:4:8"]]
- 00a97cb4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97cf8 ["INT_ADD", "register:40f0:8", ["const:a97cf8:8", "const:4:8"]]
+ 00a97cf8 ["CALL", null, ["callee:005c2710:8"]]
- 00a97cb4 bytes 97aaec97
+ 00a97cf8 bytes 86aaec97
- 00a97cc0 ["BRANCH", null, ["local:b3:8"]]
+ 00a97d04 ["BRANCH", null, ["local:b4:8"]]
- 00a97cc0 bytes 0c000014
+ 00a97d04 bytes 0c000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b3ff4b0a58f57f73e99a427093f51b"></a>

### [`00a97cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97cfc.md) → [`00a97d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97d40.md) FUN_00a97d40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "site": "00a97d58"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a97d9c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a97d6c",
      "incomplete_value": true,
      "site": "00a97d70",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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


#### 変更候補の命令位置

- 旧版 [`00a97d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97cfc.md#insn-00a97d2c) · [`00a97d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97cfc.md#insn-00a97d58)
- 新版 `00a97d70`（命令位置の公開資料なし） · `00a97d9c`（命令位置の公開資料なし）

~~~diff
- 00a97d2c ["INT_ADD", "register:40f0:8", ["const:a97d2c:8", "const:4:8"]]
- 00a97d2c ["CALL", null, ["callee:005c2710:8"]]
+ 00a97d70 ["INT_ADD", "register:40f0:8", ["const:a97d70:8", "const:4:8"]]
+ 00a97d70 ["CALL", null, ["callee:005c2710:8"]]
- 00a97d2c bytes 79aaec97
+ 00a97d70 bytes 68aaec97
- 00a97d58 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00a97d58 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a97d58 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a97d58 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00a97d58 bytes 146929b8
+ 00a97d9c ["COPY", "tmp:0:4", ["register:40a0:4"]]
+ 00a97d9c ["COPY", "tmp:1:8", ["register:4048:8"]]
+ 00a97d9c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 00a97d9c ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
+ 00a97d9c bytes 146929b8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f448b61fad5c41acc1047d64857f2029"></a>

### [`00a97d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97d6c.md) → [`00a97db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a97/00a97db0.md) FUN_00a97db0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 12.50% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a97d6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a97d6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a97d70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a97d6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a97d70",
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
      "00a97db0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a97db4",
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

- 旧版 [`00a97d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97d6c.md#insn-00a97d6c) · [`00a97d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97d6c.md#insn-00a97d70) · [`00a97d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a97/00a97d6c.md#insn-00a97d94)
- 新版 `00a97dd8`（命令位置の公開資料なし）

~~~diff
- 00a97d6c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a97d6c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a97d6c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a97d6c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a97d6c bytes fd7bbea9
- 00a97d70 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a97d70 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a97d70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a97d70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a97d70 bytes f44f01a9
- 00a97d94 ["INT_ADD", "register:40f0:8", ["const:a97d94:8", "const:4:8"]]
- 00a97d94 ["CALL", null, ["callee:005c2710:8"]]
+ 00a97dd8 ["INT_ADD", "register:40f0:8", ["const:a97dd8:8", "const:4:8"]]
+ 00a97dd8 ["CALL", null, ["callee:005c2710:8"]]
- 00a97d94 bytes 5faaec97
+ 00a97dd8 bytes 4eaaec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ac5f04540ff49cd64db4ee8ff429185"></a>

### [`00a98050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98050.md) → [`00a98094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98094.md) FUN_00a98094

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 25.00% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98050.md#insn-00a98050) · [`00a98074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98050.md#insn-00a98074)
- 新版 `00a98094`（命令位置の公開資料なし） · `00a980b8`（命令位置の公開資料なし）

~~~diff
- 00a98050 ["INT_EQUAL", "tmp:0:1", ["register:4010:4", "const:0:4"]]
- 00a98050 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00a98094 ["INT_EQUAL", "tmp:0:1", ["register:4010:4", "const:0:4"]]
+ 00a98094 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00a98050 bytes 22030034
+ 00a98094 bytes 22030034
- 00a98074 ["INT_ADD", "register:40f0:8", ["const:a98074:8", "const:4:8"]]
- 00a98074 ["CALL", null, ["callee:0081f580:8"]]
+ 00a980b8 ["INT_ADD", "register:40f0:8", ["const:a980b8:8", "const:4:8"]]
+ 00a980b8 ["CALL", null, ["callee:0081f580:8"]]
- 00a98074 bytes 431df697
+ 00a980b8 bytes 321df697
~~~


<a id="compare-5f7ea30f1d1a96cb91cd132231e1ea6c"></a>

### [`00a98398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98398.md) → [`00a983dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a983dc.md) FUN_00a983dc

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e9c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e9/006e9c88.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00a983d0",
      "incomplete_value": true,
      "site": "00a983dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a983ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98398.md#insn-00a983ac)
- 新版 `00a983f0`（命令位置の公開資料なし）

~~~diff
- 00a983ac ["INT_ADD", "register:40f0:8", ["const:a983ac:8", "const:4:8"]]
- 00a983ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a983f0 ["INT_ADD", "register:40f0:8", ["const:a983f0:8", "const:4:8"]]
+ 00a983f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a983ac bytes 751cf697
+ 00a983f0 bytes 641cf697
~~~


<a id="compare-f07bdb7cbc38c37767f48a1753d48bee"></a>

### [`00a98420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98420.md) → [`00a98464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98464.md) FUN_00a98464

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9843c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98420.md#insn-00a9843c)
- 新版 `00a98480`（命令位置の公開資料なし）

~~~diff
- 00a9843c ["INT_ADD", "register:40f0:8", ["const:a9843c:8", "const:4:8"]]
- 00a9843c ["CALL", null, ["callee:0081f580:8"]]
+ 00a98480 ["INT_ADD", "register:40f0:8", ["const:a98480:8", "const:4:8"]]
+ 00a98480 ["CALL", null, ["callee:0081f580:8"]]
- 00a9843c bytes 511cf697
+ 00a98480 bytes 401cf697
~~~


<a id="compare-4eda3972e0ffe667028b728ce91d16d9"></a>

### [`00a98990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98990.md) → [`00a989d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a989d4.md) FUN_00a989d4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a989ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98990.md#insn-00a989ac)
- 新版 `00a989f0`（命令位置の公開資料なし）

~~~diff
- 00a989ac ["INT_ADD", "register:40f0:8", ["const:a989ac:8", "const:4:8"]]
- 00a989ac ["CALL", null, ["callee:0081f580:8"]]
+ 00a989f0 ["INT_ADD", "register:40f0:8", ["const:a989f0:8", "const:4:8"]]
+ 00a989f0 ["CALL", null, ["callee:0081f580:8"]]
- 00a989ac bytes f51af697
+ 00a989f0 bytes e41af697
~~~


<a id="compare-33ecbbf9a9e3e33056bbe8fd11aa6447"></a>

### [`00a98a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98a1c.md) → [`00a98a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98a60.md) FUN_00a98a60

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98a1c.md#insn-00a98a38)
- 新版 `00a98a7c`（命令位置の公開資料なし）

~~~diff
- 00a98a38 ["INT_ADD", "register:40f0:8", ["const:a98a38:8", "const:4:8"]]
- 00a98a38 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98a7c ["INT_ADD", "register:40f0:8", ["const:a98a7c:8", "const:4:8"]]
+ 00a98a7c ["CALL", null, ["callee:0081f580:8"]]
- 00a98a38 bytes d21af697
+ 00a98a7c bytes c11af697
~~~


<a id="compare-b128dc9da4ce30d6945ae2d1d97cb74c"></a>

### [`00a98ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ca4.md) → [`00a98ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a98/00a98ce8.md) FUN_00a98ce8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ea/006eaef0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006eaef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ea/006eaef0.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a98cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a98/00a98ca4.md#insn-00a98cb8)
- 新版 `00a98cfc`（命令位置の公開資料なし）

~~~diff
- 00a98cb8 ["INT_ADD", "register:40f0:8", ["const:a98cb8:8", "const:4:8"]]
- 00a98cb8 ["CALL", null, ["callee:0081f580:8"]]
+ 00a98cfc ["INT_ADD", "register:40f0:8", ["const:a98cfc:8", "const:4:8"]]
+ 00a98cfc ["CALL", null, ["callee:0081f580:8"]]
- 00a98cb8 bytes 321af697
+ 00a98cfc bytes 211af697
~~~


<a id="compare-d2c811e45fa402ed52c29e6d1be6bc58"></a>

### [`00a996e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a996e0.md) → [`00a99724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99724.md) FUN_00a99724

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a996f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a996e0.md#insn-00a996f4)
- 新版 `00a99738`（命令位置の公開資料なし）

~~~diff
- 00a996f4 ["INT_ADD", "register:40f0:8", ["const:a996f4:8", "const:4:8"]]
- 00a996f4 ["CALL", null, ["callee:0081f580:8"]]
+ 00a99738 ["INT_ADD", "register:40f0:8", ["const:a99738:8", "const:4:8"]]
+ 00a99738 ["CALL", null, ["callee:0081f580:8"]]
- 00a996f4 bytes a317f697
+ 00a99738 bytes 9217f697
~~~


<a id="compare-eeae4753a9cc81388bde8aba20cef825"></a>

### [`00a99958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99958.md) → [`00a9999c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a9999c.md) FUN_00a9999c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99958"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9995c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a99958",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9995c",
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
      "00a9999c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a999a0",
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

- 旧版 [`00a99958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99958.md#insn-00a99958) · [`00a9995c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99958.md#insn-00a9995c)
- 新版 `00a9999c`（命令位置の公開資料なし）

~~~diff
- 00a99958 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a99958 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a99958 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a99958 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a99958 bytes fd7bbea9
- 00a9995c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a9995c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a9995c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a9995c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9995c bytes f44f01a9
+ 00a9999c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a9999c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a9999c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a9999c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a9999c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b16ac3536a7c469ff75f4e0206e9d34"></a>

### [`00a999e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a999e4.md) → [`00a99a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99a28.md) FUN_00a99a28

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`005ce03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ce03c.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 8件 [`005bc1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bc1dc.md) [`005bce20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bce20.md) [`0066367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/0066367c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/009019f4.md)
- 新版 呼出元 3件 [`005ce03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ce03c.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 8件 [`005bc1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bc1dc.md) [`005bce20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bce20.md) [`0066367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066367c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009019f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/009019f4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 81.95% / 新版 81.95%

CFGの説明率　旧版 10.20% / 新版 11.36%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99b44"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99b48"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99b4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a99afc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99c04"
      ]
    ],
    [
      "unmatched:00a99b38",
      "READ",
      [
        "storage",
        "002a5fbe",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00a99b3c",
      "READ",
      [
        "storage",
        "002a5fc7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a99b40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a99c04"
      ]
    ],
    [
      "00a99b7c",
      "READ",
      [
        "storage",
        "002a6058",
        null,
        "string"
      ]
    ],
    [
      "00a99b80",
      "READ",
      [
        "storage",
        "002a6061",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a99ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a999e4.md#insn-00a99ab8) · [`00a99ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a999e4.md#insn-00a99ae8)
- 新版 `00a99afc`（命令位置の公開資料なし） · `00a99b2c`（命令位置の公開資料なし） · `00a99ae8`（命令位置の公開資料なし）

~~~diff
- 00a99ab8 ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:4", "const:0:4"]]
- 00a99ab8 ["CBRANCH", null, ["local:b36:8", "tmp:0:1"]]
+ 00a99afc ["INT_NOTEQUAL", "tmp:0:1", ["register:40a8:4", "const:0:4"]]
+ 00a99afc ["CBRANCH", null, ["local:b32:8", "tmp:0:1"]]
- 00a99ab8 bytes 55080035
+ 00a99afc bytes 55080035
- 00a99ae8 ["INT_ADD", "register:40f0:8", ["const:a99ae8:8", "const:4:8"]]
- 00a99ae8 ["CALL", null, ["callee:005bc1dc:8"]]
+ 00a99b2c ["INT_ADD", "register:40f0:8", ["const:a99b2c:8", "const:4:8"]]
+ 00a99b2c ["CALL", null, ["callee:005bc1dc:8"]]
- 00a99ae8 bytes bd89ec97
+ 00a99b2c bytes ac89ec97
+ 00a99ae8 ["INT_RIGHT", "register:4048:8", ["register:4040:8", "const:3f:8"]]
+ 00a99ae8 bytes 09fd7fd3
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-195fe4e108728e6c1e98643c5697bd87"></a>

### [`00a99c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99c94.md) → [`00a99cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a99/00a99cd8.md) FUN_00a99cd8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 14.29% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99c94"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a99c98"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a99c94",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a99c98",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a99c9c",
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
      "00a99cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a99cdc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a99ce0",
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

- 旧版 [`00a99c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99c94.md#insn-00a99c94) · [`00a99c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99c94.md#insn-00a99c98) · [`00a99c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a99/00a99c94.md#insn-00a99c9c)

~~~diff
- 00a99c94 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a99c94 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a99c94 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a99c94 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a99c94 bytes fd7bbda9
- 00a99c98 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a99c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a99c98 bytes f50b00f9
- 00a99c9c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a99c9c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a99c9c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a99c9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a99c9c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37fef9a31066acc3efd385c8848dc2bd"></a>

### [`00a9a2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a2cc.md) → [`00a9a310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a310.md) FUN_00a9a310

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a9a334",
      "incomplete_value": true,
      "site": "00a9a338",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9a2f0",
      "incomplete_value": true,
      "site": "00a9a2f4",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a2cc.md#insn-00a9a2f4) · [`00a9a2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a2cc.md#insn-00a9a2e0) · [`00a9a2f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a2cc.md#insn-00a9a2f0)
- 新版 `00a9a338`（命令位置の公開資料なし） · `00a9a324`（命令位置の公開資料なし）

~~~diff
- 00a9a2f4 ["INT_ADD", "register:40f0:8", ["const:a9a2f4:8", "const:4:8"]]
- 00a9a2f4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a338 ["INT_ADD", "register:40f0:8", ["const:a9a338:8", "const:4:8"]]
+ 00a9a338 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a2f4 bytes 07a1ec97
+ 00a9a338 bytes f6a0ec97
- 00a9a2e0 ["INT_ADD", "register:40f0:8", ["const:a9a2e0:8", "const:4:8"]]
- 00a9a2e0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a324 ["INT_ADD", "register:40f0:8", ["const:a9a324:8", "const:4:8"]]
+ 00a9a324 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a2e0 bytes a814f697
+ 00a9a324 bytes 9714f697
- 00a9a2f0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a9a2f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9a2f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9a2f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9a2f0 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a4ebc1339663c4f9602582c9d5162a"></a>

### [`00a9a33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a33c.md) → [`00a9a380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a380.md) FUN_00a9a380

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00a9a3dc"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a9a3ac",
      "incomplete_value": true,
      "site": "00a9a3b0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9a368",
      "incomplete_value": true,
      "site": "00a9a36c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "00a9a3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9a39c"
      ]
    ],
    [
      "unmatched:00a9a39c",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9a3a0",
      "READ",
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
      "00a9a3b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9a3e0"
      ]
    ],
    [
      "00a9a3e0",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00a9a3e4",
      "READ",
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

- 旧版 [`00a9a36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a33c.md#insn-00a9a36c) · [`00a9a398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a33c.md#insn-00a9a398) · [`00a9a3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a33c.md#insn-00a9a3a8)
- 新版 `00a9a3b0`（命令位置の公開資料なし）

~~~diff
- 00a9a36c ["INT_ADD", "register:40f0:8", ["const:a9a36c:8", "const:4:8"]]
- 00a9a36c ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a3b0 ["INT_ADD", "register:40f0:8", ["const:a9a3b0:8", "const:4:8"]]
+ 00a9a3b0 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a36c bytes e9a0ec97
+ 00a9a3b0 bytes d8a0ec97
- 00a9a398 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00a9a398 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00a9a398 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00a9a398 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00a9a398 bytes 146929b8
- 00a9a3a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00a9a3a8 ["RETURN", null, ["register:0:8"]]
- 00a9a3a8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-918b352767a1ca9aa80e546adbb29c61"></a>

### [`00a9a48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a48c.md) → [`00a9a4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a4d0.md) FUN_00a9a4d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a9a4f4",
      "incomplete_value": true,
      "site": "00a9a4f8",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9a4b0",
      "incomplete_value": true,
      "site": "00a9a4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a48c.md#insn-00a9a4b4) · [`00a9a4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a48c.md#insn-00a9a4a0) · [`00a9a4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a48c.md#insn-00a9a4b0)
- 新版 `00a9a4f8`（命令位置の公開資料なし） · `00a9a4e4`（命令位置の公開資料なし）

~~~diff
- 00a9a4b4 ["INT_ADD", "register:40f0:8", ["const:a9a4b4:8", "const:4:8"]]
- 00a9a4b4 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a4f8 ["INT_ADD", "register:40f0:8", ["const:a9a4f8:8", "const:4:8"]]
+ 00a9a4f8 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a4b4 bytes 97a0ec97
+ 00a9a4f8 bytes 86a0ec97
- 00a9a4a0 ["INT_ADD", "register:40f0:8", ["const:a9a4a0:8", "const:4:8"]]
- 00a9a4a0 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9a4e4 ["INT_ADD", "register:40f0:8", ["const:a9a4e4:8", "const:4:8"]]
+ 00a9a4e4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9a4a0 bytes 3814f697
+ 00a9a4e4 bytes 2714f697
- 00a9a4b0 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00a9a4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9a4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9a4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9a4b0 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2a352e1e50a48d4ad3be361afffa489"></a>

### [`00a9a56c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a56c.md) → [`00a9a5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9a5b0.md) FUN_00a9a5b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 15.79% / 新版 15.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a5f0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9a614"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a9a634"
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
      "00a9a604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9a5cc"
      ]
    ],
    [
      "00a9a60c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9a618"
      ]
    ],
    [
      "unmatched:00a9a5cc",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ],
  "added": [
    [
      "00a9a604",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9a610"
      ]
    ],
    [
      "00a9a60c",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9a65c"
      ]
    ],
    [
      "00a9a634",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9a65c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9a5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a56c.md#insn-00a9a5bc) · [`00a9a5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a56c.md#insn-00a9a5cc) · [`00a9a5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9a56c.md#insn-00a9a5f0)
- 新版 `00a9a600`（命令位置の公開資料なし）

~~~diff
- 00a9a5bc ["INT_ADD", "register:40f0:8", ["const:a9a5bc:8", "const:4:8"]]
- 00a9a5bc ["CALL", null, ["callee:005c2710:8"]]
+ 00a9a600 ["INT_ADD", "register:40f0:8", ["const:a9a600:8", "const:4:8"]]
+ 00a9a600 ["CALL", null, ["callee:005c2710:8"]]
- 00a9a5bc bytes 55a0ec97
+ 00a9a600 bytes 44a0ec97
- 00a9a5cc ["INT_ADD", "register:40f0:8", ["const:a9a5cc:8", "const:4:8"]]
- 00a9a5cc ["CALL", null, ["callee:0081f580:8"]]
- 00a9a5cc bytes ed13f697
- 00a9a5f0 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a9a5f0 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00a9a5f0 bytes 48010034
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0db3efce9f7dce684e91768866981ea"></a>

### [`00a9abd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9abd0.md) → [`00a9ac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9ac14.md) FUN_00a9ac14

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9abec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9abd0.md#insn-00a9abec) · [`00a9ac00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9abd0.md#insn-00a9ac00) · [`00a9ac04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9abd0.md#insn-00a9ac04)
- 新版 `00a9ac30`（命令位置の公開資料なし） · `00a9ac44`（命令位置の公開資料なし） · `00a9ac48`（命令位置の公開資料なし）

~~~diff
- 00a9abec ["INT_ADD", "register:40f0:8", ["const:a9abec:8", "const:4:8"]]
- 00a9abec ["CALL", null, ["callee:0081f580:8"]]
+ 00a9ac30 ["INT_ADD", "register:40f0:8", ["const:a9ac30:8", "const:4:8"]]
+ 00a9ac30 ["CALL", null, ["callee:0081f580:8"]]
- 00a9abec bytes 6512f697
+ 00a9ac30 bytes 5412f697
- 00a9ac00 ["INT_ADD", "register:40f0:8", ["const:a9ac00:8", "const:4:8"]]
- 00a9ac00 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9ac44 ["INT_ADD", "register:40f0:8", ["const:a9ac44:8", "const:4:8"]]
+ 00a9ac44 ["CALL", null, ["callee:005c2710:8"]]
- 00a9ac00 bytes c49eec97
+ 00a9ac44 bytes b39eec97
- 00a9ac04 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00a9ac04 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a9ac04 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a9ac04 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00a9ac48 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00a9ac48 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a9ac48 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a9ac48 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00a9ac04 bytes 40010036
+ 00a9ac48 bytes 40010036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e72f78d77dea68a460a41c8f58ea2f4b"></a>

### [`00a9ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9ac3c.md) → [`00a9ac80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9a/00a9ac80.md) FUN_00a9ac80

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9ac50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9ac3c.md#insn-00a9ac50) · [`00a9ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9ac3c.md#insn-00a9ac64) · [`00a9ac68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9a/00a9ac3c.md#insn-00a9ac68)
- 新版 `00a9ac94`（命令位置の公開資料なし） · `00a9aca8`（命令位置の公開資料なし） · `00a9acac`（命令位置の公開資料なし）

~~~diff
- 00a9ac50 ["INT_ADD", "register:40f0:8", ["const:a9ac50:8", "const:4:8"]]
- 00a9ac50 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9ac94 ["INT_ADD", "register:40f0:8", ["const:a9ac94:8", "const:4:8"]]
+ 00a9ac94 ["CALL", null, ["callee:0081f580:8"]]
- 00a9ac50 bytes 4c12f697
+ 00a9ac94 bytes 3b12f697
- 00a9ac64 ["INT_ADD", "register:40f0:8", ["const:a9ac64:8", "const:4:8"]]
- 00a9ac64 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9aca8 ["INT_ADD", "register:40f0:8", ["const:a9aca8:8", "const:4:8"]]
+ 00a9aca8 ["CALL", null, ["callee:005c2710:8"]]
- 00a9ac64 bytes ab9eec97
+ 00a9aca8 bytes 9a9eec97
- 00a9ac68 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00a9ac68 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a9ac68 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a9ac68 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a9acac ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00a9acac ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a9acac ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a9acac ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a9ac68 bytes 60000037
+ 00a9acac bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55b9c37cb9be0a32711be33906d60f3d"></a>

### [`00a9c330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9c330.md) → [`00a9c374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9c374.md) FUN_00a9c374

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9c344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9c330.md#insn-00a9c344)
- 新版 `00a9c388`（命令位置の公開資料なし）

~~~diff
- 00a9c344 ["INT_ADD", "register:40f0:8", ["const:a9c344:8", "const:4:8"]]
- 00a9c344 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9c388 ["INT_ADD", "register:40f0:8", ["const:a9c388:8", "const:4:8"]]
+ 00a9c388 ["CALL", null, ["callee:0081f580:8"]]
- 00a9c344 bytes 8f0cf697
+ 00a9c388 bytes 7e0cf697
~~~


<a id="compare-d5f07e89e7b8960e1173c28ee60abb36"></a>

### [`00a9c93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9c93c.md) → [`00a9c980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9c980.md) FUN_00a9c980

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9c958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9c93c.md#insn-00a9c958)
- 新版 `00a9c99c`（命令位置の公開資料なし）

~~~diff
- 00a9c958 ["INT_ADD", "register:40f0:8", ["const:a9c958:8", "const:4:8"]]
- 00a9c958 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9c99c ["INT_ADD", "register:40f0:8", ["const:a9c99c:8", "const:4:8"]]
+ 00a9c99c ["CALL", null, ["callee:0081f580:8"]]
- 00a9c958 bytes 0a0bf697
+ 00a9c99c bytes f90af697
~~~


<a id="compare-d2031d78350bf5732fbf41d302d1eff7"></a>

### [`00a9ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9ca70.md) → [`00a9cab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9cab4.md) FUN_00a9cab4

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`006e62f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e6/006e62f8.md) [`006ecae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006ecae4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006e62f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e6/006e62f8.md) [`006ecae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006ecae4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9ca84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9ca70.md#insn-00a9ca84)
- 新版 `00a9cac8`（命令位置の公開資料なし）

~~~diff
- 00a9ca84 ["INT_ADD", "register:40f0:8", ["const:a9ca84:8", "const:4:8"]]
- 00a9ca84 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9cac8 ["INT_ADD", "register:40f0:8", ["const:a9cac8:8", "const:4:8"]]
+ 00a9cac8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9ca84 bytes bf0af697
+ 00a9cac8 bytes ae0af697
~~~


<a id="compare-fea3745d46287c4c7abca3a9dbf8db03"></a>

### [`00a9cc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cc00.md) → [`00a9cc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9cc44.md) FUN_00a9cc44

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e7/006e79bc.md) [`006eb464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`006e79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e7/006e79bc.md) [`006eb464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006eb/006eb464.md) [`006eccf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ec/006eccf4.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9cc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cc00.md#insn-00a9cc1c)
- 新版 `00a9cc60`（命令位置の公開資料なし）

~~~diff
- 00a9cc1c ["INT_ADD", "register:40f0:8", ["const:a9cc1c:8", "const:4:8"]]
- 00a9cc1c ["CALL", null, ["callee:0081f580:8"]]
+ 00a9cc60 ["INT_ADD", "register:40f0:8", ["const:a9cc60:8", "const:4:8"]]
+ 00a9cc60 ["CALL", null, ["callee:0081f580:8"]]
- 00a9cc1c bytes 590af697
+ 00a9cc60 bytes 480af697
~~~


<a id="compare-a471b0933b266cb7e37157e81ea92945"></a>

### [`00a9cc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cc4c.md) → [`00a9cc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9c/00a9cc90.md) FUN_00a9cc90

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 6件 [`005ce03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ce03c.md) [`005ced48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ce/005ced48.md) [`005d6c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005d6/005d6c3c.md) [`006ddfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006ddfb8.md) [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 6件 [`005ce03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ce03c.md) [`005ced48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ce/005ced48.md) [`005d6c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005d6/005d6c3c.md) [`006ddfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006dd/006ddfb8.md) [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9cc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9c/00a9cc4c.md#insn-00a9cc60)
- 新版 `00a9cca4`（命令位置の公開資料なし）

~~~diff
- 00a9cc60 ["INT_ADD", "register:40f0:8", ["const:a9cc60:8", "const:4:8"]]
- 00a9cc60 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9cca4 ["INT_ADD", "register:40f0:8", ["const:a9cca4:8", "const:4:8"]]
+ 00a9cca4 ["CALL", null, ["callee:0081f580:8"]]
- 00a9cc60 bytes 480af697
+ 00a9cca4 bytes 370af697
~~~


<a id="compare-96fde7c0807af315ca0d7b49701f8a34"></a>

### [`00a9d458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d458.md) → [`00a9d49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d49c.md) FUN_00a9d49c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 1件 [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d458"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d45c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9d458",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9d45c",
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
      "00a9d49c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a9d4a0",
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

- 旧版 [`00a9d458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d458.md#insn-00a9d458) · [`00a9d45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d458.md#insn-00a9d45c)
- 新版 `00a9d49c`（命令位置の公開資料なし）

~~~diff
- 00a9d458 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a9d458 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a9d458 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a9d458 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a9d458 bytes fd7bbea9
- 00a9d45c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a9d45c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a9d45c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a9d45c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9d45c bytes f44f01a9
+ 00a9d49c ["COPY", "tmp:0:8", ["register:40e8:8"]]
+ 00a9d49c ["COPY", "tmp:1:8", ["register:40f0:8"]]
+ 00a9d49c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
+ 00a9d49c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
+ 00a9d49c bytes fd7bbea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e2aab97e7d82c66d75035173254075"></a>

### [`00a9d538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d538.md) → [`00a9d57c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d57c.md) FUN_00a9d57c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d538"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d53c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9d538",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9d53c",
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
      "00a9d57c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a9d580",
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

- 旧版 [`00a9d538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d538.md#insn-00a9d538) · [`00a9d53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d538.md#insn-00a9d53c) · [`00a9d560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d538.md#insn-00a9d560)
- 新版 `00a9d5a4`（命令位置の公開資料なし）

~~~diff
- 00a9d538 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a9d538 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a9d538 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00a9d538 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a9d538 bytes fd7bbea9
- 00a9d53c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a9d53c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a9d53c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00a9d53c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9d53c bytes f44f01a9
- 00a9d560 ["INT_ADD", "register:40f0:8", ["const:a9d560:8", "const:4:8"]]
- 00a9d560 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d5a4 ["INT_ADD", "register:40f0:8", ["const:a9d5a4:8", "const:4:8"]]
+ 00a9d5a4 ["CALL", null, ["callee:005c2710:8"]]
- 00a9d560 bytes 6c94ec97
+ 00a9d5a4 bytes 5b94ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0153c8c106089e8bea23f03a551978f4"></a>

### [`00a9d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d5a0.md) → [`00a9d5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d5e4.md) FUN_00a9d5e4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d5a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9d5a4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9d5a0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9d5a4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9d5a8",
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
      "00a9d5e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00a9d5e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00a9d5ec",
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

- 旧版 [`00a9d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d5a0.md#insn-00a9d5a0) · [`00a9d5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d5a0.md#insn-00a9d5a4) · [`00a9d5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d5a0.md#insn-00a9d5a8)

~~~diff
- 00a9d5a0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a9d5a0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a9d5a0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00a9d5a0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00a9d5a0 bytes fd7bbda9
- 00a9d5a4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00a9d5a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00a9d5a4 bytes f50b00f9
- 00a9d5a8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00a9d5a8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00a9d5a8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a9d5a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9d5a8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc606c1b4fe2ed6e11e2fd3cdab66bde"></a>

### [`00a9d60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d60c.md) → [`00a9d650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9d/00a9d650.md) FUN_00a9d650

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006d6d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006d6/006d6d04.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 55.56% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00a9d628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d60c.md#insn-00a9d628) · [`00a9d640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d60c.md#insn-00a9d640) · [`00a9d644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9d/00a9d60c.md#insn-00a9d644)
- 新版 `00a9d66c`（命令位置の公開資料なし） · `00a9d684`（命令位置の公開資料なし） · `00a9d688`（命令位置の公開資料なし）

~~~diff
- 00a9d628 ["INT_ADD", "register:40f0:8", ["const:a9d628:8", "const:4:8"]]
- 00a9d628 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9d66c ["INT_ADD", "register:40f0:8", ["const:a9d66c:8", "const:4:8"]]
+ 00a9d66c ["CALL", null, ["callee:0081f580:8"]]
- 00a9d628 bytes d607f697
+ 00a9d66c bytes c507f697
- 00a9d640 ["INT_ADD", "register:40f0:8", ["const:a9d640:8", "const:4:8"]]
- 00a9d640 ["CALL", null, ["callee:005c2710:8"]]
+ 00a9d684 ["INT_ADD", "register:40f0:8", ["const:a9d684:8", "const:4:8"]]
+ 00a9d684 ["CALL", null, ["callee:005c2710:8"]]
- 00a9d640 bytes 3494ec97
+ 00a9d684 bytes 2394ec97
- 00a9d644 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00a9d644 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00a9d644 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00a9d644 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00a9d688 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00a9d688 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00a9d688 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00a9d688 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00a9d644 bytes 40010037
+ 00a9d688 bytes 40010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46fb12de6c9bfbd2b9618dc9f6d9849b"></a>

### [`00a9e66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e66c.md) → [`00a9e6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9e6b0.md) _INIT_243

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a9e6ec",
      "incomplete_value": true,
      "site": "00a9e708",
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
    "old": {
      "definition_site": "00a9e6a8",
      "incomplete_value": true,
      "site": "00a9e6c4",
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
                "const:2dd:8"
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
      "definition_site": "00a9e710",
      "incomplete_value": true,
      "site": "00a9e72c",
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
    "old": {
      "definition_site": "00a9e6cc",
      "incomplete_value": true,
      "site": "00a9e6e8",
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
                "const:2f0:8"
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
      "definition_site": "00a9e730",
      "incomplete_value": true,
      "site": "00a9e74c",
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
    "old": {
      "definition_site": "00a9e6ec",
      "incomplete_value": true,
      "site": "00a9e708",
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
                "const:46:8"
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
      "00a9e6ec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a9e710",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a9e730",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a9e6ec",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00a9e710",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00a9e730",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9e6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e66c.md#insn-00a9e6a4) · [`00a9e7cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e66c.md#insn-00a9e7cc) · [`00a9e8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e66c.md#insn-00a9e8a0)
- 新版 `00a9e6e8`（命令位置の公開資料なし） · `00a9e810`（命令位置の公開資料なし） · `00a9e8e4`（命令位置の公開資料なし）

~~~diff
- 00a9e6a4 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00a9e6a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9e6a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9e6a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a9e6e8 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00a9e6e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9e6e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9e6e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9e6a4 bytes 29750b91
+ 00a9e6e8 bytes 29dd0d91
- 00a9e7cc ["INT_ADD", "register:40f0:8", ["const:a9e7cc:8", "const:4:8"]]
- 00a9e7cc ["CALL", null, ["callee:00418cb8:8"]]
+ 00a9e810 ["INT_ADD", "register:40f0:8", ["const:a9e810:8", "const:4:8"]]
+ 00a9e810 ["CALL", null, ["callee:00418cb8:8"]]
- 00a9e7cc bytes 3be9e597
+ 00a9e810 bytes 2ae9e597
- 00a9e8a0 ["INT_ADD", "register:40f0:8", ["const:a9e8a0:8", "const:4:8"]]
- 00a9e8a0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00a9e8e4 ["INT_ADD", "register:40f0:8", ["const:a9e8e4:8", "const:4:8"]]
+ 00a9e8e4 ["CALL", null, ["callee:00bdafe0:8"]]
- 00a9e8a0 bytes bcf10494
+ 00a9e8e4 bytes bff10494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c2814d9272f0c2b3e76e10d5b218fbf"></a>

### [`00a9e9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e9fc.md) → [`00a9ea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9ea40.md) FUN_00a9ea40

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 15件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0066398c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/0066398c.md) [`0078aefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078a/0078aefc.md) [`0078af80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078a/0078af80.md) [`007bd9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bd9d0.md)
- 新版 呼出元 2件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 15件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0066398c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066398c.md) [`0078aefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078a/0078aefc.md) [`0078af80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078a/0078af80.md) [`007bd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd9d0.md)

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 90.93% / 新版 90.93%

CFGの説明率　旧版 70.45% / 新版 71.26%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9ed88"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9eda4"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9ee38"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a9ed74",
      "READ",
      [
        "storage",
        "00c1b820",
        null,
        "pointer"
      ]
    ],
    [
      "00a9ed78",
      "DATA",
      [
        "storage",
        "00c24604",
        null,
        null
      ]
    ],
    [
      "00a9edb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9ed90"
      ]
    ]
  ],
  "added": [
    [
      "00a9ed74",
      "READ",
      [
        "storage",
        "00c1b870",
        null,
        "pointer"
      ]
    ],
    [
      "00a9ed78",
      "DATA",
      [
        "storage",
        "00c24654",
        null,
        null
      ]
    ],
    [
      "00a9edb4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9edd4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9ed88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e9fc.md#insn-00a9ed88) · [`00a9eda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e9fc.md#insn-00a9eda4)
- 新版 `00a9edcc`（命令位置の公開資料なし）

~~~diff
- 00a9ed88 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a9ed88 ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
- 00a9ed88 bytes 08010035
- 00a9eda4 ["INT_EQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00a9eda4 ["CBRANCH", null, ["local:b26:8", "tmp:0:1"]]
- 00a9eda4 bytes 08030034
+ 00a9edcc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00a9edcc ["CBRANCH", null, ["local:b23:8", "tmp:0:1"]]
+ 00a9edcc bytes 08010035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c6fea9d071c87b6b3da2f05d8e4fca"></a>

### [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md) → [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md) FUN_00a9f124

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 48件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a9e9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e9fc.md) [`00a9f954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f954.md) [`00a9f9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f9fc.md) [`00a9fb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 48件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a9ea40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9e/00a9ea40.md) [`00a9f998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f998.md) [`00a9fa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9fa40.md) [`00a9fbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9fbcc.md) · 呼出先 5件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 65.32% / 新版 65.32%

CFGの説明率　旧版 26.14% / 新版 25.99%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 32件, `unresolved_call_alignment` 14件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f1a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f254"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9f268"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a9f168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00a9f140"
      ]
    ],
    [
      "unmatched:00a9f13c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f1a4"
      ]
    ],
    [
      "unmatched:00a9f14c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f178"
      ]
    ]
  ],
  "added": [
    [
      "00a9f168",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f184"
      ]
    ],
    [
      "00a9f180",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f1a4"
      ]
    ],
    [
      "00a9f190",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9f178"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9f1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md#insn-00a9f1a0)
- 新版 `00a9f1a0`（命令位置の公開資料なし） · `00a9f1e4`（命令位置の公開資料なし）

~~~diff
- 00a9f1a0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d48:8"]]
- 00a9f1a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00a9f1a0 bytes 28a706f9
+ 00a9f1a0 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00a9f1a0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00a9f1a0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00a9f1a0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00a9f1a0 bytes da220091
+ 00a9f1e4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d48:8"]]
+ 00a9f1e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00a9f1e4 bytes 28a706f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eec713b909665839909306f8c0a1afb3"></a>

### [`00a9f838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md) → [`00a9f87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f87c.md) FUN_00a9f87c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 44.44% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00a9f868",
      "incomplete_value": true,
      "site": "00a9f86c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00a9f894",
      "DATA",
      [
        "storage",
        "00239df0",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00a9f8d8",
      "DATA",
      [
        "storage",
        "00239df0",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9f86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md#insn-00a9f86c) · [`00a9f858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md#insn-00a9f858) · [`00a9f874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md#insn-00a9f874)
- 新版 `00a9f8b0`（命令位置の公開資料なし） · `00a9f89c`（命令位置の公開資料なし） · `00a9f8b8`（命令位置の公開資料なし）

~~~diff
- 00a9f86c ["INT_ADD", "register:40f0:8", ["const:a9f86c:8", "const:4:8"]]
- 00a9f86c ["CALL", null, ["callee:005c2710:8"]]
+ 00a9f8b0 ["INT_ADD", "register:40f0:8", ["const:a9f8b0:8", "const:4:8"]]
+ 00a9f8b0 ["CALL", null, ["callee:005c2710:8"]]
- 00a9f86c bytes a98bec97
+ 00a9f8b0 bytes 988bec97
- 00a9f858 ["INT_ADD", "register:40f0:8", ["const:a9f858:8", "const:4:8"]]
- 00a9f858 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9f89c ["INT_ADD", "register:40f0:8", ["const:a9f89c:8", "const:4:8"]]
+ 00a9f89c ["CALL", null, ["callee:0081f580:8"]]
- 00a9f858 bytes 4afff597
+ 00a9f89c bytes 39fff597
- 00a9f874 ["INT_ADD", "register:40f0:8", ["const:a9f874:8", "const:4:8"]]
- 00a9f874 ["CALL", null, ["callee:0081f580:8"]]
+ 00a9f8b8 ["INT_ADD", "register:40f0:8", ["const:a9f8b8:8", "const:4:8"]]
+ 00a9f8b8 ["CALL", null, ["callee:0081f580:8"]]
- 00a9f874 bytes 43fff597
+ 00a9f8b8 bytes 32fff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab2f2dcda17ad295cfdb76dd13a2a7b"></a>

### [`00a9f9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f9fc.md) → [`00a9fa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9fa40.md) FUN_00a9fa40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006453ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00645/006453ac.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 7件 [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`00644304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00644/00644304.md) [`007cf950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf950.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006453ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006453ac.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 7件 [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`00644304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00644/00644304.md) [`007cf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf950.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 50.00% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9fb0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9fb4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00a9fb50"
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
      "unmatched:00a9fb0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9fbc8"
      ]
    ],
    [
      "unmatched:00a9fb4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9fbc8"
      ]
    ]
  ],
  "added": [
    [
      "00a9fb50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9fbc8"
      ]
    ],
    [
      "00a9fb90",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00a9fbc8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9fb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f9fc.md#insn-00a9fb0c) · [`00a9fb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f9fc.md#insn-00a9fb4c)
- 新版 `00a9fb4c`（命令位置の公開資料なし）

~~~diff
- 00a9fb0c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a9fb0c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00a9fb0c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00a9fb0c bytes c9030054
- 00a9fb4c ["BOOL_NEGATE", "tmp:0:1", ["register:102:1"]]
- 00a9fb4c ["BOOL_OR", "tmp:1:1", ["tmp:0:1", "register:101:1"]]
- 00a9fb4c ["CBRANCH", null, ["local:b15:8", "tmp:1:1"]]
- 00a9fb4c bytes c9010054
+ 00a9fb4c ["INT_LESSEQUAL", "register:105:1", ["register:4050:8", "register:4048:8"]]
+ 00a9fb4c ["INT_SBORROW", "register:106:1", ["register:4048:8", "register:4050:8"]]
+ 00a9fb4c ["INT_SUB", "tmp:0:8", ["register:4048:8", "register:4050:8"]]
+ 00a9fb4c ["INT_SLESS", "register:107:1", ["tmp:0:8", "const:0:8"]]
+ 00a9fb4c bytes 3f010aeb
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28abb97a8d39b73255f87e10e4cf906c"></a>

### [`00a9fb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md) → [`00a9fbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9fbcc.md) FUN_00a9fbcc

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006e4/006e4aec.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 15件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0066398c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/0066398c.md) [`0078aefc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078a/0078aefc.md) [`0078af80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0078a/0078af80.md) [`007bd9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007bd/007bd9d0.md)
- 新版 呼出元 2件 [`006e4aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006e4/006e4aec.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 15件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0066398c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/0066398c.md) [`0078aefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078a/0078aefc.md) [`0078af80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0078a/0078af80.md) [`007bd9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007bd/007bd9d0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.37% / 新版 82.37%

CFGの説明率　旧版 34.26% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `return_value_candidate` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9fb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9fb8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00a9fb90"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00a9fb8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9fb90",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00a9fb94",
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
      "00a9fbd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00a9fbd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00a9fbd8",
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

- 旧版 [`00a9fb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md#insn-00a9fb8c) · [`00a9fb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md#insn-00a9fb90) · [`00a9fb94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9fb88.md#insn-00a9fb94)

~~~diff
- 00a9fb8c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00a9fb8c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00a9fb8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00a9fb8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9fb8c bytes fd7b02a9
- 00a9fb90 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00a9fb90 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00a9fb90 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00a9fb90 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9fb90 bytes fc6f03a9
- 00a9fb94 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00a9fb94 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00a9fb94 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00a9fb94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00a9fb94 bytes fa6704a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f007697da69c699a9a1129dd16ab9115"></a>

### [`00aa02cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa02cc.md) → [`00aa0310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0310.md) FUN_00aa0310

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 72.09% / 新版 72.09%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa02cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa02cc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa02d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa02cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa02d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa02d4",
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
      "00aa0310",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0314",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0318",
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

- 旧版 [`00aa02cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa02cc.md#insn-00aa02cc) · [`00aa02d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa02cc.md#insn-00aa02d0) · [`00aa02d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa02cc.md#insn-00aa02d4)

~~~diff
- 00aa02cc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa02cc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa02cc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa02cc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa02cc bytes fd7bbda9
- 00aa02d0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa02d0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa02d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa02d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa02d0 bytes f65701a9
- 00aa02d4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa02d4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa02d4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa02d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa02d4 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e13f07e8f160ba7ce411a1070aba617f"></a>

### [`00aa0378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0378.md) → [`00aa03bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa03bc.md) FUN_00aa03bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa0394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0378.md#insn-00aa0394) · [`00aa03a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0378.md#insn-00aa03a8) · [`00aa03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0378.md#insn-00aa03b0)
- 新版 `00aa03d8`（命令位置の公開資料なし） · `00aa03ec`（命令位置の公開資料なし） · `00aa03f4`（命令位置の公開資料なし）

~~~diff
- 00aa0394 ["INT_ADD", "register:40f0:8", ["const:aa0394:8", "const:4:8"]]
- 00aa0394 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa03d8 ["INT_ADD", "register:40f0:8", ["const:aa03d8:8", "const:4:8"]]
+ 00aa03d8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa0394 bytes 7bfcf597
+ 00aa03d8 bytes 6afcf597
- 00aa03a8 ["INT_ADD", "register:40f0:8", ["const:aa03a8:8", "const:4:8"]]
- 00aa03a8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa03ec ["INT_ADD", "register:40f0:8", ["const:aa03ec:8", "const:4:8"]]
+ 00aa03ec ["CALL", null, ["callee:005c2710:8"]]
- 00aa03a8 bytes da88ec97
+ 00aa03ec bytes c988ec97
- 00aa03b0 ["INT_ADD", "register:40f0:8", ["const:aa03b0:8", "const:4:8"]]
- 00aa03b0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa03f4 ["INT_ADD", "register:40f0:8", ["const:aa03f4:8", "const:4:8"]]
+ 00aa03f4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa03b0 bytes 74fcf597
+ 00aa03f4 bytes 63fcf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-711133df6ed2cd2b147e64486af08df1"></a>

### [`00aa04c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa04c8.md) → [`00aa050c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa050c.md) FUN_00aa050c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00956d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00956/00956d58.md) · 呼出先 4件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 1件 [`00956d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00956/00956d58.md) · 呼出先 4件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa0538",
      "incomplete_value": true,
      "site": "00aa053c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa04f4",
      "incomplete_value": true,
      "site": "00aa04f8",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
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
      "definition_site": "00aa056c",
      "incomplete_value": true,
      "site": "00aa058c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
      "definition_site": "00aa0564",
      "incomplete_value": true,
      "site": "00aa058c",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
          ]
        ]
      ]
    },
    "old": null,
    "ordinal": 3,
    "slot": 2
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa04f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa04c8.md#insn-00aa04f8) · [`00aa0548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa04c8.md#insn-00aa0548) · [`00aa04e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa04c8.md#insn-00aa04e4)
- 新版 `00aa053c`（命令位置の公開資料なし） · `00aa058c`（命令位置の公開資料なし） · `00aa0528`（命令位置の公開資料なし）

~~~diff
- 00aa04f8 ["INT_ADD", "register:40f0:8", ["const:aa04f8:8", "const:4:8"]]
- 00aa04f8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa053c ["INT_ADD", "register:40f0:8", ["const:aa053c:8", "const:4:8"]]
+ 00aa053c ["CALL", null, ["callee:005c2710:8"]]
- 00aa04f8 bytes 8688ec97
+ 00aa053c bytes 7588ec97
- 00aa0548 ["INT_ADD", "register:40f0:8", ["const:aa0548:8", "const:4:8"]]
- 00aa0548 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa058c ["INT_ADD", "register:40f0:8", ["const:aa058c:8", "const:4:8"]]
+ 00aa058c ["CALL", null, ["callee:00a9f124:8"]]
- 00aa0548 bytes e6faff97
+ 00aa058c bytes e6faff97
- 00aa04e4 ["INT_ADD", "register:40f0:8", ["const:aa04e4:8", "const:4:8"]]
- 00aa04e4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa0528 ["INT_ADD", "register:40f0:8", ["const:aa0528:8", "const:4:8"]]
+ 00aa0528 ["CALL", null, ["callee:0081f580:8"]]
- 00aa04e4 bytes 27fcf597
+ 00aa0528 bytes 16fcf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ae892531fa6d769b1f50d1e22300429"></a>

### [`00aa0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0568.md) → [`00aa05ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa05ac.md) FUN_00aa05ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0059e424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059e/0059e424.md) [`0059f0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f0c8.md) [`0059f288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f288.md) [`0059f454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059f454.md) · 呼出先 14件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`005c2f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2f30.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md)
- 新版 呼出元 12件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) [`0059e424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059e/0059e424.md) [`0059f0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f0c8.md) [`0059f288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f288.md) [`0059f454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059f/0059f454.md) · 呼出先 14件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`0047c518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c518.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`005c2f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2f30.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 33.90% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 5件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa056c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa056c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0570"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa056c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0570",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0574",
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
      "00aa05b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aa05b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aa05b8",
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

- 旧版 [`00aa056c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0568.md#insn-00aa056c) · [`00aa0570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0568.md#insn-00aa0570) · [`00aa0574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0568.md#insn-00aa0574)

~~~diff
- 00aa056c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa056c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa056c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa056c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa056c bytes fd7b02a9
- 00aa0570 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00aa0570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00aa0570 bytes f91b00f9
- 00aa0574 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00aa0574 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00aa0574 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aa0574 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0574 bytes f85f04a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9461827495220e09cffaabc8e048569"></a>

### [`00aa0a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0a1c.md) → [`00aa0a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0a60.md) FUN_00aa0a60

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 67.65% / 新版 67.65%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0a8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa0ad0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa0a8c",
      "incomplete_value": true,
      "site": "00aa0a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa0a48",
      "incomplete_value": true,
      "site": "00aa0a4c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00aa0a90",
      "DATA",
      [
        "storage",
        "00239dc8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa0ad4",
      "DATA",
      [
        "storage",
        "00239dc8",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0a1c.md#insn-00aa0a4c) · [`00aa0a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0a1c.md#insn-00aa0a8c)
- 新版 `00aa0a90`（命令位置の公開資料なし） · `00aa0a8c`（命令位置の公開資料なし）

~~~diff
- 00aa0a4c ["INT_ADD", "register:40f0:8", ["const:aa0a4c:8", "const:4:8"]]
- 00aa0a4c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa0a90 ["INT_ADD", "register:40f0:8", ["const:aa0a90:8", "const:4:8"]]
+ 00aa0a90 ["CALL", null, ["callee:005c2710:8"]]
- 00aa0a4c bytes 3187ec97
+ 00aa0a90 bytes 2087ec97
- 00aa0a8c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa0a8c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aa0a8c ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa0a8c ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00aa0a8c bytes 0801899a
+ 00aa0a8c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aa0a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa0a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa0a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aa0a8c bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10b994ca31134195a90999763e3fc219"></a>

### [`00aa0aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0aa4.md) → [`00aa0ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0ae8.md) FUN_00aa0ae8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 55.88% / 新版 55.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0aa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0aa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0aa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0aa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0aac",
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
      "00aa0ae8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0aec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0af0",
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

- 旧版 [`00aa0aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0aa4.md#insn-00aa0aa4) · [`00aa0aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0aa4.md#insn-00aa0aa8) · [`00aa0aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0aa4.md#insn-00aa0aac)

~~~diff
- 00aa0aa4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0aa4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0aa4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0aa4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0aa4 bytes fd7bbda9
- 00aa0aa8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa0aa8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa0aa8 bytes f50b00f9
- 00aa0aac ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0aac ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0aac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0aac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0aac bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-723cd32be9da76a9cfd3b5beee3d0926"></a>

### [`00aa0b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0b2c.md) → [`00aa0b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0b70.md) FUN_00aa0b70

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0b2c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0b30"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0b2c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0b30",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0b34",
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
      "00aa0b70",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0b74",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0b78",
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

- 旧版 [`00aa0b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0b2c.md#insn-00aa0b2c) · [`00aa0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0b2c.md#insn-00aa0b30) · [`00aa0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0b2c.md#insn-00aa0b34)

~~~diff
- 00aa0b2c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0b2c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0b2c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0b2c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0b2c bytes fd7bbda9
- 00aa0b30 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa0b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa0b30 bytes f50b00f9
- 00aa0b34 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0b34 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0b34 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0b34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0b34 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4f3f8e5387b991593c04459b35520a5"></a>

### [`00aa0bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0bb4.md) → [`00aa0bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0bf8.md) FUN_00aa0bf8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 55.88% / 新版 55.88%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0bb4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0bb8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0bb4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0bb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0bbc",
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
      "00aa0bf8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0bfc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0c00",
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

- 旧版 [`00aa0bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0bb4.md#insn-00aa0bb4) · [`00aa0bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0bb4.md#insn-00aa0bb8) · [`00aa0bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0bb4.md#insn-00aa0bbc)

~~~diff
- 00aa0bb4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0bb4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0bb4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0bb4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0bb4 bytes fd7bbda9
- 00aa0bb8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa0bb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa0bb8 bytes f50b00f9
- 00aa0bbc ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0bbc ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0bbc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0bbc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0bbc bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68391988493b1009844b12dfacef35a7"></a>

### [`00aa0c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0c3c.md) → [`00aa0c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0c80.md) FUN_00aa0c80

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_store_alignment

命令の説明率　旧版 51.11% / 新版 51.11%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0c3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0c40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0c3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0c44",
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
      "00aa0c80",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0c84",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0c88",
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

- 旧版 [`00aa0c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0c3c.md#insn-00aa0c3c) · [`00aa0c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0c3c.md#insn-00aa0c40) · [`00aa0c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0c3c.md#insn-00aa0c44)

~~~diff
- 00aa0c3c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0c3c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0c3c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0c3c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0c3c bytes fd7bbda9
- 00aa0c40 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa0c40 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa0c40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa0c40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0c40 bytes f65701a9
- 00aa0c44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0c44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0c44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0c44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0c44 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0429b3a806d5ec1d792a93957a51150d"></a>

### [`00aa0cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0cf0.md) → [`00aa0d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0d34.md) FUN_00aa0d34

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`009f560c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f5/009f560c.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`009f5650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f5/009f5650.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 66.67% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0cf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0cf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0cf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0cf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0cf8",
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
      "00aa0d34",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0d38",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0d3c",
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

- 旧版 [`00aa0cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0cf0.md#insn-00aa0cf0) · [`00aa0cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0cf0.md#insn-00aa0cf4) · [`00aa0cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0cf0.md#insn-00aa0cf8)

~~~diff
- 00aa0cf0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0cf0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0cf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0cf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0cf0 bytes fd7bbda9
- 00aa0cf4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa0cf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa0cf4 bytes f50b00f9
- 00aa0cf8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0cf8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0cf8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0cf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0cf8 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a69133dfccc56eb73a027cafc9b7fd91"></a>

### [`00aa0d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0d78.md) → [`00aa0dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0dbc.md) FUN_00aa0dbc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`009f560c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f5/009f560c.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`009f5650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f5/009f5650.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 40.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0de8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa0e2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa0dec",
      "incomplete_value": true,
      "site": "00aa0dfc",
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
              [
                "live",
                "register:4040:8"
              ]
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


#### 変更候補の命令位置

- 旧版 [`00aa0de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0d78.md#insn-00aa0de8) · [`00aa0d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0d78.md#insn-00aa0d94)
- 新版 `00aa0e2c`（命令位置の公開資料なし） · `00aa0dd8`（命令位置の公開資料なし）

~~~diff
- 00aa0de8 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa0de8 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aa0de8 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa0de8 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00aa0de8 bytes 0801899a
+ 00aa0e2c ["COPY", "tmp:0:8", ["register:4040:8"]]
+ 00aa0e2c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
+ 00aa0e2c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aa0e2c ["COPY", "register:4040:8", ["tmp:0:8"]]
+ 00aa0e2c bytes 0801899a
- 00aa0d94 ["INT_ADD", "register:40f0:8", ["const:aa0d94:8", "const:4:8"]]
- 00aa0d94 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa0dd8 ["INT_ADD", "register:40f0:8", ["const:aa0dd8:8", "const:4:8"]]
+ 00aa0dd8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa0d94 bytes fbf9f597
+ 00aa0dd8 bytes eaf9f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f14012c492ee4c42f2d763b3bd83ab"></a>

### [`00aa0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0e90.md) → [`00aa0ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0ed4.md) FUN_00aa0ed4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`005bcea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa0eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0e90.md#insn-00aa0eac) · [`00aa0ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0e90.md#insn-00aa0ec0) · [`00aa0ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0e90.md#insn-00aa0ec8)
- 新版 `00aa0ef0`（命令位置の公開資料なし） · `00aa0f04`（命令位置の公開資料なし） · `00aa0f0c`（命令位置の公開資料なし）

~~~diff
- 00aa0eac ["INT_ADD", "register:40f0:8", ["const:aa0eac:8", "const:4:8"]]
- 00aa0eac ["CALL", null, ["callee:0081f580:8"]]
+ 00aa0ef0 ["INT_ADD", "register:40f0:8", ["const:aa0ef0:8", "const:4:8"]]
+ 00aa0ef0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa0eac bytes b5f9f597
+ 00aa0ef0 bytes a4f9f597
- 00aa0ec0 ["INT_ADD", "register:40f0:8", ["const:aa0ec0:8", "const:4:8"]]
- 00aa0ec0 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa0f04 ["INT_ADD", "register:40f0:8", ["const:aa0f04:8", "const:4:8"]]
+ 00aa0f04 ["CALL", null, ["callee:005c2710:8"]]
- 00aa0ec0 bytes 1486ec97
+ 00aa0f04 bytes 0386ec97
- 00aa0ec8 ["INT_ADD", "register:40f0:8", ["const:aa0ec8:8", "const:4:8"]]
- 00aa0ec8 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa0f0c ["INT_ADD", "register:40f0:8", ["const:aa0f0c:8", "const:4:8"]]
+ 00aa0f0c ["CALL", null, ["callee:0081f580:8"]]
- 00aa0ec8 bytes aef9f597
+ 00aa0f0c bytes 9df9f597
~~~


<a id="compare-d267ac0b1764f61108bccfe80c4a907a"></a>

### [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) → [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) FUN_00aa0f64

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) · 呼出先 67件 [`00a9f838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f838.md) [`00aa147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa147c.md) [`00aa1524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1524.md) [`00aa164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa164c.md) [`00aa16f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa16f4.md)
- 新版 呼出元 1件 [`0059815c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00598/0059815c.md) · 呼出先 67件 [`00a9f87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f87c.md) [`00aa14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa14c0.md) [`00aa1568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1568.md) [`00aa1690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1690.md) [`00aa1738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1738.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.17% / 新版 94.17%

CFGの説明率　旧版 30.89% / 新版 28.64%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0f20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa0f24"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa0f20",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0f24",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa0f28",
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
      "00aa0f64",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa0f68",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa0f6c",
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

- 旧版 [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md#insn-00aa0f20) · [`00aa0f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md#insn-00aa0f24) · [`00aa0f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md#insn-00aa0f28)

~~~diff
- 00aa0f20 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa0f20 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa0f20 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa0f20 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa0f20 bytes fd7bbda9
- 00aa0f24 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa0f24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa0f24 bytes f50b00f9
- 00aa0f28 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa0f28 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa0f28 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa0f28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa0f28 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ac678a544603c39d123b60acff41dc4"></a>

### [`00aa147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa147c.md) → [`00aa14c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa14c0.md) FUN_00aa14c0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa147c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa147c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1480"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa147c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1480",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa14d4",
      "DATA",
      [
        "storage",
        "00239e1c",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa14c0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa14c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa1518",
      "DATA",
      [
        "storage",
        "00239e1c",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa147c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa147c.md#insn-00aa147c) · [`00aa1480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa147c.md#insn-00aa1480) · [`00aa14ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa147c.md#insn-00aa14ac)
- 新版 `00aa14f0`（命令位置の公開資料なし）

~~~diff
- 00aa147c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa147c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa147c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa147c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa147c bytes fd7bbda9
- 00aa1480 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa1480 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa1480 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa1480 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa1480 bytes f65701a9
- 00aa14ac ["INT_ADD", "register:40f0:8", ["const:aa14ac:8", "const:4:8"]]
- 00aa14ac ["CALL", null, ["callee:005c2710:8"]]
+ 00aa14f0 ["INT_ADD", "register:40f0:8", ["const:aa14f0:8", "const:4:8"]]
+ 00aa14f0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa14ac bytes 9984ec97
+ 00aa14f0 bytes 8884ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27eacb004e44ab476b208857eeb96209"></a>

### [`00aa1524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1524.md) → [`00aa1568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1568.md) FUN_00aa1568

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 5件 [`0044abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 5件 [`0044abe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abe4.md) [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.14% / 新版 85.14%

CFGの説明率　旧版 8.00% / 新版 8.70%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1524"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1528"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa1524",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1528",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa152c",
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
      "00aa1568",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aa156c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa1570",
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

- 旧版 [`00aa1524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1524.md#insn-00aa1524) · [`00aa1528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1524.md#insn-00aa1528) · [`00aa152c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1524.md#insn-00aa152c)

~~~diff
- 00aa1524 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa1524 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa1524 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aa1524 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa1524 bytes fd7bbca9
- 00aa1528 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa1528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00aa1528 bytes f70b00f9
- 00aa152c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa152c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa152c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa152c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa152c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-779b8417588b95ada0fdfdf8cbb91969"></a>

### [`00aa164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa164c.md) → [`00aa1690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1690.md) FUN_00aa1690

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa164c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa164c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1650"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa164c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1650",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1654",
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
      "00aa1690",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa1694",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa1698",
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

- 旧版 [`00aa164c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa164c.md#insn-00aa164c) · [`00aa1650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa164c.md#insn-00aa1650) · [`00aa1654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa164c.md#insn-00aa1654)

~~~diff
- 00aa164c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa164c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa164c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa164c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa164c bytes fd7bbda9
- 00aa1650 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa1650 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa1650 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa1650 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa1650 bytes f65701a9
- 00aa1654 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa1654 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa1654 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa1654 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa1654 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0398c71e52aeab4b5ce9b93c7eec3def"></a>

### [`00aa16f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa16f4.md) → [`00aa1738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1738.md) FUN_00aa1738

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa1764",
      "incomplete_value": true,
      "site": "00aa1768",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa1720",
      "incomplete_value": true,
      "site": "00aa1724",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
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
      "unmatched:00aa174c",
      "DATA",
      [
        "storage",
        "00239e04",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa1790",
      "DATA",
      [
        "storage",
        "00239e04",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa16f4.md#insn-00aa1724) · [`00aa1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa16f4.md#insn-00aa1710) · [`00aa1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa16f4.md#insn-00aa1720)
- 新版 `00aa1768`（命令位置の公開資料なし） · `00aa1754`（命令位置の公開資料なし）

~~~diff
- 00aa1724 ["INT_ADD", "register:40f0:8", ["const:aa1724:8", "const:4:8"]]
- 00aa1724 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1768 ["INT_ADD", "register:40f0:8", ["const:aa1768:8", "const:4:8"]]
+ 00aa1768 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1724 bytes fb83ec97
+ 00aa1768 bytes ea83ec97
- 00aa1710 ["INT_ADD", "register:40f0:8", ["const:aa1710:8", "const:4:8"]]
- 00aa1710 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1754 ["INT_ADD", "register:40f0:8", ["const:aa1754:8", "const:4:8"]]
+ 00aa1754 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1710 bytes 9cf7f597
+ 00aa1754 bytes 8bf7f597
- 00aa1720 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa1720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa1720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa1720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa1720 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a97e2511bb442fdf544a026d9f590e40"></a>

### [`00aa1844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1844.md) → [`00aa1888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1888.md) FUN_00aa1888

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 61.90% / 新版 38.24%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa18b4",
      "incomplete_value": true,
      "site": "00aa18b8",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa1870",
      "incomplete_value": true,
      "site": "00aa1874",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1844.md#insn-00aa1874) · [`00aa18b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1844.md#insn-00aa18b8) · [`00aa1860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1844.md#insn-00aa1860)
- 新版 `00aa18b8`（命令位置の公開資料なし） · `00aa18a4`（命令位置の公開資料なし）

~~~diff
- 00aa1874 ["INT_ADD", "register:40f0:8", ["const:aa1874:8", "const:4:8"]]
- 00aa1874 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa18b8 ["INT_ADD", "register:40f0:8", ["const:aa18b8:8", "const:4:8"]]
+ 00aa18b8 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1874 bytes a783ec97
+ 00aa18b8 bytes 9683ec97
- 00aa18b8 ["INT_SEXT", "tmp:0:8", ["register:4098:4"]]
- 00aa18b8 ["INT_SEXT", "tmp:1:8", ["register:4048:4"]]
- 00aa18b8 ["INT_MULT", "tmp:2:8", ["tmp:0:8", "tmp:1:8"]]
- 00aa18b8 ["INT_ADD", "register:4040:8", ["register:4040:8", "tmp:2:8"]]
- 00aa18b8 bytes 6822299b
- 00aa1860 ["INT_ADD", "register:40f0:8", ["const:aa1860:8", "const:4:8"]]
- 00aa1860 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa18a4 ["INT_ADD", "register:40f0:8", ["const:aa18a4:8", "const:4:8"]]
+ 00aa18a4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1860 bytes 48f7f597
+ 00aa18a4 bytes 37f7f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65a0890cef0a2e6dd5ae087572a6d65e"></a>

### [`00aa1a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1a68.md) → [`00aa1aac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1aac.md) FUN_00aa1aac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 4件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 41.94% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa1ad8",
      "incomplete_value": true,
      "site": "00aa1adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
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
      "00aa1ae8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1b30"
      ]
    ],
    [
      "unmatched:00aa1aec",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1af0",
      "READ",
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
      "00aa1ae8",
      "UNCONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1b14"
      ]
    ],
    [
      "00aa1b14",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aa1b18",
      "READ",
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

- 旧版 [`00aa1a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1a68.md#insn-00aa1a98) · [`00aa1a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1a68.md#insn-00aa1a84) · [`00aa1a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1a68.md#insn-00aa1a9c)
- 新版 `00aa1adc`（命令位置の公開資料なし） · `00aa1ac8`（命令位置の公開資料なし） · `00aa1ae0`（命令位置の公開資料なし）

~~~diff
- 00aa1a98 ["INT_ADD", "register:40f0:8", ["const:aa1a98:8", "const:4:8"]]
- 00aa1a98 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1adc ["INT_ADD", "register:40f0:8", ["const:aa1adc:8", "const:4:8"]]
+ 00aa1adc ["CALL", null, ["callee:005c2710:8"]]
- 00aa1a98 bytes 1e83ec97
+ 00aa1adc bytes 0d83ec97
- 00aa1a84 ["INT_ADD", "register:40f0:8", ["const:aa1a84:8", "const:4:8"]]
- 00aa1a84 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1ac8 ["INT_ADD", "register:40f0:8", ["const:aa1ac8:8", "const:4:8"]]
+ 00aa1ac8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1a84 bytes bff6f597
+ 00aa1ac8 bytes aef6f597
- 00aa1a9c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa1a9c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa1a9c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa1a9c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa1ae0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa1ae0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa1ae0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa1ae0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa1a9c bytes 60000037
+ 00aa1ae0 bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7db9f3e15b7fb1ab7828431b27372e8"></a>

### [`00aa1afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1afc.md) → [`00aa1b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1b40.md) FUN_00aa1b40

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 4件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 10.00% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1afc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1b00"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa1afc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1b00",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa1b04",
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
      "00aa1b40",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa1b44",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa1b48",
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

- 旧版 [`00aa1afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1afc.md#insn-00aa1afc) · [`00aa1b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1afc.md#insn-00aa1b00) · [`00aa1b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1afc.md#insn-00aa1b04)

~~~diff
- 00aa1afc ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa1afc ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa1afc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa1afc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa1afc bytes fd7bbda9
- 00aa1b00 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aa1b00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00aa1b00 bytes f50b00f9
- 00aa1b04 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa1b04 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa1b04 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa1b04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa1b04 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40736004ca61fc77ee2f602dbc7c9c30"></a>

### [`00aa1c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1c24.md) → [`00aa1c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1c68.md) FUN_00aa1c68

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 4件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 4件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 66.67% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa1c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1c24.md#insn-00aa1c40) · [`00aa1c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1c24.md#insn-00aa1c54) · [`00aa1c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1c24.md#insn-00aa1c64)
- 新版 `00aa1c84`（命令位置の公開資料なし） · `00aa1c98`（命令位置の公開資料なし） · `00aa1ca8`（命令位置の公開資料なし）

~~~diff
- 00aa1c40 ["INT_ADD", "register:40f0:8", ["const:aa1c40:8", "const:4:8"]]
- 00aa1c40 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1c84 ["INT_ADD", "register:40f0:8", ["const:aa1c84:8", "const:4:8"]]
+ 00aa1c84 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1c40 bytes 50f6f597
+ 00aa1c84 bytes 3ff6f597
- 00aa1c54 ["INT_ADD", "register:40f0:8", ["const:aa1c54:8", "const:4:8"]]
- 00aa1c54 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1c98 ["INT_ADD", "register:40f0:8", ["const:aa1c98:8", "const:4:8"]]
+ 00aa1c98 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1c54 bytes af82ec97
+ 00aa1c98 bytes 9e82ec97
- 00aa1c64 ["INT_ADD", "register:40f0:8", ["const:aa1c64:8", "const:4:8"]]
- 00aa1c64 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1ca8 ["INT_ADD", "register:40f0:8", ["const:aa1ca8:8", "const:4:8"]]
+ 00aa1ca8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1c64 bytes 47f6f597
+ 00aa1ca8 bytes 36f6f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1147d4fc36cb8cfb6554a29f66a11fe7"></a>

### [`00aa1cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1cb8.md) → [`00aa1cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1cfc.md) FUN_00aa1cfc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa1cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1cb8.md#insn-00aa1cd4) · [`00aa1ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1cb8.md#insn-00aa1ce8) · [`00aa1cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1cb8.md#insn-00aa1cf0)
- 新版 `00aa1d18`（命令位置の公開資料なし） · `00aa1d2c`（命令位置の公開資料なし） · `00aa1d34`（命令位置の公開資料なし）

~~~diff
- 00aa1cd4 ["INT_ADD", "register:40f0:8", ["const:aa1cd4:8", "const:4:8"]]
- 00aa1cd4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1d18 ["INT_ADD", "register:40f0:8", ["const:aa1d18:8", "const:4:8"]]
+ 00aa1d18 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1cd4 bytes 2bf6f597
+ 00aa1d18 bytes 1af6f597
- 00aa1ce8 ["INT_ADD", "register:40f0:8", ["const:aa1ce8:8", "const:4:8"]]
- 00aa1ce8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1d2c ["INT_ADD", "register:40f0:8", ["const:aa1d2c:8", "const:4:8"]]
+ 00aa1d2c ["CALL", null, ["callee:005c2710:8"]]
- 00aa1ce8 bytes 8a82ec97
+ 00aa1d2c bytes 7982ec97
- 00aa1cf0 ["INT_ADD", "register:40f0:8", ["const:aa1cf0:8", "const:4:8"]]
- 00aa1cf0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa1d34 ["INT_ADD", "register:40f0:8", ["const:aa1d34:8", "const:4:8"]]
+ 00aa1d34 ["CALL", null, ["callee:0081f580:8"]]
- 00aa1cf0 bytes 24f6f597
+ 00aa1d34 bytes 13f6f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653fa074e0783363b7c147f6ae3ce2cb"></a>

### [`00aa1d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1d60.md) → [`00aa1da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa1/00aa1da4.md) FUN_00aa1da4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 28.57% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa1d84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa1dc8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa1e38",
      "incomplete_value": true,
      "site": "00aa1e3c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00aa1d84",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1e08"
      ]
    ],
    [
      "unmatched:00aa1e64",
      "DATA",
      [
        "storage",
        "00239e14",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa1dc8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa1e08"
      ]
    ],
    [
      "00aa1ea8",
      "DATA",
      [
        "storage",
        "00239e14",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa1d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1d60.md#insn-00aa1d84) · [`00aa1e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa1/00aa1d60.md#insn-00aa1e3c)
- 新版 `00aa1dc8`（命令位置の公開資料なし） · `00aa1e80`（命令位置の公開資料なし）

~~~diff
- 00aa1d84 ["CBRANCH", null, ["local:b3:8", "register:101:1"]]
- 00aa1d84 bytes 00020054
+ 00aa1dc8 ["CBRANCH", null, ["local:b4:8", "register:101:1"]]
+ 00aa1dc8 bytes 00020054
- 00aa1e3c ["INT_ADD", "register:40f0:8", ["const:aa1e3c:8", "const:4:8"]]
- 00aa1e3c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa1e80 ["INT_ADD", "register:40f0:8", ["const:aa1e80:8", "const:4:8"]]
+ 00aa1e80 ["CALL", null, ["callee:005c2710:8"]]
- 00aa1e3c bytes 3582ec97
+ 00aa1e80 bytes 2482ec97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db5ff727937709df6ed661f86779e0e5"></a>

### [`00aa200c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa200c.md) → [`00aa2050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2050.md) FUN_00aa2050

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa2028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa200c.md#insn-00aa2028) · [`00aa203c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa200c.md#insn-00aa203c) · [`00aa2044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa200c.md#insn-00aa2044)
- 新版 `00aa206c`（命令位置の公開資料なし） · `00aa2080`（命令位置の公開資料なし） · `00aa2088`（命令位置の公開資料なし）

~~~diff
- 00aa2028 ["INT_ADD", "register:40f0:8", ["const:aa2028:8", "const:4:8"]]
- 00aa2028 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa206c ["INT_ADD", "register:40f0:8", ["const:aa206c:8", "const:4:8"]]
+ 00aa206c ["CALL", null, ["callee:0081f580:8"]]
- 00aa2028 bytes 56f5f597
+ 00aa206c bytes 45f5f597
- 00aa203c ["INT_ADD", "register:40f0:8", ["const:aa203c:8", "const:4:8"]]
- 00aa203c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa2080 ["INT_ADD", "register:40f0:8", ["const:aa2080:8", "const:4:8"]]
+ 00aa2080 ["CALL", null, ["callee:005c2710:8"]]
- 00aa203c bytes b581ec97
+ 00aa2080 bytes a481ec97
- 00aa2044 ["INT_ADD", "register:40f0:8", ["const:aa2044:8", "const:4:8"]]
- 00aa2044 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2088 ["INT_ADD", "register:40f0:8", ["const:aa2088:8", "const:4:8"]]
+ 00aa2088 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2044 bytes 4ff5f597
+ 00aa2088 bytes 3ef5f597
~~~


<a id="compare-af001f452295fa0d24a48fe81c2d81a6"></a>

### [`00aa20c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa20c4.md) → [`00aa2108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2108.md) FUN_00aa2108

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2134"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00aa2178"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa2134",
      "incomplete_value": true,
      "site": "00aa2138",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00aa2138",
      "DATA",
      [
        "storage",
        "00239dd4",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa217c",
      "DATA",
      [
        "storage",
        "00239dd4",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa20f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa20c4.md#insn-00aa20f4) · [`00aa2134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa20c4.md#insn-00aa2134) · [`00aa2138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa20c4.md#insn-00aa2138)
- 新版 `00aa2138`（命令位置の公開資料なし）

~~~diff
- 00aa20f4 ["INT_ADD", "register:40f0:8", ["const:aa20f4:8", "const:4:8"]]
- 00aa20f4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa2138 ["INT_ADD", "register:40f0:8", ["const:aa2138:8", "const:4:8"]]
+ 00aa2138 ["CALL", null, ["callee:005c2710:8"]]
- 00aa20f4 bytes 8781ec97
+ 00aa2138 bytes 7681ec97
- 00aa2134 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa2134 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aa2134 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa2134 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00aa2134 bytes 0801899a
- 00aa2138 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa2138 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00aa2138 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00aa2138 bytes 080140b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1ad77666f1abc5a009b2e840f82e1dc"></a>

### [`00aa2154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2154.md) → [`00aa2198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2198.md) FUN_00aa2198

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 68.89% / 新版 68.89%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa2184",
      "incomplete_value": true,
      "site": "00aa2188",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "unmatched:00aa21b0",
      "DATA",
      [
        "storage",
        "002f4924",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa21dc",
      "DATA",
      [
        "storage",
        "002f4918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aa21f4",
      "DATA",
      [
        "storage",
        "002f4924",
        null,
        null
      ]
    ],
    [
      "00aa2220",
      "DATA",
      [
        "storage",
        "002f4918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa2188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2154.md#insn-00aa2188) · [`00aa2174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2154.md#insn-00aa2174) · [`00aa2190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2154.md#insn-00aa2190)
- 新版 `00aa21cc`（命令位置の公開資料なし） · `00aa21b8`（命令位置の公開資料なし） · `00aa21d4`（命令位置の公開資料なし）

~~~diff
- 00aa2188 ["INT_ADD", "register:40f0:8", ["const:aa2188:8", "const:4:8"]]
- 00aa2188 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa21cc ["INT_ADD", "register:40f0:8", ["const:aa21cc:8", "const:4:8"]]
+ 00aa21cc ["CALL", null, ["callee:005c2710:8"]]
- 00aa2188 bytes 6281ec97
+ 00aa21cc bytes 5181ec97
- 00aa2174 ["INT_ADD", "register:40f0:8", ["const:aa2174:8", "const:4:8"]]
- 00aa2174 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa21b8 ["INT_ADD", "register:40f0:8", ["const:aa21b8:8", "const:4:8"]]
+ 00aa21b8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2174 bytes 03f5f597
+ 00aa21b8 bytes f2f4f597
- 00aa2190 ["INT_ADD", "register:40f0:8", ["const:aa2190:8", "const:4:8"]]
- 00aa2190 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa21d4 ["INT_ADD", "register:40f0:8", ["const:aa21d4:8", "const:4:8"]]
+ 00aa21d4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2190 bytes fcf4f597
+ 00aa21d4 bytes ebf4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b4bdb296965141966ac1d1b0b421395"></a>

### [`00aa2208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2208.md) → [`00aa224c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa224c.md) FUN_00aa224c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 52.94% / 新版 52.94%

CFGの説明率　旧版 10.00% / 新版 10.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2280"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa238c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa23e4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa2284",
      "DATA",
      [
        "storage",
        "00239e34",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "unmatched:00aa22a0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005c2710"
      ]
    ],
    [
      "unmatched:00aa22a8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ],
  "added": [
    [
      "00aa22c8",
      "DATA",
      [
        "storage",
        "00239e34",
        null,
        "Elf64_Rela[1792]"
      ]
    ],
    [
      "00aa22e4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "005c2710"
      ]
    ],
    [
      "00aa22ec",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "0081f580"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa2280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2208.md#insn-00aa2280) · [`00aa22a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2208.md#insn-00aa22a0) · [`00aa22a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2208.md#insn-00aa22a8)

~~~diff
- 00aa2280 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa2280 ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00aa2280 ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00aa2280 ["COPY", "register:4040:8", ["tmp:0:8"]]
- 00aa2280 bytes 2801889a
- 00aa22a0 ["INT_ADD", "register:40f0:8", ["const:aa22a0:8", "const:4:8"]]
- 00aa22a0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa22a0 bytes 1c81ec97
- 00aa22a8 ["INT_ADD", "register:40f0:8", ["const:aa22a8:8", "const:4:8"]]
- 00aa22a8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa22a8 bytes b6f4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-210dcd3544ff432e0385ea354504b060"></a>

### [`00aa246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa246c.md) → [`00aa24b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa24b0.md) FUN_00aa24b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 84.78% / 新版 84.78%

CFGの説明率　旧版 14.29% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2504"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa2548"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa2504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa246c.md#insn-00aa2504) · [`00aa2488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa246c.md#insn-00aa2488)
- 新版 `00aa2548`（命令位置の公開資料なし） · `00aa24cc`（命令位置の公開資料なし）

~~~diff
- 00aa2504 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa2504 ["RETURN", null, ["register:0:8"]]
- 00aa2504 bytes c0035fd6
+ 00aa2548 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa2548 ["RETURN", null, ["register:0:8"]]
+ 00aa2548 bytes c0035fd6
- 00aa2488 ["INT_ADD", "register:40f0:8", ["const:aa2488:8", "const:4:8"]]
- 00aa2488 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa24cc ["INT_ADD", "register:40f0:8", ["const:aa24cc:8", "const:4:8"]]
+ 00aa24cc ["CALL", null, ["callee:0081f580:8"]]
- 00aa2488 bytes 3ef4f597
+ 00aa24cc bytes 2df4f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d28af89da3d38b3c0a43f0c68c08b2d4"></a>

### [`00aa2524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2524.md) → [`00aa2568`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2568.md) FUN_00aa2568

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 89.13% / 新版 89.13%

CFGの説明率　旧版 25.00% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa2540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2524.md#insn-00aa2540) · [`00aa2554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2524.md#insn-00aa2554) · [`00aa255c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2524.md#insn-00aa255c)
- 新版 `00aa2584`（命令位置の公開資料なし） · `00aa2598`（命令位置の公開資料なし） · `00aa25a0`（命令位置の公開資料なし）

~~~diff
- 00aa2540 ["INT_ADD", "register:40f0:8", ["const:aa2540:8", "const:4:8"]]
- 00aa2540 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2584 ["INT_ADD", "register:40f0:8", ["const:aa2584:8", "const:4:8"]]
+ 00aa2584 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2540 bytes 10f4f597
+ 00aa2584 bytes fff3f597
- 00aa2554 ["INT_ADD", "register:40f0:8", ["const:aa2554:8", "const:4:8"]]
- 00aa2554 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa2598 ["INT_ADD", "register:40f0:8", ["const:aa2598:8", "const:4:8"]]
+ 00aa2598 ["CALL", null, ["callee:005c2710:8"]]
- 00aa2554 bytes 6f80ec97
+ 00aa2598 bytes 5e80ec97
- 00aa255c ["INT_ADD", "register:40f0:8", ["const:aa255c:8", "const:4:8"]]
- 00aa255c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa25a0 ["INT_ADD", "register:40f0:8", ["const:aa25a0:8", "const:4:8"]]
+ 00aa25a0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa255c bytes 09f4f597
+ 00aa25a0 bytes f8f3f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d420c84415a5790ac2959b3b60d738d"></a>

### [`00aa274c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa274c.md) → [`00aa2790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2790.md) FUN_00aa2790

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa27bc",
      "incomplete_value": true,
      "site": "00aa27c0",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa2778",
      "incomplete_value": true,
      "site": "00aa277c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa277c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa274c.md#insn-00aa277c) · [`00aa2768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa274c.md#insn-00aa2768) · [`00aa2778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa274c.md#insn-00aa2778)
- 新版 `00aa27c0`（命令位置の公開資料なし） · `00aa27ac`（命令位置の公開資料なし）

~~~diff
- 00aa277c ["INT_ADD", "register:40f0:8", ["const:aa277c:8", "const:4:8"]]
- 00aa277c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa27c0 ["INT_ADD", "register:40f0:8", ["const:aa27c0:8", "const:4:8"]]
+ 00aa27c0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa277c bytes e57fec97
+ 00aa27c0 bytes d47fec97
- 00aa2768 ["INT_ADD", "register:40f0:8", ["const:aa2768:8", "const:4:8"]]
- 00aa2768 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa27ac ["INT_ADD", "register:40f0:8", ["const:aa27ac:8", "const:4:8"]]
+ 00aa27ac ["CALL", null, ["callee:0081f580:8"]]
- 00aa2768 bytes 86f3f597
+ 00aa27ac bytes 75f3f597
- 00aa2778 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa2778 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa2778 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa2778 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa2778 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582df2bc801a4a4b7401593aed015a27"></a>

### [`00aa27c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa27c4.md) → [`00aa2808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2808.md) FUN_00aa2808

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 83.33% / 新版 71.43%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa27e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa27c4.md#insn-00aa27e0) · [`00aa27f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa27c4.md#insn-00aa27f4) · [`00aa2804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa27c4.md#insn-00aa2804)
- 新版 `00aa2824`（命令位置の公開資料なし） · `00aa2838`（命令位置の公開資料なし） · `00aa2848`（命令位置の公開資料なし）

~~~diff
- 00aa27e0 ["INT_ADD", "register:40f0:8", ["const:aa27e0:8", "const:4:8"]]
- 00aa27e0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2824 ["INT_ADD", "register:40f0:8", ["const:aa2824:8", "const:4:8"]]
+ 00aa2824 ["CALL", null, ["callee:0081f580:8"]]
- 00aa27e0 bytes 68f3f597
+ 00aa2824 bytes 57f3f597
- 00aa27f4 ["INT_ADD", "register:40f0:8", ["const:aa27f4:8", "const:4:8"]]
- 00aa27f4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa2838 ["INT_ADD", "register:40f0:8", ["const:aa2838:8", "const:4:8"]]
+ 00aa2838 ["CALL", null, ["callee:005c2710:8"]]
- 00aa27f4 bytes c77fec97
+ 00aa2838 bytes b67fec97
- 00aa2804 ["INT_ADD", "register:40f0:8", ["const:aa2804:8", "const:4:8"]]
- 00aa2804 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa2848 ["INT_ADD", "register:40f0:8", ["const:aa2848:8", "const:4:8"]]
+ 00aa2848 ["CALL", null, ["callee:0081f580:8"]]
- 00aa2804 bytes 5ff3f597
+ 00aa2848 bytes 4ef3f597
~~~


<a id="compare-830c146e9d4f3f21bda1c399b6943076"></a>

### [`00aa2910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2910.md) → [`00aa2954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2954.md) FUN_00aa2954

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 7.69% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2910"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa2914"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa2910",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa2914",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa2918",
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
      "00aa2954",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa2958",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa295c",
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

- 旧版 [`00aa2910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2910.md#insn-00aa2910) · [`00aa2914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2910.md#insn-00aa2914) · [`00aa2918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2910.md#insn-00aa2918)

~~~diff
- 00aa2910 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa2910 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa2910 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa2910 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa2910 bytes fd7bbda9
- 00aa2914 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa2914 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa2914 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa2914 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa2914 bytes f65701a9
- 00aa2918 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa2918 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa2918 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa2918 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa2918 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e05724fd7eda4dfd69707e96165c28f"></a>

### [`00aa30a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa30a8.md) → [`00aa30ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa30ec.md) FUN_00aa30ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 12.50% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa311c",
      "incomplete_value": true,
      "site": "00aa3120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa30d8",
      "incomplete_value": true,
      "site": "00aa30dc",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa311c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa3160"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa30dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa30a8.md#insn-00aa30dc) · [`00aa311c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa30a8.md#insn-00aa311c)
- 新版 `00aa3120`（命令位置の公開資料なし） · `00aa311c`（命令位置の公開資料なし）

~~~diff
- 00aa30dc ["INT_ADD", "register:40f0:8", ["const:aa30dc:8", "const:4:8"]]
- 00aa30dc ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3120 ["INT_ADD", "register:40f0:8", ["const:aa3120:8", "const:4:8"]]
+ 00aa3120 ["CALL", null, ["callee:005c2710:8"]]
- 00aa30dc bytes 8d7dec97
+ 00aa3120 bytes 7c7dec97
- 00aa311c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa311c ["RETURN", null, ["register:0:8"]]
- 00aa311c bytes c0035fd6
+ 00aa311c ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aa311c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa311c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa311c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aa311c bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38392e96ce86bf1b3e5953985294edd1"></a>

### [`00aa3168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3168.md) → [`00aa31ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa31ac.md) FUN_00aa31ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa3198",
      "incomplete_value": true,
      "site": "00aa319c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa319c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3168.md#insn-00aa319c) · [`00aa3188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3168.md#insn-00aa3188) · [`00aa3198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3168.md#insn-00aa3198)
- 新版 `00aa31e0`（命令位置の公開資料なし） · `00aa31cc`（命令位置の公開資料なし）

~~~diff
- 00aa319c ["INT_ADD", "register:40f0:8", ["const:aa319c:8", "const:4:8"]]
- 00aa319c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa31e0 ["INT_ADD", "register:40f0:8", ["const:aa31e0:8", "const:4:8"]]
+ 00aa31e0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa319c bytes 5d7dec97
+ 00aa31e0 bytes 4c7dec97
- 00aa3188 ["INT_ADD", "register:40f0:8", ["const:aa3188:8", "const:4:8"]]
- 00aa3188 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa31cc ["INT_ADD", "register:40f0:8", ["const:aa31cc:8", "const:4:8"]]
+ 00aa31cc ["CALL", null, ["callee:0081f580:8"]]
- 00aa3188 bytes fef0f597
+ 00aa31cc bytes edf0f597
- 00aa3198 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa3198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa3198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa3198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa3198 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c593e9a897ce46c13b3e2f6d5822d88a"></a>

### [`00aa3228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3228.md) → [`00aa326c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa326c.md) FUN_00aa326c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 18.18% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa3258",
      "incomplete_value": true,
      "site": "00aa325c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa325c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3228.md#insn-00aa325c) · [`00aa3248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3228.md#insn-00aa3248) · [`00aa3264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3228.md#insn-00aa3264)
- 新版 `00aa32a0`（命令位置の公開資料なし） · `00aa328c`（命令位置の公開資料なし） · `00aa32a8`（命令位置の公開資料なし）

~~~diff
- 00aa325c ["INT_ADD", "register:40f0:8", ["const:aa325c:8", "const:4:8"]]
- 00aa325c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa32a0 ["INT_ADD", "register:40f0:8", ["const:aa32a0:8", "const:4:8"]]
+ 00aa32a0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa325c bytes 2d7dec97
+ 00aa32a0 bytes 1c7dec97
- 00aa3248 ["INT_ADD", "register:40f0:8", ["const:aa3248:8", "const:4:8"]]
- 00aa3248 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa328c ["INT_ADD", "register:40f0:8", ["const:aa328c:8", "const:4:8"]]
+ 00aa328c ["CALL", null, ["callee:0081f580:8"]]
- 00aa3248 bytes cef0f597
+ 00aa328c bytes bdf0f597
- 00aa3264 ["INT_ADD", "register:40f0:8", ["const:aa3264:8", "const:4:8"]]
- 00aa3264 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa32a8 ["INT_ADD", "register:40f0:8", ["const:aa32a8:8", "const:4:8"]]
+ 00aa32a8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3264 bytes c7f0f597
+ 00aa32a8 bytes b6f0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83b998838f01e9ab8c942da23c9442e6"></a>

### [`00aa3468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3468.md) → [`00aa34ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa34ac.md) FUN_00aa34ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`005bcea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005bc/005bcea8.md) [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 6件 [`005bcea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005bc/005bcea8.md) [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa3488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3468.md#insn-00aa3488) · [`00aa349c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3468.md#insn-00aa349c) · [`00aa34a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3468.md#insn-00aa34a4)
- 新版 `00aa34cc`（命令位置の公開資料なし） · `00aa34e0`（命令位置の公開資料なし） · `00aa34e8`（命令位置の公開資料なし）

~~~diff
- 00aa3488 ["INT_ADD", "register:40f0:8", ["const:aa3488:8", "const:4:8"]]
- 00aa3488 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa34cc ["INT_ADD", "register:40f0:8", ["const:aa34cc:8", "const:4:8"]]
+ 00aa34cc ["CALL", null, ["callee:0081f580:8"]]
- 00aa3488 bytes 3ef0f597
+ 00aa34cc bytes 2df0f597
- 00aa349c ["INT_ADD", "register:40f0:8", ["const:aa349c:8", "const:4:8"]]
- 00aa349c ["CALL", null, ["callee:005c2710:8"]]
+ 00aa34e0 ["INT_ADD", "register:40f0:8", ["const:aa34e0:8", "const:4:8"]]
+ 00aa34e0 ["CALL", null, ["callee:005c2710:8"]]
- 00aa349c bytes 9d7cec97
+ 00aa34e0 bytes 8c7cec97
- 00aa34a4 ["INT_ADD", "register:40f0:8", ["const:aa34a4:8", "const:4:8"]]
- 00aa34a4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa34e8 ["INT_ADD", "register:40f0:8", ["const:aa34e8:8", "const:4:8"]]
+ 00aa34e8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa34a4 bytes 37f0f597
+ 00aa34e8 bytes 26f0f597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-670829655cc2ecf714751c5b9758eb30"></a>

### [`00aa3528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3528.md) → [`00aa356c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa356c.md) FUN_00aa356c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 11.11% / 新版 5.56%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa359c"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa35e0"
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
      "00aa35b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aa35a0"
      ]
    ]
  ],
  "added": [
    [
      "00aa35b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aa35e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3528.md#insn-00aa359c) · [`00aa3548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3528.md#insn-00aa3548)
- 新版 `00aa35e0`（命令位置の公開資料なし） · `00aa358c`（命令位置の公開資料なし）

~~~diff
- 00aa359c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa359c ["RETURN", null, ["register:0:8"]]
- 00aa359c bytes c0035fd6
+ 00aa35e0 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa35e0 ["RETURN", null, ["register:0:8"]]
+ 00aa35e0 bytes c0035fd6
- 00aa3548 ["INT_ADD", "register:40f0:8", ["const:aa3548:8", "const:4:8"]]
- 00aa3548 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa358c ["INT_ADD", "register:40f0:8", ["const:aa358c:8", "const:4:8"]]
+ 00aa358c ["CALL", null, ["callee:0081f580:8"]]
- 00aa3548 bytes 0ef0f597
+ 00aa358c bytes fdeff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f670e8ddc5a76a2ce5cebc24414c481"></a>

### [`00aa35e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa35e8.md) → [`00aa362c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa362c.md) FUN_00aa362c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 23.53% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa35e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa35e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa35ec"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa35e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa35ec",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa35f0",
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
      "00aa362c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa3630",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa3634",
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

- 旧版 [`00aa35e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa35e8.md#insn-00aa35e8) · [`00aa35ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa35e8.md#insn-00aa35ec) · [`00aa35f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa35e8.md#insn-00aa35f0)

~~~diff
- 00aa35e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa35e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa35e8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa35e8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa35e8 bytes fd7bbda9
- 00aa35ec ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa35ec ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa35ec ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa35ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa35ec bytes f65701a9
- 00aa35f0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa35f0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa35f0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa35f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa35f0 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc2cb15ffe9b73b0f8b767273538c6dd"></a>

### [`00aa3750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3750.md) → [`00aa3794`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3794.md) FUN_00aa3794

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 88.10% / 新版 88.10%

CFGの説明率　旧版 16.67% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa377c",
      "incomplete_value": true,
      "site": "00aa3780",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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
      "definition_site": "00aa37f8",
      "incomplete_value": true,
      "site": "00aa3824",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
      "definition_site": "00aa37fc",
      "incomplete_value": true,
      "site": "00aa3824",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
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

- 旧版 [`00aa3780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3750.md#insn-00aa3780) · [`00aa37e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3750.md#insn-00aa37e0) · [`00aa376c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3750.md#insn-00aa376c)
- 新版 `00aa37c4`（命令位置の公開資料なし） · `00aa3824`（命令位置の公開資料なし） · `00aa37b0`（命令位置の公開資料なし）

~~~diff
- 00aa3780 ["INT_ADD", "register:40f0:8", ["const:aa3780:8", "const:4:8"]]
- 00aa3780 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa37c4 ["INT_ADD", "register:40f0:8", ["const:aa37c4:8", "const:4:8"]]
+ 00aa37c4 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3780 bytes e47bec97
+ 00aa37c4 bytes d37bec97
- 00aa37e0 ["INT_ADD", "register:40f0:8", ["const:aa37e0:8", "const:4:8"]]
- 00aa37e0 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa3824 ["INT_ADD", "register:40f0:8", ["const:aa3824:8", "const:4:8"]]
+ 00aa3824 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa37e0 bytes 40eeff97
+ 00aa3824 bytes 40eeff97
- 00aa376c ["INT_ADD", "register:40f0:8", ["const:aa376c:8", "const:4:8"]]
- 00aa376c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa37b0 ["INT_ADD", "register:40f0:8", ["const:aa37b0:8", "const:4:8"]]
+ 00aa37b0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa376c bytes 85eff597
+ 00aa37b0 bytes 74eff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a813ff093cbf94a9f49a82b8cbd78e1"></a>

### [`00aa37f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa37f8.md) → [`00aa383c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa383c.md) FUN_00aa383c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa3894",
      "incomplete_value": true,
      "site": "00aa38a8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa3898",
      "incomplete_value": true,
      "site": "00aa38a8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
      "definition_site": "00aa389c",
      "incomplete_value": true,
      "site": "00aa38a8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4098:4"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa3854",
      "DATA",
      [
        "storage",
        "00239eec",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa3898",
      "DATA",
      [
        "storage",
        "00239eec",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa38a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa37f8.md#insn-00aa38a8) · [`00aa38c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa37f8.md#insn-00aa38c4)
- 新版 `00aa38ec`（命令位置の公開資料なし） · `00aa3908`（命令位置の公開資料なし）

~~~diff
- 00aa38a8 ["INT_ADD", "register:40f0:8", ["const:aa38a8:8", "const:4:8"]]
- 00aa38a8 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa38ec ["INT_ADD", "register:40f0:8", ["const:aa38ec:8", "const:4:8"]]
+ 00aa38ec ["CALL", null, ["callee:00a9f124:8"]]
- 00aa38a8 bytes 0eeeff97
+ 00aa38ec bytes 0eeeff97
- 00aa38c4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa38c4 ["RETURN", null, ["register:0:8"]]
- 00aa38c4 bytes c0035fd6
+ 00aa3908 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa3908 ["RETURN", null, ["register:0:8"]]
+ 00aa3908 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5332ca8a31147b54817158550ee89377"></a>

### [`00aa38c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa38c8.md) → [`00aa390c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa390c.md) FUN_00aa390c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 27.27% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa38e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa38c8.md#insn-00aa38e4) · [`00aa38f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa38c8.md#insn-00aa38f8) · [`00aa38fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa38c8.md#insn-00aa38fc)
- 新版 `00aa3928`（命令位置の公開資料なし） · `00aa393c`（命令位置の公開資料なし） · `00aa3940`（命令位置の公開資料なし）

~~~diff
- 00aa38e4 ["INT_ADD", "register:40f0:8", ["const:aa38e4:8", "const:4:8"]]
- 00aa38e4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3928 ["INT_ADD", "register:40f0:8", ["const:aa3928:8", "const:4:8"]]
+ 00aa3928 ["CALL", null, ["callee:0081f580:8"]]
- 00aa38e4 bytes 27eff597
+ 00aa3928 bytes 16eff597
- 00aa38f8 ["INT_ADD", "register:40f0:8", ["const:aa38f8:8", "const:4:8"]]
- 00aa38f8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa393c ["INT_ADD", "register:40f0:8", ["const:aa393c:8", "const:4:8"]]
+ 00aa393c ["CALL", null, ["callee:005c2710:8"]]
- 00aa38f8 bytes 867bec97
+ 00aa393c bytes 757bec97
- 00aa38fc ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa38fc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa38fc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa38fc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa3940 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa3940 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa3940 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa3940 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa38fc bytes e0000037
+ 00aa3940 bytes e0000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0128eaef29295b8bf5ebeda2cfee7726"></a>

### [`00aa3a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3a00.md) → [`00aa3a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3a44.md) FUN_00aa3a44

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa3a70",
      "incomplete_value": true,
      "site": "00aa3a74",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
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
      "definition_site": "00aa3a74",
      "incomplete_value": true,
      "site": "00aa3a90",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a8:4"
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
    "new": null,
    "old": {
      "definition_site": "00aa3a64",
      "incomplete_value": true,
      "site": "00aa3a90",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:40a0:4"
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
      "unmatched:00aa3a58",
      "DATA",
      [
        "storage",
        "00239ecc",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ],
  "added": [
    [
      "00aa3a9c",
      "DATA",
      [
        "storage",
        "00239ecc",
        null,
        "Elf64_Rela[1792]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa3a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3a00.md#insn-00aa3a30) · [`00aa3a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3a00.md#insn-00aa3a90) · [`00aa3a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3a00.md#insn-00aa3a1c)
- 新版 `00aa3a74`（命令位置の公開資料なし） · `00aa3ad4`（命令位置の公開資料なし） · `00aa3a60`（命令位置の公開資料なし）

~~~diff
- 00aa3a30 ["INT_ADD", "register:40f0:8", ["const:aa3a30:8", "const:4:8"]]
- 00aa3a30 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3a74 ["INT_ADD", "register:40f0:8", ["const:aa3a74:8", "const:4:8"]]
+ 00aa3a74 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3a30 bytes 387bec97
+ 00aa3a74 bytes 277bec97
- 00aa3a90 ["INT_ADD", "register:40f0:8", ["const:aa3a90:8", "const:4:8"]]
- 00aa3a90 ["CALL", null, ["callee:00a9f124:8"]]
+ 00aa3ad4 ["INT_ADD", "register:40f0:8", ["const:aa3ad4:8", "const:4:8"]]
+ 00aa3ad4 ["CALL", null, ["callee:00a9f124:8"]]
- 00aa3a90 bytes 94edff97
+ 00aa3ad4 bytes 94edff97
- 00aa3a1c ["INT_ADD", "register:40f0:8", ["const:aa3a1c:8", "const:4:8"]]
- 00aa3a1c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3a60 ["INT_ADD", "register:40f0:8", ["const:aa3a60:8", "const:4:8"]]
+ 00aa3a60 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3a1c bytes d9eef597
+ 00aa3a60 bytes c8eef597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9785c0743ec8fc79e544c05415b95739"></a>

### [`00aa3aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3aa8.md) → [`00aa3aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3aec.md) FUN_00aa3aec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 4件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 12.50% / 新版 12.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa3b18",
      "incomplete_value": true,
      "site": "00aa3b1c",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa3ad4",
      "incomplete_value": true,
      "site": "00aa3ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa3ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3aa8.md#insn-00aa3ad8) · [`00aa3ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3aa8.md#insn-00aa3ac4) · [`00aa3ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3aa8.md#insn-00aa3ad4)
- 新版 `00aa3b1c`（命令位置の公開資料なし） · `00aa3b08`（命令位置の公開資料なし）

~~~diff
- 00aa3ad8 ["INT_ADD", "register:40f0:8", ["const:aa3ad8:8", "const:4:8"]]
- 00aa3ad8 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3b1c ["INT_ADD", "register:40f0:8", ["const:aa3b1c:8", "const:4:8"]]
+ 00aa3b1c ["CALL", null, ["callee:005c2710:8"]]
- 00aa3ad8 bytes 0e7bec97
+ 00aa3b1c bytes fd7aec97
- 00aa3ac4 ["INT_ADD", "register:40f0:8", ["const:aa3ac4:8", "const:4:8"]]
- 00aa3ac4 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3b08 ["INT_ADD", "register:40f0:8", ["const:aa3b08:8", "const:4:8"]]
+ 00aa3b08 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3ac4 bytes afeef597
+ 00aa3b08 bytes 9eeef597
- 00aa3ad4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00aa3ad4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa3ad4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa3ad4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa3ad4 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dd996eb2b7fb0a5a4ed1375d1273048"></a>

### [`00aa3b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3b60.md) → [`00aa3ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3ba4.md) FUN_00aa3ba4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00a9f0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9f/00a9f0e0.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00a9f124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a9f/00a9f124.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3b60"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3b64"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aa3b60",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa3b64",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aa3b68",
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
      "00aa3ba4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aa3ba8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aa3bac",
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

- 旧版 [`00aa3b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3b60.md#insn-00aa3b60) · [`00aa3b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3b60.md#insn-00aa3b64) · [`00aa3b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3b60.md#insn-00aa3b68)

~~~diff
- 00aa3b60 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aa3b60 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aa3b60 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aa3b60 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aa3b60 bytes fd7bbda9
- 00aa3b64 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aa3b64 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aa3b64 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aa3b64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa3b64 bytes f65701a9
- 00aa3b68 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aa3b68 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aa3b68 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aa3b68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aa3b68 bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aca0022bdefba4676b2ca1a02e727f9"></a>

### [`00aa3bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3bec.md) → [`00aa3c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3c30.md) FUN_00aa3c30

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`0065f258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069e/0069ef54.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00a960ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a96/00a960ac.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa4fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4fb0.md)
- 新版 呼出元 5件 [`0065f258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f258.md) [`0069ef54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069e/0069ef54.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00a960f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a96/00a960f0.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa4ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4ff4.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa3c60",
      "incomplete_value": true,
      "site": "00aa3c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa3c1c",
      "incomplete_value": true,
      "site": "00aa3c20",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3c60"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa3ca4"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa3c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3bec.md#insn-00aa3c20) · [`00aa3c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3bec.md#insn-00aa3c60)
- 新版 `00aa3c64`（命令位置の公開資料なし） · `00aa3c60`（命令位置の公開資料なし）

~~~diff
- 00aa3c20 ["INT_ADD", "register:40f0:8", ["const:aa3c20:8", "const:4:8"]]
- 00aa3c20 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3c64 ["INT_ADD", "register:40f0:8", ["const:aa3c64:8", "const:4:8"]]
+ 00aa3c64 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3c20 bytes bc7aec97
+ 00aa3c64 bytes ab7aec97
- 00aa3c60 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa3c60 ["RETURN", null, ["register:0:8"]]
- 00aa3c60 bytes c0035fd6
+ 00aa3c60 ["COPY", "tmp:0:8", ["register:4048:8"]]
+ 00aa3c60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa3c60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa3c60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aa3c60 bytes 0001098b
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0e6c26dad7961f889b7aa1add0f749b"></a>

### [`00aa3cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3cac.md) → [`00aa3cf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3cf0.md) FUN_00aa3cf0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 4件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`006a4d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a4/006a4d58.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 4件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`006a4d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a4/006a4d58.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa3cd8",
      "incomplete_value": true,
      "site": "00aa3cdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4040:8"
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3d20"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa3d64"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa3cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3cac.md#insn-00aa3cdc) · [`00aa3d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3cac.md#insn-00aa3d20)
- 新版 `00aa3d20`（命令位置の公開資料なし） · `00aa3d64`（命令位置の公開資料なし）

~~~diff
- 00aa3cdc ["INT_ADD", "register:40f0:8", ["const:aa3cdc:8", "const:4:8"]]
- 00aa3cdc ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3d20 ["INT_ADD", "register:40f0:8", ["const:aa3d20:8", "const:4:8"]]
+ 00aa3d20 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3cdc bytes 8d7aec97
+ 00aa3d20 bytes 7c7aec97
- 00aa3d20 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa3d20 ["RETURN", null, ["register:0:8"]]
- 00aa3d20 bytes c0035fd6
+ 00aa3d64 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa3d64 ["RETURN", null, ["register:0:8"]]
+ 00aa3d64 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b89121d1ee89fecfc15ac5be0bd61ef"></a>

### [`00aa3d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3d40.md) → [`00aa3d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3d84.md) FUN_00aa3d84

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_return_alignment

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 20.00% / 新版 25.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa3d6c",
      "incomplete_value": true,
      "site": "00aa3d70",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "live",
            "register:4048:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": null,
    "old": {
      "site": "00aa3db4"
    }
  },
  {
    "confidence": "limited",
    "kind": "return_position_unpaired",
    "new": {
      "site": "00aa3df8"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa3d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3d40.md#insn-00aa3d70) · [`00aa3db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3d40.md#insn-00aa3db4)
- 新版 `00aa3db4`（命令位置の公開資料なし） · `00aa3df8`（命令位置の公開資料なし）

~~~diff
- 00aa3d70 ["INT_ADD", "register:40f0:8", ["const:aa3d70:8", "const:4:8"]]
- 00aa3d70 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3db4 ["INT_ADD", "register:40f0:8", ["const:aa3db4:8", "const:4:8"]]
+ 00aa3db4 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3d70 bytes 687aec97
+ 00aa3db4 bytes 577aec97
- 00aa3db4 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aa3db4 ["RETURN", null, ["register:0:8"]]
- 00aa3db4 bytes c0035fd6
+ 00aa3df8 ["COPY", "register:0:8", ["register:40f0:8"]]
+ 00aa3df8 ["RETURN", null, ["register:0:8"]]
+ 00aa3df8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bf93f5520a7c4add3b3b4f8a1f76d55"></a>

### [`00aa3e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3e68.md) → [`00aa3eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3eac.md) FUN_00aa3eac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa3e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3e68.md#insn-00aa3e84) · [`00aa3e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3e68.md#insn-00aa3e98) · [`00aa3ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3e68.md#insn-00aa3ea0)
- 新版 `00aa3ec8`（命令位置の公開資料なし） · `00aa3edc`（命令位置の公開資料なし） · `00aa3ee4`（命令位置の公開資料なし）

~~~diff
- 00aa3e84 ["INT_ADD", "register:40f0:8", ["const:aa3e84:8", "const:4:8"]]
- 00aa3e84 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3ec8 ["INT_ADD", "register:40f0:8", ["const:aa3ec8:8", "const:4:8"]]
+ 00aa3ec8 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3e84 bytes bfedf597
+ 00aa3ec8 bytes aeedf597
- 00aa3e98 ["INT_ADD", "register:40f0:8", ["const:aa3e98:8", "const:4:8"]]
- 00aa3e98 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa3edc ["INT_ADD", "register:40f0:8", ["const:aa3edc:8", "const:4:8"]]
+ 00aa3edc ["CALL", null, ["callee:005c2710:8"]]
- 00aa3e98 bytes 1e7aec97
+ 00aa3edc bytes 0d7aec97
- 00aa3ea0 ["INT_ADD", "register:40f0:8", ["const:aa3ea0:8", "const:4:8"]]
- 00aa3ea0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa3ee4 ["INT_ADD", "register:40f0:8", ["const:aa3ee4:8", "const:4:8"]]
+ 00aa3ee4 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3ea0 bytes b8edf597
+ 00aa3ee4 bytes a7edf597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72b4b464504e433928e39fd7a8ed180c"></a>

### [`00aa3fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3fa4.md) → [`00aa3fe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa3/00aa3fe8.md) FUN_00aa3fe8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00aa2c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa2/00aa2c2c.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 3件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00aa2c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa2/00aa2c70.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 42.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aa4014",
      "incomplete_value": true,
      "site": "00aa4018",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
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


#### 変更候補の命令位置

- 旧版 [`00aa3fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3fa4.md#insn-00aa3fd4) · [`00aa3fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3fa4.md#insn-00aa3fc0) · [`00aa3fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3fa4.md#insn-00aa3fd8)
- 新版 `00aa4018`（命令位置の公開資料なし） · `00aa4004`（命令位置の公開資料なし） · `00aa401c`（命令位置の公開資料なし）

~~~diff
- 00aa3fd4 ["INT_ADD", "register:40f0:8", ["const:aa3fd4:8", "const:4:8"]]
- 00aa3fd4 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4018 ["INT_ADD", "register:40f0:8", ["const:aa4018:8", "const:4:8"]]
+ 00aa4018 ["CALL", null, ["callee:005c2710:8"]]
- 00aa3fd4 bytes cf79ec97
+ 00aa4018 bytes be79ec97
- 00aa3fc0 ["INT_ADD", "register:40f0:8", ["const:aa3fc0:8", "const:4:8"]]
- 00aa3fc0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4004 ["INT_ADD", "register:40f0:8", ["const:aa4004:8", "const:4:8"]]
+ 00aa4004 ["CALL", null, ["callee:0081f580:8"]]
- 00aa3fc0 bytes 70edf597
+ 00aa4004 bytes 5fedf597
- 00aa3fd8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa3fd8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa3fd8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa3fd8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa401c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa401c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa401c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa401c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa3fd8 bytes 60000037
+ 00aa401c bytes 60000037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2a68c6cf9a87f84d10189ec7ff9e68e"></a>

### [`00aa40a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa40a8.md) → [`00aa40ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa40ec.md) FUN_00aa40ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa40bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa40a8.md#insn-00aa40bc) · [`00aa40d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa40a8.md#insn-00aa40d0) · [`00aa40d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa40a8.md#insn-00aa40d4)
- 新版 `00aa4100`（命令位置の公開資料なし） · `00aa4114`（命令位置の公開資料なし） · `00aa4118`（命令位置の公開資料なし）

~~~diff
- 00aa40bc ["INT_ADD", "register:40f0:8", ["const:aa40bc:8", "const:4:8"]]
- 00aa40bc ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4100 ["INT_ADD", "register:40f0:8", ["const:aa4100:8", "const:4:8"]]
+ 00aa4100 ["CALL", null, ["callee:0081f580:8"]]
- 00aa40bc bytes 31edf597
+ 00aa4100 bytes 20edf597
- 00aa40d0 ["INT_ADD", "register:40f0:8", ["const:aa40d0:8", "const:4:8"]]
- 00aa40d0 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4114 ["INT_ADD", "register:40f0:8", ["const:aa4114:8", "const:4:8"]]
+ 00aa4114 ["CALL", null, ["callee:005c2710:8"]]
- 00aa40d0 bytes 9079ec97
+ 00aa4114 bytes 7f79ec97
- 00aa40d4 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa40d4 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa40d4 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa40d4 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa4118 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa4118 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa4118 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa4118 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa40d4 bytes 40010037
+ 00aa4118 bytes 40010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f6836e2c87ef00f62c80cf3ad8835c8"></a>

### [`00aa4168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4168.md) → [`00aa41ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa41ac.md) FUN_00aa41ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aa418c",
      "incomplete_value": true,
      "site": "00aa4190",
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
                "register:4000:8"
              ],
              "INT_MULT"
            ]
          ],
          [
            "leaf",
            "const:2678:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00aa4190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4168.md#insn-00aa4190) · [`00aa417c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4168.md#insn-00aa417c) · [`00aa4194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4168.md#insn-00aa4194)
- 新版 `00aa41d4`（命令位置の公開資料なし） · `00aa41c0`（命令位置の公開資料なし） · `00aa41d8`（命令位置の公開資料なし）

~~~diff
- 00aa4190 ["INT_ADD", "register:40f0:8", ["const:aa4190:8", "const:4:8"]]
- 00aa4190 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa41d4 ["INT_ADD", "register:40f0:8", ["const:aa41d4:8", "const:4:8"]]
+ 00aa41d4 ["CALL", null, ["callee:005c2710:8"]]
- 00aa4190 bytes 6079ec97
+ 00aa41d4 bytes 4f79ec97
- 00aa417c ["INT_ADD", "register:40f0:8", ["const:aa417c:8", "const:4:8"]]
- 00aa417c ["CALL", null, ["callee:0081f580:8"]]
+ 00aa41c0 ["INT_ADD", "register:40f0:8", ["const:aa41c0:8", "const:4:8"]]
+ 00aa41c0 ["CALL", null, ["callee:0081f580:8"]]
- 00aa417c bytes 01edf597
+ 00aa41c0 bytes f0ecf597
- 00aa4194 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa4194 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa4194 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa4194 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa41d8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa41d8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa41d8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa41d8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa4194 bytes 00010037
+ 00aa41d8 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70d897a5d1f6a533c064331c2dbdeae7"></a>

### [`00aa41c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa41c4.md) → [`00aa4208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4208.md) FUN_00aa4208

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a0/006a0ab4.md) [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 3件 [`006a0ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a0/006a0ab4.md) [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 40.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa41d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa41c4.md#insn-00aa41d8) · [`00aa41ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa41c4.md#insn-00aa41ec) · [`00aa41f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa41c4.md#insn-00aa41f0)
- 新版 `00aa421c`（命令位置の公開資料なし） · `00aa4230`（命令位置の公開資料なし） · `00aa4234`（命令位置の公開資料なし）

~~~diff
- 00aa41d8 ["INT_ADD", "register:40f0:8", ["const:aa41d8:8", "const:4:8"]]
- 00aa41d8 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa421c ["INT_ADD", "register:40f0:8", ["const:aa421c:8", "const:4:8"]]
+ 00aa421c ["CALL", null, ["callee:0081f580:8"]]
- 00aa41d8 bytes eaecf597
+ 00aa421c bytes d9ecf597
- 00aa41ec ["INT_ADD", "register:40f0:8", ["const:aa41ec:8", "const:4:8"]]
- 00aa41ec ["CALL", null, ["callee:005c2710:8"]]
+ 00aa4230 ["INT_ADD", "register:40f0:8", ["const:aa4230:8", "const:4:8"]]
+ 00aa4230 ["CALL", null, ["callee:005c2710:8"]]
- 00aa41ec bytes 4979ec97
+ 00aa4230 bytes 3879ec97
- 00aa41f0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa41f0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa41f0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa41f0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa4234 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa4234 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa4234 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa4234 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa41f0 bytes 00010037
+ 00aa4234 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4797567d0629b2c9e800bda3db9db9a5"></a>

### [`00aa4220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4220.md) → [`00aa4264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa4/00aa4264.md) FUN_00aa4264

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`009f1e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009f1/009f1e64.md) [`00aa0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa0/00aa0f20.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`009f1ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009f1/009f1ea8.md) [`00aa0f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aa0/00aa0f64.md) · 呼出先 2件 [`005c2710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005c2/005c2710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aa4234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4220.md#insn-00aa4234) · [`00aa4248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4220.md#insn-00aa4248) · [`00aa424c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa4/00aa4220.md#insn-00aa424c)
- 新版 `00aa4278`（命令位置の公開資料なし） · `00aa428c`（命令位置の公開資料なし） · `00aa4290`（命令位置の公開資料なし）

~~~diff
- 00aa4234 ["INT_ADD", "register:40f0:8", ["const:aa4234:8", "const:4:8"]]
- 00aa4234 ["CALL", null, ["callee:0081f580:8"]]
+ 00aa4278 ["INT_ADD", "register:40f0:8", ["const:aa4278:8", "const:4:8"]]
+ 00aa4278 ["CALL", null, ["callee:0081f580:8"]]
- 00aa4234 bytes d3ecf597
+ 00aa4278 bytes c2ecf597
- 00aa4248 ["INT_ADD", "register:40f0:8", ["const:aa4248:8", "const:4:8"]]
- 00aa4248 ["CALL", null, ["callee:005c2710:8"]]
+ 00aa428c ["INT_ADD", "register:40f0:8", ["const:aa428c:8", "const:4:8"]]
+ 00aa428c ["CALL", null, ["callee:005c2710:8"]]
- 00aa4248 bytes 3279ec97
+ 00aa428c bytes 2179ec97
- 00aa424c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00aa424c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00aa424c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00aa424c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00aa4290 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00aa4290 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00aa4290 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00aa4290 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00aa424c bytes 00010037
+ 00aa4290 bytes 00010037
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

