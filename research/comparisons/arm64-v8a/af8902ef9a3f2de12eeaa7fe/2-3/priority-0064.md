# v16.0.0 → v16.0.1 · 最優先の変更候補 (64)

[一覧の目次](README.md)

<a id="compare-ee61c3e5269aedae92190e33f2f01e1d"></a>

### [`00ac203c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md) → [`00ac2238`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac2238.md) FUN_00ac2238

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00ac224c",
      "incomplete_value": false,
      "site": "00ac2250",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac2250",
      "DATA",
      [
        "storage",
        "00c8cf90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2250",
      "DATA",
      [
        "storage",
        "00c8d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2048`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac2048) · [`00ac204c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac204c) · [`00ac2050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac203c.md#insn-00ac2050)
- 新版 `00ac2244`（命令位置の公開資料なし） · `00ac2248`（命令位置の公開資料なし） · `00ac224c`（命令位置の公開資料なし）

~~~diff
- 00ac2048 ["INT_ADD", "register:40f0:8", ["const:ac2048:8", "const:4:8"]]
- 00ac2048 ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac2244 ["INT_ADD", "register:40f0:8", ["const:ac2244:8", "const:4:8"]]
+ 00ac2244 ["CALL", null, ["callee:00c57e90:8"]]
- 00ac2048 bytes 92560694
+ 00ac2244 bytes 13570694
- 00ac204c ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00ac2248 ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00ac204c bytes 480e00d0
+ 00ac2248 bytes 480e00f0
- 00ac2050 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00ac2050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac2050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac2050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac224c ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00ac224c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac224c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac224c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac2050 bytes 08413e91
+ 00ac224c bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b1b1e0c6cdbe3e9898ac8f923607660"></a>

### [`00ac2060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md) → [`00ac225c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac225c.md) FUN_00ac225c

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac2260",
      "incomplete_value": false,
      "site": "00ac2264",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac2264",
      "DATA",
      [
        "storage",
        "00c8cf90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac2264",
      "DATA",
      [
        "storage",
        "00c8d390",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2060`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md#insn-00ac2060) · [`00ac2064`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2060.md#insn-00ac2064)
- 新版 `00ac225c`（命令位置の公開資料なし） · `00ac2260`（命令位置の公開資料なし）

~~~diff
- 00ac2060 ["COPY", "register:4040:8", ["const:c8c000:8"]]
+ 00ac225c ["COPY", "register:4040:8", ["const:c8d000:8"]]
- 00ac2060 bytes 480e00d0
+ 00ac225c bytes 480e00f0
- 00ac2064 ["COPY", "tmp:0:8", ["const:f90:8"]]
- 00ac2064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac2064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac2064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac2260 ["COPY", "tmp:0:8", ["const:390:8"]]
+ 00ac2260 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2260 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac2260 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac2064 bytes 08413e91
+ 00ac2260 bytes 08410e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-874977d08a41ea7f639fe0c3526ec454"></a>

### [`00ac2078`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md) → [`00ac2274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac2274.md) FUN_00ac2274

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b9134`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9134.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b9178`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9178.md)

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
      "site": "00ac2290",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac2094",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00ac2290",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00ac2290",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md#insn-00ac2094) · [`00ac20a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2078.md#insn-00ac20a0)
- 新版 `00ac2290`（命令位置の公開資料なし） · `00ac229c`（命令位置の公開資料なし）

~~~diff
- 00ac2094 ["INT_ADD", "register:40f0:8", ["const:ac2094:8", "const:4:8"]]
- 00ac2094 ["CALL", null, ["ram:47acb4:8"]]
+ 00ac2290 ["INT_ADD", "register:40f0:8", ["const:ac2290:8", "const:4:8"]]
+ 00ac2290 ["CALL", null, ["ram:47acf4:8"]]
- 00ac2094 bytes 08e3e697
+ 00ac2290 bytes 99e2e697
- 00ac20a0 ["INT_ADD", "register:40f0:8", ["const:ac20a0:8", "const:4:8"]]
- 00ac20a0 ["CALL", null, ["callee:0047cdd4:8"]]
+ 00ac229c ["INT_ADD", "register:40f0:8", ["const:ac229c:8", "const:4:8"]]
+ 00ac229c ["CALL", null, ["callee:0047cdd4:8"]]
- 00ac20a0 bytes 3debe697
+ 00ac229c bytes ceeae697
~~~


<a id="compare-8336c96729ec06e186f5c30aec3f03b4"></a>

### [`00ac20e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md) → [`00ac22dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac22dc.md) FUN_00ac22dc

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 11件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0067e15c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e15c.md) [`00862c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00862/00862c10.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00ac0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0454.md) · 呼出先 11件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0067e19c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e19c.md) [`00862c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00862/00862c50.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 29.68% / 新版 29.68%

CFGの説明率　旧版 4.62% / 新版 4.55%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 63件, `unresolved_call_alignment` 63件, `unresolved_store_alignment` 115件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2120"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac217c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2180"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac2120",
      "DATA",
      [
        "storage",
        "00c8d020",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ac216c",
      "READ",
      [
        "storage",
        "00ca4b38",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00ac2170",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2c78"
      ]
    ]
  ],
  "added": [
    [
      "00ac231c",
      "DATA",
      [
        "storage",
        "00c8d420",
        null,
        "pointer"
      ]
    ],
    [
      "00ac2368",
      "READ",
      [
        "storage",
        "00ca4f38",
        null,
        "undefined1"
      ]
    ],
    [
      "00ac236c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac2c78"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2120`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md#insn-00ac2120) · [`00ac217c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md#insn-00ac217c) · [`00ac2180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac20e0.md#insn-00ac2180)

~~~diff
- 00ac2120 ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00ac2120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac2120 bytes 680200f9
- 00ac217c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ac217c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ac217c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:2b:8"]]
- 00ac217c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ac217c bytes ffaf0039
- 00ac2180 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ac2180 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:20:8"]]
- 00ac2180 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ac2180 bytes e8830039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c5ed306354e297eb55c75aa4af2e07"></a>

### [`00ac2ddc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md) → [`00ac2fd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac2/00ac2fd8.md) FUN_00ac2fd8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac2f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2f54.md) · 呼出先 4件 [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`0078dc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078dc6c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00ac3150`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3150.md) · 呼出先 4件 [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`0078dcac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078dcac.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 48.39% / 新版 46.88%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2df8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac2f14"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac2ff4"
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
      "unmatched:00ac2df8",
      "DATA",
      [
        "storage",
        "00c8d020",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:00ac2e0c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac3024"
      ]
    ],
    [
      "unmatched:00ac2ecc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac30e4"
      ]
    ]
  ],
  "added": [
    [
      "00ac2ff4",
      "DATA",
      [
        "storage",
        "00c8d420",
        null,
        "pointer"
      ]
    ],
    [
      "00ac3008",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac3024"
      ]
    ],
    [
      "00ac30c8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ac30e4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2df8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md#insn-00ac2df8) · [`00ac2e0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md#insn-00ac2e0c) · [`00ac2e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2ddc.md#insn-00ac2e24)
- 新版 `00ac3020`（命令位置の公開資料なし）

~~~diff
- 00ac2df8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ac2df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac2df8 bytes 080000f9
- 00ac2e0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ac2e0c ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00ac2e0c bytes e00000b5
- 00ac2e24 ["INT_ADD", "register:40f0:8", ["const:ac2e24:8", "const:4:8"]]
- 00ac2e24 ["CALL", null, ["callee:00c57e80:8"]]
+ 00ac3020 ["INT_ADD", "register:40f0:8", ["const:ac3020:8", "const:4:8"]]
+ 00ac3020 ["CALL", null, ["callee:00c57e80:8"]]
- 00ac2e24 bytes 17530694
+ 00ac3020 bytes 98530694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20cc0778353d6e1f7d91b6b2018b9ee6"></a>

### [`00ac2fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2fb0.md) → [`00ac31ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac31ac.md) FUN_00ac31ac

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac31b8",
      "incomplete_value": false,
      "site": "00ac31b8",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac31b8",
      "DATA",
      [
        "storage",
        "00c8d040",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac31b8",
      "DATA",
      [
        "storage",
        "00c8d440",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac2fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac2/00ac2fb0.md#insn-00ac2fb8)
- 新版 `00ac31b4`（命令位置の公開資料なし）

~~~diff
- 00ac2fb8 ["COPY", "tmp:0:8", ["const:40:8"]]
- 00ac2fb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ac2fb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ac2fb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac31b4 ["COPY", "tmp:0:8", ["const:440:8"]]
+ 00ac31b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac31b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac31b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ac2fb8 bytes 29010191
+ 00ac31b4 bytes 29011191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-273157330cf646a93ca5f6e4a6c5daf4"></a>

### [`00ac306c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md) → [`00ac3268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3268.md) FUN_00ac3268

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 57.14% / 新版 57.14%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3094"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac328c"
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
      "unmatched:00ac3090",
      "DATA",
      [
        "storage",
        "00c8d0c0",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:00ac3098",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac309c",
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
      "00ac328c",
      "DATA",
      [
        "storage",
        "00c8d4c0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac3294",
      "READ",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac3298",
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

- 旧版 [`00ac3080`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac3080) · [`00ac3090`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac3090) · [`00ac3094`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac306c.md#insn-00ac3094)
- 新版 `00ac327c`（命令位置の公開資料なし）

~~~diff
- 00ac3080 ["INT_ADD", "register:40f0:8", ["const:ac3080:8", "const:4:8"]]
- 00ac3080 ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac327c ["INT_ADD", "register:40f0:8", ["const:ac327c:8", "const:4:8"]]
+ 00ac327c ["CALL", null, ["callee:00c57e90:8"]]
- 00ac3080 bytes 84520694
+ 00ac327c bytes 05530694
- 00ac3090 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00ac3090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac3090 bytes 080000f9
- 00ac3094 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8:8"]]
- 00ac3094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5000:16"]]
- 00ac3094 bytes 0080803c
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12eac6e89616224f4714f1c8818dfeb3"></a>

### [`00ac3104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md) → [`00ac3300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3300.md) FUN_00ac3300

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 38.46% / 新版 38.46%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3104"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3108"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac3104",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac3108",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac3128",
      "DATA",
      [
        "storage",
        "00c8d140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3300",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac3304",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac3324",
      "DATA",
      [
        "storage",
        "00c8d540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac3104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md#insn-00ac3104) · [`00ac3108`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md#insn-00ac3108) · [`00ac3118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3104.md#insn-00ac3118)
- 新版 `00ac3314`（命令位置の公開資料なし）

~~~diff
- 00ac3104 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac3104 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac3104 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ac3104 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac3104 bytes fd7bbea9
- 00ac3108 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac3108 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ac3108 bytes f30b00f9
- 00ac3118 ["INT_ADD", "register:40f0:8", ["const:ac3118:8", "const:4:8"]]
- 00ac3118 ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac3314 ["INT_ADD", "register:40f0:8", ["const:ac3314:8", "const:4:8"]]
+ 00ac3314 ["CALL", null, ["callee:00c57e90:8"]]
- 00ac3118 bytes 5e520694
+ 00ac3314 bytes df520694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01dee76557dcf82bca1e896ce9432cc9"></a>

### [`00ac3138`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3138.md) → [`00ac3334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3334.md) FUN_00ac3334

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac3340",
      "incomplete_value": false,
      "site": "00ac3340",
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
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac3340",
      "DATA",
      [
        "storage",
        "00c8d140",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3340",
      "DATA",
      [
        "storage",
        "00c8d540",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac3140`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3138.md#insn-00ac3140)
- 新版 `00ac333c`（命令位置の公開資料なし）

~~~diff
- 00ac3140 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00ac3140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ac3140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ac3140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac333c ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00ac333c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac333c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac333c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ac3140 bytes 29010591
+ 00ac333c bytes 29011591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad48abe12e48f5d66ffc6a5d40bcc90a"></a>

### [`00ac3154`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3154.md) → [`00ac3350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3350.md) FUN_00ac3350

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00abf2b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abf/00abf2b4.md) [`00ac32b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32b8.md) [`00ac32bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32bc.md) [`00aca9d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca9d8.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00abf4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abf/00abf4b0.md) [`00ac34b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac34b4.md) [`00ac34b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac34b8.md) [`00acabd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acabd4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.12% / 新版 95.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac3388",
      "incomplete_value": false,
      "site": "00ac3388",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac318c",
      "incomplete_value": false,
      "site": "00ac318c",
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
            "const:1b0:8"
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
      "00ac3388",
      "DATA",
      [
        "storage",
        "00c8d1b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac33c4",
      "READ",
      [
        "storage",
        "00c8d1d0",
        null,
        "pointer"
      ]
    ],
    [
      "00ac33c4",
      "READ",
      [
        "storage",
        "00c8d1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac3388",
      "DATA",
      [
        "storage",
        "00c8d5b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac33c4",
      "READ",
      [
        "storage",
        "00c8d5d0",
        null,
        "pointer"
      ]
    ],
    [
      "00ac33c4",
      "READ",
      [
        "storage",
        "00c8d5d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac317c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3154.md#insn-00ac317c) · [`00ac3184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3154.md#insn-00ac3184) · [`00ac31a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3154.md#insn-00ac31a0)
- 新版 `00ac3378`（命令位置の公開資料なし） · `00ac3380`（命令位置の公開資料なし） · `00ac339c`（命令位置の公開資料なし）

~~~diff
- 00ac317c ["INT_ADD", "register:40f0:8", ["const:ac317c:8", "const:4:8"]]
- 00ac317c ["CALL", null, ["callee:00abf4b0:8"]]
+ 00ac3378 ["INT_ADD", "register:40f0:8", ["const:ac3378:8", "const:4:8"]]
+ 00ac3378 ["CALL", null, ["callee:00abf4b0:8"]]
- 00ac317c bytes 4ef0ff97
+ 00ac3378 bytes 4ef0ff97
- 00ac3184 ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00ac3184 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac3184 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac3184 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac3380 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00ac3380 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac3380 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac3380 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac3184 bytes 08c10691
+ 00ac3380 bytes 08c11691
- 00ac31a0 ["INT_ADD", "register:40f0:8", ["const:ac31a0:8", "const:4:8"]]
- 00ac31a0 ["CALL", null, ["callee:00acabd4:8"]]
+ 00ac339c ["INT_ADD", "register:40f0:8", ["const:ac339c:8", "const:4:8"]]
+ 00ac339c ["CALL", null, ["callee:00acabd4:8"]]
- 00ac31a0 bytes 0e1e0094
+ 00ac339c bytes 0e1e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dabc86177cb05ef3232f37636c89ebdb"></a>

### [`00ac32a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32a4.md) → [`00ac34a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac34a0.md) FUN_00ac34a0

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac34ac",
      "incomplete_value": false,
      "site": "00ac34ac",
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
            "const:5b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac32b0",
      "incomplete_value": false,
      "site": "00ac32b0",
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
            "const:1b0:8"
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
      "00ac34ac",
      "DATA",
      [
        "storage",
        "00c8d1b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac34ac",
      "DATA",
      [
        "storage",
        "00c8d5b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac32ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32a4.md#insn-00ac32ac)
- 新版 `00ac34a8`（命令位置の公開資料なし）

~~~diff
- 00ac32ac ["COPY", "tmp:0:8", ["const:1b0:8"]]
- 00ac32ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ac32ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ac32ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac34a8 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00ac34a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac34a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac34a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ac32ac bytes 29c10691
+ 00ac34a8 bytes 29c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11f167d42b9778c2f7177f111f4c0828"></a>

### [`00ac32c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32c0.md) → [`00ac34bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac34bc.md) FUN_00ac34bc

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 4件 [`00756264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00756/00756264.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`0085bb30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085bb30.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`007562a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00756/007562a4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`0085bb70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085bb70.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.61% / 新版 82.61%

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
      "site": "00ac32f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac32f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3320"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac32e8",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ac32ec",
      "READ",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ac32f4",
      "WRITE",
      [
        "storage",
        "00ca4568",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ac34e4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00ac34e8",
      "READ",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ],
    [
      "00ac34f0",
      "WRITE",
      [
        "storage",
        "00ca4968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac32f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32c0.md#insn-00ac32f4) · [`00ac32f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32c0.md#insn-00ac32f8) · [`00ac3320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac32c0.md#insn-00ac3320)

~~~diff
- 00ac32f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:568:8"]]
- 00ac32f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00ac32f4 bytes 09b502f9
- 00ac32f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
- 00ac32f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00ac32f8 bytes cabe02f9
- 00ac3320 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:578:8"]]
- 00ac3320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00ac3320 bytes d4be02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc308f8a45ddbcbf1f3826a777fc6c85"></a>

### [`00ac33b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md) → [`00ac35b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac35b4.md) FUN_00ac35b4

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00ac35d8",
      "incomplete_value": false,
      "site": "00ac35d8",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac35d8",
      "DATA",
      [
        "storage",
        "00c8d240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac35d8",
      "DATA",
      [
        "storage",
        "00c8d640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac33cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md#insn-00ac33cc) · [`00ac33d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33b8.md#insn-00ac33d8)
- 新版 `00ac35c8`（命令位置の公開資料なし） · `00ac35d4`（命令位置の公開資料なし）

~~~diff
- 00ac33cc ["INT_ADD", "register:40f0:8", ["const:ac33cc:8", "const:4:8"]]
- 00ac33cc ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac35c8 ["INT_ADD", "register:40f0:8", ["const:ac35c8:8", "const:4:8"]]
+ 00ac35c8 ["CALL", null, ["callee:00c57e90:8"]]
- 00ac33cc bytes b1510694
+ 00ac35c8 bytes 32520694
- 00ac33d8 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00ac33d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac33d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac33d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac35d4 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00ac35d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac35d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac35d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac33d8 bytes 08010991
+ 00ac35d4 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97c9644e42cf6c8068e41aa7af704d78"></a>

### [`00ac33ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33ec.md) → [`00ac35e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac35e8.md) FUN_00ac35e8

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac35f4",
      "incomplete_value": false,
      "site": "00ac35f4",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac35f4",
      "DATA",
      [
        "storage",
        "00c8d240",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac35f4",
      "DATA",
      [
        "storage",
        "00c8d640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac33f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac33ec.md#insn-00ac33f4)
- 新版 `00ac35f0`（命令位置の公開資料なし）

~~~diff
- 00ac33f4 ["COPY", "tmp:0:8", ["const:240:8"]]
- 00ac33f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ac33f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ac33f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac35f0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00ac35f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac35f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac35f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ac33f4 bytes 29010991
+ 00ac35f0 bytes 29011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0843791f8d5cb396493db7e468f9aff"></a>

### [`00ac3408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md) → [`00ac3604`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3604.md) FUN_00ac3604

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0048ce10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce10.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008b79cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b79cc.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0048ce50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce50.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008b7a10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b7a10.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.58% / 新版 93.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac36e8",
      "incomplete_value": true,
      "site": "00ac36fc",
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
                "const:baa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac3714",
      "incomplete_value": false,
      "site": "00ac371c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac363c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac3440",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00ac363c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00ac3658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00ac36a8",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "qword"
      ]
    ]
  ],
  "added": [
    [
      "00ac363c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00ac3658",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00ac36a8",
      "DATA",
      [
        "storage",
        "0039b1b4",
        null,
        "dword"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac3440`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac3440) · [`00ac345c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac345c) · [`00ac3490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3408.md#insn-00ac3490)
- 新版 `00ac363c`（命令位置の公開資料なし） · `00ac3658`（命令位置の公開資料なし） · `00ac368c`（命令位置の公開資料なし）

~~~diff
- 00ac3440 ["INT_ADD", "register:40f0:8", ["const:ac3440:8", "const:4:8"]]
- 00ac3440 ["CALL", null, ["ram:47acb4:8"]]
+ 00ac363c ["INT_ADD", "register:40f0:8", ["const:ac363c:8", "const:4:8"]]
+ 00ac363c ["CALL", null, ["ram:47acf4:8"]]
- 00ac3440 bytes 1ddee697
+ 00ac363c bytes aedde697
- 00ac345c ["INT_ADD", "register:40f0:8", ["const:ac345c:8", "const:4:8"]]
- 00ac345c ["CALL", null, ["ram:47acb4:8"]]
+ 00ac3658 ["INT_ADD", "register:40f0:8", ["const:ac3658:8", "const:4:8"]]
+ 00ac3658 ["CALL", null, ["ram:47acf4:8"]]
- 00ac345c bytes 16dee697
+ 00ac3658 bytes a7dde697
- 00ac3490 ["INT_ADD", "register:40f0:8", ["const:ac3490:8", "const:4:8"]]
- 00ac3490 ["CALL", null, ["callee:0048ce50:8"]]
+ 00ac368c ["INT_ADD", "register:40f0:8", ["const:ac368c:8", "const:4:8"]]
+ 00ac368c ["CALL", null, ["callee:0048ce50:8"]]
- 00ac3490 bytes 6026e797
+ 00ac368c bytes f125e797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816a5585b52005a1175a97ca94d3621b"></a>

### [`00ac3678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md) → [`00ac3874`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3874.md) FUN_00ac3874

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00ac3888",
      "incomplete_value": false,
      "site": "00ac388c",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac388c",
      "DATA",
      [
        "storage",
        "00c8d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac388c",
      "DATA",
      [
        "storage",
        "00c8d6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac3684`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md#insn-00ac3684) · [`00ac368c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3678.md#insn-00ac368c)
- 新版 `00ac3880`（命令位置の公開資料なし） · `00ac3888`（命令位置の公開資料なし）

~~~diff
- 00ac3684 ["INT_ADD", "register:40f0:8", ["const:ac3684:8", "const:4:8"]]
- 00ac3684 ["CALL", null, ["callee:00c57e90:8"]]
+ 00ac3880 ["INT_ADD", "register:40f0:8", ["const:ac3880:8", "const:4:8"]]
+ 00ac3880 ["CALL", null, ["callee:00c57e90:8"]]
- 00ac3684 bytes 03510694
+ 00ac3880 bytes 84510694
- 00ac368c ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00ac368c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac368c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac368c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac3888 ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00ac3888 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac3888 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac3888 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac368c bytes 08c10a91
+ 00ac3888 bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d249996224ef69b141889367a3b705d9"></a>

### [`00ac369c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac369c.md) → [`00ac3898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3898.md) FUN_00ac3898

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00ac389c",
      "incomplete_value": false,
      "site": "00ac38a0",
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
            "const:6b0:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac38a0",
      "DATA",
      [
        "storage",
        "00c8d2b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac38a0",
      "DATA",
      [
        "storage",
        "00c8d6b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac36a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac369c.md#insn-00ac36a0)
- 新版 `00ac389c`（命令位置の公開資料なし）

~~~diff
- 00ac36a0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00ac36a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac36a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac36a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac389c ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 00ac389c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac389c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac389c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac36a0 bytes 08c10a91
+ 00ac389c bytes 08c11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0eb81463ea7498929abf7e8284279743"></a>

### [`00ac36f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac36f4.md) → [`00ac38f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac38f0.md) _INIT_244

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 71.75% / 新版 71.75%

CFGの説明率　旧版 35.00% / 新版 34.15%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `unresolved_store_alignment` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac36f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac36f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac36fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac36f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac36fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac3700",
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
      "00ac38f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00ac38f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac38fc",
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

- 旧版 [`00ac36f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac36f4.md#insn-00ac36f8) · [`00ac36fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac36f4.md#insn-00ac36fc) · [`00ac3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac36f4.md#insn-00ac3700)

~~~diff
- 00ac36f8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac36f8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac36f8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:f0:8"]]
- 00ac36f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac36f8 bytes fd7b0fa9
- 00ac36fc ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ac36fc ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ac36fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:100:8"]]
- 00ac36fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac36fc bytes fc5710a9
- 00ac3700 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ac3700 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ac3700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:110:8"]]
- 00ac3700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac3700 bytes f44f11a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ebd90d13d3ef1e93d8d6c9e04693f2d"></a>

### [`00ac3a84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3a84.md) → [`00ac3c80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac3/00ac3c80.md) FUN_00ac3c80

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00856dec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00856/00856dec.md) · 呼出先 28件 [`0043dd98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043d/0043dd98.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046d9a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d9a4.md) [`0046e4f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046e/0046e4f8.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md)
- 新版 呼出元 1件 [`00856e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00856/00856e2c.md) · 呼出先 28件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046d9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d9e4.md) [`0046e538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046e/0046e538.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 52.75% / 新版 52.75%

CFGの説明率　旧版 32.29% / 新版 32.48%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 4件, `store_condition` 3件, `store_value` 1件, `unresolved_branch_alignment` 75件, `unresolved_call_alignment` 101件, `unresolved_store_alignment` 79件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3acc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3b10"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac3d8c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac3acc",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac3ae0",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00ac3b10",
      "DATA",
      [
        "storage",
        "00336f64",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00ac3cc8",
      "WRITE",
      [
        "storage",
        "Stack[-0x78]",
        null,
        null
      ]
    ],
    [
      "00ac3cdc",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00ac3d0c",
      "DATA",
      [
        "storage",
        "00336f64",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac3acc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3a84.md#insn-00ac3acc) · [`00ac3b10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3a84.md#insn-00ac3b10) · [`00ac3b90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac3/00ac3a84.md#insn-00ac3b90)
- 新版 `00ac3d8c`（命令位置の公開資料なし）

~~~diff
- 00ac3acc ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00ac3acc ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:ffffffffffffffe8:8"]]
- 00ac3acc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ac3acc bytes a8831ef8
- 00ac3b10 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:10:8"]]
- 00ac3b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00ac3b10 bytes 281300b9
- 00ac3b90 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
- 00ac3b90 ["CBRANCH", null, ["local:b27:8", "tmp:0:1"]]
+ 00ac3d8c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:4", "const:0:4"]]
+ 00ac3d8c ["CBRANCH", null, ["local:b25:8", "tmp:0:1"]]
- 00ac3b90 bytes c8030035
+ 00ac3d8c bytes c8030035
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9651860faab1803c53a0f6bd9f74221a"></a>

### [`00ac52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md) → [`00ac54f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac5/00ac54f0.md) FUN_00ac54f0

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00859b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b18.md) · 呼出先 21件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md)
- 新版 呼出元 1件 [`00859b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b58.md) · 呼出先 21件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 57.11% / 新版 57.11%

CFGの説明率　旧版 22.22% / 新版 22.22%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 34件, `call_target` 12件, `unresolved_branch_alignment` 52件, `unresolved_call_alignment` 83件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ac556c",
      "incomplete_value": true,
      "site": "00ac556c",
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
      "definition_site": "00ac5370",
      "incomplete_value": true,
      "site": "00ac5370",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ac559c",
      "incomplete_value": true,
      "site": "00ac559c",
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
      "definition_site": "00ac53a0",
      "incomplete_value": true,
      "site": "00ac53a0",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac54d0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac5568",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00ac5378",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "unmatched:00ac5380",
      "PARAM",
      [
        "storage",
        "00c70d78",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00ac5568",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00ac5574",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00ac557c",
      "PARAM",
      [
        "storage",
        "00c71178",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac53a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md#insn-00ac53a0) · [`00ac54d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md#insn-00ac54d0) · [`00ac5510`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md#insn-00ac5510)
- 新版 `00ac559c`（命令位置の公開資料なし）

~~~diff
- 00ac53a0 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00ac53a0 ["CBRANCH", null, ["local:b46:8", "tmp:0:1"]]
+ 00ac559c ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
+ 00ac559c ["CBRANCH", null, ["local:b55:8", "tmp:0:1"]]
- 00ac53a0 bytes 801300b4
+ 00ac559c bytes 801300b4
- 00ac54d0 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ac54d0 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00ac54d0 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00ac54d0 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00ac54d0 bytes 08a5881a
- 00ac5510 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ac5510 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00ac5510 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00ac5510 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00ac5510 bytes 09a5881a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd940bcbd740479c3361846063366d05"></a>

### [`00ac6a98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md) → [`00ac6c94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac6/00ac6c94.md) FUN_00ac6c94

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md) · 呼出先 13件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00ac54f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac5/00ac54f0.md) · 呼出先 13件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 85.06% / 新版 85.06%

CFGの説明率　旧版 62.79% / 新版 62.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 5件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac6b80"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac6bf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac6e0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac6af8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:00ac6b28",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:00ac6b30",
      "DATA",
      [
        "storage",
        "00336f58",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00ac6cf4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac6d24",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac6d2c",
      "DATA",
      [
        "storage",
        "00336f58",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac6af8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md#insn-00ac6af8) · [`00ac6b28`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md#insn-00ac6b28) · [`00ac6b80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac6/00ac6a98.md#insn-00ac6b80)

~~~diff
- 00ac6af8 ["INT_ADD", "register:40f0:8", ["const:ac6af8:8", "const:4:8"]]
- 00ac6af8 ["CALL", null, ["ram:46c984:8"]]
- 00ac6af8 bytes a397e697
- 00ac6b28 ["INT_ADD", "register:40f0:8", ["const:ac6b28:8", "const:4:8"]]
- 00ac6b28 ["CALL", null, ["ram:46c984:8"]]
- 00ac6b28 bytes 9797e697
- 00ac6b80 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ac6b80 ["COPY", "tmp:1:4", ["register:4000:4"]]
- 00ac6b80 ["BOOL_NEGATE", "tmp:2:1", ["tmp:0:1"]]
- 00ac6b80 ["CBRANCH", null, ["const:2:4", "tmp:2:1"]]
- 00ac6b80 bytes 0aa4801a
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13c7526a258a896fad02291322e2c013"></a>

### [`00ac7008`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md) → [`00ac7204`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7204.md) FUN_00ac7204

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00ac52f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac5/00ac52f4.md) · 呼出先 13件 [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`004687c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/004687c4.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 1件 [`00ac54f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac5/00ac54f0.md) · 呼出先 13件 [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`00468804`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468804.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 77.87% / 新版 77.87%

CFGの説明率　旧版 24.29% / 新版 23.94%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `call_target` 1件, `store_condition` 1件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac7170"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac7210"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac726c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac7068",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:00ac7098",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "unmatched:00ac70a0",
      "DATA",
      [
        "storage",
        "00336f58",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00ac7264",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac7294",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac729c",
      "DATA",
      [
        "storage",
        "00336f58",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac7050`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md#insn-00ac7050) · [`00ac7068`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md#insn-00ac7068) · [`00ac7098`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7008.md#insn-00ac7098)
- 新版 `00ac724c`（命令位置の公開資料なし）

~~~diff
- 00ac7050 ["INT_ADD", "register:40f0:8", ["const:ac7050:8", "const:4:8"]]
- 00ac7050 ["CALL", null, ["callee:00467b2c:8"]]
+ 00ac724c ["INT_ADD", "register:40f0:8", ["const:ac724c:8", "const:4:8"]]
+ 00ac724c ["CALL", null, ["callee:00467b2c:8"]]
- 00ac7050 bytes a782e697
+ 00ac724c bytes 3882e697
- 00ac7068 ["INT_ADD", "register:40f0:8", ["const:ac7068:8", "const:4:8"]]
- 00ac7068 ["CALL", null, ["ram:46c984:8"]]
- 00ac7068 bytes 4796e697
- 00ac7098 ["INT_ADD", "register:40f0:8", ["const:ac7098:8", "const:4:8"]]
- 00ac7098 ["CALL", null, ["ram:46c984:8"]]
- 00ac7098 bytes 3b96e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff26b5aba1961208a963efa0d45ffb9"></a>

### [`00ac7578`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md) → [`00ac7774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7774.md) _INIT_245

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00ac77b0",
      "incomplete_value": true,
      "site": "00ac77cc",
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac77d4",
      "incomplete_value": true,
      "site": "00ac77f0",
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
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac77f4",
      "incomplete_value": true,
      "site": "00ac7810",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
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
      "00ac77b0",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00ac77d4",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00ac77f4",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ac77b0",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00ac77d4",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00ac77f4",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac75b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md#insn-00ac75b0) · [`00ac76d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md#insn-00ac76d8) · [`00ac77ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7578.md#insn-00ac77ac)
- 新版 `00ac77ac`（命令位置の公開資料なし） · `00ac78d4`（命令位置の公開資料なし） · `00ac79a8`（命令位置の公開資料なし）

~~~diff
- 00ac75b0 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 00ac75b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ac75b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ac75b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ac77ac ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 00ac77ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac77ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ac77ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ac75b0 bytes 29993b91
+ 00ac77ac bytes 29993c91
- 00ac76d8 ["INT_ADD", "register:40f0:8", ["const:ac76d8:8", "const:4:8"]]
- 00ac76d8 ["CALL", null, ["callee:0043b7f8:8"]]
+ 00ac78d4 ["INT_ADD", "register:40f0:8", ["const:ac78d4:8", "const:4:8"]]
+ 00ac78d4 ["CALL", null, ["callee:0043b7f8:8"]]
- 00ac76d8 bytes 38d0e597
+ 00ac78d4 bytes c9cfe597
- 00ac77ac ["INT_ADD", "register:40f0:8", ["const:ac77ac:8", "const:4:8"]]
- 00ac77ac ["CALL", null, ["callee:00c57e30:8"]]
+ 00ac79a8 ["INT_ADD", "register:40f0:8", ["const:ac79a8:8", "const:4:8"]]
+ 00ac79a8 ["CALL", null, ["callee:00c57e30:8"]]
- 00ac77ac bytes a1400694
+ 00ac79a8 bytes 22410694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d06d5ebbc977e14ae61fa5b47eb3ffaa"></a>

### [`00ac798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md) → [`00ac7b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7b88.md) FUN_00ac7b88

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00789c10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789c10.md) [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`008cb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb298.md) [`008d305c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d305c.md) [`008feb94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feb94.md) · 呼出先 4件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac7de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md)
- 新版 呼出元 8件 [`00789c50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789c50.md) [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`008cb434`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb434.md) [`008d31f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d31f8.md) [`008fed30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fed30.md) · 呼出先 4件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac7fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7fe0.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

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
      "site": "00ac7ce8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac7aec",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ac7ce8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00ac7ed8",
      "READ",
      [
        "storage",
        "00c9b130",
        null,
        "pointer"
      ]
    ],
    [
      "00ac7edc",
      "DATA",
      [
        "storage",
        "00ca3d5c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ac7ce8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac7ed8",
      "READ",
      [
        "storage",
        "00c9b530",
        null,
        "pointer"
      ]
    ],
    [
      "00ac7edc",
      "DATA",
      [
        "storage",
        "00ca415c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac7aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md#insn-00ac7aec) · [`00ac7ce8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md#insn-00ac7ce8) · [`00ac79e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md#insn-00ac79e4)
- 新版 `00ac7ce8`（命令位置の公開資料なし） · `00ac7ee4`（命令位置の公開資料なし） · `00ac7be0`（命令位置の公開資料なし）

~~~diff
- 00ac7aec ["INT_ADD", "register:40f0:8", ["const:ac7aec:8", "const:4:8"]]
- 00ac7aec ["CALL", null, ["ram:46c984:8"]]
+ 00ac7ce8 ["INT_ADD", "register:40f0:8", ["const:ac7ce8:8", "const:4:8"]]
+ 00ac7ce8 ["CALL", null, ["ram:46c9c4:8"]]
- 00ac7aec bytes a693e697
+ 00ac7ce8 bytes 3793e697
- 00ac7ce8 ["INT_ADD", "register:40f0:8", ["const:ac7ce8:8", "const:4:8"]]
- 00ac7ce8 ["CALL", null, ["callee:008514f8:8"]]
+ 00ac7ee4 ["INT_ADD", "register:40f0:8", ["const:ac7ee4:8", "const:4:8"]]
+ 00ac7ee4 ["CALL", null, ["callee:008514f8:8"]]
- 00ac7ce8 bytes f425f697
+ 00ac7ee4 bytes 8525f697
- 00ac79e4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac79e4 ["INT_ADD", "register:40f0:8", ["const:ac79e4:8", "const:4:8"]]
- 00ac79e4 ["CALLIND", null, ["register:0:8"]]
+ 00ac7be0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac7be0 ["INT_ADD", "register:40f0:8", ["const:ac7be0:8", "const:4:8"]]
+ 00ac7be0 ["CALLIND", null, ["register:0:8"]]
- 00ac79e4 bytes 00013fd6
+ 00ac7be0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1455e63520a13bf50212ed4e13720a93"></a>

### [`00ac7de4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md) → [`00ac7fe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7fe0.md) FUN_00ac7fe0

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac798c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac798c.md) · 呼出先 14件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0046d934`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046d934.md) [`0046da08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046d/0046da08.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md)
- 新版 呼出元 1件 [`00ac7b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac7/00ac7b88.md) · 呼出先 14件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0046d974`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046d974.md) [`0046da48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046d/0046da48.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.65% / 新版 99.65%

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
      "definition_site": "00ac82e4",
      "incomplete_value": true,
      "site": "00ac82e8",
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac809c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac7ea0",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00ac809c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00ac82d8",
      "READ",
      [
        "storage",
        "002c4118",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ac809c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00ac82d8",
      "READ",
      [
        "storage",
        "002c4158",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac7ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md#insn-00ac7ea0) · [`00ac7e1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md#insn-00ac7e1c) · [`00ac7e30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac7/00ac7de4.md#insn-00ac7e30)
- 新版 `00ac809c`（命令位置の公開資料なし） · `00ac8018`（命令位置の公開資料なし） · `00ac802c`（命令位置の公開資料なし）

~~~diff
- 00ac7ea0 ["INT_ADD", "register:40f0:8", ["const:ac7ea0:8", "const:4:8"]]
- 00ac7ea0 ["CALL", null, ["ram:47acb4:8"]]
+ 00ac809c ["INT_ADD", "register:40f0:8", ["const:ac809c:8", "const:4:8"]]
+ 00ac809c ["CALL", null, ["ram:47acf4:8"]]
- 00ac7ea0 bytes 85cbe697
+ 00ac809c bytes 16cbe697
- 00ac7e1c ["INT_ADD", "register:40f0:8", ["const:ac7e1c:8", "const:4:8"]]
- 00ac7e1c ["CALL", null, ["callee:008514f8:8"]]
+ 00ac8018 ["INT_ADD", "register:40f0:8", ["const:ac8018:8", "const:4:8"]]
+ 00ac8018 ["CALL", null, ["callee:008514f8:8"]]
- 00ac7e1c bytes a725f697
+ 00ac8018 bytes 3825f697
- 00ac7e30 ["INT_ADD", "register:40f0:8", ["const:ac7e30:8", "const:4:8"]]
- 00ac7e30 ["CALL", null, ["callee:008514f8:8"]]
+ 00ac802c ["INT_ADD", "register:40f0:8", ["const:ac802c:8", "const:4:8"]]
+ 00ac802c ["CALL", null, ["callee:008514f8:8"]]
- 00ac7e30 bytes a225f697
+ 00ac802c bytes 3325f697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822c0e1e977cea272b6b3cbc327dbf38"></a>

### [`00ac8660`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md) → [`00ac885c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac885c.md) FUN_00ac885c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`0082c824`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082c824.md) [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md) [`006534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md)
- 新版 呼出元 3件 [`0082c864`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082c864.md) [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) · 呼出先 6件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006534dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534dc.md) [`006534e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534e0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac89a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac89a8.md)

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
      "definition_site": "00ac88d4",
      "incomplete_value": false,
      "site": "00ac88d8",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac88b4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac86b8",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00ac88b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00ac88d8",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8928",
      "READ",
      [
        "storage",
        "00c73458",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac88b4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac88d8",
      "DATA",
      [
        "storage",
        "00c73838",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8928",
      "READ",
      [
        "storage",
        "00c73858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac86b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86b8) · [`00ac86b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86b4) · [`00ac86d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8660.md#insn-00ac86d8)
- 新版 `00ac88b4`（命令位置の公開資料なし） · `00ac88b0`（命令位置の公開資料なし） · `00ac88d4`（命令位置の公開資料なし）

~~~diff
- 00ac86b8 ["INT_ADD", "register:40f0:8", ["const:ac86b8:8", "const:4:8"]]
- 00ac86b8 ["CALL", null, ["ram:46c984:8"]]
+ 00ac88b4 ["INT_ADD", "register:40f0:8", ["const:ac88b4:8", "const:4:8"]]
+ 00ac88b4 ["CALL", null, ["ram:46c9c4:8"]]
- 00ac86b8 bytes b390e697
+ 00ac88b4 bytes 4490e697
- 00ac86b4 ["INT_ADD", "register:40f0:8", ["const:ac86b4:8", "const:4:8"]]
- 00ac86b4 ["CALL", null, ["callee:008514f8:8"]]
+ 00ac88b0 ["INT_ADD", "register:40f0:8", ["const:ac88b0:8", "const:4:8"]]
+ 00ac88b0 ["CALL", null, ["callee:008514f8:8"]]
- 00ac86b4 bytes 8123f697
+ 00ac88b0 bytes 1223f697
- 00ac86d8 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00ac86d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ac86d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ac86d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ac88d4 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00ac88d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac88d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ac88d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ac86d8 bytes 08e11091
+ 00ac88d4 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8073fa06f1e73eade00455f0d00b939"></a>

### [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md) → [`00ac89a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac89a8.md) FUN_00ac89a8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`006430b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00643/006430b0.md) [`0067e7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e7b8.md) [`006e4d2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e4/006e4d2c.md) [`0073c8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073c/0073c8f8.md) [`008dc798`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dc/008dc798.md) · 呼出先 5件 [`00acae6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acae6c.md) [`00acb00c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb00c.md) [`00acb010`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb010.md) [`00acb044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb044.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 12件 [`006430f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00643/006430f0.md) [`0067e7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e7f8.md) [`006e4d6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e4/006e4d6c.md) [`0073c938`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073c/0073c938.md) [`008dc934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dc/008dc934.md) · 呼出先 5件 [`00acb068`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb068.md) [`00acb208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb208.md) [`00acb20c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb20c.md) [`00acb240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb240.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00ac8a74",
      "incomplete_value": false,
      "site": "00ac8a88",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8a74",
      "incomplete_value": false,
      "site": "00ac8a94",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
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
      "00ac8a88",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8a94",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8ac0",
      "READ",
      [
        "storage",
        "00c8d360",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac8a88",
      "DATA",
      [
        "storage",
        "00c8d740",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8a94",
      "DATA",
      [
        "storage",
        "00c8d740",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8ac0",
      "READ",
      [
        "storage",
        "00c8d760",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8808`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8808) · [`00ac8834`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8834) · [`00ac8844`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md#insn-00ac8844)
- 新版 `00ac8a04`（命令位置の公開資料なし） · `00ac8a30`（命令位置の公開資料なし） · `00ac8a40`（命令位置の公開資料なし）

~~~diff
- 00ac8808 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac8808 ["INT_ADD", "register:40f0:8", ["const:ac8808:8", "const:4:8"]]
- 00ac8808 ["CALLIND", null, ["register:0:8"]]
+ 00ac8a04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac8a04 ["INT_ADD", "register:40f0:8", ["const:ac8a04:8", "const:4:8"]]
+ 00ac8a04 ["CALLIND", null, ["register:0:8"]]
- 00ac8808 bytes 00013fd6
+ 00ac8a04 bytes 00013fd6
- 00ac8834 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ac8834 ["INT_ADD", "register:40f0:8", ["const:ac8834:8", "const:4:8"]]
- 00ac8834 ["CALLIND", null, ["register:0:8"]]
+ 00ac8a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ac8a30 ["INT_ADD", "register:40f0:8", ["const:ac8a30:8", "const:4:8"]]
+ 00ac8a30 ["CALLIND", null, ["register:0:8"]]
- 00ac8834 bytes 00013fd6
+ 00ac8a30 bytes 00013fd6
- 00ac8844 ["INT_ADD", "register:40f0:8", ["const:ac8844:8", "const:4:8"]]
- 00ac8844 ["CALL", null, ["callee:00acb068:8"]]
+ 00ac8a40 ["INT_ADD", "register:40f0:8", ["const:ac8a40:8", "const:4:8"]]
+ 00ac8a40 ["CALL", null, ["callee:00acb068:8"]]
- 00ac8844 bytes 8a090094
+ 00ac8a40 bytes 8a090094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d90f7b9ee7aec7b6e305fcc5911106"></a>

### [`00ac8a74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md) → [`00ac8c70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8c70.md) FUN_00ac8c70

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 5件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 6件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0065349c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/0065349c.md) [`006534a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00653/006534a0.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00ac87ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac87ac.md)
- 新版 呼出元 5件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) [`00ac0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0454.md) · 呼出先 6件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`006534dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534dc.md) [`006534e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00653/006534e0.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00ac89a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac89a8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 54.55% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件, `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ac8cc8",
      "incomplete_value": false,
      "site": "00ac8ccc",
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
            "const:838:8"
          ]
        ]
      ]
    },
    "old": {
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8b34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ac8d30"
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
      "00ac8ca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00ac8ccc",
      "DATA",
      [
        "storage",
        "00c73438",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8d1c",
      "READ",
      [
        "storage",
        "00c73458",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ac8ca8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00ac8ccc",
      "DATA",
      [
        "storage",
        "00c73838",
        null,
        "undefined *"
      ]
    ],
    [
      "00ac8d1c",
      "READ",
      [
        "storage",
        "00c73858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8aac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md#insn-00ac8aac) · [`00ac8b34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8a74.md#insn-00ac8b34)
- 新版 `00ac8ca8`（命令位置の公開資料なし） · `00ac8d30`（命令位置の公開資料なし）

~~~diff
- 00ac8aac ["INT_ADD", "register:40f0:8", ["const:ac8aac:8", "const:4:8"]]
- 00ac8aac ["CALL", null, ["ram:46c984:8"]]
+ 00ac8ca8 ["INT_ADD", "register:40f0:8", ["const:ac8ca8:8", "const:4:8"]]
+ 00ac8ca8 ["CALL", null, ["ram:46c9c4:8"]]
- 00ac8aac bytes b68fe697
+ 00ac8ca8 bytes 478fe697
- 00ac8b34 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ac8b34 ["CBRANCH", null, ["local:b8:8", "tmp:0:1"]]
- 00ac8b34 bytes 21030054
+ 00ac8d30 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
+ 00ac8d30 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
+ 00ac8d30 bytes 21030054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14194f553965be68c9a8133c1ba41fac"></a>

### [`00ac8b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8b9c.md) → [`00ac8d98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8d98.md) FUN_00ac8d98

採用 · 移動量 `+0x1fc` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00a7239c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a72/00a7239c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00a72594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a72/00a72594.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-b70366f51c64078721b514a38384d998"></a>

### [`00ac8c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c00.md) → [`00ac8dfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8dfc.md) FUN_00ac8dfc

採用 · 移動量 `+0x1fc` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 11件 [`00693418`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00693/00693418.md) [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ccd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082c/0082ccd8.md) [`008c3818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c3/008c3818.md) [`008c506c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c5/008c506c.md) · 呼出先 0件 
- 新版 呼出元 11件 [`00693458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00693/00693458.md) [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082cd18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082c/0082cd18.md) [`008c385c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c3/008c385c.md) [`008c5208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c5/008c5208.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-4f00f6657ea116bfb7bc3486e5f26a57"></a>

### [`00ac8c14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c14.md) → [`00ac8e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8e10.md) FUN_00ac8e10

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 11件 [`00659e5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00659/00659e5c.md) [`0065bdec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065b/0065bdec.md) [`0068adf0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068adf0.md) [`0068c5d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068c/0068c5d0.md) [`006d1fa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d1/006d1fa4.md) · 呼出先 0件 
- 新版 呼出元 11件 [`00659e9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00659/00659e9c.md) [`0065be2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065b/0065be2c.md) [`0068ae30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068ae30.md) [`0068c610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068c/0068c610.md) [`006d1fe4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d1/006d1fe4.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-a30b48704977c533b783ba906283d931"></a>

### [`00ac8c60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md) → [`00ac8e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8e5c.md) FUN_00ac8e5c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 8件 [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) [`0068aa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068aa48.md) [`006d3dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md) [`00700118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700118.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 6件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00859b0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00859/00859b0c.md) [`0085b264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b264.md) [`0085b26c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b26c.md) [`0085b2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0085b/0085b2a0.md)
- 新版 呼出元 8件 [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) [`0068aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md) [`006d3e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d3/006d3e3c.md) [`00700158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700158.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 6件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00859b4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00859/00859b4c.md) [`0085b2a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2a4.md) [`0085b2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2ac.md) [`0085b2e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0085b/0085b2e0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 80.82% / 新版 80.82%

CFGの説明率　旧版 52.38% / 新版 45.83%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 2件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8d6c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00ac8f68"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8cf4"
    }
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ac8cd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md#insn-00ac8cd0) · [`00ac8cf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md#insn-00ac8cf4) · [`00ac8d68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8c60.md#insn-00ac8d68)
- 新版 `00ac8ecc`（命令位置の公開資料なし）

~~~diff
- 00ac8cd0 ["INT_ADD", "register:40f0:8", ["const:ac8cd0:8", "const:4:8"]]
- 00ac8cd0 ["CALL", null, ["callee:00ac8f80:8"]]
+ 00ac8ecc ["INT_ADD", "register:40f0:8", ["const:ac8ecc:8", "const:4:8"]]
+ 00ac8ecc ["CALL", null, ["callee:00ac8f80:8"]]
- 00ac8cd0 bytes 2d000094
+ 00ac8ecc bytes 2d000094
- 00ac8cf4 ["COPY", "register:5100:4", ["register:5020:4"]]
- 00ac8cf4 ["COPY", "register:5104:4", ["const:0:4"]]
- 00ac8cf4 ["COPY", "register:5108:8", ["const:0:8"]]
- 00ac8cf4 ["COPY", "register:5110:8", ["const:0:8"]]
- 00ac8cf4 bytes 2868221e
- 00ac8d68 ["COPY", "register:5000:4", ["register:5000:4"]]
- 00ac8d68 ["COPY", "register:5004:4", ["const:0:4"]]
- 00ac8d68 ["COPY", "register:5008:8", ["const:0:8"]]
- 00ac8d68 ["COPY", "register:5010:8", ["const:0:8"]]
- 00ac8d68 bytes 0068211e
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a8adb532ad06713c54a6ad6f0d30588"></a>

### [`00ac8ec8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ec8.md) → [`00ac90c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac90c4.md) FUN_00ac90c4

採用 · 移動量 `+0x1fc` · 根拠 `leaf_bytes_and_unique_code_order` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `compiler_shape_candidate`

- 旧版 呼出元 8件 [`00657f4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00657/00657f4c.md) [`0068aa48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068a/0068aa48.md) [`006d3dfc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d3/006d3dfc.md) [`00700118`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700118.md) [`00769d44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00769/00769d44.md) · 呼出先 0件 
- 新版 呼出元 8件 [`00657f8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00657/00657f8c.md) [`0068aa88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068a/0068aa88.md) [`006d3e3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d3/006d3e3c.md) [`00700158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700158.md) [`00769d84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00769/00769d84.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 0.00% / 新版 0.00%

CFGの説明率　旧版 0.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-bcbaa80cc24c884b9de4d302ce93a4d2"></a>

### [`00ac8ee4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ee4.md) → [`00ac90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac90e0.md) FUN_00ac90e0

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`0065cc8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065c/0065cc8c.md) [`0065d5f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0065d/0065d5f0.md) [`0068bdd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0068b/0068bdd0.md) [`006d4d54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006d4/006d4d54.md) [`00700504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700504.md) · 呼出先 4件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`00ac8d84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8d84.md)
- 新版 呼出元 9件 [`0065cccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065c/0065cccc.md) [`0065d630`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0065d/0065d630.md) [`0068be10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0068b/0068be10.md) [`006d4d94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006d4/006d4d94.md) [`00700544`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700544.md) · 呼出先 4件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`00ac8f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac8/00ac8f80.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 68.71% / 新版 68.71%

CFGの説明率　旧版 5.00% / 新版 2.86%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 26件, `unresolved_branch_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8f54"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac8f84"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ac9150"
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
      "unmatched:00ac913c",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac915c",
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
      "00ac9338",
      "READ",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ac9358",
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

- 旧版 [`00ac8f54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ee4.md#insn-00ac8f54) · [`00ac8f84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ee4.md#insn-00ac8f84) · [`00ac8fb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8ee4.md#insn-00ac8fb8)
- 新版 `00ac91b4`（命令位置の公開資料なし）

~~~diff
- 00ac8f54 ["COPY", "register:5120:4", ["register:5000:4"]]
- 00ac8f54 ["COPY", "register:5124:4", ["const:0:4"]]
- 00ac8f54 ["COPY", "register:5128:8", ["const:0:8"]]
- 00ac8f54 ["COPY", "register:5130:8", ["const:0:8"]]
- 00ac8f54 bytes 0968211e
- 00ac8f84 ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00ac8f84 ["COPY", "tmp:1:4", ["register:4048:4"]]
- 00ac8f84 ["CBRANCH", null, ["const:2:4", "tmp:0:1"]]
- 00ac8f84 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00ac8f84 bytes 3811881a
- 00ac8fb8 ["INT_ADD", "register:40f0:8", ["const:ac8fb8:8", "const:4:8"]]
- 00ac8fb8 ["CALL", null, ["callee:00469c04:8"]]
+ 00ac91b4 ["INT_ADD", "register:40f0:8", ["const:ac91b4:8", "const:4:8"]]
+ 00ac91b4 ["CALL", null, ["callee:00469c04:8"]]
- 00ac8fb8 bytes 0383e697
+ 00ac91b4 bytes 9482e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de20e38459c59c063d96bff58e49b13b"></a>

### [`00ac9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md) → [`00ac9594`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9594.md) FUN_00ac9594

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 12件 [`0078def8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078d/0078def8.md) [`0078e240`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0078e/0078e240.md) [`0082f0e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082f0e8.md) [`008c2878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c2/008c2878.md) [`008fd364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fd/008fd364.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 12件 [`0078df38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078d/0078df38.md) [`0078e280`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0078e/0078e280.md) [`0082f128`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082f128.md) [`008c28bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c2/008c28bc.md) [`008fd500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fd/008fd500.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.89% / 新版 86.89%

CFGの説明率　旧版 14.29% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9398"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac939c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9398",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac939c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9404",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ]
  ],
  "added": [
    [
      "00ac9594",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac9598",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac9600",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9398`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md#insn-00ac9398) · [`00ac939c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md#insn-00ac939c) · [`00ac93ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9398.md#insn-00ac93ec)
- 新版 `00ac95e8`（命令位置の公開資料なし）

~~~diff
- 00ac9398 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac9398 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac9398 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00ac9398 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ac9398 bytes fd7bbea9
- 00ac939c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00ac939c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00ac939c bytes f30b00f9
- 00ac93ec ["INT_ADD", "register:40f0:8", ["const:ac93ec:8", "const:4:8"]]
- 00ac93ec ["CALL", null, ["callee:008b79c8:8"]]
+ 00ac95e8 ["INT_ADD", "register:40f0:8", ["const:ac95e8:8", "const:4:8"]]
+ 00ac95e8 ["CALL", null, ["callee:008b79c8:8"]]
- 00ac93ec bytes 66b9f797
+ 00ac95e8 bytes f8b8f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e646cae33b964bfa84b40028448a057"></a>

### [`00ac948c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md) → [`00ac9688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9688.md) FUN_00ac9688

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 9件 [`00838a34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00838/00838a34.md) [`008bf810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bf/008bf810.md) [`008d2908`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d2/008d2908.md) [`008d8570`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d8/008d8570.md) [`008d9a68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d9/008d9a68.md) · 呼出先 3件 [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b7984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b7/008b7984.md)
- 新版 呼出元 9件 [`00838a74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00838/00838a74.md) [`008bf854`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bf/008bf854.md) [`008d2aa4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d2/008d2aa4.md) [`008d870c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d8/008d870c.md) [`008d9c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d9/008d9c04.md) · 呼出先 3件 [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b79c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b7/008b79c8.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 91.80% / 新版 91.80%

CFGの説明率　旧版 28.57% / 新版 28.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac94f8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac952c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00ac9530",
      "incomplete_value": false,
      "site": "00ac9534",
      "value": [
        "leaf",
        "const:1:8"
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
      "unmatched:00ac94f8",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ],
    [
      "unmatched:00ac952c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ]
  ],
  "added": [
    [
      "00ac96f4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ],
    [
      "00ac9728",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "008b79c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac94f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md#insn-00ac94f8) · [`00ac952c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md#insn-00ac952c) · [`00ac9534`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac948c.md#insn-00ac9534)
- 新版 `00ac9730`（命令位置の公開資料なし）

~~~diff
- 00ac94f8 ["INT_ADD", "register:40f0:8", ["const:ac94f8:8", "const:4:8"]]
- 00ac94f8 ["CALL", null, ["callee:008b79c8:8"]]
- 00ac94f8 bytes 23b9f797
- 00ac952c ["INT_ADD", "register:40f0:8", ["const:ac952c:8", "const:4:8"]]
- 00ac952c ["CALL", null, ["callee:008b79c8:8"]]
- 00ac952c bytes 16b9f797
- 00ac9534 ["INT_ADD", "register:40f0:8", ["const:ac9534:8", "const:4:8"]]
- 00ac9534 ["CALL", null, ["callee:008b6f18:8"]]
+ 00ac9730 ["INT_ADD", "register:40f0:8", ["const:ac9730:8", "const:4:8"]]
+ 00ac9730 ["CALL", null, ["callee:008b6f18:8"]]
- 00ac9534 bytes 68b6f797
+ 00ac9730 bytes fab5f797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7483bf4d95e3a66fd1feae149e5ae564"></a>

### [`00ac9580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9580.md) → [`00ac977c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac977c.md) FUN_00ac977c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 10件 [`00646040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00646/00646040.md) [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006e7950`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006e7/006e7950.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`008dd868`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008dd/008dd868.md) · 呼出先 6件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`0046961c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/0046961c.md)
- 新版 呼出元 10件 [`00646080`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00646/00646080.md) [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`006e7990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006e7/006e7990.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`008dda04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008dd/008dda04.md) · 呼出先 6件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`0046965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/0046965c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.88% / 新版 77.88%

CFGの説明率　旧版 20.75% / 新版 21.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9594"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac9598"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac9594",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac9598",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac95b4",
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
      "00ac9790",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00ac9794",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00ac97b0",
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

- 旧版 [`00ac9594`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9580.md#insn-00ac9594) · [`00ac9598`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9580.md#insn-00ac9598) · [`00ac95b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9580.md#insn-00ac95b4)

~~~diff
- 00ac9594 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ac9594 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ac9594 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ac9594 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9594 bytes f65706a9
- 00ac9598 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ac9598 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ac9598 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00ac9598 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac9598 bytes f44f07a9
- 00ac95b4 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 00ac95b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ac95b4 bytes e80f00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4815452b901e8bc99a73f87b61b11e73"></a>

### [`00ac98c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98c0.md) → [`00ac9abc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9abc.md) FUN_00ac9abc

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 5件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008fe848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008fe848.md) [`00a3dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3d/00a3dc60.md) [`00ac0258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac0258.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) [`008fe9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe9e4.md) [`00a3de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3de58.md) [`00ac0454`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0454.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-812e719c1e5fe854934ef51a0cfb099b"></a>

### [`00ac98d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98d8.md) → [`00ac9ad4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9ad4.md) FUN_00ac9ad4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 2件 [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`00a73338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a73/00a73338.md) · 呼出先 0件 
- 新版 呼出元 2件 [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`00a73530`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a73/00a73530.md) · 呼出先 0件 

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

<a id="compare-555cffcf06a270ccb80f0d65d90d620d"></a>

### [`00ac98f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md) → [`00ac9aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9aec.md) FUN_00ac9aec

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`008d1aa4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d1/008d1aa4.md) [`008fe848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008fe848.md) · 呼出先 17件 [`0057be68`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0057b/0057be68.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md) [`008b6eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6eec.md)
- 新版 呼出元 7件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`008d1c40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d1/008d1c40.md) [`008fe9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe9e4.md) · 呼出先 17件 [`0057bea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0057b/0057bea8.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md) [`008b6f30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f30.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 86.75% / 新版 86.75%

CFGの説明率　旧版 54.05% / 新版 54.79%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_condition` 3件, `store_value` 1件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 3件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac98f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac98f4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ac98f8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ac98f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac98f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ac98fc",
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
      "00ac9af0",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ac9af4",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ac9af8",
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

- 旧版 [`00ac98f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md#insn-00ac98f4) · [`00ac98f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md#insn-00ac98f8) · [`00ac98fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac98f0.md#insn-00ac98fc)

~~~diff
- 00ac98f4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ac98f4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ac98f4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:80:8"]]
- 00ac98f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac98f4 bytes fd7b08a9
- 00ac98f8 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:90:8"]]
- 00ac98f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c8:8"]]
- 00ac98f8 bytes f94b00f9
- 00ac98fc ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ac98fc ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ac98fc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00ac98fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ac98fc bytes f85f0aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29155911d79fe8f68421588fed2482e8"></a>

### [`00ac9d64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9d64.md) → [`00ac9f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac9/00ac9f60.md) FUN_00ac9f60

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00788c6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00788/00788c6c.md) [`0082ede0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082e/0082ede0.md) [`008caa24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ca/008caa24.md) [`008fe848`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008fe848.md) [`00a3dc60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3d/00a3dc60.md) · 呼出先 15件 [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`005d8b88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005d8/005d8b88.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6ed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6ed4.md)
- 新版 呼出元 6件 [`00788cac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00788/00788cac.md) [`0082ee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082e/0082ee20.md) [`008cabc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ca/008cabc0.md) [`008fe9e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008fe/008fe9e4.md) [`00a3de58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3d/00a3de58.md) · 呼出先 15件 [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`005d8bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005d8/005d8bc8.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f18.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aca0d0",
      "incomplete_value": false,
      "site": "00aca0e4",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ac9ed4",
      "incomplete_value": false,
      "site": "00ac9ee8",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac9f9c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00ac9da0",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00ac9f9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca038",
      "READ",
      [
        "storage",
        "00c9af68",
        null,
        "pointer"
      ]
    ],
    [
      "00aca04c",
      "DATA",
      [
        "storage",
        "00c8b358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ac9f9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca038",
      "READ",
      [
        "storage",
        "00c9b368",
        null,
        "pointer"
      ]
    ],
    [
      "00aca04c",
      "DATA",
      [
        "storage",
        "00c8b758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ac9da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9d64.md#insn-00ac9da0) · [`00ac9d9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9d64.md#insn-00ac9d9c) · [`00ac9db0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac9/00ac9d64.md#insn-00ac9db0)
- 新版 `00ac9f9c`（命令位置の公開資料なし） · `00ac9f98`（命令位置の公開資料なし） · `00ac9fac`（命令位置の公開資料なし）

~~~diff
- 00ac9da0 ["INT_ADD", "register:40f0:8", ["const:ac9da0:8", "const:4:8"]]
- 00ac9da0 ["CALL", null, ["ram:46c984:8"]]
+ 00ac9f9c ["INT_ADD", "register:40f0:8", ["const:ac9f9c:8", "const:4:8"]]
+ 00ac9f9c ["CALL", null, ["ram:46c9c4:8"]]
- 00ac9da0 bytes f98ae697
+ 00ac9f9c bytes 8a8ae697
- 00ac9d9c ["INT_ADD", "register:40f0:8", ["const:ac9d9c:8", "const:4:8"]]
- 00ac9d9c ["CALL", null, ["callee:008514f8:8"]]
+ 00ac9f98 ["INT_ADD", "register:40f0:8", ["const:ac9f98:8", "const:4:8"]]
+ 00ac9f98 ["CALL", null, ["callee:008514f8:8"]]
- 00ac9d9c bytes c71df697
+ 00ac9f98 bytes 581df697
- 00ac9db0 ["INT_ADD", "register:40f0:8", ["const:ac9db0:8", "const:4:8"]]
- 00ac9db0 ["CALL", null, ["callee:00489f4c:8"]]
+ 00ac9fac ["INT_ADD", "register:40f0:8", ["const:ac9fac:8", "const:4:8"]]
+ 00ac9fac ["CALL", null, ["callee:00489f4c:8"]]
- 00ac9db0 bytes 5700e797
+ 00ac9fac bytes e8ffe697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-240ffaa02e574bb305d3be9b94deda1e"></a>

### [`00aca074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca074.md) → [`00aca270`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca270.md) FUN_00aca270

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 7件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) [`008d3700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008d3/008d3700.md) [`008feea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feea4.md) · 呼出先 7件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 7件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) [`008d389c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008d3/008d389c.md) [`008ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff040.md) · 呼出先 7件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.65% / 新版 97.65%

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
      "site": "00aca2b8",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca0bc",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00aca384",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca188",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aca2b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca384",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00aca2b8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca384",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca0bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca074.md#insn-00aca0bc) · [`00aca188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca074.md#insn-00aca188) · [`00aca09c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca074.md#insn-00aca09c)
- 新版 `00aca2b8`（命令位置の公開資料なし） · `00aca384`（命令位置の公開資料なし） · `00aca298`（命令位置の公開資料なし）

~~~diff
- 00aca0bc ["INT_ADD", "register:40f0:8", ["const:aca0bc:8", "const:4:8"]]
- 00aca0bc ["CALL", null, ["ram:46c984:8"]]
+ 00aca2b8 ["INT_ADD", "register:40f0:8", ["const:aca2b8:8", "const:4:8"]]
+ 00aca2b8 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca0bc bytes 328ae697
+ 00aca2b8 bytes c389e697
- 00aca188 ["INT_ADD", "register:40f0:8", ["const:aca188:8", "const:4:8"]]
- 00aca188 ["CALL", null, ["ram:46c984:8"]]
+ 00aca384 ["INT_ADD", "register:40f0:8", ["const:aca384:8", "const:4:8"]]
+ 00aca384 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca188 bytes ff89e697
+ 00aca384 bytes 9089e697
- 00aca09c ["INT_ADD", "register:40f0:8", ["const:aca09c:8", "const:4:8"]]
- 00aca09c ["CALL", null, ["callee:00467860:8"]]
+ 00aca298 ["INT_ADD", "register:40f0:8", ["const:aca298:8", "const:4:8"]]
+ 00aca298 ["CALL", null, ["callee:00467860:8"]]
- 00aca09c bytes e175e697
+ 00aca298 bytes 7275e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b35aed02935748d8ba8ecb0684826c0"></a>

### [`00aca1c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca1c8.md) → [`00aca3c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca3c4.md) FUN_00aca3c4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) [`008feea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feea4.md) [`00a3e32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e32c.md) · 呼出先 11件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md)
- 新版 呼出元 6件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) [`008ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff040.md) [`00a3e524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e524.md) · 呼出先 11件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.78% / 新版 97.78%

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
      "site": "00aca404",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca208",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00aca4ac",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca2b0",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aca404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca4ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00aca404",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca4ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca208`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca1c8.md#insn-00aca208) · [`00aca2b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca1c8.md#insn-00aca2b0) · [`00aca1fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca1c8.md#insn-00aca1fc)
- 新版 `00aca404`（命令位置の公開資料なし） · `00aca4ac`（命令位置の公開資料なし） · `00aca3f8`（命令位置の公開資料なし）

~~~diff
- 00aca208 ["INT_ADD", "register:40f0:8", ["const:aca208:8", "const:4:8"]]
- 00aca208 ["CALL", null, ["ram:46c984:8"]]
+ 00aca404 ["INT_ADD", "register:40f0:8", ["const:aca404:8", "const:4:8"]]
+ 00aca404 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca208 bytes df89e697
+ 00aca404 bytes 7089e697
- 00aca2b0 ["INT_ADD", "register:40f0:8", ["const:aca2b0:8", "const:4:8"]]
- 00aca2b0 ["CALL", null, ["ram:46c984:8"]]
+ 00aca4ac ["INT_ADD", "register:40f0:8", ["const:aca4ac:8", "const:4:8"]]
+ 00aca4ac ["CALL", null, ["ram:46c9c4:8"]]
- 00aca2b0 bytes b589e697
+ 00aca4ac bytes 4689e697
- 00aca1fc ["INT_ADD", "register:40f0:8", ["const:aca1fc:8", "const:4:8"]]
- 00aca1fc ["CALL", null, ["callee:00467860:8"]]
+ 00aca3f8 ["INT_ADD", "register:40f0:8", ["const:aca3f8:8", "const:4:8"]]
+ 00aca3f8 ["CALL", null, ["callee:00467860:8"]]
- 00aca1fc bytes 8975e697
+ 00aca3f8 bytes 1a75e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-674123cd1078883dc93d698d00bd4b4b"></a>

### [`00aca330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca330.md) → [`00aca52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca52c.md) FUN_00aca52c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) [`008feea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feea4.md) [`00a3e32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e32c.md) · 呼出先 12件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046aecc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046a/0046aecc.md)
- 新版 呼出元 6件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) [`008ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff040.md) [`00a3e524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e524.md) · 呼出先 12件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046af0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046a/0046af0c.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

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
      "site": "00aca56c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca370",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00aca634",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca438",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00aca56c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca634",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00aca56c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca634",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca370`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca330.md#insn-00aca370) · [`00aca438`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca330.md#insn-00aca438) · [`00aca364`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca330.md#insn-00aca364)
- 新版 `00aca56c`（命令位置の公開資料なし） · `00aca634`（命令位置の公開資料なし） · `00aca560`（命令位置の公開資料なし）

~~~diff
- 00aca370 ["INT_ADD", "register:40f0:8", ["const:aca370:8", "const:4:8"]]
- 00aca370 ["CALL", null, ["ram:46c984:8"]]
+ 00aca56c ["INT_ADD", "register:40f0:8", ["const:aca56c:8", "const:4:8"]]
+ 00aca56c ["CALL", null, ["ram:46c9c4:8"]]
- 00aca370 bytes 8589e697
+ 00aca56c bytes 1689e697
- 00aca438 ["INT_ADD", "register:40f0:8", ["const:aca438:8", "const:4:8"]]
- 00aca438 ["CALL", null, ["ram:46c984:8"]]
+ 00aca634 ["INT_ADD", "register:40f0:8", ["const:aca634:8", "const:4:8"]]
+ 00aca634 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca438 bytes 5389e697
+ 00aca634 bytes e488e697
- 00aca364 ["INT_ADD", "register:40f0:8", ["const:aca364:8", "const:4:8"]]
- 00aca364 ["CALL", null, ["callee:00467860:8"]]
+ 00aca560 ["INT_ADD", "register:40f0:8", ["const:aca560:8", "const:4:8"]]
+ 00aca560 ["CALL", null, ["callee:00467860:8"]]
- 00aca364 bytes 2f75e697
+ 00aca560 bytes c074e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90de41d20bd22fcffdd7e1217a2c1d2"></a>

### [`00aca4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca4cc.md) → [`00aca6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca6c8.md) FUN_00aca6c8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) [`00a79a0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a79/00a79a0c.md) [`00ac08a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac08a0.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00468b9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468b9c.md) [`00468c20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468c20.md) [`00468f48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00468/00468f48.md)
- 新版 呼出元 5件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) [`00a79c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a79/00a79c04.md) [`00ac0a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0a9c.md) · 呼出先 8件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00468bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468bdc.md) [`00468c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468c60.md) [`00468f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00468/00468f88.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.61% / 新版 98.61%

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
      "site": "00aca77c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca580",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00aca77c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00aca77c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca580`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca4cc.md#insn-00aca580) · [`00aca4f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca4cc.md#insn-00aca4f4) · [`00aca50c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca4cc.md#insn-00aca50c)
- 新版 `00aca77c`（命令位置の公開資料なし） · `00aca6f0`（命令位置の公開資料なし） · `00aca708`（命令位置の公開資料なし）

~~~diff
- 00aca580 ["INT_ADD", "register:40f0:8", ["const:aca580:8", "const:4:8"]]
- 00aca580 ["CALL", null, ["ram:46c984:8"]]
+ 00aca77c ["INT_ADD", "register:40f0:8", ["const:aca77c:8", "const:4:8"]]
+ 00aca77c ["CALL", null, ["ram:46c9c4:8"]]
- 00aca580 bytes 0189e697
+ 00aca77c bytes 9288e697
- 00aca4f4 ["INT_ADD", "register:40f0:8", ["const:aca4f4:8", "const:4:8"]]
- 00aca4f4 ["CALL", null, ["callee:00467860:8"]]
+ 00aca6f0 ["INT_ADD", "register:40f0:8", ["const:aca6f0:8", "const:4:8"]]
+ 00aca6f0 ["CALL", null, ["callee:00467860:8"]]
- 00aca4f4 bytes cb74e697
+ 00aca6f0 bytes 5c74e697
- 00aca50c ["INT_ADD", "register:40f0:8", ["const:aca50c:8", "const:4:8"]]
- 00aca50c ["CALL", null, ["callee:00467b60:8"]]
+ 00aca708 ["INT_ADD", "register:40f0:8", ["const:aca708:8", "const:4:8"]]
+ 00aca708 ["CALL", null, ["callee:00467b60:8"]]
- 00aca50c bytes 8575e697
+ 00aca708 bytes 1675e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac5ac302b45c450682e5234cb0a8e466"></a>

### [`00aca674`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca674.md) → [`00aca870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca870.md) FUN_00aca870

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008cb4a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008cb/008cb4a8.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 2件 [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008cb644`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008cb/008cb644.md) · 呼出先 8件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca8ac",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca6b0",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00aca924",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca728",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca944",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca748",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00aca8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca924",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00aca944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00aca8ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca924",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00aca944",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca6b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca674.md#insn-00aca6b0) · [`00aca728`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca674.md#insn-00aca728) · [`00aca748`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca674.md#insn-00aca748)
- 新版 `00aca8ac`（命令位置の公開資料なし） · `00aca924`（命令位置の公開資料なし） · `00aca944`（命令位置の公開資料なし）

~~~diff
- 00aca6b0 ["INT_ADD", "register:40f0:8", ["const:aca6b0:8", "const:4:8"]]
- 00aca6b0 ["CALL", null, ["ram:46c984:8"]]
+ 00aca8ac ["INT_ADD", "register:40f0:8", ["const:aca8ac:8", "const:4:8"]]
+ 00aca8ac ["CALL", null, ["ram:46c9c4:8"]]
- 00aca6b0 bytes b588e697
+ 00aca8ac bytes 4688e697
- 00aca728 ["INT_ADD", "register:40f0:8", ["const:aca728:8", "const:4:8"]]
- 00aca728 ["CALL", null, ["ram:46c984:8"]]
+ 00aca924 ["INT_ADD", "register:40f0:8", ["const:aca924:8", "const:4:8"]]
+ 00aca924 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca728 bytes 9788e697
+ 00aca924 bytes 2888e697
- 00aca748 ["INT_ADD", "register:40f0:8", ["const:aca748:8", "const:4:8"]]
- 00aca748 ["CALL", null, ["ram:46c984:8"]]
+ 00aca944 ["INT_ADD", "register:40f0:8", ["const:aca944:8", "const:4:8"]]
+ 00aca944 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca748 bytes 8f88e697
+ 00aca944 bytes 2088e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a15719169d82b6f3a1e0d4e118cb1a1"></a>

### [`00aca7ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md) → [`00aca9a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca9a8.md) FUN_00aca9a8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`008feea4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008fe/008feea4.md) [`00a3e32c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a3e/00a3e32c.md) [`00ac08a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac0/00ac08a0.md) · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 5件 [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`008ff040`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ff/008ff040.md) [`00a3e524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3e524.md) [`00ac0a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ac0/00ac0a9c.md) · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

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
      "site": "00acaa00",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca804",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00acaa00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00acaa00",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca804`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md#insn-00aca804) · [`00aca7c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md#insn-00aca7c8) · [`00aca7e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca7ac.md#insn-00aca7e8)
- 新版 `00acaa00`（命令位置の公開資料なし） · `00aca9c4`（命令位置の公開資料なし） · `00aca9e4`（命令位置の公開資料なし）

~~~diff
- 00aca804 ["INT_ADD", "register:40f0:8", ["const:aca804:8", "const:4:8"]]
- 00aca804 ["CALL", null, ["ram:46c984:8"]]
+ 00acaa00 ["INT_ADD", "register:40f0:8", ["const:acaa00:8", "const:4:8"]]
+ 00acaa00 ["CALL", null, ["ram:46c9c4:8"]]
- 00aca804 bytes 6088e697
+ 00acaa00 bytes f187e697
- 00aca7c8 ["INT_ADD", "register:40f0:8", ["const:aca7c8:8", "const:4:8"]]
- 00aca7c8 ["CALL", null, ["callee:00467860:8"]]
+ 00aca9c4 ["INT_ADD", "register:40f0:8", ["const:aca9c4:8", "const:4:8"]]
+ 00aca9c4 ["CALL", null, ["callee:00467860:8"]]
- 00aca7c8 bytes 1674e697
+ 00aca9c4 bytes a773e697
- 00aca7e8 ["INT_ADD", "register:40f0:8", ["const:aca7e8:8", "const:4:8"]]
- 00aca7e8 ["CALL", null, ["callee:00467b2c:8"]]
+ 00aca9e4 ["INT_ADD", "register:40f0:8", ["const:aca9e4:8", "const:4:8"]]
+ 00aca9e4 ["CALL", null, ["callee:00467b2c:8"]]
- 00aca7e8 bytes c174e697
+ 00aca9e4 bytes 5274e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b813b92e58ff134cd8fa3df3ba603b65"></a>

### [`00aca83c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md) → [`00acaa38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acaa38.md) FUN_00acaa38

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0082fb2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0082f/0082fb2c.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) · 呼出先 6件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 2件 [`0082fb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0082f/0082fb6c.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) · 呼出先 6件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

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
      "site": "00acaa9c",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00aca8a0",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "00acaa9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00acaa9c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aca8a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md#insn-00aca8a0) · [`00aca858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md#insn-00aca858) · [`00aca884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00aca83c.md#insn-00aca884)
- 新版 `00acaa9c`（命令位置の公開資料なし） · `00acaa54`（命令位置の公開資料なし） · `00acaa80`（命令位置の公開資料なし）

~~~diff
- 00aca8a0 ["INT_ADD", "register:40f0:8", ["const:aca8a0:8", "const:4:8"]]
- 00aca8a0 ["CALL", null, ["ram:46c984:8"]]
+ 00acaa9c ["INT_ADD", "register:40f0:8", ["const:acaa9c:8", "const:4:8"]]
+ 00acaa9c ["CALL", null, ["ram:46c9c4:8"]]
- 00aca8a0 bytes 3988e697
+ 00acaa9c bytes ca87e697
- 00aca858 ["INT_ADD", "register:40f0:8", ["const:aca858:8", "const:4:8"]]
- 00aca858 ["CALL", null, ["callee:00467860:8"]]
+ 00acaa54 ["INT_ADD", "register:40f0:8", ["const:acaa54:8", "const:4:8"]]
+ 00acaa54 ["CALL", null, ["callee:00467860:8"]]
- 00aca858 bytes f273e697
+ 00acaa54 bytes 8373e697
- 00aca884 ["INT_ADD", "register:40f0:8", ["const:aca884:8", "const:4:8"]]
- 00aca884 ["CALL", null, ["callee:00467b2c:8"]]
+ 00acaa80 ["INT_ADD", "register:40f0:8", ["const:acaa80:8", "const:4:8"]]
+ 00acaa80 ["CALL", null, ["callee:00467b2c:8"]]
- 00aca884 bytes 9a74e697
+ 00acaa80 bytes 2b74e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ecb283157bd416854cb24e8aa3e30e5"></a>

### [`00acabb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md) → [`00acadac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acadac.md) FUN_00acadac

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 19件 [`00680dc8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00680/00680dc8.md) [`006b53c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b5/006b53c4.md) [`0073edf4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0073e/0073edf4.md) [`00773854`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00773/00773854.md) [`00789da0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00789/00789da0.md) · 呼出先 5件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00469bc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00469/00469bc4.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md)
- 新版 呼出元 19件 [`00680e08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00680/00680e08.md) [`006b5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b5/006b5404.md) [`0073ee34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0073e/0073ee34.md) [`00773894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00773/00773894.md) [`00789de0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00789/00789de0.md) · 呼出先 5件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00469c04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00469/00469c04.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

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
      "site": "00acae20",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acac24",
      "value": [
        "leaf",
        "ram:46c984:8"
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
      "site": "00acae90",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acac94",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acaee4",
      "value": [
        "leaf",
        "ram:46c9c4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acace8",
      "value": [
        "leaf",
        "ram:46c984:8"
      ]
    },
    "ordinal": 14,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00acae20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00acae90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ],
    [
      "00acaee4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c984"
      ]
    ]
  ],
  "added": [
    [
      "00acae20",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00acae90",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ],
    [
      "00acaee4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0046c9c4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acac24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md#insn-00acac24) · [`00acac94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md#insn-00acac94) · [`00acace8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acabb0.md#insn-00acace8)
- 新版 `00acae20`（命令位置の公開資料なし） · `00acae90`（命令位置の公開資料なし） · `00acaee4`（命令位置の公開資料なし）

~~~diff
- 00acac24 ["INT_ADD", "register:40f0:8", ["const:acac24:8", "const:4:8"]]
- 00acac24 ["CALL", null, ["ram:46c984:8"]]
+ 00acae20 ["INT_ADD", "register:40f0:8", ["const:acae20:8", "const:4:8"]]
+ 00acae20 ["CALL", null, ["ram:46c9c4:8"]]
- 00acac24 bytes 5887e697
+ 00acae20 bytes e986e697
- 00acac94 ["INT_ADD", "register:40f0:8", ["const:acac94:8", "const:4:8"]]
- 00acac94 ["CALL", null, ["ram:46c984:8"]]
+ 00acae90 ["INT_ADD", "register:40f0:8", ["const:acae90:8", "const:4:8"]]
+ 00acae90 ["CALL", null, ["ram:46c9c4:8"]]
- 00acac94 bytes 3c87e697
+ 00acae90 bytes cd86e697
- 00acace8 ["INT_ADD", "register:40f0:8", ["const:acace8:8", "const:4:8"]]
- 00acace8 ["CALL", null, ["ram:46c984:8"]]
+ 00acaee4 ["INT_ADD", "register:40f0:8", ["const:acaee4:8", "const:4:8"]]
+ 00acaee4 ["CALL", null, ["ram:46c9c4:8"]]
- 00acace8 bytes 2787e697
+ 00acaee4 bytes b886e697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f79acca8a80d0439173aa12903efffa3"></a>

### [`00acafd8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acafd8.md) → [`00acb1d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb1d4.md) FUN_00acb1d4

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00acb1e8",
      "incomplete_value": false,
      "site": "00acb1ec",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acafec",
      "incomplete_value": false,
      "site": "00acaff0",
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
      "00acb1ec",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb1ec",
      "DATA",
      [
        "storage",
        "00c8d740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acafe4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acafd8.md#insn-00acafe4) · [`00acafec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acafd8.md#insn-00acafec)
- 新版 `00acb1e0`（命令位置の公開資料なし） · `00acb1e8`（命令位置の公開資料なし）

~~~diff
- 00acafe4 ["INT_ADD", "register:40f0:8", ["const:acafe4:8", "const:4:8"]]
- 00acafe4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00acb1e0 ["INT_ADD", "register:40f0:8", ["const:acb1e0:8", "const:4:8"]]
+ 00acb1e0 ["CALL", null, ["callee:00c57e90:8"]]
- 00acafe4 bytes ab320694
+ 00acb1e0 bytes 2c330694
- 00acafec ["COPY", "tmp:0:8", ["const:340:8"]]
- 00acafec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acafec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acafec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb1e8 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00acb1e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb1e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb1e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acafec bytes 08010d91
+ 00acb1e8 bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ada90a2428ad50eb48eb00dfa6635fd8"></a>

### [`00acaffc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaffc.md) → [`00acb1f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb1f8.md) FUN_00acb1f8

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acb1fc",
      "incomplete_value": false,
      "site": "00acb200",
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
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb000",
      "incomplete_value": false,
      "site": "00acb004",
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
      "00acb200",
      "DATA",
      [
        "storage",
        "00c8d340",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb200",
      "DATA",
      [
        "storage",
        "00c8d740",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb000`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acaffc.md#insn-00acb000)
- 新版 `00acb1fc`（命令位置の公開資料なし）

~~~diff
- 00acb000 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00acb000 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb000 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb000 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb1fc ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00acb1fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb1fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb1fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb000 bytes 08010d91
+ 00acb1fc bytes 08011d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aac9b3a4c0ff36941bf30e54769be176"></a>

### [`00acb1b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1b0.md) → [`00acb3ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb3ac.md) FUN_00acb3ac

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00acb3c0",
      "incomplete_value": false,
      "site": "00acb3c4",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb1c4",
      "incomplete_value": false,
      "site": "00acb1c8",
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
            "const:3c0:8"
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
      "00acb3c4",
      "DATA",
      [
        "storage",
        "00c8d3c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb3c4",
      "DATA",
      [
        "storage",
        "00c8d7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb1bc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1b0.md#insn-00acb1bc) · [`00acb1c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1b0.md#insn-00acb1c4)
- 新版 `00acb3b8`（命令位置の公開資料なし） · `00acb3c0`（命令位置の公開資料なし）

~~~diff
- 00acb1bc ["INT_ADD", "register:40f0:8", ["const:acb1bc:8", "const:4:8"]]
- 00acb1bc ["CALL", null, ["callee:00c57e90:8"]]
+ 00acb3b8 ["INT_ADD", "register:40f0:8", ["const:acb3b8:8", "const:4:8"]]
+ 00acb3b8 ["CALL", null, ["callee:00c57e90:8"]]
- 00acb1bc bytes 35320694
+ 00acb3b8 bytes b6320694
- 00acb1c4 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00acb1c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb1c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb1c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb3c0 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00acb3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb1c4 bytes 08010f91
+ 00acb3c0 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-476b3e7e64cfb91738e5d8b64751e0ce"></a>

### [`00acb1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1d4.md) → [`00acb3d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb3d0.md) FUN_00acb3d0

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acb3d4",
      "incomplete_value": false,
      "site": "00acb3d8",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb1d8",
      "incomplete_value": false,
      "site": "00acb1dc",
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
            "const:3c0:8"
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
      "00acb3d8",
      "DATA",
      [
        "storage",
        "00c8d3c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb3d8",
      "DATA",
      [
        "storage",
        "00c8d7c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb1d8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1d4.md#insn-00acb1d8)
- 新版 `00acb3d4`（命令位置の公開資料なし）

~~~diff
- 00acb1d8 ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00acb1d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb1d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb1d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb3d4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 00acb3d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb3d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb3d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb1d8 bytes 08010f91
+ 00acb3d4 bytes 08011f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96cd8c7cc7c5e110499649a5fc456d6d"></a>

### [`00acb1ec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md) → [`00acb3e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb3e8.md) FUN_00acb3e8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00459d34`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00459/00459d34.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00459d74`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/00459d74.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

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
      "site": "00acb488",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb28c",
      "value": [
        "leaf",
        "ram:47acb4:8"
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb494",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb298",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00acb488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00acb494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00acb488",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00acb494",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb28c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md#insn-00acb28c) · [`00acb298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md#insn-00acb298) · [`00acb204`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb1ec.md#insn-00acb204)
- 新版 `00acb488`（命令位置の公開資料なし） · `00acb494`（命令位置の公開資料なし） · `00acb400`（命令位置の公開資料なし）

~~~diff
- 00acb28c ["INT_ADD", "register:40f0:8", ["const:acb28c:8", "const:4:8"]]
- 00acb28c ["CALL", null, ["ram:47acb4:8"]]
+ 00acb488 ["INT_ADD", "register:40f0:8", ["const:acb488:8", "const:4:8"]]
+ 00acb488 ["CALL", null, ["ram:47acf4:8"]]
- 00acb28c bytes 8abee697
+ 00acb488 bytes 1bbee697
- 00acb298 ["INT_ADD", "register:40f0:8", ["const:acb298:8", "const:4:8"]]
- 00acb298 ["CALL", null, ["ram:47acb4:8"]]
+ 00acb494 ["INT_ADD", "register:40f0:8", ["const:acb494:8", "const:4:8"]]
+ 00acb494 ["CALL", null, ["ram:47acf4:8"]]
- 00acb298 bytes 87bee697
+ 00acb494 bytes 18bee697
- 00acb204 ["INT_ADD", "register:40f0:8", ["const:acb204:8", "const:4:8"]]
- 00acb204 ["CALL", null, ["callee:008b6ea4:8"]]
+ 00acb400 ["INT_ADD", "register:40f0:8", ["const:acb400:8", "const:4:8"]]
+ 00acb400 ["CALL", null, ["callee:008b6ea4:8"]]
- 00acb204 bytes 17aff797
+ 00acb400 bytes a9aef797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-035768e68ab5df2209f1fc3cfee99c3b"></a>

### [`00acb314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb314.md) → [`00acb510`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb510.md) FUN_00acb510

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00acb524",
      "incomplete_value": false,
      "site": "00acb528",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb328",
      "incomplete_value": false,
      "site": "00acb32c",
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
            "const:440:8"
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
      "00acb528",
      "DATA",
      [
        "storage",
        "00c8d440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb528",
      "DATA",
      [
        "storage",
        "00c8d840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb314.md#insn-00acb320) · [`00acb328`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb314.md#insn-00acb328)
- 新版 `00acb51c`（命令位置の公開資料なし） · `00acb524`（命令位置の公開資料なし）

~~~diff
- 00acb320 ["INT_ADD", "register:40f0:8", ["const:acb320:8", "const:4:8"]]
- 00acb320 ["CALL", null, ["callee:00c57e90:8"]]
+ 00acb51c ["INT_ADD", "register:40f0:8", ["const:acb51c:8", "const:4:8"]]
+ 00acb51c ["CALL", null, ["callee:00c57e90:8"]]
- 00acb320 bytes dc310694
+ 00acb51c bytes 5d320694
- 00acb328 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00acb328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb524 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00acb524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb328 bytes 08011191
+ 00acb524 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08814353465c34d1b4112568266f9d7d"></a>

### [`00acb338`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb338.md) → [`00acb534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb534.md) FUN_00acb534

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00acb538",
      "incomplete_value": false,
      "site": "00acb53c",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb33c",
      "incomplete_value": false,
      "site": "00acb340",
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
            "const:440:8"
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
      "00acb53c",
      "DATA",
      [
        "storage",
        "00c8d440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acb53c",
      "DATA",
      [
        "storage",
        "00c8d840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb33c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb338.md#insn-00acb33c)
- 新版 `00acb538`（命令位置の公開資料なし）

~~~diff
- 00acb33c ["COPY", "tmp:0:8", ["const:440:8"]]
- 00acb33c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb33c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb33c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acb538 ["COPY", "tmp:0:8", ["const:840:8"]]
+ 00acb538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acb538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb33c bytes 08011191
+ 00acb538 bytes 08012191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96671db09668bf305195c99e5b4ee3b2"></a>

### [`00acb350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md) → [`00acb54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb54c.md) FUN_00acb54c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047d17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047d/0047d17c.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`00b3ba6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3b/00b3ba6c.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047d1bc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047d/0047d1bc.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`00b3be94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b3b/00b3be94.md)

変更の種類 call, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb570",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb374",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00acb57c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb380",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "site": "00acb66c",
      "value": [
        "leaf",
        "ram:47acf4:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "00acb470",
      "value": [
        "leaf",
        "ram:47acb4:8"
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
      "00acb570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00acb57c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00acb66c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ]
  ],
  "added": [
    [
      "00acb570",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00acb57c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00acb66c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md#insn-00acb374) · [`00acb380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md#insn-00acb380) · [`00acb470`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb350.md#insn-00acb470)
- 新版 `00acb570`（命令位置の公開資料なし） · `00acb57c`（命令位置の公開資料なし） · `00acb66c`（命令位置の公開資料なし）

~~~diff
- 00acb374 ["INT_ADD", "register:40f0:8", ["const:acb374:8", "const:4:8"]]
- 00acb374 ["CALL", null, ["ram:47acb4:8"]]
+ 00acb570 ["INT_ADD", "register:40f0:8", ["const:acb570:8", "const:4:8"]]
+ 00acb570 ["CALL", null, ["ram:47acf4:8"]]
- 00acb374 bytes 50bee697
+ 00acb570 bytes e1bde697
- 00acb380 ["INT_ADD", "register:40f0:8", ["const:acb380:8", "const:4:8"]]
- 00acb380 ["CALL", null, ["ram:47acb4:8"]]
+ 00acb57c ["INT_ADD", "register:40f0:8", ["const:acb57c:8", "const:4:8"]]
+ 00acb57c ["CALL", null, ["ram:47acf4:8"]]
- 00acb380 bytes 4dbee697
+ 00acb57c bytes debde697
- 00acb470 ["INT_ADD", "register:40f0:8", ["const:acb470:8", "const:4:8"]]
- 00acb470 ["CALL", null, ["ram:47acb4:8"]]
+ 00acb66c ["INT_ADD", "register:40f0:8", ["const:acb66c:8", "const:4:8"]]
+ 00acb66c ["CALL", null, ["ram:47acf4:8"]]
- 00acb470 bytes 11bee697
+ 00acb66c bytes a2bde697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f730f4befa657c3444331bd8b266bb74"></a>

### [`00acb4cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4cc.md) → [`00acb6c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb6c8.md) _INIT_246

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

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
      "definition_site": "00acb704",
      "incomplete_value": true,
      "site": "00acb720",
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
                "const:f26:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb508",
      "incomplete_value": true,
      "site": "00acb524",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acb728",
      "incomplete_value": true,
      "site": "00acb744",
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
                "const:f39:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb52c",
      "incomplete_value": true,
      "site": "00acb548",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acb748",
      "incomplete_value": true,
      "site": "00acb764",
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
                "const:dc2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb54c",
      "incomplete_value": true,
      "site": "00acb568",
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
      "00acb704",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "00acb728",
      "READ",
      [
        "storage",
        "002b7ef9",
        null,
        "string"
      ]
    ],
    [
      "00acb748",
      "READ",
      [
        "storage",
        "002b8d82",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acb704",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00acb728",
      "READ",
      [
        "storage",
        "002b7f39",
        null,
        "string"
      ]
    ],
    [
      "00acb748",
      "READ",
      [
        "storage",
        "002b8dc2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb504`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4cc.md#insn-00acb504) · [`00acb62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4cc.md#insn-00acb62c) · [`00acb700`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb4cc.md#insn-00acb700)
- 新版 `00acb700`（命令位置の公開資料なし） · `00acb828`（命令位置の公開資料なし） · `00acb8fc`（命令位置の公開資料なし）

~~~diff
- 00acb504 ["COPY", "tmp:0:8", ["const:ee6:8"]]
- 00acb504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00acb504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00acb504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00acb700 ["COPY", "tmp:0:8", ["const:f26:8"]]
+ 00acb700 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00acb700 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00acb700 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00acb504 bytes 29993b91
+ 00acb700 bytes 29993c91
- 00acb62c ["INT_ADD", "register:40f0:8", ["const:acb62c:8", "const:4:8"]]
- 00acb62c ["CALL", null, ["callee:0043b7f8:8"]]
+ 00acb828 ["INT_ADD", "register:40f0:8", ["const:acb828:8", "const:4:8"]]
+ 00acb828 ["CALL", null, ["callee:0043b7f8:8"]]
- 00acb62c bytes 63c0e597
+ 00acb828 bytes f4bfe597
- 00acb700 ["INT_ADD", "register:40f0:8", ["const:acb700:8", "const:4:8"]]
- 00acb700 ["CALL", null, ["callee:00c57e30:8"]]
+ 00acb8fc ["INT_ADD", "register:40f0:8", ["const:acb8fc:8", "const:4:8"]]
+ 00acb8fc ["CALL", null, ["callee:00c57e30:8"]]
- 00acb700 bytes cc300694
+ 00acb8fc bytes 4d310694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-893c5dd1222f7f60b0034a68b00d6a76"></a>

### [`00acb85c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb85c.md) → [`00acba58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba58.md) FUN_00acba58

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00731e84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731e84.md) [`00935400`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935400.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00731ec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731ec4.md) [`0093559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/0093559c.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00acba60",
      "incomplete_value": false,
      "site": "00acba64",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb864",
      "incomplete_value": false,
      "site": "00acb868",
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
            "const:4c0:8"
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
      "00acba64",
      "DATA",
      [
        "storage",
        "00c8d4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acba64",
      "DATA",
      [
        "storage",
        "00c8d8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb85c.md#insn-00acb864)
- 新版 `00acba60`（命令位置の公開資料なし）

~~~diff
- 00acb864 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00acb864 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb864 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb864 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acba60 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00acba60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acba60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acba60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb864 bytes 08011391
+ 00acba60 bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30feda0a8760ff63f6ac29bd47d16662"></a>

### [`00acb88c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md) → [`00acba88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acba88.md) FUN_00acba88

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`00731f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731f2c.md) [`00731f88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00731/00731f88.md) [`009357b4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/009357b4.md) [`00935840`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935840.md) [`00acbe1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe1c.md) · 呼出先 3件 [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 6件 [`00731f6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731f6c.md) [`00731fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00731/00731fc8.md) [`00935950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/00935950.md) [`009359dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009359dc.md) [`00acc018`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc018.md) · 呼出先 3件 [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00acbaa4",
      "incomplete_value": false,
      "site": "00acbaa8",
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
            "const:8c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acb8a8",
      "incomplete_value": false,
      "site": "00acb8ac",
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
            "const:4c0:8"
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
      "00acbaa8",
      "DATA",
      [
        "storage",
        "00c8d4c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acbaa8",
      "DATA",
      [
        "storage",
        "00c8d8c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acb8a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md#insn-00acb8a8) · [`00acb8e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md#insn-00acb8e4) · [`00acb8f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acb88c.md#insn-00acb8f8)
- 新版 `00acbaa4`（命令位置の公開資料なし） · `00acbae0`（命令位置の公開資料なし） · `00acbaf4`（命令位置の公開資料なし）

~~~diff
- 00acb8a8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00acb8a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acb8a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acb8a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acbaa4 ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 00acbaa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acbaa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acbaa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acb8a8 bytes 08011391
+ 00acbaa4 bytes 08012391
- 00acb8e4 ["INT_ADD", "register:40f0:8", ["const:acb8e4:8", "const:4:8"]]
- 00acb8e4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00acbae0 ["INT_ADD", "register:40f0:8", ["const:acbae0:8", "const:4:8"]]
+ 00acbae0 ["CALL", null, ["callee:00c53d00:8"]]
- 00acb8e4 bytes ff1f0694
+ 00acbae0 bytes 88200694
- 00acb8f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00acb8f8 ["INT_ADD", "register:40f0:8", ["const:acb8f8:8", "const:4:8"]]
- 00acb8f8 ["CALLIND", null, ["register:0:8"]]
+ 00acbaf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00acbaf4 ["INT_ADD", "register:40f0:8", ["const:acbaf4:8", "const:4:8"]]
+ 00acbaf4 ["CALLIND", null, ["register:0:8"]]
- 00acb8f8 bytes 00013fd6
+ 00acbaf4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1f11c90456b7eec9ccab322eb16ffc3"></a>

### [`00acbb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md) → [`00acbd4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbd4c.md) FUN_00acbd4c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00935514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00935/00935514.md) · 呼出先 7件 [`00acbe7c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbe7c.md) [`00acbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbed4.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`009356b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00935/009356b0.md) · 呼出先 7件 [`00acc078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc078.md) [`00acc0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc0d0.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00acbd94",
      "incomplete_value": false,
      "site": "00acbd9c",
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
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acbb98",
      "incomplete_value": false,
      "site": "00acbba0",
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
            "const:4f0:8"
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
      "00acbd9c",
      "DATA",
      [
        "storage",
        "00c8d4f0",
        null,
        "pointer"
      ]
    ],
    [
      "00acbe00",
      "READ",
      [
        "storage",
        "00c8d500",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00acbd9c",
      "DATA",
      [
        "storage",
        "00c8d8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00acbe00",
      "READ",
      [
        "storage",
        "00c8d900",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acbb8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md#insn-00acbb8c) · [`00acbb98`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md#insn-00acbb98) · [`00acbb9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbb50.md#insn-00acbb9c)
- 新版 `00acbd88`（命令位置の公開資料なし） · `00acbd94`（命令位置の公開資料なし）

~~~diff
- 00acbb8c ["INT_ADD", "register:40f0:8", ["const:acbb8c:8", "const:4:8"]]
- 00acbb8c ["CALL", null, ["callee:00c57e90:8"]]
+ 00acbd88 ["INT_ADD", "register:40f0:8", ["const:acbd88:8", "const:4:8"]]
+ 00acbd88 ["CALL", null, ["callee:00c57e90:8"]]
- 00acbb8c bytes c12f0694
+ 00acbd88 bytes 42300694
- 00acbb98 ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 00acbb98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00acbb98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00acbb98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00acbd94 ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00acbd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00acbd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00acbd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00acbb98 bytes 08c11391
+ 00acbd94 bytes 08c12391
- 00acbb9c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00acbb9c bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-453f3fd9fc95ea70a9dec8aaf2007d75"></a>

### [`00acc030`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc030.md) → [`00acc22c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc22c.md) FUN_00acc22c

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00acbed4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbed4.md) · 呼出先 1件 [`0043b738`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b738.md)
- 新版 呼出元 1件 [`00acc0d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc0d0.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)

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
      "definition_site": "00acc238",
      "incomplete_value": false,
      "site": "00acc23c",
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
            "const:f4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acc03c",
      "incomplete_value": false,
      "site": "00acc040",
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
      "00acc238",
      "PARAM",
      [
        "storage",
        "002b7f0c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acc238",
      "PARAM",
      [
        "storage",
        "002b7f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acc040`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc030.md#insn-00acc040) · [`00acc03c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc030.md#insn-00acc03c)
- 新版 `00acc23c`（命令位置の公開資料なし） · `00acc238`（命令位置の公開資料なし）

~~~diff
- 00acc040 ["INT_ADD", "register:40f0:8", ["const:acc040:8", "const:4:8"]]
- 00acc040 ["CALL", null, ["callee:0043b778:8"]]
+ 00acc23c ["INT_ADD", "register:40f0:8", ["const:acc23c:8", "const:4:8"]]
+ 00acc23c ["CALL", null, ["callee:0043b778:8"]]
- 00acc040 bytes bebde597
+ 00acc23c bytes 4fbde597
- 00acc03c ["COPY", "tmp:0:8", ["const:f0c:8"]]
- 00acc03c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00acc03c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00acc03c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00acc238 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00acc238 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00acc238 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00acc238 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00acc03c bytes 00303c91
+ 00acc238 bytes 00303d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6abc41bd125cd780e14fbaa1151030c"></a>

### [`00acc044`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc044.md) → [`00acc240`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc240.md) _INIT_247

採用 · 移動量 `+0x1fc` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0043ae30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043a/0043ae30.md) [`0043b7b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043b7b8.md) [`00c57a30`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a30.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0043ae70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043a/0043ae70.md) [`0043b7f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b7f8.md) [`00c57e30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e30.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.45% / 新版 73.45%

CFGの説明率　旧版 51.52% / 新版 51.52%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_store_alignment` 18件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc074"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc088"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acc08c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acc074",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acc080",
      "READ",
      [
        "storage",
        "002b7ee6",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00acc088",
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
      "00acc270",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00acc27c",
      "READ",
      [
        "storage",
        "002b7f26",
        null,
        "string"
      ]
    ],
    [
      "00acc284",
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

- 旧版 [`00acc074`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc044.md#insn-00acc074) · [`00acc088`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc044.md#insn-00acc088) · [`00acc08c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc044.md#insn-00acc08c)

~~~diff
- 00acc074 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00acc074 ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00acc074 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00acc074 bytes a9831ff8
- 00acc088 ["COPY", "tmp:0:4", ["register:4050:4"]]
- 00acc088 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:21:8"]]
- 00acc088 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00acc088 bytes ea130278
- 00acc08c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:28:8"]]
- 00acc08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00acc08c bytes e92b00b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4010e9ef0e8a51fc8eab22229cb8b9ec"></a>

### [`00ace960`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md) → [`00aceb5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00aceb5c.md) FUN_00aceb5c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 16件 [`005e1264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`005e1710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md) [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) · 呼出先 11件 [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) [`007bbd08`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007bb/007bbd08.md) [`008001ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00800/008001ac.md) [`00802678`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802678.md) [`00802b18`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00802/00802b18.md)
- 新版 呼出元 16件 [`005e12a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e12a4.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`005e1750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1750.md) [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) · 呼出先 11件 [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`007bbd48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007bb/007bbd48.md) [`008001ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00800/008001ec.md) [`008026b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/008026b8.md) [`00802b58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00802/00802b58.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 81.25% / 新版 76.47%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00acec08",
      "incomplete_value": true,
      "site": "00acec0c",
      "value": [
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
      ]
    },
    "old": {
      "definition_site": "00acea0c",
      "incomplete_value": true,
      "site": "00acea10",
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
            "const:13d8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00acea10`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md#insn-00acea10) · [`00ace978`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md#insn-00ace978) · [`00ace980`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md#insn-00ace980)
- 新版 `00acec0c`（命令位置の公開資料なし） · `00aceb74`（命令位置の公開資料なし） · `00aceb7c`（命令位置の公開資料なし）

~~~diff
- 00acea10 ["INT_ADD", "register:40f0:8", ["const:acea10:8", "const:4:8"]]
- 00acea10 ["CALL", null, ["callee:0067674c:8"]]
+ 00acec0c ["INT_ADD", "register:40f0:8", ["const:acec0c:8", "const:4:8"]]
+ 00acec0c ["CALL", null, ["callee:0067674c:8"]]
- 00acea10 bytes 3f9fee97
+ 00acec0c bytes d09eee97
- 00ace978 ["INT_ADD", "register:40f0:8", ["const:ace978:8", "const:4:8"]]
- 00ace978 ["CALL", null, ["callee:00802b58:8"]]
+ 00aceb74 ["INT_ADD", "register:40f0:8", ["const:aceb74:8", "const:4:8"]]
+ 00aceb74 ["CALL", null, ["callee:00802b58:8"]]
- 00ace978 bytes 68d0f497
+ 00aceb74 bytes f9cff497
- 00ace980 ["INT_ADD", "register:40f0:8", ["const:ace980:8", "const:4:8"]]
- 00ace980 ["CALL", null, ["callee:00802ca8:8"]]
+ 00aceb7c ["INT_ADD", "register:40f0:8", ["const:aceb7c:8", "const:4:8"]]
+ 00aceb7c ["CALL", null, ["callee:00802ca8:8"]]
- 00ace980 bytes bad0f497
+ 00aceb7c bytes 4bd0f497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9878d0d2c1bbbfbf78df24310ad14866"></a>

### [`00acec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md) → [`00acee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acee20.md) FUN_00acee20

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`005e1264`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1264.md) [`005e15e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e15e0.md) [`005e1710`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005e1/005e1710.md) [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) [`007fe0c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fe/007fe0c0.md) · 呼出先 8件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00acea58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md) [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 11件 [`005e12a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e12a4.md) [`005e1620`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1620.md) [`005e1750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005e1/005e1750.md) [`007de8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de8c0.md) [`007fe100`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fe/007fe100.md) · 呼出先 8件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00acec54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) [`00aeadf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeadf0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acee88",
      "incomplete_value": true,
      "site": "00acee90",
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
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acec8c",
      "incomplete_value": true,
      "site": "00acec94",
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
                "const:920:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00acf094",
      "incomplete_value": false,
      "site": "00acf098",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acee98",
      "incomplete_value": false,
      "site": "00acee9c",
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
      "00acee88",
      "READ",
      [
        "storage",
        "002c2920",
        null,
        null
      ]
    ],
    [
      "00acf094",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acee88",
      "READ",
      [
        "storage",
        "002c2960",
        null,
        null
      ]
    ],
    [
      "00acf094",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acee9c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md#insn-00acee9c) · [`00acec5c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md#insn-00acec5c) · [`00acec8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md#insn-00acec8c)
- 新版 `00acf098`（命令位置の公開資料なし） · `00acee58`（命令位置の公開資料なし） · `00acee88`（命令位置の公開資料なし）

~~~diff
- 00acee9c ["INT_ADD", "register:40f0:8", ["const:acee9c:8", "const:4:8"]]
- 00acee9c ["CALL", null, ["callee:00442930:8"]]
+ 00acf098 ["INT_ADD", "register:40f0:8", ["const:acf098:8", "const:4:8"]]
+ 00acf098 ["CALL", null, ["callee:00442930:8"]]
- 00acee9c bytes 95cee597
+ 00acf098 bytes 26cee597
- 00acec5c ["INT_ADD", "register:40f0:8", ["const:acec5c:8", "const:4:8"]]
- 00acec5c ["CALL", null, ["callee:00acec54:8"]]
+ 00acee58 ["INT_ADD", "register:40f0:8", ["const:acee58:8", "const:4:8"]]
+ 00acee58 ["CALL", null, ["callee:00acec54:8"]]
- 00acec5c bytes 7fffff97
+ 00acee58 bytes 7fffff97
- 00acec8c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:920:8"]]
- 00acec8c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00acec8c ["COPY", "register:5030:8", ["const:0:8"]]
- 00acec8c ["COPY", "register:5038:8", ["const:0:8"]]
+ 00acee88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
+ 00acee88 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00acee88 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00acee88 ["COPY", "register:5038:8", ["const:0:8"]]
- 00acec8c bytes 0149c23d
+ 00acee88 bytes 0159c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f19bf68541bfe83f2d724b68974ba4ab"></a>

### [`00acefbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acefbc.md) → [`00acf1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acf1b8.md) FUN_00acf1b8

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md) [`006624f4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006624f4.md) [`007de880`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007de/007de880.md) [`00acc3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc3d4.md) · 呼出先 8件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00acea58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md) [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 6件 [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md) [`00662534`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662534.md) [`007de8c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007de/007de8c0.md) [`00acc5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc5d0.md) · 呼出先 8件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00acec54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) [`00aeadf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeadf0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00acf218",
      "incomplete_value": true,
      "site": "00acf220",
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
                "const:960:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf01c",
      "incomplete_value": true,
      "site": "00acf024",
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
                "const:920:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00acf3d4",
      "incomplete_value": false,
      "site": "00acf3d8",
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
            "const:1bd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf1d8",
      "incomplete_value": false,
      "site": "00acf1dc",
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
      "00acf218",
      "READ",
      [
        "storage",
        "002c2920",
        null,
        null
      ]
    ],
    [
      "00acf3d4",
      "PARAM",
      [
        "storage",
        "002a00f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00acf218",
      "READ",
      [
        "storage",
        "002c2960",
        null,
        null
      ]
    ],
    [
      "00acf3d4",
      "PARAM",
      [
        "storage",
        "002a01bd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf1dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acefbc.md#insn-00acf1dc) · [`00aceff0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acefbc.md#insn-00aceff0) · [`00acf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acefbc.md#insn-00acf01c)
- 新版 `00acf3d8`（命令位置の公開資料なし） · `00acf1ec`（命令位置の公開資料なし） · `00acf218`（命令位置の公開資料なし）

~~~diff
- 00acf1dc ["INT_ADD", "register:40f0:8", ["const:acf1dc:8", "const:4:8"]]
- 00acf1dc ["CALL", null, ["callee:00442930:8"]]
+ 00acf3d8 ["INT_ADD", "register:40f0:8", ["const:acf3d8:8", "const:4:8"]]
+ 00acf3d8 ["CALL", null, ["callee:00442930:8"]]
- 00acf1dc bytes c5cde597
+ 00acf3d8 bytes 56cde597
- 00aceff0 ["INT_ADD", "register:40f0:8", ["const:aceff0:8", "const:4:8"]]
- 00aceff0 ["CALL", null, ["callee:00acec54:8"]]
+ 00acf1ec ["INT_ADD", "register:40f0:8", ["const:acf1ec:8", "const:4:8"]]
+ 00acf1ec ["CALL", null, ["callee:00acec54:8"]]
- 00aceff0 bytes 9afeff97
+ 00acf1ec bytes 9afeff97
- 00acf01c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:920:8"]]
- 00acf01c ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
- 00acf01c ["COPY", "register:5030:8", ["const:0:8"]]
- 00acf01c ["COPY", "register:5038:8", ["const:0:8"]]
+ 00acf218 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:960:8"]]
+ 00acf218 ["LOAD", "register:5020:16", ["const:1b1:8", "tmp:0:8"]]
+ 00acf218 ["COPY", "register:5030:8", ["const:0:8"]]
+ 00acf218 ["COPY", "register:5038:8", ["const:0:8"]]
- 00acf01c bytes 0149c23d
+ 00acf218 bytes 0159c23d
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf4ae69f53280d9f2a6e3419c33c14d"></a>

### [`00acf288`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf288.md) → [`00acf484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acf484.md) FUN_00acf484

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 3件 [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 3件 [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 30.00% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00acf4e0",
      "incomplete_value": true,
      "site": "00acf4f0",
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


#### 変更候補の命令位置

- 旧版 [`00acf2ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf288.md#insn-00acf2ac) · [`00acf2b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf288.md#insn-00acf2b8) · [`00acf2c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf288.md#insn-00acf2c4)
- 新版 `00acf4a8`（命令位置の公開資料なし） · `00acf4b4`（命令位置の公開資料なし） · `00acf4c0`（命令位置の公開資料なし）

~~~diff
- 00acf2ac ["INT_ADD", "register:40f0:8", ["const:acf2ac:8", "const:4:8"]]
- 00acf2ac ["CALL", null, ["callee:00c53cd0:8"]]
+ 00acf4a8 ["INT_ADD", "register:40f0:8", ["const:acf4a8:8", "const:4:8"]]
+ 00acf4a8 ["CALL", null, ["callee:00c53cd0:8"]]
- 00acf2ac bytes 81110694
+ 00acf4a8 bytes 0a120694
- 00acf2b8 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
- 00acf2b8 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00acf4b4 ["INT_EQUAL", "tmp:0:1", ["register:40a0:8", "const:0:8"]]
+ 00acf4b4 ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
- 00acf2b8 bytes 740100b4
+ 00acf4b4 bytes 740100b4
- 00acf2c4 ["INT_ADD", "register:40f0:8", ["const:acf2c4:8", "const:4:8"]]
- 00acf2c4 ["CALL", null, ["callee:00c53d00:8"]]
+ 00acf4c0 ["INT_ADD", "register:40f0:8", ["const:acf4c0:8", "const:4:8"]]
+ 00acf4c0 ["CALL", null, ["callee:00c53d00:8"]]
- 00acf2c4 bytes 87110694
+ 00acf4c0 bytes 10120694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-900a7708b3c5101328fc466ac36b654a"></a>

### [`00acf2f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf2f8.md) → [`00acf4f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acf4f4.md) FUN_00acf4f4

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`0089b248`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0089b/0089b248.md) [`00acc3d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acc/00acc3d4.md) [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) · 呼出先 11件 [`004428f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00442/004428f0.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md) [`00936428`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00936/00936428.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 3件 [`0089b28c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0089b/0089b28c.md) [`00acc5d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acc/00acc5d0.md) [`00ae0c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0c3c.md) · 呼出先 11件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md) [`009365c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00936/009365c4.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 75.46% / 新版 75.46%

CFGの説明率　旧版 1.25% / 新版 1.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_branch_alignment` 3件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf308"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acf31c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00acf308",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acf31c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00acf320",
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
      "00acf504",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00acf518",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00acf51c",
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

- 旧版 [`00acf308`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf2f8.md#insn-00acf308) · [`00acf31c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf2f8.md#insn-00acf31c) · [`00acf320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf2f8.md#insn-00acf320)

~~~diff
- 00acf308 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00acf308 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00acf308 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00acf308 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00acf308 bytes f44f0ba9
- 00acf31c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00acf31c ["INT_ADD", "tmp:1:8", ["register:40e8:8", "const:fffffffffffffff8:8"]]
- 00acf31c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00acf31c bytes a8831ff8
- 00acf320 ["COPY", "tmp:0:8", ["const:0:8"]]
- 00acf320 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00acf320 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00acf320 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 00acf320 bytes bf7f3ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ab56b482a4c2517c25dc60c1236cb1f"></a>

### [`00acf828`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf828.md) → [`00acfa24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acfa24.md) FUN_00acfa24

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 6件 [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`009a2998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 6件 [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`009a2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2b34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00acfa60",
      "incomplete_value": false,
      "site": "00acfa78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acf864",
      "incomplete_value": false,
      "site": "00acf87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "00acfa60",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00acfa60",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acf87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf828.md#insn-00acf87c) · [`00acf864`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf828.md#insn-00acf864) · [`00acf894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf828.md#insn-00acf894)
- 新版 `00acfa78`（命令位置の公開資料なし） · `00acfa60`（命令位置の公開資料なし） · `00acfa90`（命令位置の公開資料なし）

~~~diff
- 00acf87c ["INT_ADD", "register:40f0:8", ["const:acf87c:8", "const:4:8"]]
- 00acf87c ["CALL", null, ["callee:00695bac:8"]]
+ 00acfa78 ["INT_ADD", "register:40f0:8", ["const:acfa78:8", "const:4:8"]]
+ 00acfa78 ["CALL", null, ["callee:00695bac:8"]]
- 00acf87c bytes bc18ef97
+ 00acfa78 bytes 4d18ef97
- 00acf864 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 00acf864 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00acf864 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00acf864 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00acfa60 ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 00acfa60 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00acfa60 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00acfa60 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00acf864 bytes 42d41a91
+ 00acfa60 bytes 42d41b91
- 00acf894 ["INT_ADD", "register:40f0:8", ["const:acf894:8", "const:4:8"]]
- 00acf894 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00acfa90 ["INT_ADD", "register:40f0:8", ["const:acfa90:8", "const:4:8"]]
+ 00acfa90 ["CALL", null, ["callee:00c53cd0:8"]]
- 00acf894 bytes 07100694
+ 00acfa90 bytes 90100694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4e512e2f1b0497e6109259d57b0f7c2"></a>

### [`00acf9e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md) → [`00acfbe0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acfbe0.md) FUN_00acfbe0

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 6件 [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md) [`009a2998`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009a2/009a2998.md) [`00c538b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538b0.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md) [`00c57a80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a80.md)
- 新版 呼出元 1件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 6件 [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md) [`009a2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009a2/009a2b34.md) [`00c53cd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53cd0.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md) [`00c57e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e80.md)

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
      "definition_site": "00acfc1c",
      "incomplete_value": false,
      "site": "00acfc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00acfa20",
      "incomplete_value": false,
      "site": "00acfa38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c8000:8"
          ],
          [
            "leaf",
            "const:6b5:8"
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
      "00acfc1c",
      "PARAM",
      [
        "storage",
        "002c86b5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00acfc1c",
      "PARAM",
      [
        "storage",
        "002c86f5",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfa38`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md#insn-00acfa38) · [`00acfa20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md#insn-00acfa20) · [`00acfa50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acf9e4.md#insn-00acfa50)
- 新版 `00acfc34`（命令位置の公開資料なし） · `00acfc1c`（命令位置の公開資料なし） · `00acfc4c`（命令位置の公開資料なし）

~~~diff
- 00acfa38 ["INT_ADD", "register:40f0:8", ["const:acfa38:8", "const:4:8"]]
- 00acfa38 ["CALL", null, ["callee:00695bac:8"]]
+ 00acfc34 ["INT_ADD", "register:40f0:8", ["const:acfc34:8", "const:4:8"]]
+ 00acfc34 ["CALL", null, ["callee:00695bac:8"]]
- 00acfa38 bytes 4d18ef97
+ 00acfc34 bytes de17ef97
- 00acfa20 ["COPY", "tmp:0:8", ["const:6b5:8"]]
- 00acfa20 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00acfa20 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00acfa20 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00acfc1c ["COPY", "tmp:0:8", ["const:6f5:8"]]
+ 00acfc1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00acfc1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00acfc1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00acfa20 bytes 42d41a91
+ 00acfc1c bytes 42d41b91
- 00acfa50 ["INT_ADD", "register:40f0:8", ["const:acfa50:8", "const:4:8"]]
- 00acfa50 ["CALL", null, ["callee:00c53cd0:8"]]
+ 00acfc4c ["INT_ADD", "register:40f0:8", ["const:acfc4c:8", "const:4:8"]]
+ 00acfc4c ["CALL", null, ["callee:00c53cd0:8"]]
- 00acfa50 bytes 980f0694
+ 00acfc4c bytes 21100694
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313b479720196df2ccd9986ea2856999"></a>

### [`00acfac4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md) → [`00acfcc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acfcc0.md) FUN_00acfcc0

採用 · 移動量 `+0x1fc` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) · 呼出先 17件 [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00498190`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00498/00498190.md) [`006337a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00633/006337a4.md) [`00666be8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00666/00666be8.md) [`00695b6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00695/00695b6c.md)
- 新版 呼出元 3件 [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00aec960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec960.md) · 呼出先 17件 [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`004981d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00498/004981d0.md) [`006337e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00633/006337e4.md) [`00666c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00666/00666c28.md) [`00695bac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00695/00695bac.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.33% / 新版 80.33%

CFGの説明率　旧版 57.75% / 新版 57.34%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `store_condition` 1件, `unresolved_branch_alignment` 10件, `unresolved_call_alignment` 7件, `unresolved_store_alignment` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfb1c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfdec"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00acfdf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00acfd04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00acfb18"
      ]
    ],
    [
      "00acfd08",
      "READ",
      [
        "storage",
        "00ca4220",
        null,
        "undefined4"
      ]
    ],
    [
      "unmatched:00acfb1c",
      "WRITE",
      [
        "storage",
        "00ca4220",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00acfd04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00acfd14"
      ]
    ],
    [
      "00acfd08",
      "READ",
      [
        "storage",
        "00ca4620",
        null,
        "undefined4"
      ]
    ],
    [
      "00acfd18",
      "WRITE",
      [
        "storage",
        "00ca4620",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00acfb1c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md#insn-00acfb1c) · [`00acfb24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md#insn-00acfb24) · [`00acfc6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acf/00acfac4.md#insn-00acfc6c)
- 新版 `00acfe68`（命令位置の公開資料なし）

~~~diff
- 00acfb1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:220:8"]]
- 00acfb1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:4"]]
- 00acfb1c bytes 142102b9
- 00acfb24 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00acfb24 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00acfb24 bytes 200100b4
- 00acfc6c ["INT_ADD", "register:40f0:8", ["const:acfc6c:8", "const:4:8"]]
- 00acfc6c ["CALL", null, ["callee:009e0fc0:8"]]
+ 00acfe68 ["INT_ADD", "register:40f0:8", ["const:acfe68:8", "const:4:8"]]
+ 00acfe68 ["CALL", null, ["callee:009e0fc0:8"]]
- 00acfc6c bytes 6e44fc97
+ 00acfe68 bytes 5644fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec016f3d6f1493a7f395a4c1c9245d3"></a>

### [`00ad0210`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md) → [`00ad040c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad040c.md) FUN_00ad040c

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00aed9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md) [`00af1284`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af1/00af1284.md) · 呼出先 9件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md) [`008bac84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ba/008bac84.md)
- 新版 呼出元 2件 [`00aedde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aedde0.md) [`00af16ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af1/00af16ac.md) · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bacc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ba/008bacc8.md)

変更の種類 comparison, comparison_count, constant, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 82.48% / 新版 82.48%

CFGの説明率　旧版 80.00% / 新版 80.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件, `unresolved_store_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad02b8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad02c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad02c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad02b4",
      "READ",
      [
        "storage",
        "002a17f0",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00ad02b8",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad02c0",
      "WRITE",
      [
        "storage",
        "Stack[-0xb7]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ad04b0",
      "READ",
      [
        "storage",
        "002a18bd",
        null,
        "string"
      ]
    ],
    [
      "00ad04b4",
      "WRITE",
      [
        "storage",
        "Stack[-0xc0]",
        null,
        null
      ]
    ],
    [
      "00ad04bc",
      "WRITE",
      [
        "storage",
        "Stack[-0xb7]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad02b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md#insn-00ad02b8) · [`00ad02c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md#insn-00ad02c0) · [`00ad02c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad0210.md#insn-00ad02c4)

~~~diff
- 00ad02b8 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ad02b8 ["COPY", "tmp:1:8", ["register:8:8"]]
- 00ad02b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ad02b8 bytes e8030039
- 00ad02c0 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00ad02c0 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:9:8"]]
- 00ad02c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:2"]]
- 00ad02c0 bytes e8930078
- 00ad02c4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00ad02c4 ["INT_ADD", "tmp:1:8", ["register:8:8", "const:1:8"]]
- 00ad02c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:8"]]
- 00ad02c4 bytes e91300f8
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccd36383861f3920e7f2913c41b054da"></a>

### [`00ad04dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md) → [`00ad06d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad06d8.md) FUN_00ad06d8

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00aed9b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed9b8.md) · 呼出先 9件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`008514b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00851/008514b8.md) [`008b9814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b9/008b9814.md) [`008bb0a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008bb/008bb0a8.md)
- 新版 呼出元 1件 [`00aedde0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aedde0.md) · 呼出先 9件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`008514f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00851/008514f8.md) [`008b9858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b9/008b9858.md) [`008bb0ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008bb/008bb0ec.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.37% / 新版 92.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad073c",
      "incomplete_value": true,
      "site": "00ad073c",
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
                "const:e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad0540",
      "incomplete_value": true,
      "site": "00ad0540",
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
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:fce:8"
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
      "definition_site": "00ad07b0",
      "incomplete_value": true,
      "site": "00ad07c4",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:8c7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad05b4",
      "incomplete_value": true,
      "site": "00ad05c8",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:7fa:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ad0818",
      "incomplete_value": false,
      "site": "00ad0818",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ad061c",
      "incomplete_value": false,
      "site": "00ad061c",
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
            "const:5f8:8"
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
      "00ad072c",
      "READ",
      [
        "storage",
        "002adfce",
        null,
        "string"
      ]
    ],
    [
      "00ad07b0",
      "READ",
      [
        "storage",
        "002a17fa",
        null,
        "string"
      ]
    ],
    [
      "00ad0818",
      "DATA",
      [
        "storage",
        "00c8d5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ad072c",
      "READ",
      [
        "storage",
        "002ae00e",
        null,
        "string"
      ]
    ],
    [
      "00ad07b0",
      "READ",
      [
        "storage",
        "002a18c7",
        null,
        "string"
      ]
    ],
    [
      "00ad0818",
      "DATA",
      [
        "storage",
        "00c8d9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ad0514`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md#insn-00ad0514) · [`00ad0524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md#insn-00ad0524) · [`00ad0528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad04dc.md#insn-00ad0528)
- 新版 `00ad0710`（命令位置の公開資料なし） · `00ad0720`（命令位置の公開資料なし） · `00ad0724`（命令位置の公開資料なし）

~~~diff
- 00ad0514 ["INT_ADD", "register:40f0:8", ["const:ad0514:8", "const:4:8"]]
- 00ad0514 ["CALL", null, ["callee:008514f8:8"]]
+ 00ad0710 ["INT_ADD", "register:40f0:8", ["const:ad0710:8", "const:4:8"]]
+ 00ad0710 ["CALL", null, ["callee:008514f8:8"]]
- 00ad0514 bytes e903f697
+ 00ad0710 bytes 7a03f697
- 00ad0524 ["COPY", "register:4048:8", ["const:2ad000:8"]]
+ 00ad0720 ["COPY", "register:4048:8", ["const:2ae000:8"]]
- 00ad0524 bytes e9beffb0
+ 00ad0720 bytes e9beffd0
- 00ad0528 ["COPY", "tmp:0:8", ["const:fce:8"]]
- 00ad0528 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ad0528 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ad0528 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ad0724 ["COPY", "tmp:0:8", ["const:e:8"]]
+ 00ad0724 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad0724 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ad0724 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ad0528 bytes 29393f91
+ 00ad0724 bytes 29390091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-506dc86ed4e766168b039ed39113220e"></a>

### [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md) → [`00ad6a88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6a88.md) FUN_00ad6a88

採用 · 移動量 `+0x1fc` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 6件 [`00ad075c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad0/00ad075c.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) [`00aefce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md) · 呼出先 23件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md) [`006158d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00615/006158d0.md) [`0067670c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00676/0067670c.md) [`00743d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743d50.md)
- 新版 呼出元 6件 [`00ad0958`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad0/00ad0958.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00ae0c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0c3c.md) [`00aec960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec960.md) [`00af0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0108.md) · 呼出先 23件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`005c04f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c04f0.md) [`00615910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00615/00615910.md) [`0067674c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00676/0067674c.md) [`00743d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743d90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 92.46% / 新版 92.46%

CFGの説明率　旧版 14.08% / 新版 14.18%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_condition` 1件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 14件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad688c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ad6890"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ad688c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad6890",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ad6894",
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
      "00ad6a88",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ad6a8c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00ad6a90",
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

- 旧版 [`00ad688c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md#insn-00ad688c) · [`00ad6890`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md#insn-00ad6890) · [`00ad6894`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad688c.md#insn-00ad6894)

~~~diff
- 00ad688c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ad688c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ad688c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffb0:8"]]
- 00ad688c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00ad688c bytes fd7bbba9
- 00ad6890 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ad6890 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ad6890 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00ad6890 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6890 bytes fa6701a9
- 00ad6894 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ad6894 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ad6894 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00ad6894 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ad6894 bytes f85f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5d06717145da706492f977fa1d5a26f"></a>

### [`00ae0408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0408.md) → [`00ae0830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0830.md) FUN_00ae0830

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) · 呼出先 0件 
- 新版 呼出元 2件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) [`00aed778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed778.md) · 呼出先 0件 

変更の種類 branch_condition_or_target, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment

命令の説明率　旧版 99.51% / 新版 99.51%

CFGの説明率　旧版 33.33% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

アドレスに依存する影響 `unresolved_branch_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0648"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00ae0a70"
    },
    "old": null
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0648`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0408.md#insn-00ae0648) · [`00ae06cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0408.md#insn-00ae06cc)
- 新版 `00ae0a70`（命令位置の公開資料なし） · `00ae0af4`（命令位置の公開資料なし）

~~~diff
- 00ae0648 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
- 00ae0648 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
- 00ae0648 ["COPY", "tmp:2:1", ["tmp:1:1"]]
- 00ae0648 ["COPY", "tmp:3:1", ["const:0:1"]]
- 00ae0648 bytes 40d8417a
+ 00ae0a70 ["INT_NOTEQUAL", "tmp:0:1", ["register:100:1", "register:103:1"]]
+ 00ae0a70 ["BOOL_OR", "tmp:1:1", ["register:101:1", "tmp:0:1"]]
+ 00ae0a70 ["COPY", "tmp:2:1", ["tmp:1:1"]]
+ 00ae0a70 ["COPY", "tmp:3:1", ["const:0:1"]]
+ 00ae0a70 bytes 40d8417a
- 00ae06cc ["BRANCH", null, ["local:b10:8"]]
+ 00ae0af4 ["BRANCH", null, ["local:b9:8"]]
- 00ae06cc bytes 05000014
+ 00ae0af4 bytes 05000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353fdd8d93fe707172fab2ef6144d6e9"></a>

### [`00ae0740`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0740.md) → [`00ae0b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0b68.md) FUN_00ae0b68

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 2件 [`008c8c70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008c8/008c8c70.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 4件 [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2f50.md) [`00b09234`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b09/00b09234.md) [`00b0a3cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0a3cc.md)
- 新版 呼出元 2件 [`008c8e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008c8/008c8e0c.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 4件 [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e30ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e30ec.md) [`00b0965c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b09/00b0965c.md) [`00b0a7f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0a/00b0a7f4.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 60.00% / 新版 75.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0754`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0740.md#insn-00ae0754) · [`00ae0784`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0740.md#insn-00ae0784) · [`00ae0788`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0740.md#insn-00ae0788)
- 新版 `00ae0b7c`（命令位置の公開資料なし） · `00ae0bac`（命令位置の公開資料なし） · `00ae0bb0`（命令位置の公開資料なし）

~~~diff
- 00ae0754 ["INT_ADD", "register:40f0:8", ["const:ae0754:8", "const:4:8"]]
- 00ae0754 ["CALL", null, ["callee:00b0965c:8"]]
+ 00ae0b7c ["INT_ADD", "register:40f0:8", ["const:ae0b7c:8", "const:4:8"]]
+ 00ae0b7c ["CALL", null, ["callee:00b0965c:8"]]
- 00ae0754 bytes b8a20094
+ 00ae0b7c bytes b8a20094
- 00ae0784 ["INT_ADD", "register:40f0:8", ["const:ae0784:8", "const:4:8"]]
- 00ae0784 ["CALL", null, ["callee:009e0fc0:8"]]
+ 00ae0bac ["INT_ADD", "register:40f0:8", ["const:ae0bac:8", "const:4:8"]]
+ 00ae0bac ["CALL", null, ["callee:009e0fc0:8"]]
- 00ae0784 bytes a801fc97
+ 00ae0bac bytes 0501fc97
- 00ae0788 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00ae0788 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00ae0788 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00ae0788 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00ae0bb0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00ae0bb0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00ae0bb0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00ae0bb0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00ae0788 bytes e0000036
+ 00ae0bb0 bytes e0000036
~~~


<a id="compare-c73880349259dab616ae6146733776f0"></a>

### [`00ae07b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae07b0.md) → [`00ae0bd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0bd8.md) FUN_00ae0bd8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `compiler_shape_candidate`

- 旧版 呼出元 1件 [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 1件 [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md)
- 新版 呼出元 1件 [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 1件 [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md)

変更の種類 cfg_edge_inventory

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 33.33% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00ae0810`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae07b0.md#insn-00ae0810)
- 新版 `00ae0c38`（命令位置の公開資料なし）

~~~diff
- 00ae0810 8501fc17
+ 00ae0c38 e200fc17
~~~


<a id="compare-53678ff945f268e4d36230049676a55e"></a>

### [`00ae0814`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md) → [`00ae0c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0c3c.md) FUN_00ae0c3c

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`009470d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00947/009470d0.md) [`00ad6d50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ad6/00ad6d50.md) · 呼出先 20件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00665d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md) [`008b6efc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6efc.md)
- 新版 呼出元 2件 [`0094726c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00947/0094726c.md) [`00ad6f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ad6/00ad6f4c.md) · 呼出先 20件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md) [`008b6f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6f40.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 73.55% / 新版 73.55%

CFGの説明率　旧版 46.15% / 新版 45.16%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `call_target` 1件, `unresolved_branch_alignment` 5件, `unresolved_call_alignment` 6件, `unresolved_store_alignment` 27件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae0818"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae081c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae0818",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae081c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae0820",
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
      "00ae0c40",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00ae0c44",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00ae0c48",
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

- 旧版 [`00ae0818`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md#insn-00ae0818) · [`00ae081c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md#insn-00ae081c) · [`00ae0820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0814.md#insn-00ae0820)

~~~diff
- 00ae0818 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00ae0818 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00ae0818 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:a0:8"]]
- 00ae0818 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0818 bytes fd7b0aa9
- 00ae081c ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00ae081c ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00ae081c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:b0:8"]]
- 00ae081c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae081c bytes fc6f0ba9
- 00ae0820 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00ae0820 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00ae0820 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00ae0820 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae0820 bytes fa670ca9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abf78e7bba08b15a48e9e77b88c170f5"></a>

### [`00ae9f2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md) → [`00aea354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea354.md) FUN_00aea354

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) [`00aeed24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md) [`00aefa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md) · 呼出先 10件 [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md) [`00743eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743eec.md) [`00743fb0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743fb0.md) [`00744158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744158.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md)
- 新版 呼出元 3件 [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) [`00aef14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef14c.md) [`00aefe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefe6c.md) · 呼出先 10件 [`005c04f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c04f0.md) [`00743f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743f2c.md) [`00743ff0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743ff0.md) [`00744198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744198.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 86.75% / 新版 86.75%

CFGの説明率　旧版 2.27% / 新版 2.44%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00ae9f40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00ae9f3c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae9f40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00ae9f44",
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
      "00aea364",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aea368",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aea36c",
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

- 旧版 [`00ae9f3c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md#insn-00ae9f3c) · [`00ae9f40`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md#insn-00ae9f40) · [`00ae9f44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae9/00ae9f2c.md#insn-00ae9f44)

~~~diff
- 00ae9f3c ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00ae9f3c ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00ae9f3c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00ae9f3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae9f3c bytes f85f05a9
- 00ae9f40 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00ae9f40 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00ae9f40 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:60:8"]]
- 00ae9f40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae9f40 bytes f65706a9
- 00ae9f44 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00ae9f44 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00ae9f44 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:70:8"]]
- 00ae9f44 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00ae9f44 bytes f44f07a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-080914d707f844f3c757e1e9710ff44d"></a>

### [`00aea188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md) → [`00aea5b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea5b0.md) FUN_00aea5b0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `equal` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) [`00aeed24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aee/00aeed24.md) [`00aefa44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md) · 呼出先 4件 [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md) [`00743eec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00743/00743eec.md) [`00744158`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/00744158.md) [`007441c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00744/007441c8.md)
- 新版 呼出元 3件 [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) [`00aef14c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aef14c.md) [`00aefe6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aefe6c.md) · 呼出先 4件 [`005c04f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c04f0.md) [`00743f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00743/00743f2c.md) [`00744198`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744198.md) [`00744208`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00744/00744208.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 87.10% / 新版 87.10%

CFGの説明率　旧版 21.05% / 新版 23.53%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aea68c",
      "incomplete_value": true,
      "site": "00aea690",
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
            "const:be0:8"
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
      "definition_site": "00aea688",
      "incomplete_value": true,
      "site": "00aea690",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "live",
            "register:4000:4"
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


#### 変更候補の命令位置

- 旧版 [`00aea268`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md#insn-00aea268) · [`00aea1a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md#insn-00aea1a0) · [`00aea1a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea188.md#insn-00aea1a4)
- 新版 `00aea690`（命令位置の公開資料なし）

~~~diff
- 00aea268 ["INT_ADD", "register:40f0:8", ["const:aea268:8", "const:4:8"]]
- 00aea268 ["CALL", null, ["callee:00743f2c:8"]]
+ 00aea690 ["INT_ADD", "register:40f0:8", ["const:aea690:8", "const:4:8"]]
+ 00aea690 ["CALL", null, ["callee:00743f2c:8"]]
- 00aea268 bytes 2167f197
+ 00aea690 bytes 2766f197
- 00aea1a0 ["COPY", "register:40e8:8", ["register:8:8"]]
- 00aea1a0 bytes fd030091
- 00aea1a4 ["COPY", "register:4040:8", ["const:c5b8:8"]]
- 00aea1a4 bytes 08b79852
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15394dd5d92be8ebf066c2f0928f6a23"></a>

### [`00aea2fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md) → [`00aea724`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aea724.md) FUN_00aea724

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ae0e64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0e64.md) [`00af0928`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0928.md) · 呼出先 21件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467ab0.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467b20`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467b20.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md)
- 新版 呼出元 2件 [`00ae128c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae1/00ae128c.md) [`00af0d50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0d50.md) · 呼出先 21件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467af0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467af0.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b60.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.14% / 新版 69.14%

CFGの説明率　旧版 8.33% / 新版 7.69%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea330"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea548"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea558"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aea324",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aea330",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aea77c"
      ]
    ],
    [
      "00aea760",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00aea74c",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea758",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aea77c"
      ]
    ],
    [
      "00aea760",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea330`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md#insn-00aea330) · [`00aea348`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md#insn-00aea348) · [`00aea484`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea2fc.md#insn-00aea484)
- 新版 `00aea770`（命令位置の公開資料なし） · `00aea8ac`（命令位置の公開資料なし）

~~~diff
- 00aea330 ["INT_EQUAL", "tmp:0:1", ["register:4000:8", "const:0:8"]]
- 00aea330 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aea330 bytes 200100b4
- 00aea348 ["INT_ADD", "register:40f0:8", ["const:aea348:8", "const:4:8"]]
- 00aea348 ["CALL", null, ["callee:00c58610:8"]]
+ 00aea770 ["INT_ADD", "register:40f0:8", ["const:aea770:8", "const:4:8"]]
+ 00aea770 ["CALL", null, ["callee:00c58610:8"]]
- 00aea348 bytes b2b70594
+ 00aea770 bytes a8b70594
- 00aea484 ["INT_ADD", "register:40f0:8", ["const:aea484:8", "const:4:8"]]
- 00aea484 ["CALL", null, ["callee:00469c04:8"]]
+ 00aea8ac ["INT_ADD", "register:40f0:8", ["const:aea8ac:8", "const:4:8"]]
+ 00aea8ac ["CALL", null, ["callee:00469c04:8"]]
- 00aea484 bytes d0fde597
+ 00aea8ac bytes d6fce597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df907267c75caa588ca9079c791cba2d"></a>

### [`00aea874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md) → [`00aeac9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeac9c.md) FUN_00aeac9c

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 7件 [`007fb1f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/007fb/007fb1f0.md) [`00996ea0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00996/00996ea0.md) [`009fd490`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009fd/009fd490.md) [`00a005e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a00/00a005e0.md) [`00a0213c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a02/00a0213c.md) · 呼出先 8件 [`00467820`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467820.md) [`00467aec`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467aec.md) [`00467f14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00467/00467f14.md) [`0046c984`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046c984.md) [`0046ca44`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0046c/0046ca44.md)
- 新版 呼出元 7件 [`007fb230`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fb/007fb230.md) [`0099703c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00997/0099703c.md) [`009fd62c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009fd/009fd62c.md) [`00a0077c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a00/00a0077c.md) [`00a022d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a02/00a022d8.md) · 呼出先 8件 [`00467860`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467860.md) [`00467b2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467b2c.md) [`00467f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00467/00467f54.md) [`0046c9c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046c9c4.md) [`0046ca84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0046c/0046ca84.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.94% / 新版 72.94%

CFGの説明率　旧版 9.09% / 新版 11.11%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 2件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea874"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aea878"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aea874",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aea878",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aea87c",
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
      "00aeac9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aeaca0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aeaca4",
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

- 旧版 [`00aea874`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md#insn-00aea874) · [`00aea878`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md#insn-00aea878) · [`00aea87c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea874.md#insn-00aea87c)

~~~diff
- 00aea874 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aea874 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aea874 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aea874 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aea874 bytes fd7bbca9
- 00aea878 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00aea878 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00aea878 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aea878 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aea878 bytes f85f01a9
- 00aea87c ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aea87c ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aea87c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aea87c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aea87c bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6edaefc67bf775e37cab602357349e8"></a>

### [`00aea9c8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md) → [`00aeadf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeadf0.md) FUN_00aeadf0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00acea58`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acea58.md) [`00acec24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acec24.md) [`00acefbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00acefbc.md) · 呼出先 6件 [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md) [`00c57ae0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ae0.md) [`00c57c00`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57c00.md)
- 新版 呼出元 3件 [`00acec54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acec54.md) [`00acee20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ace/00acee20.md) [`00acf1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acf1b8.md) · 呼出先 6件 [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_return_alignment

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 36.11% / 新版 28.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_branch_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaaa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaacc"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeaaf0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aeae70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aeab18"
      ]
    ],
    [
      "unmatched:00aeaaa8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeaee4"
      ]
    ],
    [
      "unmatched:00aeaacc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeaee4"
      ]
    ]
  ],
  "added": [
    [
      "00aeae70",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeaf40"
      ]
    ],
    [
      "00aeaed0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeaee4"
      ]
    ],
    [
      "00aeaef4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeaee4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaa84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md#insn-00aeaa84) · [`00aeaaa8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md#insn-00aeaaa8) · [`00aeaacc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aea9c8.md#insn-00aeaacc)
- 新版 `00aeaeac`（命令位置の公開資料なし）

~~~diff
- 00aeaa84 ["INT_ADD", "register:40f0:8", ["const:aeaa84:8", "const:4:8"]]
- 00aeaa84 ["CALL", null, ["callee:00c58450:8"]]
+ 00aeaeac ["INT_ADD", "register:40f0:8", ["const:aeaeac:8", "const:4:8"]]
+ 00aeaeac ["CALL", null, ["callee:00c58450:8"]]
- 00aeaa84 bytes 73b50594
+ 00aeaeac bytes 69b50594
- 00aeaaa8 ["INT_EQUAL", "tmp:0:1", ["register:4048:8", "const:0:8"]]
- 00aeaaa8 ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00aeaaa8 bytes a90000b4
- 00aeaacc ["BOOL_NEGATE", "tmp:0:1", ["register:101:1"]]
- 00aeaacc ["CBRANCH", null, ["local:b16:8", "tmp:0:1"]]
- 00aeaacc bytes 81ffff54
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a176b338c4c11251822c5cef5f8e216"></a>

### [`00aeab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md) → [`00aeaf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeaf94.md) FUN_00aeaf94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`005fe62c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005fe/005fe62c.md) [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) · 呼出先 18件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`006623ac`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/006623ac.md) [`00662450`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00662/00662450.md)
- 新版 呼出元 2件 [`005fe66c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005fe/005fe66c.md) [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) · 呼出先 18件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`006623ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/006623ec.md) [`00662490`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00662/00662490.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 29.03% / 新版 30.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_condition` 1件, `unresolved_branch_alignment` 21件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 21件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeab70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeab70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeab74"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeab70",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeab74",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeab78",
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
      "00aeaf98",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aeaf9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aeafa0",
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

- 旧版 [`00aeab70`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md#insn-00aeab70) · [`00aeab74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md#insn-00aeab74) · [`00aeab78`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md#insn-00aeab78)

~~~diff
- 00aeab70 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeab70 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeab70 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:c0:8"]]
- 00aeab70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeab70 bytes fd7b0ca9
- 00aeab74 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aeab74 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aeab74 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:d0:8"]]
- 00aeab74 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeab74 bytes fc6f0da9
- 00aeab78 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aeab78 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aeab78 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:e0:8"]]
- 00aeab78 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeab78 bytes fa670ea9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a74d848abf9ce9599c8db515b2c61ee"></a>

### [`00aeb4b8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb4b8.md) → [`00aeb8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aeb/00aeb8e0.md) FUN_00aeb8e0

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aeab6c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aea/00aeab6c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00aeaf94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aea/00aeaf94.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, return_value_candidate, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 13.64% / 新版 18.75%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb568"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeb990"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb4f0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb4f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb940"
      ]
    ]
  ],
  "added": [
    [
      "00aeb918",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeb940"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb4f0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb4b8.md#insn-00aeb4f0) · [`00aeb520`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb4b8.md#insn-00aeb520) · [`00aeb568`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb4b8.md#insn-00aeb568)
- 新版 `00aeb948`（命令位置の公開資料なし）

~~~diff
- 00aeb4f0 ["INT_EQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeb4f0 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00aeb4f0 bytes 480100b4
- 00aeb520 ["INT_ADD", "register:40f0:8", ["const:aeb520:8", "const:4:8"]]
- 00aeb520 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aeb948 ["INT_ADD", "register:40f0:8", ["const:aeb948:8", "const:4:8"]]
+ 00aeb948 ["CALL", null, ["callee:00c57e90:8"]]
- 00aeb520 bytes 5cb10594
+ 00aeb948 bytes 52b10594
- 00aeb568 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:10:8"]]
- 00aeb568 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aeb568 bytes 680a00f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cedd26c88dbf717fe870e1bf1c704a9b"></a>

### [`00aeb584`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md) → [`00aeb9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aeb/00aeb9ac.md) FUN_00aeb9ac

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00b28b2c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b28/00b28b2c.md) · 呼出先 11件 [`004878dc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878dc.md) [`004878fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/004878fc.md) [`00487de0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00487/00487de0.md) [`00488618`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00488/00488618.md) [`00b10cc4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b10/00b10cc4.md)
- 新版 呼出元 1件 [`00b28f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b28/00b28f54.md) · 呼出先 11件 [`0048791c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048791c.md) [`0048793c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/0048793c.md) [`00487e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00487/00487e20.md) [`00488658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00488/00488658.md) [`00b110ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b11/00b110ec.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 58.10% / 新版 58.10%

CFGの説明率　旧版 7.69% / 新版 6.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb588"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb58c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aeb588",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb58c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aeb590",
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
      "00aeb9b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aeb9b4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aeb9b8",
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

- 旧版 [`00aeb588`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md#insn-00aeb588) · [`00aeb58c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md#insn-00aeb58c) · [`00aeb590`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb584.md#insn-00aeb590)

~~~diff
- 00aeb588 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aeb588 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aeb588 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00aeb588 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb588 bytes fd7b18a9
- 00aeb58c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:190:8"]]
- 00aeb58c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 00aeb58c bytes fccb00f9
- 00aeb590 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aeb590 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aeb590 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00aeb590 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aeb590 bytes f6571aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-081b216d5b3865b13aee6c552fdbed2b"></a>

### [`00aeb76c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md) → [`00aebb94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aeb/00aebb94.md) FUN_00aebb94

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00aefce0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefce0.md) [`00af0298`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af0/00af0298.md) · 呼出先 12件 [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md) [`00665d24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00665/00665d24.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 2件 [`00af0108`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af0108.md) [`00af06c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af0/00af06c0.md) · 呼出先 12件 [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md) [`00665d64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00665/00665d64.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 80.73% / 新版 80.73%

CFGの説明率　旧版 17.65% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 4件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb93c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeb940"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeba70"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aebbcc",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbd8",
      "PARAM",
      [
        "storage",
        "00c65a58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00aebbe0",
      "PARAM",
      [
        "storage",
        "00c8d550",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00aebbcc",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbd8",
      "PARAM",
      [
        "storage",
        "00c65e58",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00aebbe0",
      "PARAM",
      [
        "storage",
        "00c8d950",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb7c4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md#insn-00aeb7c4) · [`00aeb884`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md#insn-00aeb884) · [`00aeb8d0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aeb76c.md#insn-00aeb8d0)
- 新版 `00aebbec`（命令位置の公開資料なし） · `00aebcac`（命令位置の公開資料なし）

~~~diff
- 00aeb7c4 ["INT_ADD", "register:40f0:8", ["const:aeb7c4:8", "const:4:8"]]
- 00aeb7c4 ["CALL", null, ["callee:00c58610:8"]]
+ 00aebbec ["INT_ADD", "register:40f0:8", ["const:aebbec:8", "const:4:8"]]
+ 00aebbec ["CALL", null, ["callee:00c58610:8"]]
- 00aeb7c4 bytes 93b20594
+ 00aebbec bytes 89b20594
- 00aeb884 ["INT_ADD", "register:40f0:8", ["const:aeb884:8", "const:4:8"]]
- 00aeb884 ["CALL", null, ["callee:00665d64:8"]]
+ 00aebcac ["INT_ADD", "register:40f0:8", ["const:aebcac:8", "const:4:8"]]
+ 00aebcac ["CALL", null, ["callee:00665d64:8"]]
- 00aeb884 bytes 28e9ed97
+ 00aebcac bytes 2ee8ed97
- 00aeb8d0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb8d0 ["INT_ADD", "register:40f0:8", ["const:aeb8d0:8", "const:4:8"]]
- 00aeb8d0 ["CALLIND", null, ["register:0:8"]]
- 00aeb8d0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce0cc53619ff1d631d19101b10700fc1"></a>

### [`00aebb48`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md) → [`00aebf70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aeb/00aebf70.md) FUN_00aebf70

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 3件 [`00700ab8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00700/00700ab8.md) [`00707528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00707/00707528.md) [`008ef858`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008ef/008ef858.md) · 呼出先 10件 [`0047e89c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e89c.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`00664dd0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00664/00664dd0.md) [`00b0376c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b03/00b0376c.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 3件 [`00700af8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00700/00700af8.md) [`00707568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00707/00707568.md) [`008ef9f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008ef/008ef9f4.md) · 呼出先 10件 [`0047e8dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e8dc.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`00664e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00664/00664e10.md) [`00b03b94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b03/00b03b94.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.51% / 新版 70.51%

CFGの説明率　旧版 13.04% / 新版 15.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebb4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebb4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebb50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebb4c",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebb50",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebb54",
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
      "00aebf74",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aebf78",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aebf7c",
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

- 旧版 [`00aebb4c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md#insn-00aebb4c) · [`00aebb50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md#insn-00aebb50) · [`00aebb54`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebb48.md#insn-00aebb54)

~~~diff
- 00aebb4c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebb4c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebb4c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00aebb4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebb4c bytes fd7b03a9
- 00aebb50 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aebb50 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aebb50 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:40:8"]]
- 00aebb50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebb50 bytes fc6f04a9
- 00aebb54 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aebb54 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aebb54 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:50:8"]]
- 00aebb54 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebb54 bytes fa6705a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b58e7a861ca7c885ff83af6490e47170"></a>

### [`00aebdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebdb8.md) → [`00aec1e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec1e0.md) FUN_00aec1e0

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00adf01c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00adf/00adf01c.md) · 呼出先 2件 [`0043bb64`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0043b/0043bb64.md) [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 1件 [`00adf218`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00adf/00adf218.md) · 呼出先 2件 [`0043bba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bba4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 80.39% / 新版 80.39%

CFGの説明率　旧版 16.67% / 新版 27.78%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_condition` 1件, `unresolved_branch_alignment` 3件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebdb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebdb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebdbc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebdb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebdbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebdc0",
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
      "00aec1e0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ],
    [
      "00aec1e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aec1e8",
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

- 旧版 [`00aebdb8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebdb8.md#insn-00aebdb8) · [`00aebdbc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebdb8.md#insn-00aebdbc) · [`00aebdc0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebdb8.md#insn-00aebdc0)

~~~diff
- 00aebdb8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebdb8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebdb8 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffc0:8"]]
- 00aebdb8 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aebdb8 bytes fd7bbca9
- 00aebdbc ["INT_ADD", "tmp:0:8", ["register:8:8", "const:10:8"]]
- 00aebdbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b8:8"]]
- 00aebdbc bytes f70b00f9
- 00aebdc0 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aebdc0 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aebdc0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aebdc0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebdc0 bytes f65702a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-100dc33342f0c1a471f0bf4dbf8b17a5"></a>

### [`00aebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md) → [`00aec2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec2ac.md) FUN_00aec2ac

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00aec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec104.md) · 呼出先 7件 [`0067e5a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0067e/0067e5a8.md) [`006822e4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00682/006822e4.md) [`006b21a4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b2/006b21a4.md) [`006b7654`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006b7/006b7654.md) [`00c538e0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c53/00c538e0.md)
- 新版 呼出元 1件 [`00aec52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec52c.md) · 呼出先 7件 [`0067e5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0067e/0067e5e8.md) [`00682324`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00682/00682324.md) [`006b21e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b2/006b21e4.md) [`006b7694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006b7/006b7694.md) [`00c53d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53d00.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 58.75% / 新版 58.75%

CFGの説明率　旧版 35.94% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 9件, `unresolved_store_alignment` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aebe88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aebe84",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebe88",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aebe8c",
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
      "00aec2ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aec2b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aec2b4",
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

- 旧版 [`00aebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md#insn-00aebe84) · [`00aebe88`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md#insn-00aebe88) · [`00aebe8c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md#insn-00aebe8c)

~~~diff
- 00aebe84 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aebe84 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aebe84 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aebe84 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aebe84 bytes fd7bbda9
- 00aebe88 ["COPY", "tmp:0:8", ["register:40b0:8"]]
- 00aebe88 ["COPY", "tmp:1:8", ["register:40a8:8"]]
- 00aebe88 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aebe88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebe88 bytes f65701a9
- 00aebe8c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aebe8c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aebe8c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aebe8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aebe8c bytes f44f02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3115265d9606319b62cd5bffa18805bf"></a>

### [`00aec104`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec104.md) → [`00aec52c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec52c.md) FUN_00aec52c

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `observed` · 参照 `equal` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00aebe84`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aeb/00aebe84.md) [`00c57ab0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57ab0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00aec2ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec2ac.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)

変更の種類 cfg_edge_inventory, constant, operands_and_dependencies

命令の説明率　旧版 100.00% / 新版 100.00%

CFGの説明率　旧版 100.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

#### 変更候補の命令位置

- 旧版 [`00aec114`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec104.md#insn-00aec114)
- 新版 `00aec53c`（命令位置の公開資料なし）

~~~diff
- 00aec114 ["INT_ADD", "register:40f0:8", ["const:aec114:8", "const:4:8"]]
- 00aec114 ["CALL", null, ["callee:00aec2ac:8"]]
+ 00aec53c ["INT_ADD", "register:40f0:8", ["const:aec53c:8", "const:4:8"]]
+ 00aec53c ["CALL", null, ["callee:00aec2ac:8"]]
- 00aec114 bytes 5cffff97
+ 00aec53c bytes 5cffff97
~~~


<a id="compare-f4244120585ae9aca73b141495c64745"></a>

### [`00aec17c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md) → [`00aec5a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec5a4.md) FUN_00aec5a4

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 10件 [`00440e80`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00440/00440e80.md) [`00470800`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00470/00470800.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`005c04b0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005c0/005c04b0.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00470840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00470/00470840.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`005c04f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/005c0/005c04f0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.88% / 新版 77.88%

CFGの説明率　旧版 19.05% / 新版 14.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_condition` 1件, `unresolved_branch_alignment` 4件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec180"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec184"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec180",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec184",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec188",
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
      "00aec5a8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00aec5ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00aec5b0",
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

- 旧版 [`00aec180`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md#insn-00aec180) · [`00aec184`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md#insn-00aec184) · [`00aec188`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec17c.md#insn-00aec188)

~~~diff
- 00aec180 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aec180 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aec180 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aec180 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec180 bytes fd7b01a9
- 00aec184 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00aec184 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00aec184 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aec184 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec184 bytes fc6f02a9
- 00aec188 ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00aec188 ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00aec188 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:30:8"]]
- 00aec188 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec188 bytes fa6703a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ade3f3cf1a2935e8713018a665199140"></a>

### [`00aec4e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md) → [`00aec910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec910.md) FUN_00aec910

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00aec934",
      "incomplete_value": false,
      "site": "00aec934",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec50c",
      "incomplete_value": false,
      "site": "00aec50c",
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
            "const:5f8:8"
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
      "00aec934",
      "DATA",
      [
        "storage",
        "00c8d5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aec934",
      "DATA",
      [
        "storage",
        "00c8d9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec4fc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md#insn-00aec4fc) · [`00aec508`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec4e8.md#insn-00aec508)
- 新版 `00aec924`（命令位置の公開資料なし） · `00aec930`（命令位置の公開資料なし）

~~~diff
- 00aec4fc ["INT_ADD", "register:40f0:8", ["const:aec4fc:8", "const:4:8"]]
- 00aec4fc ["CALL", null, ["callee:00c57e90:8"]]
+ 00aec924 ["INT_ADD", "register:40f0:8", ["const:aec924:8", "const:4:8"]]
+ 00aec924 ["CALL", null, ["callee:00c57e90:8"]]
- 00aec4fc bytes 65ad0594
+ 00aec924 bytes 5bad0594
- 00aec508 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00aec508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec930 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00aec930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec508 bytes 08e11791
+ 00aec930 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-540d46ed7fe4686d2e548e4c4a0fbe3f"></a>

### [`00aec51c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md) → [`00aec944`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec944.md) FUN_00aec944

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aec950",
      "incomplete_value": false,
      "site": "00aec950",
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
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec528",
      "incomplete_value": false,
      "site": "00aec528",
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
            "const:5f8:8"
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
      "00aec950",
      "DATA",
      [
        "storage",
        "00c8d5f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aec950",
      "DATA",
      [
        "storage",
        "00c8d9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec524`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec51c.md#insn-00aec524)
- 新版 `00aec94c`（命令位置の公開資料なし）

~~~diff
- 00aec524 ["COPY", "tmp:0:8", ["const:5f8:8"]]
- 00aec524 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00aec524 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00aec524 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00aec94c ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00aec94c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00aec94c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00aec94c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00aec524 bytes 29e11791
+ 00aec94c bytes 29e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f505600ad5ea4dd6e6d6cac18c86690"></a>

### [`00aec538`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md) → [`00aec960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aec/00aec960.md) FUN_00aec960

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 29件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`0047e5cc`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047e5cc.md) [`0047ed74`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047e/0047ed74.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`0047e60c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047e60c.md) [`0047edb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047e/0047edb4.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.18% / 新版 72.18%

CFGの説明率　旧版 23.70% / 新版 26.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 1件, `store_condition` 2件, `unresolved_branch_alignment` 9件, `unresolved_call_alignment` 11件, `unresolved_store_alignment` 24件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec650"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec70c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec718"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aec9ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aec5ac",
      "READ",
      [
        "storage",
        "00ca4578",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec5b4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeca00"
      ]
    ]
  ],
  "added": [
    [
      "00aec9ac",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aec9d4",
      "READ",
      [
        "storage",
        "00ca4978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec9dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aeca00"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec650`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md#insn-00aec650) · [`00aec70c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md#insn-00aec70c) · [`00aec718`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aec/00aec538.md#insn-00aec718)

~~~diff
- 00aec650 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:38:8"]]
- 00aec650 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aec650 bytes e81f00f9
- 00aec70c ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00aec70c ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:ffffffffffffffff:8"]]
- 00aec70c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec70c bytes 2bf11f38
- 00aec718 ["COPY", "tmp:0:4", ["register:4058:4"]]
- 00aec718 ["COPY", "tmp:1:8", ["register:4048:8"]]
- 00aec718 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec718 bytes 2b010039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cb728ec50e5dcfb45cf03a85992172c"></a>

### [`00aed1c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md) → [`00aed5e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed5e8.md) FUN_00aed5e8

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed1e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed610"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": null,
    "old": {
      "definition_site": "00aed1d0",
      "incomplete_value": false,
      "site": "00aed1d4",
      "value": [
        "leaf",
        "const:20:8"
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
      "unmatched:00aed1e8",
      "DATA",
      [
        "storage",
        "00c8d6f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aed610",
      "DATA",
      [
        "storage",
        "00c8daf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed1d4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md#insn-00aed1d4) · [`00aed1e8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed1c0.md#insn-00aed1e8)
- 新版 `00aed5fc`（命令位置の公開資料なし） · `00aed610`（命令位置の公開資料なし）

~~~diff
- 00aed1d4 ["INT_ADD", "register:40f0:8", ["const:aed1d4:8", "const:4:8"]]
- 00aed1d4 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aed5fc ["INT_ADD", "register:40f0:8", ["const:aed5fc:8", "const:4:8"]]
+ 00aed5fc ["CALL", null, ["callee:00c57e90:8"]]
- 00aed1d4 bytes 2faa0594
+ 00aed5fc bytes 25aa0594
- 00aed1e8 ["COPY", "tmp:0:8", ["register:4000:8"]]
- 00aed1e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00aed1e8 bytes 080000f9
+ 00aed610 ["COPY", "tmp:0:8", ["register:4000:8"]]
+ 00aed610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00aed610 bytes 080000f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e3b1d9d649098ab9ecbaff726c2f0ac"></a>

### [`00aed228`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md) → [`00aed650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed650.md) FUN_00aed650

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 5件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`008b6e60`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/008b6/008b6e60.md) [`00a466f8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a466f8.md) [`00a469c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a46/00a469c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`008b6ea4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008b6/008b6ea4.md) [`00a468f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a468f0.md) [`00a46bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a46/00a46bb8.md)

変更の種類 branch_condition_or_target, call, call_target, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 55.56% / 新版 41.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed2a0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed2a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed6c8"
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
      "00aed674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00aed680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aed2a0",
      "DATA",
      [
        "storage",
        "00335ff4",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00aed674",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed680",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed6c8",
      "DATA",
      [
        "storage",
        "00335ff4",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed24c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md#insn-00aed24c) · [`00aed258`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md#insn-00aed258) · [`00aed2a0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed228.md#insn-00aed2a0)
- 新版 `00aed674`（命令位置の公開資料なし） · `00aed680`（命令位置の公開資料なし）

~~~diff
- 00aed24c ["INT_ADD", "register:40f0:8", ["const:aed24c:8", "const:4:8"]]
- 00aed24c ["CALL", null, ["ram:47acb4:8"]]
+ 00aed674 ["INT_ADD", "register:40f0:8", ["const:aed674:8", "const:4:8"]]
+ 00aed674 ["CALL", null, ["ram:47acf4:8"]]
- 00aed24c bytes 9a36e697
+ 00aed674 bytes a035e697
- 00aed258 ["INT_ADD", "register:40f0:8", ["const:aed258:8", "const:4:8"]]
- 00aed258 ["CALL", null, ["ram:47acb4:8"]]
+ 00aed680 ["INT_ADD", "register:40f0:8", ["const:aed680:8", "const:4:8"]]
+ 00aed680 ["CALL", null, ["ram:47acf4:8"]]
- 00aed258 bytes 9736e697
+ 00aed680 bytes 9d35e697
- 00aed2a0 ["COPY", "tmp:0:4", ["register:40a0:4"]]
- 00aed2a0 ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00aed2a0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 00aed2a0 ["INT_LEFT", "tmp:2:8", ["tmp:2:8", "const:0:8"]]
- 00aed2a0 bytes 14692a38
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d35ba371b3b2dbce4602e24f0a56ae27"></a>

### [`00aed300`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md) → [`00aed728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed728.md) FUN_00aed728

採用 · 移動量 `+0x428` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c57a90`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c57a90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)

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
      "definition_site": "00aed74c",
      "incomplete_value": false,
      "site": "00aed74c",
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
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed324",
      "incomplete_value": false,
      "site": "00aed324",
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
            "const:778:8"
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
      "00aed74c",
      "DATA",
      [
        "storage",
        "00c8d778",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aed74c",
      "DATA",
      [
        "storage",
        "00c8db78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed314`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md#insn-00aed314) · [`00aed320`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed300.md#insn-00aed320)
- 新版 `00aed73c`（命令位置の公開資料なし） · `00aed748`（命令位置の公開資料なし）

~~~diff
- 00aed314 ["INT_ADD", "register:40f0:8", ["const:aed314:8", "const:4:8"]]
- 00aed314 ["CALL", null, ["callee:00c57e90:8"]]
+ 00aed73c ["INT_ADD", "register:40f0:8", ["const:aed73c:8", "const:4:8"]]
+ 00aed73c ["CALL", null, ["callee:00c57e90:8"]]
- 00aed314 bytes dfa90594
+ 00aed73c bytes d5a90594
- 00aed320 ["COPY", "tmp:0:8", ["const:778:8"]]
- 00aed320 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed320 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed320 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed748 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00aed748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed320 bytes 08e11d91
+ 00aed748 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff9a1a68567bef0870baa5148d7e2a9"></a>

### [`00aed350`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md) → [`00aed778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed778.md) FUN_00aed778

採用 · 移動量 `+0x428` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 7件 [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`009e0e24`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e0/009e0e24.md) [`009e2f50`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009e2/009e2f50.md) [`00ae0408`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ae0/00ae0408.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`009e0fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e0/009e0fc0.md) [`009e30ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009e3/009e30ec.md) [`00ae0830`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00ae0/00ae0830.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 85.06% / 新版 85.06%

CFGの説明率　旧版 23.33% / 新版 26.92%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `call_target` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed3c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed3c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aed7e8"
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
      "00aed79c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00aed7a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aed3c8",
      "DATA",
      [
        "storage",
        "00332a31",
        null,
        "fde_table_entry"
      ]
    ]
  ],
  "added": [
    [
      "00aed79c",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed7a8",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed7f0",
      "DATA",
      [
        "storage",
        "00332a31",
        null,
        "fde_table_entry"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed374`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md#insn-00aed374) · [`00aed380`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md#insn-00aed380) · [`00aed3a8`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed350.md#insn-00aed3a8)
- 新版 `00aed79c`（命令位置の公開資料なし） · `00aed7a8`（命令位置の公開資料なし） · `00aed7d0`（命令位置の公開資料なし）

~~~diff
- 00aed374 ["INT_ADD", "register:40f0:8", ["const:aed374:8", "const:4:8"]]
- 00aed374 ["CALL", null, ["ram:47acb4:8"]]
+ 00aed79c ["INT_ADD", "register:40f0:8", ["const:aed79c:8", "const:4:8"]]
+ 00aed79c ["CALL", null, ["ram:47acf4:8"]]
- 00aed374 bytes 5036e697
+ 00aed79c bytes 5635e697
- 00aed380 ["INT_ADD", "register:40f0:8", ["const:aed380:8", "const:4:8"]]
- 00aed380 ["CALL", null, ["ram:47acb4:8"]]
+ 00aed7a8 ["INT_ADD", "register:40f0:8", ["const:aed7a8:8", "const:4:8"]]
+ 00aed7a8 ["CALL", null, ["ram:47acf4:8"]]
- 00aed380 bytes 4d36e697
+ 00aed7a8 bytes 5335e697
- 00aed3a8 ["INT_ADD", "register:40f0:8", ["const:aed3a8:8", "const:4:8"]]
- 00aed3a8 ["CALL", null, ["callee:00ae0830:8"]]
+ 00aed7d0 ["INT_ADD", "register:40f0:8", ["const:aed7d0:8", "const:4:8"]]
+ 00aed7d0 ["CALL", null, ["callee:00ae0830:8"]]
- 00aed3a8 bytes 18ccff97
+ 00aed7d0 bytes 18ccff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e73aa15dc0ea3a8fe0e568af7eaa2420"></a>

### [`00aed528`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md) → [`00aed950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aed/00aed950.md) FUN_00aed950

採用 · 移動量 `+0x428` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 19件 [`00447eb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00447/00447eb4.md) [`0047acb4`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047a/0047acb4.md) [`0047cd94`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0047c/0047cd94.md) [`00489f0c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00489/00489f0c.md) [`0048ce14`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/0048c/0048ce14.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00447ef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00447/00447ef4.md) [`0047acf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047a/0047acf4.md) [`0047cdd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0047c/0047cdd4.md) [`00489f4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00489/00489f4c.md) [`0048ce54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0048c/0048ce54.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 87.06% / 新版 87.06%

CFGの説明率　旧版 37.70% / 新版 34.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `call_target` 2件, `unresolved_branch_alignment` 3件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed5c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed5c4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed5c8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aed988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "00aed9a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acb4"
      ]
    ],
    [
      "unmatched:00aed5b8",
      "READ",
      [
        "storage",
        "0029f7a5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aed988",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed9a4",
      "UNCONDITIONAL_CALL",
      [
        "unresolved_target",
        "0047acf4"
      ]
    ],
    [
      "00aed9e0",
      "READ",
      [
        "storage",
        "0029f872",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed560`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md#insn-00aed560) · [`00aed57c`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md#insn-00aed57c) · [`00aed5c0`](../../../../reference/16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aed/00aed528.md#insn-00aed5c0)
- 新版 `00aed988`（命令位置の公開資料なし） · `00aed9a4`（命令位置の公開資料なし）

~~~diff
- 00aed560 ["INT_ADD", "register:40f0:8", ["const:aed560:8", "const:4:8"]]
- 00aed560 ["CALL", null, ["ram:47acb4:8"]]
+ 00aed988 ["INT_ADD", "register:40f0:8", ["const:aed988:8", "const:4:8"]]
+ 00aed988 ["CALL", null, ["ram:47acf4:8"]]
- 00aed560 bytes d535e697
+ 00aed988 bytes db34e697
- 00aed57c ["INT_ADD", "register:40f0:8", ["const:aed57c:8", "const:4:8"]]
- 00aed57c ["CALL", null, ["ram:47acb4:8"]]
+ 00aed9a4 ["INT_ADD", "register:40f0:8", ["const:aed9a4:8", "const:4:8"]]
+ 00aed9a4 ["CALL", null, ["ram:47acf4:8"]]
- 00aed57c bytes ce35e697
+ 00aed9a4 bytes d434e697
- 00aed5c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed5c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed5c0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:11:8"]]
- 00aed5c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed5c0 bytes ff470039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

